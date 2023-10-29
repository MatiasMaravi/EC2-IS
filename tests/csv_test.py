import unittest
import requests
import math
import pandas as pd

def haversine(lat1, lon1, lat2, lon2):
    # Convertimos las coordenadas de grados a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Fórmula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radio de la Tierra en kilómetros (aproximadamente 6371 km)
    r = 6371.0
    
    # Calculamos la distancia
    distance = c * r
    
    return distance

class CSV:
    def __init__(self):
        self.df = pd.read_csv("worldcities.csv")
    
    def obtener_coordenadas(self, city, country):
        result = (self.df["city_ascii"] == city) & (self.df["country"] == country)
        cityRow = self.df.loc[result].values.tolist()
        
        if len(cityRow) == 0:
            # print("Error: Ciudad no existe")
            return 0, 0

        cityRow = cityRow[0]
        
        return cityRow[2], cityRow[3]
    
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        latitud1, longitud1 = self.obtener_coordenadas(ciudad1,pais1)
        latitud2, longitud2 = self.obtener_coordenadas(ciudad2,pais2)

        if latitud1 == 0 and longitud1 == 0:
            return 0
        
        if latitud2 == 0 and longitud2 == 0:
            return 0
        
        distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
        return distancia

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