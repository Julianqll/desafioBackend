# Desafio Stracon

## Estructura del Repositorio

El repositorio consta de dos partes principales:

- **backend/**: Contiene el código fuente del backend construido con Django.
- **client/**: Es un submódulo que contiene el código fuente del frontend construido con React.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone --recurse-submodules https://github.com/Julianqll/desafioBackend
    ```

2. Creamos un ambiente virtual:

   ```bash
   cd desafioBackend
   python3 -m venv venv
   source venv/bin/activate 
    ```

3. Instalar los requerimientos para el backend

   ```bash
   pip install -r requirements.txt
    ```

4. En otra terminal para el cliente, instalar los requerimientos para el mismo

   ```bash
   cd client
   npm install
    ```

## Inicialización

1. En el terminal del backend:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python group.py
    ```

2. Corremo el servidor backend:

   ```bash
   python manage.py runserver
    ```

3. En el terminal del cliente:

   ```bash
   npm run dev
    ```
