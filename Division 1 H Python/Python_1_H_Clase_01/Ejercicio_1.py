#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

tipo = ""
precio = 0
cantidad = 0
marca = ""
fabricante = ""

bandera_precio = True
bandera_cantidad = True

contador_barbijos = 0
contador_jabones = 0
cantidad_jabones = 0

for iteracion in range(5):
    tipo = input("Ingrese el tipo de producto: barbijo - jabon - alcohol \n")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("Error!! Ingrese el tipo de producto: barbijo - jabon - alcohol \n")

    precio = input("Ingrese el precio entre 100 y 300 \n")
    precio = int(precio)
    while(precio < 100 or precio > 300 ):
        precio = input("Error!! Ingrese el precio entre 100 y 300 \n")
        precio = int(precio)

    cantidad = input("Ingrese la cantidad de unidades \n")
    cantidad = int(cantidad)
    while(cantidad < 0 or cantidad > 1000):
        cantidad = input("Error!! Ingrese la cantidad de unidades \n")
        cantidad = int(cantidad)
    
    marca = input("Ingrese la marca del producto \n")
    
    fabricante = input("Ingrese el fabricante del producto \n")

    if(tipo == "barbijo"):
        contador_barbijos += 1
        if(bandera_precio == True):
            precio_caro = precio
            cantidad_maxima = cantidad
            fabricante_maximo = fabricante
            bandera_precio = False
        elif(precio > precio_caro):
            precio_caro = precio
            cantidad_maxima = cantidad
            fabricante_maximo = fabricante

    if(bandera_cantidad == True):
        tipo_mas_cantidad = tipo
        unidades_maximo = cantidad
        fabricante_mas_cantidad = fabricante
        bandera_cantidad = False
    elif(cantidad > unidades_maximo):
        tipo_mas_cantidad = tipo
        unidades_maximo = cantidad
        fabricante_mas_cantidad = fabricante

    if(tipo == "jabon"):
        contador_jabones += 1
        cantidad_jabones += cantidad

if(contador_barbijos == 0):
    print("No se ingresaron barbijos \n")
else:
    print("El barbijo mas caro cuesta: $"+str(precio_caro)+", la cantidad de unidades: "+str(cantidad_maxima)+", del fabricante: "+fabricante_maximo+"\n")

print("El ítem con más unidades es: "+tipo_mas_cantidad+", del fabricante: "+fabricante_mas_cantidad+"\n")

if(contador_jabones == 0):
    print("No se ingresaron jabones \n")
else:
    print("En total hay "+str(cantidad_jabones)+" unidades de jabones \n")
