
from data_stark import lista_personajes
"""
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }
"""

"""
1.1 -- Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
-- nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un 
nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
-- En el caso que el nombre del personaje contenga el 
   artículo ‘the’ se deberá omitir de las iniciales
-- Se deberá verificar si el nombre contiene un guión ‘-’ y sólo 
   en el caso que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
-- Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.

1.2 -- Crear la función ‘definir_iniciales_nombre’ la cual 
recibirá como parámetro:
heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario 
recibido como parámetro. La clave se deberá llamar ‘iniciales’ 
y su valor será el obtenido de llamar a la función ‘extraer_iniciales’
La función deberá validar:
-- Que el dato recibido sea del tipo diccionario
-- Que el  diccionario contengan la clave ‘nombre’  
-- En caso de encontrar algún error retornar False, 
   caso contrario retornar True

1.3 -- Crear la función ‘agregar_iniciales_nombre’ la cual recibirá 
como parámetro:
-- lista_heroes: lista de personajes
Se deberá validar:
-- Que lista_heroes sea del tipo lista
-- Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada 
héroe a la función definir_iniciales_nombre.

En caso que la función definir_iniciales_nombre() retorne False 
entonces se deberá detener la iteración e informar por pantalla el 
siguiente mensaje: ‘El origen de datos no contiene el formato correcto’ 
La función deberá devolver True en caso de haber finalizado con éxito 
o False en caso de que haya ocurrido un error


"""

def extraer_iniciales(nombre_heroe:str):

    iniciales = ""

    if(len(nombre_heroe) > 0):    
        if(nombre_heroe.count("the ") > 0):
            nombre_heroe = nombre_heroe.replace("the ","")
        if(nombre_heroe.count("-") > 0):
            nombre_heroe = nombre_heroe.replace("-"," ")
        nombre_heroe = nombre_heroe.split(" ")
        for palabras in nombre_heroe:
            iniciales += "{0}.".format(palabras[0].upper())
    else:
        return "N/A"


    return iniciales

extraer_iniciales("nombre")


"""for heroe in lista_personajes:
    nombre_heroe = heroe["nombre"]
    
    print(extraer_iniciales(nombre_heroe))"""


# 1 crear funcion llamada "definir_iniciales_nombre" --> ok
# 2 parametro "heroe" que sera diccionario --> ok
# 3 validar que el dato sea tipo diccionario --> ok
# 4 validar que el diccionario contenga la clave "nombre" --> ok
# 5 si se encuentra algun error retornar "False" de lo contrario --> ok
#   retornar True
# 6 la funcion debe agregar una nueva clave llamada "iniciales" --> ok
# 7 extraer el valor de la clave nueva de la funcion "extraer_iniciales" --> ok
def definir_iniciales_nombre(heroe:dict):
    retorno = True
    
    if(type(heroe) == dict):
        if "nombre" in heroe:
            heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
            print(heroe)
        else:
            retorno = False
    else:
        retorno = False
    return retorno

"""for heroe in lista_personajes:
    definir_iniciales_nombre(heroe)"""
# 1 - Crear la función ‘agregar_iniciales_nombre’ --> ok
# 2 - parámetro: (lista_heroes: lista de personajes) --> ok
# 3 - validar que lista_heroes sea del tipo lista --> ok
# 4 - validar que la lista contenga al menos un elemento
# 5 - La función deberá iterar la lista_heroes pasándole cada 
#     héroe a la función definir_iniciales_nombre.
# 6 - En caso que la función definir_iniciales_nombre() retorne False 
#     entonces se deberá detener la iteración e informar por pantalla el 
#     siguiente mensaje: ‘El origen de datos no contiene el formato correcto’
# 7 - La función deberá devolver True en caso de haber finalizado con éxito 
#     o False en caso de que haya ocurrido un error

def agregar_iniciales_nombre(lista_heroes:list):
    retorno = True
    if(type(lista_heroes) == list):
        if(len(lista_heroes) > 0):
            for heroe in lista_heroes:
                if(definir_iniciales_nombre(heroe) == True):
                    heroe = definir_iniciales_nombre(heroe)
                else:
                    print("El origen de datos no contiene el formato correcto")
                    retorno = False
                    break
        else:
            retorno = False
    return retorno