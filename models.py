from main import app
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

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

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(100), unique = True, nullable = False)
    insumos = db.relationship(
        'Insumos',
        secondary = produto_insumo,
        backref='produto',
        lazy = 'subquery'
    )

