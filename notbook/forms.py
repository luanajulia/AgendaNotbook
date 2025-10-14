#formulario de login do site
from re import RegexFlag
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, PasswordField, SubmitField, IntegerField, SelectField, HiddenField, DateField, TextAreaField, FileField, BooleanField, DateTimeField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from notbook.model import Usuario, Computadores, Softwares

class FormLogin(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    botao_confirmar = SubmitField("Fazer Login")

class Criarconta(FlaskForm):
    username = StringField("Usuario:", validators=[DataRequired()])
    departamento = StringField("Departamento:", validators=[DataRequired()])
    ramal = IntegerField("Ramal:", validators=[DataRequired()])
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired(), Length(6, 20)])
    nivel = SelectField('Nivel de acesso', choices=[
                  ('usuario', 'usuario'),
                  ('Manutenção', 'Manutenção'), 
                  ('Tecnico', 'Tecnico'),
                  ('Administrador', 'Administrador')])
    confirmacao_senha = PasswordField("confirme sua senha", validators=[DataRequired(), EqualTo("senha")])
    confirmar_conta = SubmitField("Criar Conta")
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")
       
class Criar_computadores(FlaskForm):
    te = StringField("Nome da Maquina:", validators=[DataRequired()])
    usuario = StringField("Nome do usuario:")
    processador = StringField("Processador:", validators=[DataRequired()])
    memoria = StringField("Memoria:", validators=[DataRequired()])
    disco_rigido = StringField("Disco Rigido:")
    disco_rigido_2 = StringField("Segundo Disco Rigido:")
    tipo = StringField("Tipo", validators=[DataRequired()])
    monitores = StringField("Quant. Monitores:", validators=[DataRequired()])
    enviar_dados = SubmitField("Enviar")

class Criar_Softwares(FlaskForm):
    nome = StringField("Nome do Software:", validators=[DataRequired()])
    validade = StringField("Data de Validade:", validators=[DataRequired()])
    versao = StringField("Versão:", validators=[DataRequired()])
    usando = IntegerField("Versão:", validators=[DataRequired()])
    enviar = SubmitField("submeter")

class ChamadoForm(FlaskForm):
    username = StringField("Usuario:", validators=[ DataRequired()])
    departamento = StringField("Departamento:", validators=[DataRequired()])
    descricao = TextAreaField("Descrição:", validators=[DataRequired()])
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    tipo = SelectField('Tipo de Suporte', choices=[
                  ('Outro', 'Escolha...'), 
                  ('Impressora', 'Impressora'),
                  ('Power Bi', 'Power Bi'),
                  ('Telefone', 'Telefone'),
                  ('Computador', 'Computador'),
                  ('Toner', 'Toner'),
                  ('Rede', 'Rede'),
                  ('Protheus', 'Protheus'),
                  ('Outro', 'Outro')])
    status = SelectField('Status do chamado', choices=[ 
                  ('novo', 'Novo'),
                  ('atribuido', 'Atribuido'),
                  ('fechado', 'Fechado')])
    feedback = TextAreaField("Feedback:")
    atribuido = StringField("Atribuido:")
    imagem = FileField("Foto do Problema")
    enviar_chamado = SubmitField("Enviar")

class Criar_Agendamento(FlaskForm):
    sala = SelectField('Sala', choices=[ 
                  ('sala de treinamento', 'sala de treinamento'),
                  ('sala da cadeira amarela', 'sala da cadeira amarela'),
                  ('sala de reuniao', 'sala de reuniao')])
    data = DateField("Data:", validators=[DataRequired()])
    horario = StringField("Horario:", validators=[DataRequired()])
    username = StringField("Usuario:", validators=[DataRequired()])
    enviar = SubmitField("Agendar")

