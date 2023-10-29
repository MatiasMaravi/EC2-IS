# EC2-IS
EC2 de Ingenieria de software
## Integrantes
- Matias Maravi Anyosa
- Alejandro Calizaya Alvarez
- Leandro Machaca Soloaga

## Crear entorno virtual
```
python3 -m venv venv
```
## Activar entorno virtual
```
source venv/bin/activate
```

## Instalar dependencias
```
pip install -r requirements.txt
```

## Ejecutar servidor
```zsh
python3 app.py
```

## Ejecutar los tests unitarios

```bash
cd tests
#Test de la clase API
python3 test_api.py

#Test de la clase CSV
python3 test_csv.py
```

## Casos de Prueba Manual
| Test Case | Precondition | Test Steps | Test Data | Expected Results |
|--------|--------|--------|--------|-------|
|Verifica el calculo de las distancias entre 2 ciudades validas usando API|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método API <br> 4. Ingresar 2 ciudades válidas <br> 5. Click en "Calcular Distancia" |Ciudad 1 : Buenos Aires <br> Pais 1: Argentina <br> Ciudad 2: Cordoba <br> Pais 2: Argentina|Distancia: 642.4468335604646 km|
|Verifica el calculo de las distancias entre 2 ciudades validas usando CSV|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método CSV <br> 4. Ingresar 2 ciudades válidas <br> 5. Click en "Calcular Distancia" |Ciudad 1 : Buenos Aires <br> Pais 1: Argentina <br> Ciudad 2: Cordoba <br> Pais 2: Argentina|Distancia: 646.2713861985634 km|
|Verifica el calculo de las distancias entre 2 ciudades iguales usando CSV|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método CSV <br> 4. Ingresar la misma ciudad 2 veces <br> 5. Click en "Calcular Distancia" |Ciudad 1 : Buenos Aires <br> Pais 1: Argentina <br> Ciudad 2: Buenos Aires <br> Pais 2: Argentina|Distancia: 0 km|
|Verifica el calculo de las distancias entre 2 ciudades iguales usando API|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método API <br> 4. Ingresar la misma ciudad 2 veces <br> 5. Click en "Calcular Distancia" |Ciudad 1 : Buenos Aires <br> Pais 1: Argentina <br> Ciudad 2: Buenos Aires <br> Pais 2: Argentina|Distancia: 0 km|
|Verifica el calculo de las distancias entre 2 ciudades invalidas usando CSV|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método CSV <br> 4. Ingresar 2 ciudades válidas <br> 5. Click en "Calcular Distancia" |Ciudad 1 : fasfsafasf <br> Pais 1: adddd <br> Ciudad 2: uyjgfj <br> Pais 2: gavwqfaf|Distancia: 0 km|
|Verifica el calculo de las distancias entre 2 ciudades invalidas usando API|Tener instalado python3 y pip3, asi como todas las dependencias|1. Ejecutar el servidor con el comando python3 app.py <br> 2. Ingresar al siguiente link http://127.0.0.1:5000 <br> 3. Seleccionar el método API <br> 4. Ingresar 2 ciudades válidas <br> 5. Click en "Calcular Distancia" |Ciudad 1 : fasfsafasf <br> Pais 1: adddd <br> Ciudad 2: uyjgfj <br> Pais 2: gavwqfaf|Distancia: 0 km|