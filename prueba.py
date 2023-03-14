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
        lineas = len(file.readlines())
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
            if s != Tset[i][3]:
                print(f"Pesos {W} no sirven con el ejemplo {i}")
                errores += 1
        certeza = lineas-errores
        print(W, "son los pesos correctos con el ", errores, "% de certeza")    
        return True
            
            


#print(ingerir("filename1.txt"))
print(comprobar("filename2.txt", [1.4199999999999995, 1.752216239999992, -2.4290569600000014]))