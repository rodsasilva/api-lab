from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Criar uma API Flask
app = Flask(__name__)
# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog1.db'

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela postagem

class usuarios(db.Model):
    __tablename__='usuarios'
    id_usuarios = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.Numeric)
    created_on=db.Column(db.DateTime)
    admin = db.Column(db.Boolean)
    
    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
# Executar o comando para criar o banco de dados
"""def inicializar_banco():
    db.drop_all()
    db.create_all()
    #usuário administradores
    usu= usuarios(username='rodrigo2',name='rodrigo', email='oi@oi.com.br',password ='12345',admin=True) # LEMBRANDO QUE É DA CLASSE AUTOR
    db.session.add(usu)
    db.session.commit()"""

usuarios
"""if __name__ == '__main__':
    inicializar_banco()"""