""" Ejercicio Integrador 03

La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar 
datos de heroínas y héroes, para para tener un control de las condiciones 
de heroes existentes, nos solicitan:

1 - Nombre de Heroína/Héroe
2 - EDAD (mayores a 18 años)
3 - Sexo ("m", "f" o "nb")
4 - Habilidad ("fuerza", "magia", "inteligencia").

A su vez, el programa deberá mostrar por consola lo siguiente:

A - Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
B - El sexo y nombre de Heroe | Heroína de mayor edad.
C - La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
D - El promedio de edad entre Heroinas.
E - El promedio de edad entre Heroes de fuerza. """

nombre = ""
edad = 0
sexo = ""
habilidad = ""

respuesta = "s"
iteracion = 0
bandera_mas_joven = True
contador_fuerza = 0
bandera_mayor_edad = True
heroinas_fuerza_magia = 0
contador_heroinas = 0
cantidad_edad_heroinas = 0
contador_heroes_fuerza = 0
cantidad_edad_heroes_fuerza = 0

while(respuesta == "s"):

    nombre = input("Ingrese nombre de heroe/heroina \n")
    while(nombre == ""):
        nombre = input("Error!! Ingrese nombre de heroe/heroina \n")

    edad = input("Ingrese edad de heroe/heroina \n")
    edad = int(edad)
    while(edad < 18):
        edad = input("Error!! Ingrese edad de heroe/heroina \n")
        edad = int(edad)

    sexo = input("Ingrese sexo de heroe/heroina: m - f - nb \n")
    while(sexo != "m" and sexo != "f" and sexo != "nb"):
        sexo = input("Error!! Ingrese sexo de heroe/heroina: m - f - nb \n")

    habilidad = input("Ingrese tipo de habilidad de heroe/heroina: fuerza - magia - inteligencia \n")
    while(habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = input("Error!! Ingrese tipo de habilidad de heroe/heroina: fuerza - magia - inteligencia \n")

    if(habilidad == "fuerza"):
        contador_fuerza += 1
        if(bandera_mas_joven == True):
            nombre_mas_joven = nombre
            edad_mas_joven = edad
            bandera_mas_joven = False
        elif(edad < edad_mas_joven):
            nombre_mas_joven = nombre
            edad_mas_joven = edad

    if(bandera_mayor_edad == True):
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        mayor_edad = edad
        bandera_mayor_edad = False
    elif(edad > mayor_edad):
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        mayor_edad = edad

    if(sexo == "f"):
        contador_heroinas += 1
        cantidad_edad_heroinas += edad
        if(habilidad == "fuerza" or habilidad == "magia"):
            heroinas_fuerza_magia += 1
    elif(sexo == "m" and habilidad == "fuerza"):
        contador_heroes_fuerza += 1
        cantidad_edad_heroes_fuerza += edad

        
    iteracion += 1
    respuesta = input("Seguir ingresando datos?? (s / n) \n")

if(contador_fuerza == 0):
    mensaje_a = "No se ingresaron heroes/heroinas con habilidad de fuerza \n"
else:
    mensaje_a = "El nombre de heroe/heroina de fuerza mas joven es: "+nombre_mas_joven+" con "+str(edad_mas_joven)+" años \n"

mensaje_b = "El sexo y nombre de heroe/heroina de mayor edad es: "+sexo_mayor_edad+" "+nombre_mayor_edad+" con "+str(mayor_edad)+" años \n"

if(heroinas_fuerza_magia == 0):
    mensaje_c = "No se ingresaron heroinas con habilidad de fuerza o magia \n"
else:
    mensaje_c = "La cantidad de heroinas que tienen habilidad de fuerza o magia es: "+str(heroinas_fuerza_magia)+" \n"

if(contador_heroinas == 0):
    mensaje_d = "No se ingresaron heroinas \n"
else:
    promedio_edad_heroinas = cantidad_edad_heroinas / contador_heroinas
    mensaje_d = "El promedio de edad entre heroinas es: "+str(promedio_edad_heroinas)+" años \n"


if(contador_heroes_fuerza == 0):
    mensaje_e = "No se ingresaron heroes con habilidad de fuerza \n"
else:
    promedio_edad_heroes_fuerza = cantidad_edad_heroes_fuerza / contador_heroes_fuerza
    mensaje_e = "El promedio de edad entre heroes de fuerza es: "+str(promedio_edad_heroes_fuerza)+" años"

print(mensaje_a + mensaje_b + mensaje_c + mensaje_d + mensaje_e)
