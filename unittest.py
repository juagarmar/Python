import unittest

class Fraccion(object):
    """Clase que representa una fracción matemática"""
    
    def __init__(self, numerador, denominador):
        """Inicializa el objeto fracción"""
        self.numerador=numerador
        self.denominador=denominador
    
    def get_numerador(self):
        """Retorna el numerador de la fracción"""
        return self.numerador
    
    def get_denominador(self):
        """Retorna el denominador de la fracción"""
        return self.denominador
    
    def multiplica(self, other):
        """Devuelve la multiplicación de fracciones"""
        return Fraccion(self.get_numerador() * other.get_numerador(), self.get_denominador()*other.get_denominador())
    

class TestFraccion(unittest.TestCase):

    def test_crear_fraccion(self):
        f = Fraccion(1, 2)
        self.assertIsNotNone(f)
        
    def test_numerador(self):
        f = Fraccion(1, 2)
        self.assertEqual(f.get_numerador(), 1)
        
    def test_denominador(self):
        f = Fraccion(2, 4)
        """Faltan paréntesis en la función get_denominador"""
        self.assertEqual(f.get_denominador(), 4)
    
    def test_multiplicacion_fracciones(self):
        f1 = Fraccion(1, 2)
        f2 = Fraccion(2, 5)
        
        f3 = f1.multiplica(f2)
        
        self.assertEqual(f3.get_numerador(), 2)
        self.assertEqual(f3.get_denominador(), 10)

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestFraccion )
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
