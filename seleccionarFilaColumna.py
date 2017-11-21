

def elejirColumna(columna):
    menu = "ABCDER"

    for x in range(len(menu)):
        if menu[x] == columna:

            return True

    return False


def elejirFila(fila):

    menu = "12345R"

    for x in range(len(menu)):
        if menu[x] == fila:

            return True

    return False

def elejirColumnaFila():
    posicionColumna,posicionFila= 1,1
    columna = False
    while columna != True:
        posicionColumna = input("ingrese una letra de la A hasta la E para columna o R para Reiniciar: ").upper()
        columna = elejirColumna(posicionColumna)
        if columna == False:
            print("ingrese una opcion invalida")
            continue
        if posicionColumna == "R":
            break

        fila = False
        while fila != True:
            posicionFila = input("ingrese un numero del 1 al 5 para fila: ").upper()
            fila = elejirFila(posicionFila)
            if fila == False:
                print("Ingreso una Opcion Invalida")

        if posicionFila == "R":
            break
    return posicionColumna,posicionFila

