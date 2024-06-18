from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instância do flask
app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage.db' #define a configuração de uri; /// significa que é um arquivo local
db = SQLAlchemy(app)

from app.controllers import defoult