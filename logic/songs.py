import json
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
    songDirector = input("Ingrese el/la artista de su cancion: ")
    songGender = input("Ingrese el genero de su cancion: ")
    jh = {
        "song_title" : songTitle,
        "book_author" : songDirector,
        "book_gender" : songGender
    }
    data.append(jh)
    saveAllSongs(data)