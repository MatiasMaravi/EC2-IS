from classes.api import API
from classes.mock import Mock
from classes.csv import CSV

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
    def load(self):
        self.register_builder("api", API)
        self.register_builder("mock", Mock)
        self.register_builder("csv", CSV)
