from design.elements import *
from logic.books import *
from logic.movies import *
from logic.songs import *
from logic.all import *
from logic.saveAndLoad import *
import json 


books = []
songs = []
movies = []

collections = {
      "books": [],
      "songs": [],
      "movies": []
}


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
                                        case 1: addElementBooks(books, collections)

                                        case 2: addElementMovies(movies, collections)

                                        case 3: addElementSongs(songs, collections)
                                        
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
                                    match searchElements():
                                        case 1:
                                                searchAllsTitle()
                                        case 2:
                                                searchAllsA_A_D()
                                        case 3:
                                                searchAllGender()
                                        case 4: menuActive = False
                                                
                                except Exception as e:        
                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                        input("Presiona Enter para continuar...")   
                                              
                    case 4:
                            menuActive = True
                            while menuActive:
                                try:
                                    match editElementsType():
                                        case 1:
                                                editActive = True
                                                while editActive:
                                                        try:
                                                            match editElements():
                                                                    
                                                                    case 1: editBooksElementsTitle()
                                                                    
                                                                    case 2 : editBooksElementsA_D_D()
                                                                    
                                                                    case 3: editBooksElementsGender()
                                                                    
                                                                    case 4: editBooksElementsCategory()
                                                                    
                                                                    case 5: editActive = False
                                                        
                                                        except Exception as e:        
                                                                print(f"Error: {e}. Selecciona una opción correcta.")
                                                                input("Presiona Enter para continuar...")
                                                               
                                        case 2:
                                                editActive = True
                                                while editActive:
                                                        try:
                                                            match editElements():
                                                                    
                                                                    case 1: editMoviesElementsTitle()
                                                                    
                                                                    case 2 : editMoviesElementsA_D_D()
                                                                    
                                                                    case 3: editMoviesElementsGender()
                                                                    
                                                                    case 4: editMoviesElementsCategory()
                                                                    
                                                                    case 5: editActive = False
                                                        
                                                        except Exception as e:        
                                                                print(f"Error: {e}. Selecciona una opción correcta.")
                                                                input("Presiona Enter para continuar...")             
                                        case 3:
                                                editActive = True
                                                while editActive:
                                                        try:
                                                            match editElements():
                                                                    
                                                                    case 1: editSongsElementsTitle()
                                                                    
                                                                    case 2 : editSongsElementsA_D_D()
                                                                    
                                                                    case 3: editSongsElementsGender()
                                                                    
                                                                    case 4: editSongsElementsCategory()
                                                                    
                                                                    case 5: editActive = False
                                                        
                                                        except Exception as e:        
                                                                print(f"Error: {e}. Selecciona una opción correcta.")
                                                                input("Presiona Enter para continuar...")
                                        case 4: 
                                                menuActive= False
                                except Exception as e:        
                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                        input("Presiona Enter para continuar...")
                            
                    case 5:
                            menuActive = True
                            while menuActive:
                                try:
                                   match deleteElementType():
                                         case 1:
                                               deleteActive = True
                                               while deleteActive:
                                                try:
                                                        match deleteElement():
                                                                case 1: 
                                                                    removeBooksTitle()
                                                                case 2:
                                                                    pass
                                                                case 3:
                                                                    deleteActive = False
                                                except Exception as e:        
                                                        print(f"Error: {e}. Selecciona una opción correcta.")
                                                        input("Presiona Enter para continuar...")
                                         case 2:
                                                deleteActive = True
                                                while deleteActive:
                                                        try:
                                                                match deleteElement():
                                                                        case 1: 
                                                                                removeMoviesTitle()
                                                                        case 2:
                                                                                pass
                                                                        case 3:
                                                                                deleteActive = False
                                                        except Exception as e:        
                                                                print(f"Error: {e}. Selecciona una opción correcta.")
                                                                input("Presiona Enter para continuar...")
                                         case 3:
                                                deleteActive = True
                                                while deleteActive:
                                                        try:
                                                                match deleteElement():
                                                                        case 1: 
                                                                                removeSongsTitle()
                                                                        case 2:
                                                                                pass
                                                                        case 3:
                                                                                deleteActive = False
                                                        except Exception as e:        
                                                                print(f"Error: {e}. Selecciona una opción correcta.")
                                                                input("Presiona Enter para continuar...")                        
                                         case 4: menuActive = False

                                except Exception as e:        
                                         print(f"Error: {e}. Selecciona una opción correcta.")
                                         input("Presiona Enter para continuar...")
                                                                         
                    case 6:
                            menuActive = True
                            while menuActive:
                                try:
                                    match categoryElements():
                                        case 1:
                                                searchCategoryBooks()
                                        case 2:
                                                searchCategoryMovies()
                                        case 3:
                                                searchCategorySongs()
                                        case 4:
                                                menuActive = False
                                except Exception as e:        
                                    print(f"Error: {e}. Selecciona una opción correcta.")
                                    input("Presiona Enter para continuar...")
                    case 7: 
                            menuActive = True
                            while menuActive:
                                    opc = saveCollections()
                                    match opc:
                                        case 1:
                                                save(books, songs, movies, collections)
                                        case 2:
                                                pass
                                        case 3:
                                                input('Press Enter....')
                                                menuActive = False
                                                           
                                        
                    case _:
                            print("Esta opcion no existe")                    
            except Exception as e:        
                    print(f"Error: {e}. Selecciona una opción correcta.")
                    input("Presiona Enter para continuar...")
                    
                        



                    
