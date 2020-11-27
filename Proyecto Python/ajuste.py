"""
Ajuste de curva por el metodo de minimos cuadrados
"""

import numpy as np
import validador
import archivos

epsilon = 4

def leerEjercicio():
    try:
        filename = input("Ingrese el nombre del archivo a cargar ejemplo: ")
        cargarEjemplo(filename,True)
    except:
        print("ARCHIVO INVALIDO")

        
def cargarEjemplo(filename="ajuste",isSave=False):
    
    if isSave:
        file = archivos.leerGuardado(filename)
    else:
        file = archivos.leerArchivo(filename)
    
    datos = file.read().split("\n")

    data = []

    for dato in datos:
        valores = dato.split("|")
        data.append([valores[0] , valores[1]])

    calcular(data, len(data)-1)
    file.close()


def guardarEjercicio(data,filename):
    file = archivos.guardarArchivo(filename)

    for dato in data:
        file.write(f"{dato[0]}|{dato[1]}")

    file.close()

def nuevoEjercicio():
    print("\t\t\tMinimos cuadrados\t\t\t")
    
    n = validador.requestInt("Ingrese el numero de datos a ingresar: ")
    
    data = []
    for i in range(n):
        x = validador.requestReal(f"Ingrese el valor para x{i}: ")
        y = validador.requestReal(f"Ingrese el valor para f(x{i}): ")
        data.append([x,y])

    polinomios = validador.requestInt("Ingrese los polinomios a calcular: ")
    
    if polinomios > len(data) - 1 :
        print("Se haran los polinomios maximos si se excede")
        polinomios = len(data) - 1

    calcular(data,polinomios)

    save = input("Ingrese s o S si quiere guardar este ejercicio: ")
    if save == 'S' or save == 's':
        filename = input("Ingrese el nombre del archivo (sin extension): ")
        guardarEjercicio(data,filename)


def calcular(data,polynomials):
    print("\t\tMinimos cuadrados\n\n")


    xSum = [0 for i in range(2*polynomials)]
    xYSum = [0 for i in range(polynomials+1)]

    for i in range(polynomials*2):
        xSum[i] = getSummatory(data,i+1)
    
    for i in range(polynomials+1):
        xYSum[i] = getSumXY(data,i)
    
    for i in range(len(xSum)):
        print(f"x^{i+1} = {xSum[i]}")

    for i in range(len(xYSum)):
        print(f"x^{i+1}y = {xYSum[i]}")

    print("\n\n")

    for i in range(polynomials):
        print(f"Solucion polinomio grado {i+1}")
        print("*"*10,"Sistema","*"*10)
        coefMatr = [0 for i in range(i+2)]
        coefSol = [0 for i in range(i+2)]
        for j in  range(i+2):
            coefEq = getEquation(i+1,j,xSum,len(data))
            coefMatr[j] = coefEq 
            coefSol[j] = xYSum[j]
            print(f" = {xYSum[j]}")

        a = np.array(coefMatr)
        b = np.array(coefSol)
        x = np.linalg.solve(a, b)
        print("*"*10,"Soluciones","*"*10)
        for i in range(len(x)):
            print(f"a{i} = {round(x[i],epsilon)}")

        print("*"*10,"Ecuacion","*"*10)

        for i in range(len(x)):
            if i == 0:
                print(f"y = {round(x[i],epsilon)}",end='')
            else:
                print(f" + {round(x[i],epsilon)}x^{i}",end='')
        print("\n")


#Order -> Orden del polinomio
#n -> Numero de ecuacion
#xSum -> Coeficientes x^n
#data -> n (Si se requiere, solo para n=0)
def getEquation(order,n,xSum,terms):
    data = [0 for i in range(order+1)]  #Order 1 -> 2 terminos y asi
    for i in range(len(data)): #Se llena el array
        if i == 0 and n == 0:    #No podemos acceder a data[-1]
            data[0] = terms
        else:
            data[i] = round(xSum[n-1+i],epsilon)
        if i != 0:
            print(" + ",end='')
        print(f"{data[i]:.4f}a{i}",end='')
    return data 

def getSumXY(data,pow):
    total = 0
    for i in range(len(data)):
        total += data[i][0]**pow *data[i][1]
    return round(total,epsilon)

def getSummatory(data,pow):
    total = 0
    for i in range(len(data)):
        total += data[i][0]**pow
    return round(total,epsilon)
