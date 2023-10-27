from collections import namedtuple
import csv
from datetime import datetime


Entrenos = namedtuple("Entrenos", "tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido")
def lee_entrenos(fichero):

    res = []
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M").date() 
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = float(frecuencia)
            compartido = bool(compartido)
            if compartido == "N":
                compartido = False 
            else:
                compartido = True
            tupla = Entrenos(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            res.append(tupla)
            

    return res


