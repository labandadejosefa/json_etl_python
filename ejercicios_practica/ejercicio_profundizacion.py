#Ejercicio de PROFUNDIZACIÓN - JSON_ETL - MELI

import json
import requests
import matplotlib.pyplot as plt
from sqlalchemy import true

def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    response = requests.get(url) #accedo y guardo en "response" lo que pido con requests, de la url
    json_data = response.json() #obtengo esa información como archivo json
    dataset = json_data["results"] #accedo a "results" del original
    filtrada_pesos = [x for x in dataset if x["currency_id"]=='ARS'] 

    #--ahora tengo que escribir esta lista como DICCIO, sólo con {"price": ..., "condition": ...} 
    lista_diccios = [dict(price = x["price"], condition = x["condition"]) for x in filtrada_pesos]

    return lista_diccios


def transform(dataset,min,max): 
    lista_menor = [x for x in dataset if x["price"]< min]
    lista_intervalo = [x for x in dataset if (x["price"]>= min and x["price"]<= max)]
    lista_mayor = [x for x in dataset if x["price"]> max]

    lista_final = [len(lista_menor),len(lista_intervalo), len(lista_mayor)]
    
    return lista_final 


def report(data):
    valores = ['Menores al MÍNIMO', 'En el INTERVALO', 'Mayores al MÁXIMO']
    fig = plt.figure()
    fig.suptitle('Distribución de precios de alquileres', fontsize = 14)
    explode = (0,0.1,0)
    colores = ['#008080','#F75D59','#F4A460']

    plt.pie(data, labels=valores, explode=explode, autopct= '%1.1f%%', shadow=True, startangle=90, colors=colores)
    plt.axis('equal')
    plt.show()



if __name__ == "__main__":
    min = float(input('Ingrese un valor MÍNIMO de precio de alquiler:\n$'))
    max = float(input('Ingrese un valor MÁXIMO de precio de alquiler:\n$'))

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)

