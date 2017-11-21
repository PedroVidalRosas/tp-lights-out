import niveles
import seleccionarFilaColumna
import posicionDeColumnaYFilaEnElMapa



def mostrarmapa(mapa):
    for x in range(len(mapa)):
        print(mapa[x])


def juegopredeterminado():

    nivel = 1
    while nivel != 6:

        mapa = niveles.niveles(nivel)
        mostrarmapa(mapa)
        posicionColumna,posicionFila = seleccionarFilaColumna.elejirColumnaFila()
        posicionColumna,posicionFila = posicionDeColumnaYFilaEnElMapa.devolverPosicionDeColumnaYFilaDelMapa(mapa,posicionColumna,posicionFila)

        print(posicionColumna,posicionFila)
        nivel += 1

juegopredeterminado()