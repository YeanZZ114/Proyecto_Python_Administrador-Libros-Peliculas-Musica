import json
import os
from tabulate import tabulate
#Buscar en todos los json los elementos con el titulo solicitado
def searchAllsTitle():
       while(True):
        file = 'data'
        #definimos la variable para tener acceso a todos los json
        filesJson = ['books.json', 'movies.json', 'songs.json']
        #solicitamos el titulo que vamos a buscar
        titleSearch = input("Introduce el título que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            #buscamos en las rutas anteriores el titulo
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                    #encontramos el titulo solicitado
                results.extend([item for item in data if item['titulo'].lower() == titleSearch.lower()])
            else:
                #nigun elemento tenia el titulo buscado
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
                #imprimimos el elemento con el titulo solicitado
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
        
 #buscamos el autor, director o artista solicitado en todos los json    
def searchAllsA_A_D():
       while(True):
        file = 'data'
           #definimos la variable con los 3 json
        filesJson = ['books.json', 'movies.json', 'songs.json']
        #solicitamos el a/d/a 
        searchA_A_D = input("Introduce el autor/director/artista que deseas buscar: ")
        results = []
        for archive in filesJson:
            #buscamos en las rutas
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                    #encontramos el a/d/a
                results.extend([item for item in data if item['autor/director/artista'].lower() == searchA_A_D.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
                #imprimimos los elementos con el a/d/a pedido
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

#buscamos por genero en todos los json
def searchAllGender():
       while(True):
        file = 'data'
        #abrimos en una variable todos los json
        filesJson = ['books.json', 'movies.json', 'songs.json']
        #solicitamos el genero buscado
        searchGender = input("Introduce el genero que deseas buscar: ")
        results = []
        for archive in filesJson:
            #buscamos en los json
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archivo:
                    data = json.load(archivo)
                    #encontramos el genero buscamos en los elementos
                results.extend([item for item in data if item['genero'].lower() == searchGender.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            #imprimimos los elemento
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
         

            