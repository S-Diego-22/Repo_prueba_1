from main import pokemones

"""
{
    "id": 1,
    "nombre": "bulbasaur",
    "tipo": ["planta"],
    "evoluciones": ["ivysaur", "venusaur"],
    "poder": 4,
    "fortaleza":["agua"],
    "debilidad":["fuego"]
},
"""
def obtener_nombre_pokemon(dic_pokemones:dict):
    """
    Recorre los diccionarios de la lista de pokemones para obtener el nombre
    de cada uno

    parametros: diccionario nuevo

    retorna: none
    """

    for pokemon in pokemones:
        dic_pokemones = pokemon["nombre"]
    return dic_pokemones

nombres = obtener_nombre_pokemon(["nombre"])

print(nombres)