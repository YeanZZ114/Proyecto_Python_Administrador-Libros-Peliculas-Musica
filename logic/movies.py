import json
from tabulate import tabulate 
def findAllMovies():
    with open ("data/movies.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict
    
def saveAllMovies(data):
    with open ("data/movies.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo movies.json"
    
def addElementMovies():
    data = findAllMovies()
    movieTitle = input("Ingrese el titulo de su pelicula: ")
    movieDirector = input("Ingrese el/la director(a) de su pelicula: ")
    movieGender = input("Ingrese el genero de su pelicula: ")
    gh = {
        "movie_title" : movieTitle,
        "movie_director" : movieDirector,
        "movie_gender" : movieGender
    }
    data.append(gh)
    saveAllMovies(data)

def seeAllMovies():
    with open('data/movies.json', 'r', encoding='utf-8') as file:
        movies = json.loads(file)           
        if isinstance(movies, list):
            print(tabulate(movies, headers="keys", tablefmt="fancy_outline"))
        else:
            print("Error")

with open('data/movies.json', "r", encoding="utf-8") as file:
    colectionMovies = json.load(file)
if not all(key in colectionMovies for key in ["books", "movies", "songs"]):
                colectionMovies = {"books": [], "movies": [], "songs": []}

def searchMoviesTitle():
    searchTitle = input("Introduce el Título que deseas buscar: ").lower()
    results = []
    for category, items in colectionMovies.items():
            for item in items:
                if searchTitle in str(item.get("movie_title", "")).lower():
                        itemData = {
                            "Título": item.get("movie_title", ""),
                            "Autor/Director/Artista": item.get("movie_director", ""),
                            "Género": item.get("movie_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por título.")

def searchMoviesDirector():
    searchDirector = input("Introduce el Autor/Director/Artista que deseas buscar: ").lower()
    results = []
    for category, items in colectionMovies.items():
        for item in items:
            if searchDirector in str(item.get("movie_director", "")).lower():
                        itemData = {
                            "Título": item.get("movie_title", ""),
                            "Autor/Director/Artista": item.get("movie_director", ""),
                            "Género": item.get("movie_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por autor/director/artista.")

def searchMoviesGender():
    searchGender = input("Introduce el Género que deseas buscar: ").lower()
    results = []
    for category, items in colectionMovies.items():
        for item in items:
            if searchGender in str(item.get("moovie_gender", "")).lower():
                        itemData = {
                            "Título": item.get("movie_title", ""),
                            "Autor/Director/Artista": item.get("movie_director"),
                            "Género": item.get("movie_gender", ""),
                        }
                        results.append(itemData)
    if results:
                print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
                print("No se encontraron elementos que coincidan con tu búsqueda por género.")      