from models import Insumos, Produto
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


class Calculator:
   
   @staticmethod
   def calculator(form_data):
        resultados=[]
        total_emergia = 0

        for insumo in Insumos.query.all():
            key = f"qtd_{insumo.id}"
            qtd = form_data.get(key)

            if qtd:
                qtd = float(qtd)
                emergia = qtd * insumo.UEV
                total_emergia += emergia

                resultados.append ({
                    "item": insumo.insumo,
                    "qtd": qtd,
                    "emergia": emergia
                })
            
        return resultados, total_emergia