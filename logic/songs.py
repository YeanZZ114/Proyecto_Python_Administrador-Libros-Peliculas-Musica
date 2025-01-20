import json
from tabulate import tabulate
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

def addElementSongs():
    data = findAllSongs()
    songTitle = input("Ingrese el titulo de su cancion: ")
    songArtist = input("Ingrese el/la artista de su cancion: ")
    songGender = input("Ingrese el genero de su cancion: ")
    jh = {
        "song_title" : songTitle,
        "song_artist" : songArtist,
        "song_gender" : songGender
    }
    data.append(jh)
    saveAllSongs(data)

def seeAllSongs():
    with open('data/songs.json', 'r', encoding='utf-8') as file:
        songs = json.loads(file)           
        if isinstance(songs, list):
            print(tabulate(songs, headers="keys", tablefmt="fancy_outline"))
        else:
            print("Error")


with open('data/songs.json', "r", encoding="utf-8") as file:
    coleccion = json.load(file)
if not all(key in coleccion for key in ["books", "movies", "songs"]):
                coleccion = {"books": [], "movies": [], "songs": []}

def searchSongsTitle():
    searchTitle = input("Introduce el Título que deseas buscar: ").lower()
    results = []
    for category, items in coleccion.items():
            for item in items:
                if searchTitle in str(item.get("song_title", "")).lower():
                        itemData = {
                            "Título": item.get("song_title", ""),
                            "Autor/Director/Artista": item.get("song_artist", ""),
                            "Género": item.get("song_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por título.")

def searchSongsArtist():
    searchArtist = input("Introduce el Autor/Director/Artista que deseas buscar: ").lower()
    results = []
    for category, items in coleccion.items():
        for item in items:
            if searchArtist in str(item.get("song_artist", "")).lower():
                        itemData = {
                            "Título": item.get("song_title", ""),
                            "Autor/Director/Artista": item.get("song_artist", ""),
                            "Género": item.get("song_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por autor/director/artista.")

def searchSongsGender():
    searchGender = input("Introduce el Género que deseas buscar: ").lower()
    results = []
    for category, items in coleccion.items():
        for item in items:
            if searchGender in str(item.get("song_gender", "")).lower():
                        itemData = {
                            "Título": item.get("song_title", ""),
                            "Autor/Director/Artista": item.get("song_artist"),
                            "Género": item.get("song_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por género.")


