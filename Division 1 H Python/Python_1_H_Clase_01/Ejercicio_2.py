""" Ejercicio Integrador 02

Suasnavas Diego

La división de alimentos está trabajando en un pequeño software
para cargar las compras de ingredientes para la cocina de Industrias Wayne. 

Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.

1 - PESO: (entre 10 y 100 kilos)
2 - PRECIO POR KILO: (mayor a 0 [cero]).
3 - TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).

Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento 
sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento 
sobre el precio bruto.

A - El importe total a pagar, BRUTO sin descuento.
B - El importe total a pagar con descuento (Solo si corresponde).
C - Informar el tipo de alimento más caro.
D - El promedio de precio por kilo en total. """

peso = 0
precio = 0
tipo = ""

iteracion = 0
respuesta = "s"
total_compra = 0
total_kilo = 0
descuento = 0.0
bandera_tipo_caro  = True

while(respuesta == "s"): #El bucle se repite solamente al ingresar la "s"

    peso = input("Ingrese el peso entre 10 y 100 kilos \n")
    peso = float(peso)
    while(peso < 10 or peso > 100):
        peso = input("Error!! Ingrese el peso entre 10 y 100 kilos \n")
        peso = float(peso)

    precio = input("Ingrese el precio por kilo \n")
    precio = float(precio)
    while(precio < 1):
        precio = input("Error!! Ingrese el precio por kilo \n")
        precio = float(precio)
        
    tipo = input("Ingrese el tipo de alimento: vegetal - animal - mezcla \n")
    while(tipo != "vegetal" and tipo != "animal" and tipo != "mezcla"):
        tipo = input("Error!! Ingrese el tipo de alimento: vegetal - animal - mezcla \n")

    total_compra += precio # Esto es para sumar es total de precios ingresados
    total_kilo += peso # Acá acumulo el peso total por cada iteracion

    if(bandera_tipo_caro == True): # Para entrar solo una ves y tener el precio y tipo
        precio_mas_caro = precio
        tipo_mas_caro = tipo
        bandera_tipo_caro = False # Para que no entre mas y directamente vaya al elif
    elif(precio > precio_mas_caro): # Aca comparo para obtener le precio mas alto con su tipo
        precio_mas_caro = precio
        tipo_mas_caro = tipo

    iteracion += 1
    respuesta = input("Seguir ingresando?? (s / n) \n") # si se ingresa otra letra que no sea la "s" sale del bucle

if(total_kilo > 300): # Condicionales para saber que descuento se aplica
    descuento = 25.0
elif(total_kilo > 100):
    descuento = 15.0

importe_total = total_compra - (total_compra * descuento / 100) 

if(descuento == 0.0): 
    mensaje_b = "No hay descuento \n"
else:
    mensaje_b = "El descuento es del "+str(descuento)+"% y el importe con descuesto es: $"+str(importe_total)+"\n" # se muestra este mensaje en caso que haya descuento

promedio_precio = total_compra / iteracion

mensaje_a = "El importe bruto es de: $"+str(total_compra)+"\n"
mensaje_c = "El tipo de alimento mas caro es: "+tipo_mas_caro+"\n"
mensaje_d = "El promedio de precio por kilo es: $"+str(promedio_precio)

print(mensaje_a + mensaje_b + mensaje_c + mensaje_d)