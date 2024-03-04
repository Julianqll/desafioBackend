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
   python prelude.py
    ```

2. Corremo el servidor backend:

   ```bash
   python manage.py runserver
    ```

3. En el terminal del cliente:

   ```bash
   npm run dev
    ```

## Interacción
Puede ingresar a: [Stracon Portal](http://localhost:5173/ ) <br>
Para ingresar a la plataforma existen 3 usuarios, especificados en `prelude.py`
1. Admin
   - Username: **admin**
   - Password: **admin123**
2. Colocador
   - Username: **colocador1**
   - Password: **password2**
3. Aprobador
   - Username: **aprobador1**
   - Password: **password3**

## Documentación API
Para consultar la documentación del API Rest: [Portal API Docs](http://127.0.0.1:8000/portal/api/schema/docs/ ) <br>