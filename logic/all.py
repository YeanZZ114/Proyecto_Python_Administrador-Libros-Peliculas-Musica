import json
import os
from tabulate import tabulate

def searchAllsTitle():
       while(True):
        file = 'data'
        filesJson = ['books.json', 'movies.json', 'songs.json']
        titleSearch = input("Introduce el título que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                results.extend([item for item in data if item['titulo'].lower() == titleSearch.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para este titulo")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue
        
def searchAllsA_A_D():
       while(True):
        file = 'data'
        filesJson = ['books.json', 'movies.json', 'songs.json']
        searchA_A_D = input("Introduce el autor/director/artista que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                results.extend([item for item in data if item['autor/director/artista'].lower() == searchA_A_D.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para este autor/director/artista")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue
def searchAllGender():
       while(True):
        file = 'data'
        filesJson = ['books.json', 'movies.json', 'songs.json']
        searchGender = input("Introduce el genero que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                results.extend([item for item in data if item['genero'].lower() == searchGender.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para este genero")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue
         

            