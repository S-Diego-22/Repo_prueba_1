lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def encontrar_el_minimo_maximo(lista_calculada:list,orden:str)-> list:

    result = 0

    for i in range(len(lista_calculada)):
        if orden == "max_a_min" and lista_calculada[i] > lista_calculada[result]:
            result = i
        if orden == "min_a_max" and lista_calculada[i] < lista_calculada[result]:
            result = i

    return result

def ordenar_lista(lista_a_ordenar:list) -> list:
    lista_copia = lista_a_ordenar[:]

    lista_ordenada = []

    while len(lista_copia) > 0:
        elemento = encontrar_el_minimo_maximo(lista_copia,"min_a_max")
        lista_ordenada.append(lista_copia.pop(elemento))
    return lista_ordenada

resultado = ordenar_lista(lista)

print(resultado)