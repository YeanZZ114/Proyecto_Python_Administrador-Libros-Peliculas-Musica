from data.datosJSON import *



def save(books, songs, movies, collections):
    libros = abrirArchivo(RUTA_BOOK)
    musica = abrirArchivo(RUTA_MUSIC)
    peliculas = abrirArchivo(RUTA_MOVIES)
    coleccion = abrirArchivo(RUTA_COLECCION)
    libros.extend(books)
    musica.extend(songs)
    peliculas.extend(movies)
    coleccion["books"].extend(collections["books"])
    coleccion["movies"].extend(collections["movies"])
    coleccion["songs"].extend(collections["songs"])
    guardarArchivo(RUTA_BOOK, libros)
    guardarArchivo(RUTA_MUSIC, musica)
    guardarArchivo(RUTA_MOVIES, peliculas)
    guardarArchivo(RUTA_COLECCION, coleccion)
    print('Hecho')
    input('Press Enter....')




