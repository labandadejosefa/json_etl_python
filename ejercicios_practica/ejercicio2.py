# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt
from sqlalchemy import true

import seaborn as sns

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)actualizaciones@infd.edu.ar 
    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get(url)
    data = response.json()

    usuarios = []

    for user in data:
        if user['completed'] == True:
            usuario = user['userId']
            usuarios.append(usuario)
    
    repeticiones = dict(zip(usuarios,map(lambda x: usuarios.count(x),usuarios)))

    for k,v in repeticiones.items():
        print(f'El usuario {k}, completó {v} cursos') #Este FOR para imprimir el diccio con "usuario:cursos que completó"
    
    figu = plt.figure()
    st = figu.suptitle('Cursos completados por usuario', fontsize=13)
    
    palette = sns.color_palette("inferno_r", 10)

    plt.bar(range(len(repeticiones)), repeticiones.values(), align='center', color=palette)
    plt.xticks(range(len(repeticiones)), list(repeticiones.keys()))

    plt.xlabel('Usuarios')
    plt.ylabel('Cursos completados')
    plt.show()

    print("terminamos")


    