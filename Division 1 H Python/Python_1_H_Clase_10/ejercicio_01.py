from random import randint, shuffle
from functools import reduce


lista_palabras = [
    "Goku", "Vegeta", "Frieza", "Cell", "Beerus", 'Krillin'
]

# Refactoprizar la funcion clasica usando lambda
def sup_triangulo(base: int, altura: int) -> float:
    return (base*altura)/2

calculo = lambda base, altura : (base * altura) / 2
#print(calculo(15,5))


# Refactorizar la funcion clasica usando lambda y map
def aplicar_mayusculas(lista_palabras: list) -> list:
    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].upper()
    return lista_palabras

lista_mayusculas = list(map(lambda elemento : elemento.upper(),lista_palabras))

#print(lista_mayusculas)

# Refactorizar la funcion usando lambda y reduce
def obtener_mas_letras(lista: list) -> str:
    seleccionado = ''
    for palabra in lista:
        if len(palabra) > len(seleccionado):
            seleccionado = palabra
    return seleccionado

elemento_mas_letras = reduce(lambda elemento_uno , elemento_dos: elemento_uno if len(elemento_uno) > len(elemento_dos) else elemento_dos , lista_palabras)

#print(elemento_mas_letras)

# refactorizar la funcion usando lambda y filter
def obtener_nombres_cantidad_letras(lista: list, cantidad: int) -> list:
    seleccionados = list()
    for palabra in lista:
        if len(palabra) == cantidad:
            seleccionados.insert(0, palabra)
    return seleccionados

cantidad_letras_elemento = list(filter(lambda elemento : len(elemento) == 6 , lista_palabras))

#print(cantidad_letras_elemento)

# refactorizar usando shuffle
def ordenar_random_lista(lista: list) -> list:
    maximo = len(lista)
    desordenada = list()
    while len(desordenada) < len(lista):
        indice = randint(0, maximo)
        for elemento in lista:
            desordenada.insert(indice, elemento)
    return desordenada

shuffle(lista_palabras)
#print(lista_palabras)

# Refactorizar usando sort y lambda
def ordenar_burbujeo(lista: list) -> list:
    lista_copia = lista.copy()
    for i in range(len(lista_copia)-1):
        for j in range(i+1, len(lista_copia)):
            if lista_copia[i] > lista_copia[j]:
                lista_copia[i], lista_copia[j] = lista_copia[j], lista_copia[i]
    return lista_copia

orden = sorted(lista_palabras , key = lambda x : x[0])

#print(orden)


heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

# Refactorizar usando zip
for ind_h in range(len(heroes)):
    for ind_a in range(ind_h, len(ataques)):
        for ind_v in range(ind_h, len(villanos)):
            mensaje =\
                f"""
                {heroes[ind_h].capitalize()}
                Lanza un {ataques[ind_a].capitalize()}
                a {villanos[ind_v].capitalize()}
                """
           # print(mensaje)
            break
        break

    #print(mensaje)

for h, v, a in zip(heroes,villanos,ataques):
    print("{0} \nlanza su {2} \na {1}\n".format(h,v,a).capitalize())