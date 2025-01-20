import json
import os
import tabulate

def searchAllsTitle():
       while(True):
        file = 'data'
        filesJson = ['books.json', 'movies.json', 'musics.json']
        titleSearch = input("Introduce el título que deseas buscar: ")
        results = []
        for archive in filesJson:
            archivePath = os.path.join(file, archive)
            if os.path.exists(archivePath, ):
                with open(archivePath, 'r') as archive:
                    data = json.load(archive)
                results.extend([item for item in data if item['titulo'].lower() == titleSearch.lower()])
            else:
                print(f"El archivo {archive} no se encontró en la carpeta {file}.")
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("No se encontraron resultados para este titulo")
        back = input(
                "¿Deseas volver? (Si/No)"
                )
        if back.lower() == "si":
                break
        else:
             continue
        
#def searchAllsA_A_D():
