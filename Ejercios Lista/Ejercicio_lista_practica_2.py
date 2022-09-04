"""
Ejercicio 02

1- Una cervecería desea guardar los nombres de sus clientes a medida que van realizando 
los pedidos para luego imprimir los nombres de todos los clientes. Se solicita crear 
un programa que almacene dichos nombres en una lista hasta que el usuario desee 
y luego, una vez finalizado el ingreso, imprima la lista por pantalla.

2- Utilizando el programa anterior, ahora se necesitan guardar más datos del cliente. 
Se tiene que guardar en cada posición de la lista,  el nombre, la cantidad de 
cervezas compradas y la edad del cliente. Para lo cual se deberá crear un 
diccionario con el siguientes datos

-- nombre: Karen
-- cantidad_cervezas: 2
-- edad: 36

Al finalizar la carga se deberán mostrar por pantalla a todos los clientes que sean mayores de 30 años.

3- Se anexará al programa anterior una lista que contenga diccionarios que 
guarden las distintas características que tienen las cervezas que se venden. 
Por ejemplo: { “Ipa”: { “codigo” : 25007 , ”ibu” : 18 , ”marca” : ”Patagonia” } }

4 - Se agrega al diccionario del punto dos un campo que indique que tipo de 
cerveza consume, ya que estas pueden ser más de una y de 
distinto tipo, dicho campo deberá ser una lista.

--nombre: Marina
--cantidad: 2
--edad: 30
--cerveza_comprada: ipa , apa

Imprimir los datos de la cerveza ipa junto a los datos del cliente

"""
"""lista_nombres = []

respuesta = "si"
nombre_cliente = ""
iteraciones = 0

while(respuesta == "si"):

    nombre_cliente = input("Ingrese nombre del cliente \n")
    while(nombre_cliente == ""):
        nombre_cliente = input("Nombre no valido, ingrese nombre del cliente \n")

    lista_nombres.append(nombre_cliente)

    iteraciones += 1
    respuesta = input("Seguir ingresando?? si / no \n")

print(lista_nombres)"""

lista_nombres = []

nombre_cliente = ""
edad_cliente = 0
cantidad_cervezas = 0

respuesta = "si"
iteraciones = 0

while(respuesta == "si"):

    nombre_cliente = input("Ingrese nombre del cliente \n")
    while(nombre_cliente == ""):
        nombre_cliente = input("Nombre no valido, ingrese nombre del cliente \n")

    edad_cliente = input("Ingrese edad del cliente \n")
    edad_cliente = int(edad_cliente)
    while(edad_cliente < 18):
        edad_cliente = input("Error!! Ingrese edad del cliente \n")
        edad_cliente = int(edad_cliente)

    cantidad_cervezas = input("Ingrese cantidad de cervezas que compro el cliente \n")
    cantidad_cervezas = int(cantidad_cervezas)
    while(cantidad_cervezas < 1):
        cantidad_cervezas = input("Error!! Ingrese cantidad de cervezas que compro el cliente \n")
        cantidad_cervezas = int(cantidad_cervezas)
    
    dic_clientes = {"Nombre":nombre_cliente,"Edad":edad_cliente,"cantidad de cervezas":cantidad_cervezas}

    lista_nombres.append(dic_clientes)

    #if(edad_cliente > 30):
        

    iteraciones += 1
    respuesta = input("Seguir ingresando?? si / no \n")

print(lista_nombres)

