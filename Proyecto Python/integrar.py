"""
Formulas de integracion con Newton Cotes
"""

epsilon = 4

import math
import archivos
import validador

def leerEjercicio():
    try:
        filename = input("Ingrese el nombre del archivo a cargar ejemplo: ")
        cargarEjemplo(filename,True)
    except:
        print("ARCHIVO INVALIDO")

        
def cargarEjemplo(filename="integrar",isSave=False):
        
    if isSave:
        file = archivos.leerGuardado(filename)
    else:
        file = archivos.leerArchivo("integrar")

    datos = file.read().split("\n")

    headers = datos[0].split("|")

    a = float(headers[0])
    b = float(headers[1])
    n = int(headers[1])
    
    data = []

    for i in range(1,len(datos)):
        data.append(float(datos[i]))

    calcular(a,b,n,data)
    file.close()

def guardarEjercicio(a,b,h,data,filename):
    file = archivos.guardarArchivo(filename)

    file.write(f"{a}|{b}|{h}")

    for dato in data:
        file.write(dato)

    file.close()



def nuevoEjercicio():
    limits = validador.requestLimits("Ingrese los limites de integracion: ")

    n = validador.requestLimits("Ingrese cuantos subintervalos tiene: ")
    fun = input("Ingrese la funcion a tabular en terminos de x y sintaxis python: ")

    h = (limits[0] - limits[1])/n
    
    data = []

    if fun == "":
        for i in range(n+1):
            x = limits[0] + h*i
            y = validador.requestReal(f"Ingrese el valor para f{x}: ")
            data.append(y)
    else:
        try:
            x = 1
            eval(fun)
            for i in range(n):
                x = limits[0] + h*i
                y = eval(fun)
                data.append(y)
        except:
            print("La funcion no es valida")
            return

    calcular(limits[0],limits[1],n,data) 

    save = input("Ingrese s o S si quiere guardar este ejercicio: ")
    if save == 'S' or save == 's':
        filename = input("Ingrese el nombre del archivo (sin extension): ")
        guardarEjercicio(limits[0],limits[1],n,data,filename)



def calcular(a,b,n,data):
    print("\t\tNewton Cotes\n\n")

    h = (b-a)/n

    for i in range(len(data)):
        x = a + h*i
        y = data[i]
        print(f"x = {x} , y = {y}")

    print("*"*10,"Trapecio compuesto","*"*10)
    getCompositeTrapeze(data,h)

    print("*"*10,"Simpson 1/3 compuesto","*"*10)
    getSimpson1over3(data,h)

    print("*"*10,"Simpson 3/8 compuesto","*"*10)
    getSimpson3over8(data,h)

def getCompositeTrapeze(data,h):
    total = data[0]
    print(f"{h}/2({data[0]} + 2(",end='')
    for i in range(1,len(data)-1):
        if i!= 1:
            print(" + ",end='')
        print(data[i],end='')
        total += 2*data[i]
    print(f") + {data[len(data)-1]}) = ",end='')
    total += data[len(data)-1]
    total = round(total*h/2,epsilon)
    print(total)
    return total

def getSimpson1over3(data,h):
    total = data[0]
    n = len(data)
    print(f"{h}/3({data[0]} + 4(",end='')
    for i in range(1,n-1,2):
        if i != 1:
            print(" + ",end='')
        print(data[i],end='')
        total += 4*data[i]
    print(") + 2(",end='')
    for i in range(2,n-1,2):
        if i != 2:
            print(" + ",end='')
        print(data[i],end='')
        total += 2*data[i]
    print(f") + {data[n-1]}) = ",end='')
    total += data[n-1]
    total = round(total*h/3,epsilon)
    print(total)
    return total

def getSimpson3over8(data,h):
    n = len(data)
    total = data[0]
    print(f"3*{h}/8({data[0]} + 3(",end='')
    for i in range(1,n-1):
        if i % 3 != 0:
            if i != 1:
                print(" + ",end='')
            print(data[i],end='')
            total += 3*data[i]
    print(") + 2(",end='')
    for i in range(1,n-3):
        if i*3 < n:
            if i != 1:
                print(" + ",end='')
            print(data[i*3],end='')
            total += 2*data[i*3]
    print(f") + {data[n-1]}) = ",end='')
    total += data[n-1]
    total = round(3/8*total*h,epsilon)
    print(total)
    return total
