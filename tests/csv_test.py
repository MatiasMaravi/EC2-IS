import unittest
import sys
sys.path.append('../')  # Agrega el directorio raíz al sys.path
from classes.csv import CSV
class TestCSV(unittest.TestCase):    
    def test_coordenadas(self):
        csv = CSV()
        lat1,lon1 = csv.obtener_coordenadas('Buenos Aires','Argentina')
        self.assertEqual(lat1, -34.5997)
        self.assertEqual(lon1, -58.3819)

        lat2,lon2 = csv.obtener_coordenadas('Cordoba','Argentina')
        self.assertEqual(lat2, -31.4167)
        self.assertEqual(lon2, -64.1833)
    
    def test_existe_ciudad(self):
        csv = CSV()
        lat1, lon1 = csv.obtener_coordenadas('finoaofinakfo','dadkjanbdkjad')
        self.assertEqual(lat1,0)
        self.assertEqual(lon1,0)
    
    def test_distancia_haversine(self):
        csv = CSV()
        distancia = csv.calcular_distancia('Buenos Aires','Argentina','Cordoba','Argentina')
        self.assertEqual(distancia, 646.2713861985634)

    def test_ciudad_duplicada(self):
        csv = CSV()
        distancia = csv.calcular_distancia('Buenos Aires','Argentina','Buenos Aires','Argentina')
        self.assertEqual(distancia,0)

if __name__ == '__main__':
    unittest.main()