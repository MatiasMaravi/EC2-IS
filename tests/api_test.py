import unittest
import requests
import math

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
class API:
    def __init__(self) -> None:
        pass
    def obtener_coordenadas(self, ciudad,pais):
        url = f"https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json"
        response = requests.get(url)
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parseamos la respuesta JSON
            data = response.json()
            if len(data) == 0:
                print("Error: Ciudad no existe")
                return 0,0
            data = data[0]
            # Imprimimos la respuesta
            latitud1 = data["lat"]
            longitud1 = data["lon"]
            # print(f"Ciudad: {ciudad}")
            # print(f"Latitud: {latitud1}")
            # print(f"Longitud: {longitud1}")
            return latitud1,longitud1
        else:
            # Imprimimos un mensaje de error si la solicitud falla
            print("Error al obtener los datos de la API")
            return 0,0
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        latitud1, longitud1 = self.obtener_coordenadas(ciudad1,pais1)
        latitud2, longitud2 = self.obtener_coordenadas(ciudad2,pais2)
        distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
        return distancia

class TestAPI(unittest.TestCase):    
    def test_coordenadas(self):
        api = API()
        lat1,lon1 = api.obtener_coordenadas('Buenos Aires','Argentina')
        lat2,lon2 = api.obtener_coordenadas('Cordoba','Argentina')
        self.assertEqual(lat1,'-34.6075682')
        self.assertEqual(lon1,'-58.4370894')
        self.assertEqual(lat2,'-31.4166867')
        self.assertEqual(lon2,'-64.1834193')
    def test_distancia_haversine(self):
        api = API()
        distancia = api.calcular_distancia('Buenos Aires','Argentina','Cordoba','Argentina')
        self.assertEqual(distancia,642.4468335604646)
    def test_existe_ciudad(self):
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