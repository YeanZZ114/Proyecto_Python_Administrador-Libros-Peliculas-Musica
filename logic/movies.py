import json
from tabulate import tabulate 
import os
def findAllMovies():
    with open ("data/movies.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict
    
def saveAllMovies(data):
    with open ("data/movies.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo movies.json"
    
def addElementMovies():
    data = findAllMovies()
    movieTitle = input("Ingrese el titulo de su pelicula: ")
    movieDirector = input("Ingrese el/la director(a) de su pelicula: ")
    movieGender = input("Ingrese el genero de su pelicula: ")
    movieCategory = input("Ingrese la categoria de su pelicula(Infantil, Antigua,+18 ,Culto...)")
    gh = {
        "titulo" : movieTitle,
        "autor/director/artista" : movieDirector,
        "genero" : movieGender
    }
    data.append(gh)
    saveAllMovies(data)

def seeAllMovies():
    data = findAllMovies()
    datamodify = []
    for diccionario in data:
        datamodify.append(diccionario)
    print(tabulate(datamodify, headers='keys', tablefmt='grid', numalign="center"))

def listMovies():
        movies = findAllMovies("movies")
        movies1 = []
        for diccionario in movies:
              diccionario.pop("titulo")
              diccionario.pop("autor/director/artista")
              diccionario.pop("genero")
              movies1.append(diccionario)
        print(tabulate(movies1, headers="keys", tablefmt="grid"))
        
def searchCategoryMovies():
       while(True):
        file = 'data'
        filesJson = ['movies.json']
        searchCategory = input("Introduce la categoria de las peliculas que deseas buscar: ")
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