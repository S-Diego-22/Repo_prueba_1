from data_stark import lista_personajes

"""
Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 
los siguientes puntos, utilizando un menú que permita 
acceder a cada uno de los puntos por separado.
A -- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B -- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C -- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
D -- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
E -- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
F -- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
G -- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
H -- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
I -- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
J -- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K -- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L -- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
M -- Listar todos los superhéroes agrupados por color de ojos.
N -- Listar todos los superhéroes agrupados por color de pelo.
O -- Listar todos los superhéroes agrupados por tipo de inteligencia

"""

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
# --------------- Funcion para usar en Punto A, Punto B --------#
def mostrar_lista_nombres(genero_personajes:str)->str:
    """
    imprime solamente la lista de superheroes si se 
    ingresa "M" solo masculinos, si 
    ingresa "F" solo femeninos.

    paso como parametro la palabra clave "genero_personajes"
    donde se almacenara la lista de nombres en base a la opcion
    que se seleccione, sea "M" o sea "F"
    """
    for superheroes in lista_personajes:
        if(superheroes["genero"] == genero_personajes):
            print(superheroes["nombre"])

# ----------------- Punto A --------------------------#
def imprimir_nombres_superheroes_masculinos()->str:
    """
    Imprime la lista de nombres del genero masculino
    """
    mostrar_lista_nombres("M")
# ----------------- Punto B ------------------------#
def imprimir_nombres_superheroes_femeninos()->str:
    """
    Imprime la lista de nombres del genero femenino
    """
    mostrar_lista_nombres("F")

# --------- Funcion para usar en Punto C - D - F - G -------------------------------------#
def calcular_maximo_minimo_altura_superheroes(genero:dict,longitud:str)-> dict:
    """
    calcula el maximo/minimo de la lista en base a la altura, donde se selecciona el
    genero requerido para calcular

    parametros: "genero" para seleccionar con cual realizar la operacion del calculo
    "M" para masculinos o "F" para femeninos. Y el parametro "longitud" donde selecciono
    entre "max" (maximo) o "min" (minimo) dependiendo de lo que se requiera calcular

    me retorna un diccionario con el superheroe en base a los parametros seleccionados
    que se quiere calcular
    """

    max_min_altura = lista_personajes[0]
    primer_max_min = True
    acumulador_altura = 0

    for superheroes in lista_personajes:
        altura_float = float(max_min_altura["altura"])
        superheroes_float = float(superheroes["altura"])
        acumulador_altura += superheroes_float
        if(superheroes["genero"] == genero):
            if(primer_max_min == True):
                max_min_altura = superheroes
                primer_max_min = False
            elif(longitud == "min" and superheroes_float < altura_float):
                    max_min_altura = superheroes
            elif(longitud == "max" and superheroes_float > altura_float):
                    max_min_altura = superheroes
    
    return max_min_altura
#-------------------- Punto C ------------------------------------------#
def calcular_maxima_altura_heroe_masculino()-> dict:
    """
    muestra diccionario superheroe masculino mas alto
    """
    heroe_mas_alto = calcular_maximo_minimo_altura_superheroes("M","max")

    print(heroe_mas_alto)
#-------------------- Punto D ------------------------------------------#
def calcular_maxima_altura_heroe_femenino()-> dict:
    """
    muestra diccionario superheroe femenino mas alto
    """
    heroe_mas_alta = calcular_maximo_minimo_altura_superheroes("F","max")

    print(heroe_mas_alta)
#-------------------- Punto E ------------------------------------------#
def calcular_minima_altura_heroe_masculino()-> dict:
    """
    muestra diccionario superheroe masculino mas bajo
    """
    heroe_mas_bajo = calcular_maximo_minimo_altura_superheroes("M","min")

    print(heroe_mas_bajo)
#-------------------- Punto F ------------------------------------------#
def calcular_minima_altura_heroe_femenino()-> dict:
    """
    muestra diccionario superheroe femenino mas bajo
    """
    heroe_mas_baja = calcular_maximo_minimo_altura_superheroes("F","min")

    print(heroe_mas_baja)
#------------------- Funcion para usar en Punto G - H -------------------#
def calcular_promedio_super_heroes(genero:str)->float:
    """
    calcula promedio en base altura dependiendo del genero ingresado,
    sea "M" o "F"

    parametro "genero" para que se pueda ingresar "M" para masculinos,
    y "F" para femeninos

    me retorna el valor del promedio en base al genero que se ingrese
    """

    acumulador_altura = 0
    contador_altura = 0

    for superheroes in lista_personajes:
        if(superheroes["genero"] == genero):
            superheroes_float = float(superheroes["altura"])
            acumulador_altura += superheroes_float
            contador_altura += 1
            
    promedio = acumulador_altura / contador_altura
    return promedio

