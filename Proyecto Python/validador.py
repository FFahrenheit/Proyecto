"""
Funciones para validar
tipos de entrada
"""


def requestInt(message = "Ingrese un valor entero: ",warning="Solo numeros enteros"):
    while True:
        n = input(message)
        try:
            n = int(n)
            if n > 1:
                return n
        except ValueError:
            print(warning)

def requestReal(message = "Ingrese el valor correspondiente", warning="Ingrese un numero real"):
    while True:
        n = input(message)
        try:
            n = float(n)
            return n
        except ValueError:
            print(warning)

def requestLimits(message = "Ingrese los limites de integracion", warning = "Ingrese un numero valido"):
    print(message)
    while True:
        a = input("Ingrese el limite inferior: ")
        try:
            a = float(a)
            break
        except ValueError:
            print(warning)
    while True:
        b = input("Ingrese el limite superior: ")
        try:
            b = float(b)
            if b > a:
                return [ a , b ]
        except ValueError:
            print(warning)

def requestEDO():
    while True:
        edo = input("Ingrese la ecuacion diferencial en terminos de \"x\" y \"y\": ")
        x = y = 0; x+=y   #Odio la warning xd 
        try:
            eval(edo)
            return edo
        except:
            continue

