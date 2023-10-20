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
        latitud = 0
        longitud = 0
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parseamos la respuesta JSON
            data = response.json()
            data = data[0]
            # Imprimimos la respuesta
            latitud1 = data["lat"]
            longitud1 = data["lon"]
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


class Mock:
    def __init__(self) -> None:
        pass
    def obtener_coordenadas(self,ciudad,pais):
        return 100,100
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        return 100
    
class CSV:
    def __init__(self):
        pass
    def obtener_coordenadas(self,city,country):
        df = pd.read_csv("worldcities.csv")
        result = (df["city_ascii"] == city) & (df["country"] == country)
        cityRow = df.loc[result].values.tolist()
        if len(cityRow) == 0:
            return 0

        cityRow = cityRow[0]
        return cityRow[2], cityRow[3]
    def calcular_distancia(self,ciudad1,pais1,ciudad2,pais2):
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        latitud1, longitud1 = self.obtener_coordenadas(ciudad1,pais1)
        latitud2, longitud2 = self.obtener_coordenadas(ciudad2,pais2)
        distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
        return distancia


# Funciones
def getCityData(df, city: str, country: str):
    result = (df["city_ascii"] == city) & (df["country"] == country)
    cityRow = df.loc[result].values.tolist()
    if len(cityRow) == 0:
        return 0
    return cityRow[0]


def haversineCSV(city1: str, country1: str, city2: str, country2: str):
    if city1 == city2 and country1 == country2:
        return "Son la misma localidad"
    
    df = pd.read_csv("worldcities.csv")
    fRow = getCityData(df, city1, country1)
    if fRow == 0:
        return f"No existe la localidad de {city1} en el pais {country1}"

    sRow = getCityData(df, city2, country2)
    if sRow == 0:
        return f"No existe la localidad de {city2} en el pais {country2}"

    dist = round(haversine(fRow[2], fRow[3], sRow[2], sRow[3]), 2)
    return f"La distancia entre {city1} y {city2} es: {dist}km"

class Factory:
    def __init__(self,ciudad1,pais1,ciudad2,pais2):
        self.ciudad1 = ciudad1
        self.pais1 = pais1
        self.ciudad2 = ciudad2
        self.pais2 = pais2
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder()
    
factory = Factory("Bogota","Colombia","Lima","Peru")
factory.register_builder('api', API)
factory.register_builder('mock', Mock)
factory.register_builder('csv', CSV)


objeto1 = factory.create('mock')
distancia = objeto1.calcular_distancia("Bogota","Colombia","Lima","Peru")
print(distancia)