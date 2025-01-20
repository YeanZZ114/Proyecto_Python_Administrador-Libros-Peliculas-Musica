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