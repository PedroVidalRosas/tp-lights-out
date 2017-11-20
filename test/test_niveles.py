import niveles
import unittest

class NivelesTest(unittest.TestCase):

    def testNivelesSiRecibeUnaLetraDeberiaDevolverUnaListaVacia(self):

        nivel = "a"

        resultado = niveles.niveles(nivel)

        self.assertEqual(resultado,[])

    def testNivelesRecibeUnNivelSeisDeberiaDevolverUnaListaVacia(self):

        nivel = 6

        resultado = niveles.niveles(nivel)

        self.assertEqual(resultado,[])

    def testNivelesRecibeNivelMenosUnoDeberiaDevolverUnaListaVacia(self):

        nivel = -1

        resultado = niveles.niveles((nivel))

        self.assertEqual(resultado,[])

    def testNivelesRecibeNivelUnoDevuelveElNivelUno(self):

        nivel = 1

        resultado = niveles.niveles(nivel)

        self.assertEqual(resultado,['   A B C D E',
                                    '1 |0 0 . 0 0',
                                    '2 |0 . 0 . 0',
                                    '3 |. 0 0 0 .',
                                    '4 |0 . 0 . 0',
                                    '5 |0 0 . 0 0'])
    def testNivelesRecibeNivelCincoDeberiaDevolverElNIvelCinco(self):

        nivel = 5

        resultado = niveles.niveles(nivel)

        self.assertEqual(resultado,['   A B C D E',
                                   '1 |. . . 0 0',
                                   '2 |. . . 0 0',
                                   '3 |. . . . .',
                                   '4 |0 0 . . .',
                                   '5 |0 0 . . .'])