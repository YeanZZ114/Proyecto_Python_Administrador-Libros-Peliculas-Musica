def mainMenu():
    opc = int(input('''
                        ===========================================
                                Administrador de Colección
                        ===========================================
                        1. Añadir un Nuevo Elemento
                        2. Ver Todos los Elementos
                        3. Buscar un Elemento
                        4. Editar un Elemento
                        5. Eliminar un Elemento
                        6. Ver Elementos por Categoría
                        7. Guardar y Cargar Colección
                        8. Salir
                        ===========================================
                        Selecciona una opción (1-8):
                       '''))
    return opc
    
def addElement():
    opc = int(input('''
                        ===========================================
                                Añadir un Nuevo Elemento
                        ===========================================
                        ¿Qué tipo de elemento deseas añadir?
                        1. Libro
                        2. Película
                        3. Música
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
 '''))
    return opc
   
def allElements():
    opc = int(input('''
                        ===========================================
                                Ver Todos los Elementos
                        ===========================================
                        ¿Qué categoría deseas ver?
                        1. Ver Todos los Libros
                        2. Ver Todas las Películas
                        3. Ver Toda la Música
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
                          ''' ))
    return opc

def searchElementType():
        opc = int(input ('''
                        ===========================================
                                Buscar un Elemento
                        ===========================================
                        ¿Que deseas buscar?
                        1. Buscar libro
                        2. Buscar pelicula
                        3. Buscar canción
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
 '''))
        return opc
    
def searchElements():
    opc = int(input ('''
                        ===========================================
                                Buscar un Elemento
                        ===========================================
                        ¿Cómo deseas buscar?
                        1. Buscar por Título
                        2. Buscar por Autor/Director/Artista
                        3. Buscar por Género
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
 '''))
    return opc
    
def editElements():
    opc = int(input('''
                        ===========================================
                                Editar un Elemento
                        ===========================================
                        ¿Qué tipo de cambio deseas realizar?
                        1. Editar Título
                        2. Editar Autor/Director/Artista
                        3. Editar Género
                        4. Editar Valoración
                        5. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-5): 
                       '''))
    return opc

def deleteElementType():
    opc = int(input('''
                        ===========================================
                                Eliminar un Elemento
                        ===========================================
                        ¿Que tipo de elemento desea eliminar?
                        1. Libro
                        2. Pelicula
                        3. Canción
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
                         '''))
    return opc

def deleteElement():
    opc = int(input('''
                        ===========================================
                                Eliminar un Elemento
                        ===========================================
                        ¿Cómo deseas eliminar?
                        1. Eliminar por Título
                        2. Eliminar por Identificador Único
                        3. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-3):
                         '''))
    return opc
    
def categoryElements():
    opc = int(input('''
                        ===========================================
                                Ver Elementos por Categoría
                        ===========================================
                        ¿Qué categoría deseas ver?
                        1. Ver Libros
                        2. Ver Películas
                        3. Ver Música
                        4. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-4):
                           '''))
    return opc

def saveCollections():
    opc = int(input('''
                        ===========================================
                                Guardar y Cargar Colección
                        ===========================================
                        ¿Qué deseas hacer?
                        1. Guardar la Colección Actual
                        2. Cargar una Colección Guardada
                        3. Regresar al Menú Principal
                        ===========================================
                        Selecciona una opción (1-3):
                       '''))
    return opc

