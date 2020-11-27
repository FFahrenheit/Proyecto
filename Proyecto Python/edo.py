"""
Solucionar de PVI usando metodo de Runge Kutta
"""
epsilon = 4

import validador
import archivos

def leerEjercicio():
    try:
        filename = input("Ingrese el nombre del archivo a cargar ejemplo: ")
        cargarEjemplo(filename,True)
    except:
        print("ARCHIVO INVALIDO")

def cargarEjemplo(filename = "edo",isSave = False):

    if isSave:
        file = archivos.leerGuardado(filename)
    else:
        file = archivos.leerArchivo(filename)
    
    datos = file.read().split("\n")

    edo = datos[0]
    x0 = float(datos[1])
    y0 = float(datos[2])
    xf = float(datos[3])
    n = int(datos[4])

    calcular(edo,x0,y0,xf,n)

    file.close()


def nuevoEjercicio():
    edo = validador.requestEDO()

    x0 = validador.requestReal("Ingrese el valor inicial de x (x0): ")
    y0 = validador.requestReal(f"Ingrese el valor de f({x0}): ")
    xf = validador.requestReal("Ingrese el valor de x a encontrar y (xf): ")
    n = validador.requestInt("Ingrese el numero de subintervalos a dividir: ")

    calcular(edo,x0,y0,xf,n)

    save = input("Ingrese s o S si quiere guardar este ejercicio: ")
    if save == 'S' or save == 's':
        filename = input("Ingrese el nombre del archivo (sin extension): ")
        guardarEjercicio(edo,x0,y0,xf,n,filename)


def guardarEjercicio(edo,x0,y0,xf,n,filename):
    file = archivos.guardarArchivo(filename)

    file.write(edo)
    file.write(x0)
    file.write(y0)
    file.write(xf)
    file.write(n)

    file.close()



def calcular(edo,x0,y0,xf,n):    
    print("\t\tRunge-Kutta para E.D.O con P.V.I")
    
    h = round((xf-x0)/n,epsilon)

    print("EDO: ",edo)
    print(f"h = ({xf}-{x0})/{n}")
    print(f"h = {h}")

    xn = x0 
    yn = y0         #Para empezar

    for i in range(n):
        print("*"*10,"Iteracion ",i+1,"*"*10)
        xi = round(xn,epsilon)
        yi = round(yn,epsilon)

        xn = xi + h 
        print(f"x{i+1} = {xi} + {h} = {xn}")

        print(f"k1 = f({xi},{yi}) = ",end='')
        k1 = round(getFunction(edo,xi,yi),epsilon)
        print(f"{printFunction(edo,xi,yi)} = {k1}")

        print(f"k2 = f({xi} + {h}/2,{yi} + {h}*{k1}/2) = ",end='')
        k2 = round(getFunction(edo,xi+h/2, yi+h*k1/2),epsilon)
        print(f"{printFunction(edo,xi + h/2,yi+h*k1/2)} = {k2}")

        print(f"k3 = f({xi} + {h}/2,{yi} + {h}*{k2}/2) = ",end='')
        k3 = round(getFunction(edo,xi+h/2,yi + h*k2/2),epsilon)
        print(f"{printFunction(edo,xi+h/2,yi + h*k2/2)} = {k3}")

        print(f"k4 = f({xi} + {h},{yi} + {h}*{k3}) = ",end='')
        k4 = round(getFunction(edo,xi+h, yi + h*k3),epsilon)
        print(f"{printFunction(edo,xi + h, yi + h*k3)} = {k4}")
        
        yn = yi + (h/6)*(k1+2*k2+2*k3+k4)

        print(f"y{i+1} = {yi} + ({h}/6)({k1}+2({k2})+2({k3})+{k4}) = {yn:.4f}")


def printFunction(edo,x,y):
    nuevaFuncion = edo 
    nuevaFuncion = nuevaFuncion.replace("x","{x}")
    nuevaFuncion = nuevaFuncion.replace("y","{y}")

    nuevaFuncion = f"f\"{nuevaFuncion}\""

    return eval(nuevaFuncion)

def getFunction(edo,x,y):
    return eval(edo)
