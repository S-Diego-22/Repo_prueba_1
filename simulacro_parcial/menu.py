import json
def obtener_datos_json(path:str):

    with open(path , "r") as archivo_json:
        lista_json = json.load(archivo_json)
    return lista_json


while True:
    respuesta = input("ingrese opcion: \n1 - Mostrar msj\n2 - Salir\n")
    if respuesta == "1":
        print(obtener_datos_json("c:/Users/Dgamer/Desktop/Repositorio de prueba/simulacro_parcial/data_stark.json"))
    elif respuesta == "2":
        break