import json
from tabulate import tabulate
import os

def findAllBooks():
    with open ("data/books.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict  
    
def saveAllBooks(data):
    with open ("data/books.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo books.json"

def addElementBooks():
    data = findAllBooks()
    bookTitle = input("Ingrese el titulo de su libro: ")
    bookDirector = input("Ingrese el/la autor(a) de su libro: ")
    bookGender = input("Ingrese el genero de su libro: ")
    bookCategory = input("Ingrese la categoria de su libro(Novela, Biografia, Poesia...)")
    sh = {
        "titulo" : bookTitle,
        "autor/director/artista" : bookDirector,
        "genero" : bookGender,
        "categoria" : bookCategory
    }
    data.append(sh)
    saveAllBooks(data)

def seeAllBooks():
    data = findAllBooks()
    datamodify = []
    for diccionario in data:
           datamodify.append(diccionario)
    print(tabulate(datamodify, headers='keys', tablefmt='grid', numalign="center"))

def listBooks():
        books = findAllBooks("books")
        books1 = []
        for diccionario in books:
              diccionario.pop("titulo")
              diccionario.pop("autor/director/artista")
              diccionario.pop("genero")
              books1.append(diccionario)
        print(tabulate(books1, headers="keys", tablefmt="grid"))
        
def searchCategoryBooks():
       while(True):
        file = 'data'
        filesJson = ['books.json']
        searchCategory = input("Introduce la categoria de los libros que deseas buscar: ")
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