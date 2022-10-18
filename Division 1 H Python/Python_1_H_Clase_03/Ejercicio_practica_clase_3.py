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
Desafío #00:

A - Analizar detenidamente el set de datos
B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
G - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
H - Calcular e informar cual es el superhéroe más y menos pesado.
I - Ordenar el código implementando una función para cada uno de los valores informados.
J - Construir un menú que permita elegir qué dato obtener

"""
"""# A
for datos_heroes in lista_personajes:
    print(datos_heroes)"""

"""# B
for datos_heroes in lista_personajes:
    print(datos_heroes["nombre"])"""

"""# C
for datos_heroes in lista_personajes:
    float(datos_heroes["altura"])
    print(datos_heroes["nombre"],float(datos_heroes["altura"]))"""

# D
def calcular_heroe_mas_alto():
    heroe_mas_alto = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["altura"])
        altura_maxima_float = float(heroe_mas_alto["altura"])
        if(dato_heroe_float > altura_maxima_float):
            heroe_mas_alto = dato_heroe

    print("Heroe mas alto\nAltura: {0}\n".format(float(heroe_mas_alto["altura"])))


# Esta es otra forma de hacer el maximo
"""altura_maxima = lista_personajes[0]
altura_maxima_float = lista_personajes[0]["altura"]

for dato_heroe in lista_personajes:
    
    dato_heroe_float = float(dato_heroe["altura"])
    
    if(dato_heroe_float > altura_maxima_float):
        altura_maxima = dato_heroe
        altura_maxima_float = dato_heroe_float

print(altura_maxima)"""

# E
def calcular_heroe_mas_bajo():
    heroe_mas_bajo = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["altura"])
        altura_minima_float = float(heroe_mas_bajo["altura"])
        if(dato_heroe_float < altura_minima_float):
            heroe_mas_bajo = dato_heroe

    print("Heroe mas bajo\nAltura: {0}\n".format(float(heroe_mas_bajo["altura"])))

# F
def calcular_promedio_altura_total_heroes():
    acumulador_altura = 0

    for promedio_altura in lista_personajes:
        acumulador_altura_float = float(promedio_altura["altura"])
        acumulador_altura += acumulador_altura_float

    print("Altura promedio\n{0:.2f}\n".format(acumulador_altura/len(lista_personajes)))

# G 1
def mostrar_nombre_heroe_mas_alto():
    heroe_mas_alto = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["altura"])
        altura_maxima_float = float(heroe_mas_alto["altura"])
        if(dato_heroe_float > altura_maxima_float):
            heroe_mas_alto = dato_heroe

    print("Heroe mas alto\nNombre: {0}\n".format(heroe_mas_alto["nombre"]))

# G 2
def mostrar_nombre_heroe_mas_bajo():
    heroe_mas_bajo = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["altura"])
        altura_minima_float = float(heroe_mas_bajo["altura"])
        if(dato_heroe_float < altura_minima_float):
            heroe_mas_bajo = dato_heroe
        
    print("Heroe mas bajo\nNombre: {0}\n".format(heroe_mas_bajo["nombre"]))

# H 1
def calcular_heroe_mas_pesado():
    heroe_mas_pesado = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["peso"])
        peso_maximo_float = float(heroe_mas_pesado["peso"])
        if(dato_heroe_float > peso_maximo_float):
            heroe_mas_pesado = dato_heroe

    print("Heroe mas pesado\nNombre: {0} - Peso: {1}\n".format(heroe_mas_pesado["nombre"],float(heroe_mas_pesado["peso"])))

# H 2
def calcular_heroe_mas_liviano():
    heroe_mas_liviano = lista_personajes[0]

    for dato_heroe in lista_personajes:
        dato_heroe_float = float(dato_heroe["altura"])
        peso_minimo_float = float(heroe_mas_liviano["altura"])
        if(dato_heroe_float < peso_minimo_float):
            heroe_mas_liviano = dato_heroe

    print("Heroe mas bajo\nNombre: {0} - Peso: {1}\n".format(heroe_mas_liviano["nombre"],float(heroe_mas_liviano["peso"])))

while True:
    respuesta = input("\n1-Longitud de heroe mas alto\n2-Longitud de heroe mas bajo\n3-Promedio de altura total de heroes\n4-Nombre de heroe mas alto\n5-Nombre de heroe mas bajo\n6-Nombre y peso de heroe mas pesado\n7-Nombre y peso de heroe mas liviano\n8-Salir\n-->")
    if(respuesta == "1"):
        calcular_heroe_mas_alto()
    elif(respuesta == "2"):
        calcular_heroe_mas_bajo()
    elif(respuesta == "3"):
        calcular_promedio_altura_total_heroes()
    elif(respuesta == "4"):
        mostrar_nombre_heroe_mas_alto()
    elif(respuesta == "5"):
        mostrar_nombre_heroe_mas_bajo()
    elif(respuesta == "6"):
        calcular_heroe_mas_pesado()
    elif(respuesta == "7"):
       calcular_heroe_mas_liviano()
    elif(respuesta == "8"):
        break


