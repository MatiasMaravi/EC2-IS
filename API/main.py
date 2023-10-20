import requests
import math
# Definimos las variables
ciudad1, pais1 = "Bogota", "Colombia"

# Construimos la URL con las variables
url = f"https://nominatim.openstreetmap.org/search?q={ciudad1},{pais1}&format=json"

# Realizamos la solicitud a la API
response = requests.get(url)

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

def obtener_coordenadas(ciudad,pais):
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

def calcular_distancia(ciudad1,pais1,ciudad2,pais2):
    url = f"https://nominatim.openstreetmap.org/search?q={ciudad1},{pais1}&format=json"
    response = requests.get(url)
    # Verificamos si la solicitud fue exitosa (código de estado 200)
    latitud1, longitud1 = obtener_coordenadas(ciudad1,pais1)
    latitud2, longitud2 = obtener_coordenadas(ciudad2,pais2)
    distancia = haversine(float(latitud1),float(longitud1),float(latitud2),float(longitud2))
    print("Las coordenadas de ",ciudad1," son ",latitud1,", ",longitud1)
    print("Las coordenadas de ",ciudad2," son ",latitud2,", ",longitud2)
    print("La distancia entre ",ciudad1," y ",ciudad2," es de ",distancia," km")
    
calcular_distancia("Bogota","Colombia","Lima","Peru")