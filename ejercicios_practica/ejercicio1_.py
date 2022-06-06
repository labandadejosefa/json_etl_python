# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    idolo = {
            "nombre": "Carl",
            "apellido": "Sagan",
            "DNI": 5777552,
            "armario": [
                {
                 "prenda": "chaqueta", 
                 "cantidad": 5, 
                 "color": "caqui"
                },
                {
                 "prenda": "polera", 
                 "cantidad": 7, 
                 "color": "varios"
                },
                {
                 "prenda": "parka", 
                 "cantidad": 1, 
                 "color": "naranja"
                },
                {
                 "prenda": "camisa", 
                 "cantidad": 3, 
                 "color": "celeste"
                }
                ]
            }

    with open('primer_json.json', 'w') as jsonfile:
        datos = [idolo]
        json.dump(datos, jsonfile, indent=4)


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    with open('primer_json.json', 'r') as jsonfile:
        json_datos = json.load(jsonfile)

        json_string = json.dumps(json_datos, indent=4)    

        print('Muestro el contenido del archivo primer_json:\n')
        print(json_string)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")