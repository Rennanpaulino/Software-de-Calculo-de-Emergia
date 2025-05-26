from models import *
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


class Calculator:
   
   @staticmethod
   def calculator(self):
        resultados=[]
        total_emergia = 0

        for insumos in Insumos.query.all():
            qtd = float(request.form.get(insumo.insumo, 0))
            emergia = qtd * insumo.UEV
            total_emergia += emergia
            resultados.append ({
                "item": insumo.insumo,
                "emergia": emergia
            })
        return resultados, total_emergia