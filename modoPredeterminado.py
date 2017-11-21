import niveles
import seleccionarFilaColumna
import posicionDeColumnaYFilaEnElMapa
import modificarMapaSegunPosicionDeColumnaFila



def mostrarmapa(mapa):
    for x in range(len(mapa)):
        print(mapa[x])


def juegopredeterminado():

    nivel = 1
    while nivel != 6:

        mapa = niveles.niveles(nivel)
        mostrarmapa(mapa)

        #Se elije una letra para columna,dentro de los valores correctos
        #se elije un numero para fila, dentro de los valores correctos
        posicionColumna,posicionFila = seleccionarFilaColumna.elejirColumnaFila()

        #si la posicionColumna o posicionFila es "R" se reinicia
        if posicionFila == "R" or posicionColumna == "R":
            continue

        #Se devuelve la posicion que se encuentra en el mapa de posicionColumna y posicionFila
        posicionColumna,posicionFila = posicionDeColumnaYFilaEnElMapa.devolverPosicionDeColumnaYFilaDelMapa(mapa,posicionColumna,posicionFila)


        mapa = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,posicionColumna,posicionFila)

        mostrarmapa(mapa)

juegopredeterminado()