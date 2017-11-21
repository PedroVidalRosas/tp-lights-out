def devolverPosicionDeColumnaYFilaDelMapa(mapa,columna,fila):
    posicionColumna = 0
    for c in range(len(mapa[0])):
        if mapa[0][c] == columna:
            break
        posicionColumna += 1
    posicionFila = 0
    for f in range(len(mapa)):
        if mapa[f][0] == fila:
            break
        posicionFila += 1
    return posicionColumna,posicionFila