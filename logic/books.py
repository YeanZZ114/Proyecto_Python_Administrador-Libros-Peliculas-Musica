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

def addElementBooks(books, collections):
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
    books.append(sh)
    collections["books"].append(sh)
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
         
def editBooksElementsTitle():
    while(True):
        with open ("data/books.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        titleUser = input("Que titulo deseas editar?: ")
        titleEdit = input("Introduce el nuevo titulo: ")
        found = False
        for book in data:
            if book.get('titulo') == titleUser:   
                book['titulo'] = titleEdit
                found = True
        if found:
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El título ha sido actualizado.")
        else:
            print("El título no se encontró en los datos.")
            
def editBooksElementsA_D_D():
    while(True):
        with open ("data/books.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        A_D_DUser = input("Que autor/director/artista deseas editar?: ")
        A_D_DEdit = input("Introduce el nuevo autor/director/artista: ")
        found = False
        for book in data:
            if book.get('autor/director/artista') == A_D_DUser:   
                book['autor/director/artista'] = A_D_DEdit
                found = True
        if found:
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El autor/director/artista ha sido actualizado.")
        else:
            print("El autor/director/artista no se encontró en los datos.")
            
def editBooksElementsGender():
    while(True):
        with open ("data/books.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        GenderUser = input("Que genero deseas editar?: ")
        GenderEdit = input("Introduce el nuevo genero: ")
        found = False
        for book in data:
            if book.get('genero') == GenderUser:   
                book['genero'] = GenderEdit
                found = True
        if found:
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El genero ha sido actualizado.")
        else:
            print("El genero no se encontró en los datos.")

def editBooksElementsCategory():
    while(True):
        with open ("data/books.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        categoryUser = input("Que categoria deseas editar?: ")
        categoryEdit = input("Introduce la nueva categoria: ")
        found = False
        for book in data:
            if book.get('categoria') == categoryUser:   
                book['categoria'] = categoryEdit
                found = True
        if found:
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("La categoria ha sido actualizada.")
        else:
            print("La categoria no se encontró en los datos.")
            


