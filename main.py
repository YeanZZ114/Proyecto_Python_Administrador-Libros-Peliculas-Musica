from design.elements import *
from logic.books import *
from logic.movies import *
from logic.songs import *
import json 

if __name__=='__main__':
    isActive = True
    while isActive:
            try:
                match mainMenu():
                    case 8:
                            print('''Saliendo...
                                Has salido del programa''')
                            isActive = False
                    case 1:
                            menuActive = True
                            while menuActive:
                                try:
                                    match addElement():
                                        case 1: addElementBooks()

                                        case 2: addElementMovies()

                                        case 3: addElementSongs()
                                        
                                        case 4: menuActive = False
                                except Exception as e:        
                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                        input("Presiona Enter para continuar...")
                    case 2:
                            menuActive = True
                            while menuActive:
                                try:
                                    match allElements():
                                        case 1: seeAllBooks()

                                        case 2: seeAllMovies()

                                        case 3: seeAllSongs()

                                        case 4: menuActive = False
                                except Exception as e:        
                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                        input("Presiona Enter para continuar...")
                    case 3:
                            menuActive = True
                            while menuActive:
                                try:
                                    match searchElementType():
                                        case 1: 
                                                searchActive = True
                                                while searchActive:
                                                    try:
                                                        match searchElements():
                                                            case 1:
                                                                    searchBooksTitle()
                                                            case 2:
                                                                    searchBooksAuthor()
                                                            case 3:
                                                                    searchBooksGender()
                                                            case 4: 
                                                                    searchActive = False
                                                    except Exception as e:        
                                                            print(f"Error: {e}. Selecciona una opción correcta.")
                                                            input("Presiona Enter para continuar...")
                                        case 2:
                                                searchActive = True
                                                while searchActive:
                                                    try:
                                                        match searchElements():
                                                            case 1:
                                                                    searchMoviesTitle()
                                                            case 2:
                                                                    searchMoviesDirector()
                                                            case 3:
                                                                    searchMoviesGender()
                                                            case 4: 
                                                                    searchActive = False
                                                    except Exception as e:        
                                                            print(f"Error: {e}. Selecciona una opción correcta.")
                                                            input("Presiona Enter para continuar...")
                                        case 3:
                                                searchActive = True
                                                while searchActive:
                                                    try:
                                                        match searchElements():
                                                            case 1:
                                                                    searchSongsTitle()
                                                            case 2:
                                                                    searchSongsArtist()
                                                            case 3:
                                                                    searchSongsGender()
                                                            case 4: 
                                                                    searchActive = False
                                                    except Exception as e:        
                                                            print(f"Error: {e}. Selecciona una opción correcta.")
                                                            input("Presiona Enter para continuar...")
                                        case 4: searchActive = False
                                                
                                except Exception as e:        
                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                        input("Presiona Enter para continuar...")   
                                              
                    #case 4:
                     #       menuActive = True
                      #      while menuActive:
                       #         try:
                        #            match editElements():
                            
                    #case 5:
                     #       menuActive = True
                      #      while menuActive:
                       #         try:
                        #            match deleteElementType():
                    case 6:
                            menuActive = True
                            while menuActive:
                                try:
                                    match categoryElements():
                                        case 1:
                                                seeAllBooks()
                                        case 2:
                                                seeAllMovies()
                                        case 3:
                                                seeAllSongs()
                                        case 4:
                                                menuActive = False
                                except Exception as e:        
                                    print(f"Error: {e}. Selecciona una opción correcta.")
                                    input("Presiona Enter para continuar...")
                    #case 7: 
                     #       menuActive = True
                      #      while menuActive = True
                       #         try:
                        #            match saveCollections():                                      
                                        
                    case _:
                            print("Esta opcion no existe")                    
            except Exception as e:        
                    print(f"Error: {e}. Selecciona una opción correcta.")
                    input("Presiona Enter para continuar...")
                    
                        



                    
