import unittest
import eleccionDelMenuPrincipal

class EleccionDelMenuPrincipalTest(unittest.TestCase):

    def testEleccionDelMenuPrincipalRecibeCuatroDeberiaDevolverTres(self):

        eleccion = "4"

        reslutado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(reslutado,3)

    def testEleccionDelMenuPrioncipalRecineUnaLetraDeberiaDevolverTres(self):

        eleccion = "a"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,3)

    def testEleccionDelMenuPrincipalRecimeEspaciosDeberiaDevolverTres(self):

        eleccion = "    "

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,3)

    def testEleccionDelMenuPrincipalRecibeMenosUnoDeberiaDevolverTres(self):

        eleccion = "-1"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,3)

    def testEleccionDelMenuPrincipalRecibeUnoDeberiaDevolverUno(self):

        eleccion = "1"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,1)
    def testEleccionDelMenuPrincipalRecibeDosDeberiaDeolverDos(self):

        eleccion = "2"

        resultado = eleccionDelMenuPrincipal.eleccionDelMenuPrincipal(eleccion)

        self.assertEqual(resultado,2)