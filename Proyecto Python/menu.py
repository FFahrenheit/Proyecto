"""
FUNDAMENTOS FILOSOFICOS DE LA COMPUTACION SECCION D07

NOMBRE DEL ALUMNO: Ismael Iván López Murillo   Código 220975903
NOMBRE DEL ALUMNO: Edgar Manuel Cabral Serpa   Código 217552864
NOMBRE DEL ALUMNO: María José Rangel Salmerón  Código 212557817

Maestro: Conrado Cruz Gomez
PROYECTO FINAL FUNDAMENTOS FILOSÓFICOS

FECHA. 27/NOVIEMBRE/2020
TEMAS APLICADOS:
            *Listas
            *Archivos
            *Ciclos
            *Selectiva
            *Try - except
            *Variables y tipos de dato (cast)
            *Manejo de cadenas
            *Funciones
"""

import ajuste         #Ajute
import interpolar     #Interpolar
import integrar       #Integrales
import edo            #Ecuaciones

"""
edo.cargarEjemplo()    ->Ejemplo 
edo.nuevoEjercicio()   ->Solucionador
edo.leerEjercicio()    ->Leer ejercicio
"""

def mainMenu():
    print("Hola mundo!")
    """
    El MENU IRÁ ASÍ:
    • Bienvenida.
        o Mostrar Integrantes.
        o Mostrar datos del programa.
    • Ejemplos.
        o Ejemplo ecuaciones diferenciales (información cargada de archivo).
        o Ejemplo cálculo integral (información cargada de archivo).
        o Ejemplo interpolación (información cargada de archivo).
        o Ejemplo ajuste de curva (información cargada de archivo).
    • Solucionador:
        o Ecuaciones diferenciales ordinarias.
        o Cálculo integral
        o Interpolación y ajuste de curva.
        o Ajuste de curva
    • Cargar ejercicio:
        o Ecuaciones diferenciales ordinarias.
        o Cálculo integral
        o Interpolación y ajuste de curva.
        o Ajuste de curva
    """


if __name__ == "__main__":
	mainMenu()