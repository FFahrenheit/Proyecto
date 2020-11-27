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
import os

"""
edo.cargarEjemplo()    ->Ejemplo 
edo.nuevoEjercicio()   ->Solucionador
edo.leerEjercicio()    ->Leer ejercicio
"""

def mainMenu():
    opcion = "A"
    while opcion != "F":
        os.system("cls")
        print("Bienvenido")
        print("\tA: Integrantes")
        print("\tB: Datos del programa")
        print("\tC: Ejemplos")
        print("\tD: Solucionador")
        print("\tE: Cargar ejercicio desde archivo")
        print("\tF: Salir")

        opcion = str(input("Ingrese su eleccion: ")).upper()

        if opcion == "A":
            integrantes()
        elif opcion == "B":
            datos()
        elif opcion == "C":
            ejemplos()

        os.system("pause")

def ejemplos():
    while True:
        os.system("cls")
        print("EJEMPLOS")
        print("\tA: Ajuste de curva")
        print("\tB: Interpolar valor")
        print("\tC: Integrar numericamente")
        print("\tD: Ecuacion diferencial")
        print("\tE: Salir")

        opcion = str(input("Ingrese su eleccion: ")).upper()

        if opcion == "A":
            ajuste.cargarEjemplo()
        elif opcion == "B":
            interpolar.cargarEjemplo()
        elif opcion == "E":
            return

        os.system("pause")

def integrantes():
    print("Aqui imprime nuestros nombres")

def datos():
    print("Aqui imprime los datos")

if __name__ == "__main__":
	mainMenu()