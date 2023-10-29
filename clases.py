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
            data = data[0]
            # Imprimimos la respuesta
            latitud1 = data["lat"]
            longitud1 = data["lon"]
            print(f"Ciudad: {ciudad}")
            print(f"Latitud: {latitud1}")
            print(f"Longitud: {longitud1}")
            return latitud1,longitud1
        else:
            # Imprimimos un mensaje de error si la solicitud falla
            print("Error al obtener los datos de la API")
            return 0,0
    
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        if((ciudad1 == ciudad2) and (pais1 == pais2)):
            print("Error: Las ciudades son las mismas")
            return 0
            
        latitud1, longitud1 = self.obtener_coordenadas(ciudad1,pais1)
        latitud2, longitud2 = self.obtener_coordenadas(ciudad2,pais2)
        distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
        return distancia

class Mock:
    def __init__(self) -> None:
        pass
    
    def obtener_coordenadas(self,ciudad,pais):
        print(f"Ciudad: {ciudad}")
        print(f"Latitud: 100")
        print(f"Longitud: 100")
        return 100,100
    
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        return 100
    
class CSV:
    def __init__(self):
        self.df = pd.read_csv("worldcities.csv")
    
    def obtener_coordenadas(self,city,country):
        result = (self.df["city_ascii"] == city) & (self.df["country"] == country)
        cityRow = self.df.loc[result].values.tolist()
        cityRow = cityRow[0]
        print(f"Ciudad: {city}")
        print(f"Latitud: {cityRow[2]}")
        print(f"Longitud: {cityRow[3]}")
        return cityRow[2], cityRow[3]
    
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        latitud1, longitud1 = self.obtener_coordenadas(ciudad1,pais1)
        latitud2, longitud2 = self.obtener_coordenadas(ciudad2,pais2)
        distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
        return distancia

class Factory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key):
        builder = self._builders.get(key)
        if not builder:
            print("Error al crear el objeto")
            raise ValueError(key)
        return builder()
