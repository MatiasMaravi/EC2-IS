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