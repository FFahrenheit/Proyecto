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
            *Funciones (con paso, sin paso, return, default...)
            *Funciones de libreria
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
        elif opcion == "D":
            solucionador()
        elif opcion == "E":
            ejercicio()
        elif opcion == "F":
            print("Gracias por usar este programa")
            return
        else:
            print("Seleccione una opcion valida")
       
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
        elif opcion == "C":
             integrar.cargarEjemplo()
        elif opcion == "D":
            edo.cargarEjemplo()
        elif opcion == "E":
            return
        else:
            print("Seleccione una opcion valida")

        os.system("pause")

def integrantes():
    print("Los integrantes del equipo son: ")
    print("Ismael Iván López Murillo")
    print("Edgar Manuel Cabral Serpa")
    print("María José Rangel Salmerón")
def datos():
    print("Materia: Fundamentos Filosóficos de la Computación")
    print("Sección: D07")
    print("Profesor: Conrado Cruz Gomez")
    print("Proyecto Final")
    print("Fecha: 27/11/2020")

def solucionador():
    while True:
        os.system("cls")
        print("SOLUCIONADOR")
        print("\tA: Ajuste de curva")
        print("\tB: Interpolar valor")
        print("\tC: Integrar numericamente")
        print("\tD: Ecuacion diferencial")
        print("\tE: Salir")

        opcion = str(input("Ingrese su eleccion: ")).upper()

        try:
            if opcion == "A":
                ajuste.nuevoEjercicio()
            elif opcion == "B":
                interpolar.nuevoEjercicio()
            elif opcion == "C":
                integrar.nuevoEjercicio()
            elif opcion == "D":
                edo.nuevoEjercicio()
            elif opcion == "E":
                return
            else:
                print("Seleccione una opcion valida")
        except:
            print("La informacion proporcionada genero un error")

        os.system("pause")


def ejercicio():
    while True:
        os.system("cls")
        print("Cargar Ejercicios")
        print("\tA: Ajuste de curva")
        print("\tB: Interpolar valor")
        print("\tC: Integrar numericamente")
        print("\tD: Ecuacion diferencial")
        print("\tE: Salir")
                
        opcion = str(input("Ingrese su eleccion: ")).upper()

        if opcion == "A":
            ajuste.leerEjercicio()
        elif opcion == "B":
            interpolar.leerEjercicio()
        elif opcion == "C":
             integrar.leerEjercicio()
        elif opcion == "D":
            edo.leerEjercicio()
        elif opcion == "E":
            return
        else:
            print("Seleccione una opcion valida")

        os.system("pause")   

              
if __name__ == "__main__":
	mainMenu()