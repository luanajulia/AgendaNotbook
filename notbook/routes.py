#rotas do nosso site
from datetime import datetime, date, timedelta, time
from time import strftime
from flask.app import T_template_filter
from sqlalchemy.sql import func
import json
from flask import Response, abort, render_template, send_file, session, url_for, redirect, request, flash
from notbook import app, database, bcrypt
from notbook.model import Usuario, Computadores, Softwares, Chamados, Agendamento, Impressora, Toners, Cameras, Antenas, Manutencao, Materiais, Protheus, Centro, Tecnico, Colaboradores, Ausencia, Banco
from flask_login import login_required, login_user, logout_user, current_user
from notbook.forms import FormLogin, Criarconta, Criar_computadores, Criar_Softwares, ChamadoForm, Criar_Agendamento, Criar_Impressora, Criar_Camera, Criar_Antenas, Criar_Toners, ManutencaoForm, Criar_Equipamento, Form_Protheus, Criar_Centro, Criar_Tecnico, Criar_Colaborador, Criar_Ausencia, Criar_Banco
from flask_mail import Mail, Message
from sqlalchemy import desc
import os
import jinja2
from werkzeug.utils import secure_filename
import pandas as pd
import sqlite3
import pyodbc
from notbook.conexao import conx_help
from collections import defaultdict

email = 'suporte@apema.com.br'
senha = 'Apema@2019'

mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

app.config['UPLOAD_FOLDER'] = 'notbook/static' 
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) 

def get_event_data():
    
    event_data= defaultdict(list)
    try:
        
        conx_help.execute("SELECT data, concat(convert(varchar, hora ,8), ' - ', usuario) as label  FROM agenda where concluida is null")
        
        for row in conx_help.fetchall():
                # Acessa o valor da primeira coluna (a data)
                date_value = row[0] 
                label_value = row[1]

                # Converte o objeto date para uma string no formato 'YYYY-MM-DD'
                event_data[date_value.format()].append(label_value)

    finally:
        if 'conx_help' in locals() and conx_help:
            conx_help.close()
    
    return  dict(event_data)  

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        query = (
            "SELECT TOP 1 * FROM usuario WHERE email = '"
            + email
            + "' and senha = '"
            + senha
            + "' "
        )
        usuarios = conx_help.execute(query).fetchall()
        for usuario in usuarios:
            if usuario[2] == email and usuario[3] == senha:
                session["logged_in"] = True
                session["email"] = email
                session["nivel"] = usuario[5]
                session["departamento"] = usuario[4]
                session["id"] = usuario[0]
                current_user = True
                return redirect(url_for("reunioes"))
        return render_template("homepage.html", msg="Usuario Incorreto")
    return render_template("homepage.html")


@app.route("/agenda", methods=["GET", "POST"])
def agenda():
    datas = get_event_data()
    if request.method == "POST":
        username=request.form.get("username")
        titulo=request.form.get("titulo")
        sala=request.form.get("sala")
        data=request.form.get("data")
        hora=request.form.get("hora")
        if request.form.get("link"):
            link=request.form.get("link")
        else:
            link='Não tem link'
        file = request.files['arquivo']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            conx_help.execute("INSERT INTO agenda (usuario, reuniao, data, hora, link, sala, arquivo) VALUES ('"+username+"', '"+titulo+"','"+data+"','"+hora+"', '"+link+"', '"+sala+"', '"+filename+"')")
            conx_help.commit()
            confirma="Notbook agendado para '"+data+"'"
            print(confirma)
        else:
            conx_help.execute("INSERT INTO agenda (usuario, reuniao, data, hora, link, sala) VALUES ('"+username+"', '"+titulo+"','"+data+"','"+hora+"', '"+link+"', '"+sala+"')")
            conx_help.commit()
            confirma="Notbook agendado para '"+data+"'"
            print(confirma)
        msg = Message("Novo Agendamento",  sender = app.config.get("MAIL_USERNAME"), recipients= ["luanavieira@apema.com.br"])
        msg.body = f''' 
Ola :),\n
O colaborador(a): {username},\n
Tem uma reuniao: {titulo},\n
No dia: {data} às {hora},\n
Clique aqui para ir até a reuniao: http://192.168.1.51:8090 \n
Obrigada pela Atenção :) \n
Tenha um Otimo Trabalho 
'''
        mail.send(msg) 
        return redirect(url_for("agenda"))
    return render_template("agendamento.html", datas=datas)

@app.route("/reunioes", methods=["GET", "POST"])
def reunioes():
    if not session.get('logged_in'):
        return redirect(url_for('homepage'))
    emails = session['email'] 
    datas = conx_help.execute("SELECT *, convert(varchar, hora ,8) as hora, convert(varchar, data ,103) as data FROM agenda where concluida is null order by id desc ").fetchall()
    return render_template("reunioes.html", datas=datas, emails=emails)

@app.route("/concluidas", methods=["GET", "POST"])
def concluidas():
    if not session.get('logged_in'):
        return redirect(url_for('homepage'))
    emails = session['email'] 
    datas = conx_help.execute("SELECT *, convert(varchar, hora ,8) as hora, convert(varchar, data ,103) as data FROM agenda where concluida is not null order by id desc ").fetchall()
    return render_template("reunioes.html", datas=datas, emails=emails)

@app.route("/edit_reuniao/<string:id>", methods=["GET", "POST"])
def edit_reuniao(id):
    if not session.get('logged_in'):
        return redirect(url_for('homepage'))
    emails = session['email'] 
    datas = conx_help.execute("SELECT *, convert(varchar, hora ,8) as hora FROM agenda where id = '"+id+"' ").fetchall()
    if request.method == "POST":
        username=request.form.get("username")
        titulo=request.form.get("titulo")
        data=request.form.get("data")
        hora=request.form.get("hora")
        link=request.form.get("link")
        conx_help.execute("UPDATE agenda SET usuario = '"+username+"', reuniao = '"+titulo+"', data = '"+data+"', hora = '"+hora+"', link= '"+link+"' where  id = '"+id+"' ")
        conx_help.commit()  
        return redirect(url_for("reunioes"))
    return render_template("edit_reuniao.html", datas=datas, emails=emails)

@app.route("/delete/<string:id>", methods=["GET", "POST"])
def delete(id):
    excluir = "DELETE FROM agenda  WHERE id = '"+id+"'" 
    conx_help.execute(excluir)
    conx_help.commit()
    flash('computador Deleted','warning')
    return redirect(url_for("reunioes"))

@app.route("/concluir/<string:id>", methods=["GET", "POST"])
def concluir(id):
    concluir = "UPDATE agenda SET concluida = 'concluida'  WHERE id = '"+id+"'" 
    conx_help.execute(concluir)
    conx_help.commit()
    flash('computador Deleted','warning')
    return redirect(url_for("reunioes"))

@app.route("/voltar/<string:id>", methods=["GET", "POST"])
def voltar(id):
    concluir = "UPDATE agenda SET concluida = NULL  WHERE id = '"+id+"'" 
    conx_help.execute(concluir)
    conx_help.commit()
    flash('computador Deleted','warning')
    return redirect(url_for("reunioes"))


