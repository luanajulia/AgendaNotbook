#banco de dados do site
from notbook import database, login_manager
from flask_login import UserMixin
from datetime import datetime, time, UTC

@login_manager.user_loader
def load_Usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False )
    departamento = database.Column(database.String, nullable=False)
    ramal = database.Column(database.String, nullable=False)
    nivel = database.Column(database.String)
    desativado = database.Column(database.String)
    chamados = database.relationship("Chamados", backref='usuario', lazy=True)
    manutencao = database.relationship("Manutencao", backref='usuario', lazy=True)
    Agendamento = database.relationship("Agendamento", backref='usuario', lazy=True)


class Computadores(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    te = database.Column(database.String, nullable=False)
    processador = database.Column(database.String, nullable=False)
    memoria = database.Column(database.String, nullable=False)
    disco_rigido = database.Column(database.String, nullable=False)
    disco_rigido_2 = database.Column(database.String, nullable=True)
    monitores = database.Column(database.String)
    tipo = database.Column(database.String, nullable=False)

class Celulares(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    modelo = database.Column(database.String, nullable=False)
    imei = database.Column(database.String, nullable=False)
    rg = database.Column(database.String, nullable=False)
    numero = database.Column(database.String, nullable=False)

class Softwares(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    validade = database.Column(database.String, nullable=False)
    usando = database.Column(database.Integer)
    versao = database.Column(database.String, nullable=False)

class Chamados(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    departamento = database.Column(database.String, nullable=False)
    tipo = database.Column(database.String, nullable=False)
    status = database.Column(database.String, nullable=False)
    atribuido = database.Column(database.String)
    descricao = database.Column(database.String, nullable=False)
    feedback = database.Column(database.String, nullable=False)
    imagem = database.Column(database.String, nullable=True, default="default.png") 
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())

class Agendamento(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.String, database.ForeignKey('usuario.id'), nullable=False)
    data = database.Column(database.String, nullable=False)
    sala = database.Column(database.String, nullable=False)
    horario = database.Column(database.String)
    username = database.Column(database.String, nullable=False)

class Impressora(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome_impressora = database.Column(database.String, nullable=False)
    modelo_impressora = database.Column(database.String, nullable=False)
    departamento = database.Column(database.String, nullable=False)
    ip = database.Column(database.String, nullable=False)

class Toners(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    quant_toners = database.Column(database.String)
    toners =  database.Column(database.String, nullable=False)

class Antenas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    departamento = database.Column(database.String, nullable=False)
    antenas = database.Column(database.String, nullable=False)

class Cameras(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    departamento = database.Column(database.String, nullable=False)
    cameras = database.Column(database.String, nullable=False)
    quant_cameras = database.Column(database.String)

class Manutencao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    departamento = database.Column(database.String, nullable=False)
    tipo = database.Column(database.String, nullable=False)
    status = database.Column(database.String, nullable=False)
    descricao = database.Column(database.String, nullable=False)
    feedback = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now())
    data_inicio = database.Column(database.String)
    hora_inicio = database.Column(database.String)
    data_final = database.Column(database.String)
    hora_final = database.Column(database.String)
    operacao = database.Column(database.String)
    os =  database.Column(database.String, nullable=False)
    equipamento = database.Column(database.String, nullable=False)
    localizacao = database.Column(database.String, nullable=False)
    total = database.Column(database.String)
    tecnico = database.Column(database.String)

    
class Protheus(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_manutencao = database.Column(database.Integer,  nullable=False)
    codigo = database.Column(database.String)
    descricao = database.Column(database.String)

class Materiais(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    codigo = database.Column(database.Integer, nullable=False)
    equipamento = database.Column(database.String, nullable=False)
    localizacao = database.Column(database.String)
    prev = database.Column(database.String)
    pred = database.Column(database.String)
    caracteristica = database.Column(database.String)
    desativado = database.Column(database.String)

class Centro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    departamento = database.Column(database.String, nullable=False)

class Tecnico(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    nivel = database.Column(database.String, nullable=False)
    status = database.Column(database.String)

class Colaboradores(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    colaborador = database.Column(database.String, nullable=False)
    matricula = database.Column(database.String)
    departamento = database.Column(database.String, nullable=False)
    responsavel = database.Column(database.String)

class Ausencia(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    colaborador = database.Column(database.Integer, nullable=False)
    departamento = database.Column(database.String, nullable=False)
    matricula = database.Column(database.String)
    data = database.Column(database.String)
    tipo_ausencia = database.Column(database.String)
    motivo = database.Column(database.String)
    periodo_ausencia = database.Column(database.String)
    gerencia = database.Column(database.String)
    responsavel = database.Column(database.String)


class Banco(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    colaborador = database.Column(database.Integer, nullable=False)
    area = database.Column(database.String, nullable=False)
    matricula = database.Column(database.String)
    data = database.Column(database.String, nullable=False)
    atividade = database.Column(database.String, nullable=False)
    periodo = database.Column(database.String, nullable=False)
    responsavel = database.Column(database.String)
