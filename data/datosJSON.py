import json

def abrirArchivo(archivo):
    with open(f"./data/{archivo}.json","r") as archivoAbrir:
        final = json.load(archivoAbrir)
    return final


def guardarArchivo(archivo,diccionario):
    objetoJson= json.dumps(diccionario, indent=4, ensure_ascii=False)
    with open(f'./data/{archivo}.json',"w") as archivoAbrir:
        archivoAbrir.write(objetoJson)



RUTA_COLECCION = 'collections' 
RUTA_BOOK = 'books'
RUTA_MOVIES = 'movies'
RUTA_MUSIC = 'songs'