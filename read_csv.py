import pandas as pd
import math

# Funciones
def getCityData(df, city: str, country: str):
    result = (df["city_ascii"] == city) & (df["country"] == country)
    cityRow = df.loc[result].values.tolist()
    if len(cityRow) == 0:
        return 0
    return cityRow[0]

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

# Test
ci1 = input("1ra ciudad: ")
co1 = input("1er pais: ")

ci2 = input("2da ciudad: ")
co2 = input("2do pais: ")

print(haversineCSV(ci1,co1,ci2,co2))