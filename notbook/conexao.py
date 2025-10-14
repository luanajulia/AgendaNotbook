import pyodbc

con = pyodbc.connect('Driver={SQL Server};''Server=192.168.1.203;''Database=TECsuporte;''UID=sa;''PWD=Serfeliz@1505;')
conx_help = con.cursor()