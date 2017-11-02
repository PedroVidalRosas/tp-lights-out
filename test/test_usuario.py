import unittest
import usuario

class UsuarioTest(unittest.TestCase):
    def testSaludarDeberiaDevolverHola(self):
        #Arrenge
        saludoEsperado = "Hola"

        #act
        saludoRecibido = usuario.saludar()

        #Assert
        self.assertEqual(saludoEsperado,saludoRecibido)
