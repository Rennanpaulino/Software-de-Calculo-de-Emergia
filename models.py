from main import app
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import generate_password_hash, check_password_hash

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lci.db'
db = SQLAlchemy(app)

produto_insumo = db.Table('produto_insumo',
    db.Column('produto_id', db.Integer, db.ForeignKey('produto.id'), primary_key=True),
    db.Column('insumo_id', db.Integer, db.ForeignKey('insumos.id'), primary_key=True)
)

class Insumos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    insumo = db.Column(db.String(100), unique = True, nullable = False)
    unidade = db.Column(db.String (10), nullable = False)
    UEV = db.Column (db.Float, nullable = False)
    tipo = db.Column (db.String (1), nullable =False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(100), unique = True, nullable = False)
    insumos = db.relationship(
        'Insumos',
        secondary = produto_insumo,
        backref='produto',
        lazy = 'subquery'
    )

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    senha_hash = db.Column(db.String(8), nullable= False)

    def setSenha(self, senha):
        self.senha_hash = generate_password_hash(senha).decode('utf-8')

    def verifySenha(self,senha):
        return check_password_hash(self.senha_hash,)
