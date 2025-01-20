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