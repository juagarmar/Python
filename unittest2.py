import unittest
import sys

class Quaternion:
# Creamos el objeto.
    def __init__(self, w=1., x=0., y=0., z=0.):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
# Aplicando métodos mágicos
# Return obj negated (-obj)
    def __neg__(self):
        return Quaternion(-self.w, -self.x, -self.y, -self.z)
# Return a + b, for a and b numbers.
    def __add__(self, other):
        return Quaternion(self.w+other.w, self.x+other.x, self.y+other.y, self.z+other.z)
# Return a - b.
    def __sub__(self, other):
        return Quaternion(self.w-other.w, self.x-other.x, self.y-other.y, self.z-other.z)
# Aplicamos un ejemplo:
q1=Quaternion(1,3,3,1)
q2=Quaternion(2,2,3,3)
resultneg=-q1
print("Solución para el modelo neg")
print(resultneg.w)
print(resultneg.x)
print(resultneg.y)
print(resultneg.z)
print("Solución para el modelo neg")
resultadd=q1+q2
print(resultadd.w)
print(resultadd.x)
print(resultadd.y)
print(resultadd.z)
print("Solución para el modelo sub")
resultsub=q1-q2
print(resultsub.w)
print(resultsub.x)
print(resultsub.y)
print(resultsub.z)


class TestQuaternion(unittest.TestCase):      
    
    def test_neg(self):
        self.assertEqual(resultneg.w,-q1.w)
        self.assertEqual(resultneg.x,-q1.x)
        self.assertEqual(resultneg.y,-q1.y)
        self.assertEqual(resultneg.z,-q1.z)

    def test_add(self):
        self.assertEqual(resultadd.w,q1.w+q2.w)
        self.assertEqual(resultadd.x,q1.x+q2.x)
        self.assertEqual(resultadd.y,q1.y+q2.y)
        self.assertEqual(resultadd.z,q1.z+q2.z)
        
    def test_sub(self):
        self.assertEqual(resultsub.w,q1.w-q2.w)
        self.assertEqual(resultsub.x,q1.x-q2.x)
        self.assertEqual(resultsub.y,q1.y-q2.y)
        self.assertEqual(resultsub.z,q1.z-q2.z)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestQuaternion )
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
