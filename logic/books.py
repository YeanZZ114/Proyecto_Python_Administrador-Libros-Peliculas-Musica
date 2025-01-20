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
    with open('data/books.json', 'r', encoding='utf-8') as file:
        books = json.loads(file)           
        if isinstance(books, list):
            print(tabulate(books, headers="keys", tablefmt="fancy_outline"))
        else:
            print("Error")

def searchBooksTitle():

def searchBooksAuthor():

def searchBooksGender():








