def reformat(archivo):
    unoSet = []
    menoSet = []
    with open(f"{archivo}", mode="r") as file:
        while True:
            linea = file.readline()
            if linea == "":
                break
            parametros = linea.split(" ")
            if parametros[2] == "1\n":
                parametros.pop(-1)
                unoSet.append(parametros[0]+" "+parametros[1])
            else:
                parametros.pop(-1)
                menoSet.append(parametros[0]+" "+parametros[1])
               
    return unoSet, menoSet

unoSet, menoSet = reformat("filename1.txt")

with open("unos.txt", mode="w") as file:
    file.writelines(unoSet)

with open("menos.txt", mode="w") as file:
    file.writelines(menoSet)

