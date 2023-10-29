import requests
from .utils.haversine import haversine
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