class Criar_Impressora(FlaskForm):
    nome_impressora = StringField("Nome da Impressora:", validators=[DataRequired()])
    modelo_impressora = SelectField("Departamento:", choices=[('Samsung M4080FX', 'Samsung M4080FX'),
                                                                ('Kiocera  Ecosys m4125idn', 'Kiocera  Ecosys m4125idn'), 
                                                                ('HP Laser Colorida 4303FDW','HP Laser Colorida 4303FDW')])
    departamento = SelectField("Departamento:", choices=[('Administrativo', 'Administrativo'),
                                                          ('Almoxarifado', 'Almoxarifado'), 
                                                          ('Compras','Compras'),  
                                                          ('Engenharia','Engenharia'), 
                                                          ('Expedicao','Expedicao'),
                                                          ('Faturamento Engenharia','Faturamento Engenharia'),
                                                          ('Inspetores','Inspetores'),
                                                          ('Lideres','Lideres'),
                                                          ('Manutenção','Manutenção'),
                                                          ('Markenting','Markenting'),
                                                          ('PCP','PCP'),
                                                          ('Portaria','Portaria'),
                                                          ('Processos','Processos'),
                                                          ('Qualidade','Qualidade'),
                                                          ('SIPAT','SIPAT'),
                                                          ('RH', 'RH'),
                                                          ('Vendas','Vendas')])
    ip = StringField("IP da Impressora:", validators=[DataRequired()])
    enviar = SubmitField("Adcionar")

class Criar_Toners(FlaskForm):
    quant_toners = StringField("Quantidade de Toner:", validators=[DataRequired()])
    toners = SelectField("Departamento:", choices=[('Samsung M4080FX', 'Samsung M4080FX'),
                                                                ('Kiocera  Ecosys m4125idn', 'Kiocera  Ecosys m4125idn'), 
                                                                ('HP Laser Colorida 4303FDW','HP Laser Colorida 4303FDW')])
    enviar = SubmitField("Adcionar")

class Criar_Antenas(FlaskForm):
    antenas = StringField("Modelo Antena:", validators=[DataRequired()])
    departamento = SelectField("Departamento:", choices=[('Administrativo', 'Administrativo'),
                                                          ('Almoxarifado', 'Almoxarifado'), 
                                                          ('Compras','Compras'),  
                                                          ('Engenharia','Engenharia'), 
                                                          ('Expedicao','Expedicao'),
                                                          ('Faturamento Engenharia','Faturamento Engenharia'),
                                                          ('Inspetores','Inspetores'),
                                                          ('Lideres','Lideres'),
                                                          ('Manutenção','Manutenção'),
                                                          ('Markenting','Markenting'),
                                                          ('PCP','PCP'),
                                                          ('Portaria','Portaria'),
                                                          ('Processos','Processos'),
                                                          ('Qualidade','Qualidade'),
                                                          ('SIPAT','SIPAT'),
                                                          ('RH', 'RH'),
                                                          ('Vendas','Vendas')])
    enviar = SubmitField("Adcionar")

class Criar_Camera(FlaskForm):
    cameras = SelectField("Departamento:", choices=[('Vip 3240 IA', 'Vip 3240 IA'),
                                                          ('Vip S3020 G2', 'Vip S3020 G2'), 
                                                          ('VHD 1010','VHD 1010')])
    quant_cameras = StringField("Quantidade:", validators=[DataRequired()])
    departamento = SelectField("Departamento:", choices=[('Administrativo', 'Administrativo'),
                                                          ('Almoxarifado', 'Almoxarifado'), 
                                                          ('Compras','Compras'),  
                                                          ('Engenharia','Engenharia'), 
                                                          ('Expedicao','Expedicao'),
                                                          ('Faturamento Engenharia','Faturamento Engenharia'),
                                                          ('Inspetores','Inspetores'),
                                                          ('Lideres','Lideres'),
                                                          ('Manutenção','Manutenção'),
                                                          ('Markenting','Markenting'),
                                                          ('PCP','PCP'),
                                                          ('Portaria','Portaria'),
                                                          ('Processos','Processos'),
                                                          ('Qualidade','Qualidade'),
                                                          ('SIPAT','SIPAT'),
                                                          ('RH', 'RH'),
                                                          ('Vendas','Vendas')])
    enviar = SubmitField("Adcionar")

