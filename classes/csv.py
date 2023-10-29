import pandas as pd
import os
from .utils.haversine import haversine
class CSV:
    def __init__(self):
        current_dir = os.getcwd()
        self.df = pd.read_csv(current_dir+"/data/worldcities.csv")
    
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