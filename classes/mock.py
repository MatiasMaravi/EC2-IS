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