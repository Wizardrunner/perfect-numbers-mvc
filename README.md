# Números Perfectos

Este proyecto calcula números perfectos y permite exportar los resultados a un archivo CSV.

## Características

- Calcula números perfectos para un rango definido por el usuario.
- Muestra una tabla con:
  - El valor de $$\( p \)$$,
  - $$\( 2^p - 1 \)$$ (número de Mersenne),
  - Si $$\( 2^p - 1 \)$$ es primo,
  - El número perfecto correspondiente,
  - El número ordinal del número perfecto.
- Exporta los resultados válidos a un archivo CSV.

## Requisitos

- **Python 3.8 o superior**
- **Flask** (para ejecutar el servidor web)
- Un navegador para acceder a la aplicación.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Wizardrunner/perfect-numbers-mvc
   cd perfect-numbers
   ```
2. Crea un entorno virtual para aislar las dependencias del proyecto (Opcional):

```bash
python -m venv env
```
3. Activa el entorno virtual:

    En Windows:
    ```bash
    env\Scripts\activate
    ```
    En macOS/Linux:
    ```bash
    source env/bin/activate
    ```

4. Instala las dependencias necesarias:
```bash
pip install flask
   ```
5. Inicia el servidor Flask:

```bash
python app.py
```
6. Abre tu navegador y accede a http://127.0.0.1:5000
