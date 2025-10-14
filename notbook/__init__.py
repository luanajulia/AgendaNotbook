from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pyodbc

import urllib.parse
from sqlalchemy import create_engine
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=192.168.1.203;DATABASE=TECsuporte;UID=sa;PWD=Serfeliz@1505;')
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(connection_string)

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] =   "mssql+pyodbc:///?odbc_connect=%s" % params
app.config["SECRET_KEY"] = "a23c4f2fe076b10bccd840626a026aa0"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from notbook import routes