class ManutencaoForm(FlaskForm):
    username = StringField("Usuario:", validators=[ DataRequired()])
    departamento = StringField("Departamento:", validators=[DataRequired()])
    descricao = TextAreaField("Descrição:", validators=[DataRequired()])
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    tipo = SelectField('Tipo de Serviço',  choices=[
                  ('Outro', 'Escolha...'), 
                  ('Mudanca', 'Mudanca'),
                  ('Equipamento', 'Equipamento'),
                  ('NoBreak', 'NoBreak'),
                  ('Lanterna', 'Lanterna'),
                  ('Tomada', 'Tomada'),
                  ('Outro', 'Outro')])
    status = SelectField('Status do chamado', choices=[ 
                  ('novo', 'Novo'),
                  ('atribuido', 'Atribuido'),
                  ('fechado', 'Fechado')])
    feedback = TextAreaField("Feedback:")
    data_inicio = StringField("Data de Inicio da manutenção:")
    hora_inicio = StringField("Hora Inicio:")
    data_final = StringField("Data de Final da manutenção:")
    hora_final = StringField("Hora Final:")
    operacao = StringField("Operacao:")
    enviar_chamado = SubmitField("Enviar")

class Criar_Equipamento(FlaskForm):
    codigo = StringField("Codigo do Equipamento:", validators=[DataRequired()])
    equipamento = StringField("Equipamento:", validators=[DataRequired()])
    localizacao = SelectField('Localização do Equipamento', choices=[
                  ('Caldeiraria', 'Caldeiraria '),
                  ('Teste', 'Teste'),
                  ('Soldas', 'Soldas '),
                  ('Expedição', 'Expedição '),
                  ('Prensas', 'Prensas'),
                  ('Pintura', 'Pintura'),
                  ('CST', 'CST '),
                  ('Tampas', 'Tampas'),
                  ('Corte', 'Corte'),
                  ('Radiador', 'Radiador')])
    prev = SelectField('Prev', choices=[
                  (' ', 'Escolha...'),
                  ('S', 'S')])
    pred = SelectField('Pred', choices=[
                  (' ', 'Escolha...'),
                  ('S', 'S')])
    caracteristica = StringField("Caracteristica:", validators=[DataRequired()])
    desativado = StringField("Status:")
    enviar = SubmitField("submeter")

class Form_Protheus(FlaskForm):
    id_manutencao = StringField("ID:", validators=[DataRequired()])
    codigo = StringField("Codigo:", validators=[DataRequired()])
    descricao = StringField("Descricao:", validators=[DataRequired()])
    enviar_chamado = SubmitField("Adcionar")

class Criar_Centro(FlaskForm):
    usuario = StringField("Usuario:", validators=[DataRequired()])
    departamento = StringField("Centro de Custo atribuido:", validators=[DataRequired()])
    enviar = SubmitField("Atribuir")

class Criar_Tecnico(FlaskForm):
    usuario = StringField("Usuario:", validators=[DataRequired()])
    nivel = StringField("Nivel de Usuario:", validators=[DataRequired()])
    enviar = SubmitField("Adicionar")

class Criar_Colaborador(FlaskForm):
    colaborador = StringField("Usuario:", validators=[DataRequired()])
    departamento = StringField("Departamento:", validators=[DataRequired()])
    matricula = StringField("Matricula:", validators=[DataRequired()])
    enviar = SubmitField("Adicionar")

class Criar_Ausencia(FlaskForm):
    colaborador =  StringField("Nome:", validators=[DataRequired()])
    departamento = StringField("Departamento:", validators=[DataRequired()])
    matricula = StringField("Matricula:", validators=[DataRequired()])
    data = StringField("Data:", validators=[DataRequired()])
    tipo_ausencia = StringField("Tipo de Ausencia:")
    periodo_ausencia = StringField("Periodo da Ausencia:")
    motivo = TextAreaField("Motivo Da ausencia:", validators=[DataRequired()])
    gerencia = StringField("Gerencia:", validators=[DataRequired()])
    enviar = SubmitField("Enviar")


class Criar_Banco(FlaskForm):
    colaborador =  StringField("Nome:", validators=[DataRequired()])
    area = StringField("Area:", validators=[DataRequired()])
    matricula = StringField("Matricula:", validators=[DataRequired()])
    data = StringField("Data:", validators=[DataRequired()])
    periodo = StringField("Periodo da Banco:", validators=[DataRequired()])
    atividade = TextAreaField("Atividade:", validators=[DataRequired()])
    enviar = SubmitField("Enviar")
