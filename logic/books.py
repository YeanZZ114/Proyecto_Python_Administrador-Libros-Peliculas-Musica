import json
from tabulate import tabulate
import os
#definimos la funcion para buscar todos los libros
def findAllBooks():
    with open ("data/books.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict  
#definimos la funcion para guardar todos los libros   
def saveAllBooks(data):
    with open ("data/books.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo books.json"
#definimos la funcion para agregar nuevos elementos
def addElementBooks(books, collections):
    bookTitle = input("Ingrese el titulo de su libro: ")
    bookDirector = input("Ingrese el/la autor(a) de su libro: ")
    bookGender = input("Ingrese el genero de su libro: ")
    bookCategory = input("Ingrese la categoria de su libro(Novela, Biografia, Poesia...)")
    while True:
        bookID = input("Ingrese un numero de identificacion de 4 digitos unico para su libro: ")
        if bookID.isdigit() and len(bookID) == 4:
            break
        else:
            print("El ID debe ser un número de 4 dígitos. Intente nuevamente.")

    sh = {
        "titulo" : bookTitle,
        "autor/director/artista" : bookDirector,
        "genero" : bookGender,
        "categoria" : bookCategory,
        "ID" : bookID
    }
    books.append(sh)
    collections["books"].append(sh)
#definimos la funcion para mirar todos los libros
def seeAllBooks():
    data = findAllBooks()
    datamodify = []
    for diccionario in data:
           datamodify.append(diccionario)
    print(tabulate(datamodify, headers='keys', tablefmt='grid', numalign="center"))
#definimos la funcion para mostrar en lista los libros
def listBooks():
        books = findAllBooks("books")
        books1 = []
        for diccionario in books:
              diccionario.pop("titulo")
              diccionario.pop("autor/director/artista")
              diccionario.pop("genero")
              books1.append(diccionario)
        print(tabulate(books1, headers="keys", tablefmt="grid"))
 #buscar en los libros los que tienen la categoria solicitada       
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
 #definimos la funcion para poder editar los titulos de los libros        
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
        continue1 = input("¿Deseas continuar editando titulos? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de titulos.")
            break
#definimos la funcion para poder editar los autores de los libros               
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
        continue1 = input("¿Deseas continuar editando autor/director/artista? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de autor/director/artista.")
            break
 #definimos la funcion para poder editar los generos de los libros              
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
        continue1 = input("¿Deseas continuar editando generos? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de generos.")
            break
#definimos la funcion para poder editar las categorias de los libros   
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
        continue1 = input("¿Deseas continuar editando categorías? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de categorías.")
            break
 #definimos la variable para poder eliminar elementos segun su titulo           

def removeBooksTitle():
 while True:
        with open("data/books.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(tabulate(data, headers='keys', tablefmt='grid'))
        titleToRemove = input("¿Qué título de libro deseas eliminar?: ")
        updatedData = [book for book in data if book.get('titulo') != titleToRemove]
        if len(updatedData) != len(data):
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(updatedData, file, indent=4, ensure_ascii=False)
            print(f"El libro con el título '{titleToRemove}' ha sido eliminado.")
        else:
            print(f"No se encontró ningún libro con el título '{titleToRemove}'.")
        continuar = input("¿Deseas continuar eliminando libros? (Si/No): ").lower()
        if continuar != 'si':
            print("Saliendo del eliminador de libros.")
            break
def removeBooksID():
    while True:
        with open("data/books.json", "r", encoding="utf-8") as file:
            data = json.load(file)        
        print(tabulate(data, headers='keys', tablefmt='grid'))        
        idToRemove = input("¿Qué ID de libro deseas eliminar?: ")
        updated_data = [book for book in data if str(book.get('ID')) != idToRemove]
        if len(updated_data) != len(data):
            with open("data/books.json", "w", encoding="utf-8") as file:
                json.dump(updated_data, file, indent=4, ensure_ascii=False)
            print(f"El libro con el ID '{idToRemove}' ha sido eliminado.")
        else:
            print(f"No se encontró ningún libro con el ID '{idToRemove}'.")
        continuar = input("¿Deseas continuar eliminando libros? (Si/No): ").lower()
        if continuar != 'si':
            print("Saliendo del eliminador de libros.")
            break

