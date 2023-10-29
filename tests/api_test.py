import unittest
import sys
sys.path.append('../')  # Agrega el directorio raíz al sys.path
from classes.api import API


class TestAPI(unittest.TestCase):    
    def test_coordenadas(self):
        api = API()
        lat1,lon1 = api.obtener_coordenadas('Buenos Aires','Argentina')
        lat2,lon2 = api.obtener_coordenadas('Cordoba','Argentina')
        #Las coordenadas se obtuvieron de la api con el uso de postman, por eso verificamos si son las mismas a las 
        #las que obtuvimos con el uso de la api de nuestra clase
        self.assertEqual(lat1,'-34.6075682')
        self.assertEqual(lon1,'-58.4370894')
        self.assertEqual(lat2,'-31.4166867')
        self.assertEqual(lon2,'-64.1834193')
    def test_distancia_haversine(self):
        api = API()
        distancia = api.calcular_distancia('Buenos Aires','Argentina','Cordoba','Argentina')
        self.assertEqual(distancia,642.4468335604646)
    def test_noexiste_ciudad(self):
        api = API()
        lat1, lon1 = api.obtener_coordenadas('finoaofinakfo','dadkjanbdkjad')
        self.assertEqual(lat1,0)
        self.assertEqual(lon1,0)
    def test_ciudad_duplicada(self):
        api = API()
        distancia = api.calcular_distancia('Buenos Aires','Argentina','Buenos Aires','Argentina')
        self.assertEqual(distancia,0)

if __name__ == '__main__':
    unittest.main()