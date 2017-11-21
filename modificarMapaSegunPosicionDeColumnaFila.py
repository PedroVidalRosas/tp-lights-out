
def crearMapaEnUnaListaDeLista(mapa):

    # convierto el mapa recibido en una lista de lista [[  ],[  ]]
    mapaDeListaDeLista = []
    for x1 in range(0, len(mapa)):
        listaauxi = []
        for x2 in range(len(mapa[0])):
            listaauxi.append(mapa[x1][x2])
        mapaDeListaDeLista.append(listaauxi)

    return (mapaDeListaDeLista)

def convertirMapaEnUnaListaDeCadenas(mapa):
    # convierto el mapa de lista de lista en una lista de cadenas['  '.'  ']
    mapaListaDeCadenas = []
    for x1 in range(len(mapa)):
        lenn = list(mapa[x1])
        listaAux = []
        for x2 in range(len(lenn)):
            listaAux.append(mapa[x1][x2])
        mapaListaDeCadenas.append(''.join(listaAux))
    return mapaListaDeCadenas

def prenderOApagarLuz(mapa,columna,fila):
    #convierto el mapa en una lista de lista para poder modificarlo
    mapa = crearMapaEnUnaListaDeLista(mapa)

    # modico donde esta la posicion de columna y fila
    if mapa[fila][columna] == '0':
        mapa[fila][columna] = '.'
    elif mapa[fila][columna] == '.':
        mapa[fila][columna] = '0'
    # modifico donde esta la pocicion a la derecha de la posicion de columna y fila
    if columna + 2 <= (len(mapa[0])):
        if mapa[fila][columna + 2] == '0':
            mapa[fila][columna + 2] = '.'
        elif mapa[fila][columna + 2] == '.':
            mapa[fila][columna + 2] = '0'
    # modifo donde esta la posicion a la izquierda de la posicion de columna y fila
    if mapa[fila][columna - 2] == '0':
        mapa[fila][columna - 2] = '.'
    elif mapa[fila][columna - 2] == '.':
        mapa[fila][columna - 2] = '0'
    # modifico donde esta la posicion hacia arriba de la posicion de columna y fila
    if mapa[fila - 1][columna] == '0':
        mapa[fila - 1][columna] = '.'
    elif mapa[fila - 1][columna] == '.':
        mapa[fila - 1][columna] = '0'
    # modificar donde esta la pocicion hacia abajo de la posicion de columna y fila
    if fila + 1 <= (len(mapa) - 1):
        if mapa[fila + 1][columna] == '0':
            mapa[fila + 1][columna] = '.'
        elif mapa[fila + 1][columna] == '.':
            mapa[fila + 1][columna] = '0'

    # convierto el mapa en una lista de cadenas y la retorno
    mapa = convertirMapaEnUnaListaDeCadenas(mapa)
    return mapa