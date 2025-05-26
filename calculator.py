from models import Insumos, Produto
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


class Calculator:
   
   @staticmethod
   def calculator(form_data):
        resultados=[]
        total_emergia = 0
        E = 0  # Insumos comprados/importados
        N = 0  # Insumos não renováveis locais
        R = 0  # Insumos renováveis locais

        for insumo in Insumos.query.all():
            key = f"qtd_{insumo.id}"
            qtd = form_data.get(key)

            if qtd:
                qtd = float(qtd)
                emergia = qtd * insumo.UEV
                total_emergia += emergia

                if insumo.tipo == "R":
                        R +=emergia
                elif insumo.tipo == "N":
                        N += emergia
                elif insumo.tipo == "E":
                        E += emergia


                resultados.append ({
                    "item": insumo.insumo,
                    "qtd": qtd,
                    "emergia": emergia
                })

            # Cálculo dos índices
        EYR = total_emergia / E if E != 0 else None
        ELR = (E + N) / R if R != 0 else None
        ESI = (EYR / ELR) if (EYR and ELR and ELR != 0) else None

        indices = {
            "EYR": round(EYR, 4) if EYR else None,
            "ELR": round(ELR, 4) if ELR else None,
            "ESI": round(ESI, 4) if ESI else None
        }
        return resultados, total_emergia, indices