#------------------------- Punto G -------------------------------------------------------------------#

def calcula_muestra_promedio_altura_masculinos()->str:
    """
    calcula y muestra promedio de altura de masculinos
    """
    print("Promedio altura heroes masculinos: {0:.2f}".format(calcular_promedio_super_heroes("M")))

#------------------------- Punto H ------------------------------------------------------------------#
def calcula_muestra_promedio_altura_femeninos()->str:
    """
    calcula y muestra promedio de altura de femeninos
    """
    print("Promedio altura heroes Femeninos: {0:.2f}".format(calcular_promedio_super_heroes("F")))

#------------------------- Punto I --------------------------------------------------------------#

def informar_nombre_heroe_heorina_min_max_altura()->str:

    nombre_heroe_mas_alto = calcular_maxima_altura_heroe_masculino()
    nombre_heroe_mas_alta = calcular_maxima_altura_heroe_femenino()
    nombre_heroe_mas_bajo = calcular_minima_altura_heroe_masculino()
    nombre_heroe_mas_baja = calcular_minima_altura_heroe_femenino()

    informe = "Nombre de heroe de mas altura: {0}\nNombre de heroina de mas altura: {1}\n"
    informe += "Nombre de heroe de menos altura: {2}\nNombre de heroina de menos altura: {3}"

    print(informe.format(   nombre_heroe_mas_alto["nombre"],
                            nombre_heroe_mas_alta["nombre"],
                            nombre_heroe_mas_bajo["nombre"],
                            nombre_heroe_mas_baja["nombre"]))
#-------------------------------------------------------------------------------
"""

for heroes in lista_personajes:
    heroes["color_ojos"] = heroes["color_ojos"].capitalize()
    dic_color_ojos[heroes["color_ojos"]] = 0
for heroes in lista_personajes:
    dic_color_ojos[heroes["color_ojos"]] += 1
print(dic_color_ojos)
"""
"""list_q = []

for i in lista_personajes:
    list_q.append(i["color_ojos"].capitalize())

colores_x = set(list_q)

dic_cantidad = {}
for color in colores_x:
    dic_cantidad["Cantidad"] = 0
    for heroe in lista_personajes:
        if heroe["color_ojos"].capitalize() == color:
            dic_cantidad["Color"] = color
            dic_cantidad["Cantidad"] += 1
                    
    print("Color: {0} - Cantidad: {1}".format(dic_cantidad["Color"],dic_cantidad["Cantidad"]))"""


def calcular_cantidad_color_tipo(lista_color:list,tipo:str)->  dict:

    lista_para_setear = []
    for iteracion in lista_color:
        lista_para_setear.append(iteracion[tipo].capitalize())

    tipo_seteado = set(lista_para_setear)

    dic_tipo_cantidad = {}

    for iteracion_tipo in tipo_seteado:
        dic_tipo_cantidad["Cantidad"] = 0
        for i in lista_color:
            if i[tipo].capitalize() == iteracion_tipo and i[tipo] !=  "":
                dic_tipo_cantidad["Color"] = iteracion_tipo
                dic_tipo_cantidad["Cantidad"] += 1

        print(dic_tipo_cantidad)

calcular_cantidad_color_tipo(lista_personajes,"color_pelo")


    




""" dic_cantidad_color["Color"] = colores
            
dic_cantidad_color["Cantidad"] = cantidad
            
            
print("Color: {0} - Cantidad: {1}".format(dic_cantidad_color["Color"],dic_cantidad_color["Cantidad"]))"""

"""def imprimir_menu():
    
    Imprime menu
    
    while True:
        respuesta = input("\nA-Lista nombres superheroes masculinos\nB-Lista nombres superheroes femeninos\nC-Superheroe masculino mas alto\nD-Superheroe femenino mas alto\nE-Superheroe masculino mas bajo\nF-Superheroe femenino mas bajo\nZ-Salir\n-->")
        if respuesta == "A":
            imprimir_nombres_superheroes_masculinos()
        elif respuesta == "B":
            imprimir_nombres_superheroes_femeninos()
        elif respuesta == "C":
            calcular_maxima_altura_heroe_masculino()
        elif respuesta == "D":
            calcular_maxima_altura_heroe_femenino()
        elif respuesta == "E":
            calcular_minima_altura_heroe_masculino()
        elif respuesta == "F":
            calcular_minima_altura_heroe_femenino()
        elif respuesta == "Z":
            break
imprimir_menu()"""