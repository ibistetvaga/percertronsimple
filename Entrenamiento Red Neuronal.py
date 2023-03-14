import random
#Tset = [(1,1,1,1),(1,5,1,-1),(1,4,2,-1),(1,4,3,-1),(1,2,3,1),(1,3,5,1)]
random.seed()
def ingerir(archivo):
    dataSet = []
    with open(f"{archivo}", mode="r") as file:
        while True:
            linea = file.readline()
            if linea == "":
                break
            linea = linea.rstrip("\n")
            parametros = linea.split(" ")
            parametros.insert(0, 1)
            for i in range(len(parametros)):
                parametros[i] = float(parametros[i])
            dataSet.append(parametros)
    return dataSet

def comprobar(archivo, W):
    dataSet = []
    errores = 0
    with open(f"{archivo}", mode="r") as file:
        
        while True:
            linea = file.readline()
            if linea == "":
                break
            linea = linea.rstrip("\n")
            parametros = linea.split(" ")
            parametros.insert(0, 1)
            for i in range(len(parametros)):
                parametros[i] = float(parametros[i])
            dataSet.append(parametros)

        
        for i in range(len(dataSet)):
            h = W[0]*dataSet[i][0]+W[1]*dataSet[i][1]+W[2]*dataSet[i][2]
            s = signo(h)
            if s != dataSet[i][3]:
                #print(f"Pesos {W} no sirven con el ejemplo {i}")
                errores += 1
        perrores = (errores / len(dataSet)) * 100
        certeza = 100 - perrores
        print(W, "son los pesos correctos con el ", certeza, "% de certeza")    
        print(errores)
        return True
            
def signo(n):
    if n >= 0:
        return 1
    else:
        return -1

def correcto(W, Tset):
    
    for i in range(len(Tset)):
        h = W[0]*Tset[i][0]+W[1]*Tset[i][1]+W[2]*Tset[i][2]
        s = signo(h)
        if s != Tset[i][3]:
            #print(f"Pesos {W} no sirven")
            return False
    print(W)    
    return True    


def entrenar(Tset, lamb):
    
    W=[random.randint(-5, 5),random.randint(-5,5),random.randint(-5,5)]
    while (True):
        # iterar sobre cada ejemplo 
        for i in range(len(Tset)):
            
            h = W[0]*Tset[i][0]+W[1]*Tset[i][1]+W[2]*Tset[i][2]
            s = signo(h)

            # corregir pesos
            for j in range(3):
                dW = lamb*(Tset[i][3]-s)*Tset[i][j]
                W[j] = W[j] + dW

        # verificar
        if correcto(W, Tset) == True:
            break
    return W

dataSet = ingerir("filename1.txt")

print(entrenar(dataSet, 0.01))

comprobar("filename1.txt", entrenar(dataSet, 0.01))