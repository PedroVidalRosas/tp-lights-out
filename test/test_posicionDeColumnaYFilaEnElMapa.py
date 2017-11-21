import posicionDeColumnaYFilaEnElMapa
import unittest

class posicionDeColumnaYFilaEnElMapaTest(unittest.TestCase):

    def testposicionDeColumnaYFilaEnElMapaRecibeComoColumnaAYcomoFila1DeberiaDevolver1y1(self):

        columna = "A"
        fila = "1"
        mapa = ['0A','1.']

        resultadoColumna,resultadoFila = posicionDeColumnaYFilaEnElMapa.devolverPosicionDeColumnaYFilaDelMapa(mapa,columna,fila)

        self.assertEqual(resultadoColumna,1)
        self.assertEqual(resultadoFila,1)