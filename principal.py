import eleccionDelMenuPrincipal

def menuPrincipal():
    print("Bienvenido al juedo de Pedro")
    print("Puede ingresar las sigientes opciones: ")
    print("Si ingresa una opcion invalida saldra del juego")
    print("1 para jugar en modo PREDETERMINADO")
    print("2 para jugar en mmodo ALEATORIO")
    print("3 para salir")
    eleccion = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(input())
    if eleccion == 3:
        print("Saliste del Juego de Pedro")
menuPrincipal()