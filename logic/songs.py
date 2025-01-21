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

def addElementSongs(songs, collections):
    songTitle = input("Ingrese el titulo de su cancion: ")
    songArtist = input("Ingrese el/la artista de su cancion: ")
    songGender = input("Ingrese el genero de su cancion: ")
    songCategory = input("Ingrese la categoria de su cancion(Infantil, Folclor, Moderna...): ")
    while True:
        songID = input("Ingrese un numero de identificacion de 4 digitos unico para su libro: ")
        if songID.isdigit() and len(songID) == 4:
            break
        else:
            print("El ID debe ser un número de 4 dígitos. Intente nuevamente.")

    jh = {
        "titulo" : songTitle,
        "autor/director/artista" : songArtist,
        "genero" : songGender,
        "categoria" : songCategory,
        "ID" : songID
    }
    songs.append(jh)
    collections["songs"].append(jh)

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
        filesJson = ['songs.json']
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
         
         
def editSongsElementsTitle():
    while(True):
        with open ("data/songs.json", "r", encoding="utf-8" ) as file:
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
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El título ha sido actualizado.")
        else:
            print("El título no se encontró en los datos.")
        continue1 = input("¿Deseas continuar editando titulos? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de titulos.")
            break    
def editSongsElementsA_D_D():
    while(True):
        with open ("data/songs.json", "r", encoding="utf-8" ) as file:
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
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El autor/director/artista ha sido actualizado.")
        else:
            print("El autor/director/artista no se encontró en los datos.")
        continue1 = input("¿Deseas continuar editando autor/director/artista? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de autor/director/artista.")
            break       
def editSongsElementsGender():
    while(True):
        with open ("data/songs.json", "r", encoding="utf-8" ) as file:
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
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El genero ha sido actualizado.")
        else:
            print("El genero no se encontró en los datos.")
        continue1 = input("¿Deseas continuar editando generos? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de generos.")
            break
def editSongsElementsCategory():
    while(True):
        with open ("data/songs.json", "r", encoding="utf-8" ) as file:
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
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("La categoria ha sido actualizada.")
        else:
            print("La categoria no se encontró en los datos.")
        continue1 = input("¿Deseas continuar editando categorías? (Si/No): ").lower()
        if continue1 != 'si':
            print("Saliendo del editor de categorías.")
            break

def removeSongsTitle():
    while True:
        with open("data/songs.json", "r", encoding="utf-8") as file:
            data = json.load(file)        
        print(tabulate(data, headers='keys', tablefmt='grid'))        
        titleToRemove = input("¿Qué título deseas eliminar?: ")
        updatedData = [song for song in data if song.get('titulo') != titleToRemove]
        if len(updatedData) != len(data):
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(updatedData, file, indent=4, ensure_ascii=False)
            print(f"La canción con el título '{titleToRemove}' ha sido eliminada.")
        else:
            print(f"No se encontró ninguna canción con el título '{titleToRemove}'.")
        continuar = input("¿Deseas continuar eliminando canciones? (Si/No): ").lower()
        if continuar != 'si':
            print("Saliendo del eliminador de canciones.")
            break

def removeSongsID():
    while True:
        with open("data/songs.json", "r", encoding="utf-8") as file:
            data = json.load(file)       
        print(tabulate(data, headers='keys', tablefmt='grid'))        
        idToRemove = input("¿Qué ID de canción deseas eliminar?: ")
        updated_data = [song for song in data if str(song.get('ID')) != idToRemove]
        if len(updated_data) != len(data):
            with open("data/songs.json", "w", encoding="utf-8") as file:
                json.dump(updated_data, file, indent=4, ensure_ascii=False)
            print(f"La canción con el ID '{idToRemove}' ha sido eliminada.")
        else:
            print(f"No se encontró ninguna canción con el ID '{idToRemove}'.")
        continuar = input("¿Deseas continuar eliminando canciones? (Si/No): ").lower()
        if continuar != 'si':
            print("Saliendo del eliminador de canciones.")
            break