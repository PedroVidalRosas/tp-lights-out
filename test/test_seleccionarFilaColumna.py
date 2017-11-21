import seleccionarFilaColumna
import unittest

class SeleccionarFilaColumna(unittest.TestCase):

    def testelejirColumnaRecibeADeberiaDevolverTrue(self):

        columna = "A"

        resultado = seleccionarFilaColumna.elejirColumna(columna)

        self.assertEqual(resultado,True)

    def testelejirColumnaRecibeZDeberiaDevolverFalse(self):

        columna = "Z"

        resultado = seleccionarFilaColumna.elejirColumna(columna)

        self.assertEqual(resultado,False)

    def testelejirColumnaRecibeEspaciosDeberiaDevolverFalse(self):

        columna = "    "

        resultado = seleccionarFilaColumna.elejirColumna(columna)

        self.assertEqual(resultado,False)

    def testelejirColumnaRecibeUnDosDeberiaDevolverFalse(self):

        columna = "2"

        resultado = seleccionarFilaColumna.elejirColumna(columna)

        self.assertEqual(resultado,False)

    def testelejirFilaRecineUnUnoDeberiaDevolverTrue(self):

        fila = "1"

        resultado = seleccionarFilaColumna.elejirFila(fila)

        self.assertEqual(resultado,True)

    def testelejirFilaRecibeDosPalabrasDeberiaDevolverFalse(self):

        fila = "no valido"

        resultado = seleccionarFilaColumna.elejirFila(fila)

        self.assertEqual(resultado,False)

    def testelejirFilaRecibeUnSeisDeberiaDevolverFalse(self):

        fila = "6"

        resultado = seleccionarFilaColumna.elejirFila(fila)

        self.assertEqual(resultado,False)

    def testelejirFilaRecibeUnDosNegativoDeberiaDevolverFalse(self):

        fila = "-2"

        resultado = seleccionarFilaColumna.elejirFila(fila)

        self.assertEqual(resultado,False)