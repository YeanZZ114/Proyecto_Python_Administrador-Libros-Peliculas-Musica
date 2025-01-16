from design.elements import mainMenu,addElement,allElements,searchElements,editElements,deleteElement,categoryElements,saveCollections
from logic.books import addElementBooks
from logic.movies import addElementMovies
from logic.songs import addElementSongs


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
                    case _:
                            print("Esta opcion no existe")                    
            except Exception as e:        
                    print(f"Error: {e}. Selecciona una opción correcta.")
                    input("Presiona Enter para continuar...")
                    
                        



                    
