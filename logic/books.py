import json
from tabulate import tabulate
    
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

with open('data/books.json', "r", encoding="utf-8") as file:
    colectionBooks = json.load(file)
if not all(key in colectionBooks for key in ["books", "movies", "songs"]):
                colectionBooks = {"books": [], "movies": [], "songs": []}

def searchBooksTitle():
    searchTitle = input("Introduce el Título que deseas buscar: ").lower()
    results = []
    for category , items in colectionBooks.items():
            for item in items:
                if searchTitle in str(item.get("book_title", "")).lower():
                        itemData = {
                            "Título": item.get("book_title", ""),
                            "Autor/Director/Artista": item.get("book_author", ""),
                            "Género": item.get("book_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por título.")

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







