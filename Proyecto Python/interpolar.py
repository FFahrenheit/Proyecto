"""
INTERPOLACION MEDIANTE EL USO
DE DIFERENCIAS FINITAS
"""

import validador
import archivos

epsilon = 4

def leerEjercicio():
    try:
        filename = input("Ingrese el nombre del archivo a cargar ejemplo: ")
        cargarEjemplo(filename,True)
    except:
        print("ARCHIVO INVALIDO")

        
def cargarEjemplo(filename="interpolar",isSave=False):
    if isSave:
        file = archivos.leerGuardado(filename)
    else:
        file = archivos.leerArchivo(filename)

    text = file.read().split("\n")
    text.pop()

    value = float(text[0])

    data = []

    for i in range(1,len(text)):
        vals = text[i].split("|")
        data.append( [float(vals[0]), float(vals[1])])

    calcular(data,value)
    file.close()



def nuevoEjercicio():
    n = validador.requestInt("Ingrese el numero de datos a ingresar: ")
    
    data = []
    for i in range(n):
        val = []
        x = validador.requestReal(f"Ingrese el valor para x{i}: ")
        y = validador.requestReal(f"Ingrese el valor para f(x{i}): ")
        val.append(x)
        val.append(y)
        data.append(val)

    value = validador.requestReal("Ingrese el punto a interpolar: ")

    calcular(data,value)

    save = input("Ingrese \"S\" si quiere guardar este ejercicio: ")
    if save == 'S' or save == 's':
        filename = input("Ingrese el nombre del archivo (sin extension): ")
        guardarEjercicio(value,data,filename)


def guardarEjercicio(value,data,filename):
    file = archivos.guardarArchivo(filename)

    file.write(str(value)+"\n")

    for dato in data:
        file.write(f"{dato[0]}|{dato[1]}\n")

    file.close()


def calcular(data, value):
    print("\t\tDiferencias finitas\n\n")

    dif = getFiniteDifferences(data)

    n = len(data)
    
    offset = findOffest(data,value)
    print(offset)
    forward = findDirecion(data,offset)

    if forward:
        polynomials = n - 1 - offset
    else:
        offset += 1
        polynomials = offset 

    
    s = getS(data,value,offset,forward)

    for i in range(polynomials):
        total = data[offset][1]
        print(f"{total} + ", end = '')
        for j in range(i+1):
            if j != 0:
                print(" + ",end='')
            total += getMultiplers(s,j,forward) * getDif(dif,offset,j,forward) / factorial(j+1)
        total = round(total,epsilon)
        print(f" = {total:.4f}")

def getDif(dif,offset,j,forward):
    if forward:
        A = dif[offset][j+1]
    else:
        A = dif[offset-j-1][j+1]
    print("(%.4f)"%A,end='')
    return A

def factorial(n):
    t = 1
    for i in range(1,n+1):
        t *= i
    print(f"/{n}!",end='')
    return t

def getMultiplers(s,n,direction):
    t = s
    print("%.4f"%s,end='')
    for i in range(1,n+1):
        if direction:
            t *= (s-i)
            print("(%.4f - %d)"%(s,i),end='')
        else:
            t *= (s+i)
            print("(%.4f + %d)"%(s,i),end='')
    return t

def getS(data,value,off,direction):
    if direction: #Dependiendo si es hacia adelante o hacia atras
        h = abs(data[off][0] - data[off+1][0])
        print(f"s = ({value} - {data[off][0]})/{h} = ",end='')
        s = (value - data[off][0])/(h)
    else:
        h = abs(data[off][0] - data[off+1][0])
        print(f"s = ({data[off][0]} - {value})/{h} = ",end='')
        s = (data[off][0] - value)/(h)
    
    print(s,end='\n\n')
    return round(s,epsilon)

def getFiniteDifferences(data):
    n = len(data)
    dif = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(dif)): #Llenar con ceros para valores no definidos
        for j in range(len(dif[0])):
            dif[i][j] = 0
    
    for i in range(n):  #Primera columna es y
        dif[i][0] = data[i][1]
    
    for i in range(n):   #Repetir n-1 porque ya tenemos a0
        diff = i+1 #Primera iteracion necesitamos n-1, despues n-2 y así y así 
        for j in range(n-diff): 
            print(f"{dif[j+1][i]:.4f} - {dif[j][i]:.4f}")
            ak =  round(dif[j+1][i] - dif[j][i],epsilon)
            print("Δ^%d [%d] = %.4f\n"%(i+1,j,ak))
            dif[j][i+1] = ak
    printMatrix(dif) #Imprimir la matriz resultante
    return dif


def findOffest(data, value):
    n = len(data)
    for i in range(n-1):
        if data[i][0] < value and data[i+1][0] > value:
            return i 
    if data[0][0] > value:
        return 0
    else:
        return n-1

def findDirecion(data,offset):
    if offset < len(data) // 2:
        print("\t\tHacia adelante\n\n")
        return True
    else:
        print("\t\tHacia atras\n\n")
        return False

def printMatrix(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            print("%f"%data[i][j],end='\t')
        print("\n") 