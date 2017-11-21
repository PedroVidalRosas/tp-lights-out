import modificarMapaSegunPosicionDeColumnaFila
import unittest

class modificarMapaSegunPosicionDeColumnaFilaTest(unittest.TestCase):

    def testmodificarMapaSegunPosicionDeColumnaFilaRecineUnMapaConTodasLasLucesApagadasDeberiaSegunPosicionDeColumnaYFilaPrenderlas(self):
        mapa = ['. . .',
                '. . .',
                '. . .']
        columna = 2
        fila = 1

        reslutado = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,columna,fila)

        self.assertEqual(reslutado,['. 0 .',
                                    '0 0 0',
                                    '. 0 .'])

    def testmodificarMapaSegunPosicionDeColumnaFilaRecibeUnMapaConLasLuvePrendidasDeberiaDevolverSegunLaPosicionDeColumaYFilaApagarlas(self):

        mapa = ['0 0 0',
                '0 0 0',
                '0 0 0']
        columna = 2
        fila = 1

        resultado = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,columna,fila)

        self.assertEqual(resultado,['0 . 0',
                                    '. . .',
                                    '0 . 0'])

    def testmodificarMapaSegunPosicionDeColumnaFilaRecibeUnMapaConLasLucesPrendinasDeberiaDevolverUnMapaSegunLaPosiconDeColumnaYFilaApagarlas(self):

        mapa =['   A B C',
               '1 |0 0 .',
               '2 |0 . .']
        columna = 3
        fila = 1

        resultado = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,columna,fila)

        self.assertEqual(resultado,['   A B C',
                                    '1 |. . .',
                                    '2 |. . .'])

    def testmodificarMapaSegunPosicionDeColumnaFilaRecibeUnMapaConLucesApagadasDeberiaSegunPosicionDeColumnaYFilaPrederlas(self):

        mapa = ['   A B C',
                '1 |. . .',
                '2 |. . .']
        columna = 7
        fila = 2

        resultado = modificarMapaSegunPosicionDeColumnaFila.prenderOApagarLuz(mapa,columna,fila)

        self.assertEqual(resultado,['   A B C',
                                    '1 |. . 0',
                                    '2 |. 0 0'])
