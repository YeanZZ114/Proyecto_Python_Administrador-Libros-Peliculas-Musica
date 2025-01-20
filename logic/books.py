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
    print(data)
    bookTitle = input("Ingrese el titulo de su libro: ")
    bookDirector = input("Ingrese el/la autor(a) de su libro: ")
    bookGender = input("Ingrese el genero de su libro: ")
    sh = {
        "book_title" : bookTitle,
        "book_author" : bookDirector,
        "book_gender" : bookGender
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
              diccionario.pop("book_title")
              diccionario.pop("book_author")
              diccionario.pop("book_gender")
              books1.append(diccionario)
        print(tabulate(books1, headers="keys", tablefmt="grid"))

with open('data/books.json', "r", encoding="utf-8") as file:
    colectionBooks = json.load(file)
if not all(key in colectionBooks for key in ["books", "movies", "songs"]):
                colectionBooks = {"books": [], "movies": [], "songs": []}
def searchBooks():
       while(True):
        file = 'data'
        filesJson = ['books.json', 'movies.json', 'musics.json']
        titleSearch = input("Introduce el título que deseas buscar: ")
        resultados = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archive:
                    data = json.load(archive)
                resultados.extend([item for item in data if item['titulo'].lower() == titleSearch.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if resultados:
            print(tabulate(resultados, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para este titulo")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue
#def searchBooksTitle():
 #   books = findAllBooks("books")
  #  listBooks()
   # searchTitle = input("Introduce el Título que deseas buscar: ").lower()
    #results = []
  #  books for books, in books :
   #         for item in items:
    #            if searchTitle in str(item.get("book_title", "")).lower():
     #                   itemData = {
      #                      "Título": item.get("book_title", ""),
       #                     "Autor/Director/Artista": item.get("book_author", ""),
        #                    "Género": item.get("book_gender", ""),
         #               }
          #              results.append(itemData)
 #  if results:
  #              print(tabulate(results, headers="keys", tablefmt="grid"))
   # else:
    #            print("No se encontraron elementos que coincidan con tu búsqueda por título.")

def searchBooksAuthor():
    searchAuthor = input("Introduce el Autor/Director/Artista que deseas buscar: ").lower()
    results = []
    for category, items in colectionBooks.items():
        for item in items:
            if searchAuthor in str(item.get("book_author", "")).lower():
                        itemData = {
                            "Título": item.get("book_title", ""),
                            "Autor/Director/Artista": item.get("book_author", ""),
                            "Género": item.get("book_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por autor/director/artista.")

def searchBooksGender():
    searchGender = input("Introduce el Género que deseas buscar: ").lower()
    results = []
    for category, items in colectionBooks.items():
        for item in items:
            if searchGender in str(item.get("book_gender", "")).lower():
                        itemData = {
                            "Título": item.get("book_title", ""),
                            "Autor/Director/Artista": item.get("book_author"),
                            "Género": item.get("book_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por género.")









