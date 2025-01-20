import json
from tabulate import tabulate
import os

def findAllSongs():
    with open ("data/songs.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict

def saveAllSongs(data):
    with open ("data/songs.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo songs.json"

def addElementSongs():
    data = findAllSongs()
    songTitle = input("Ingrese el titulo de su cancion: ")
    songArtist = input("Ingrese el/la artista de su cancion: ")
    songGender = input("Ingrese el genero de su cancion: ")
    songCategory = input("Ingrese la categoria de su cancion(Infantil, Folclor, Moderna...): ")
    jh = {
        "titulo" : songTitle,
        "autor/director/artista" : songArtist,
        "genero" : songGender,
        "categoria" : songCategory
    }
    data.append(jh)
    saveAllSongs(data)

def seeAllSongs():
    data = findAllSongs()
    datamodify = []
    for diccionario in data:
           datamodify.append(diccionario)
    print(tabulate(datamodify, headers='keys', tablefmt='grid', numalign="center"))

def listSongs():
        songs = findAllSongs("songs")
        songs1 = []
        for diccionario in songs:
              diccionario.pop("titulo")
              diccionario.pop("autor/director/artista")
              diccionario.pop("genero")
              songs1.append(diccionario)
        print(tabulate(songs1, headers="keys", tablefmt="grid"))

def searchCategorySongs():
       while(True):
        file = 'data'
        filesJson = ['Songs.json']
        searchCategory = input("Introduce la categoria de las canciones que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                results.extend([item for item in data if item['categoria'].lower() == searchCategory.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para esta categoria")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue