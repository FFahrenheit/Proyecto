"""
Clase encargada de regresar el contenido de un archivo en 
especifico y de cargarlos en un archivo
"""

import os

def getRealPath(filename):
    directory = os.path.dirname(__file__) # directory of script
    return r'{}/archivos/'.format(directory) + filename + ".txt" # File to open

def getRealPathToSave(filename):
    directory = os.path.dirname(__file__) # directory of script
    return r'{}/archivos/saves/'.format(directory) + filename + ".txt" # File to open

def leerArchivo(filename):
    path = getRealPath(filename)
    file = open(path,"r")

    return file

def leerGuardado(filename):
    path = getRealPathToSave(filename)
    file = open(path,"r")

    return file

def guardarArchivo(filename):
    path = getRealPathToSave(filename)
    file = open(path,"w")

    return file

