# Laboratorio-2.6-Automatizacion

# Mi API REST en Python

Este proyecto es una API REST desarrollada en Python utilizando Flask y SQLite.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Inicializa la base de datos: ejecuta `python -m app.models` para crear las tablas.
4. Ejecuta la aplicación: `python -m app.main`

## Pruebas

Las pruebas se ejecutan automáticamente con GitHub Actions al hacer push o pull request.

Aquí tienes un `README.md` completo que incluye la documentación de la API REST en Python, junto con información adicional sobre el proyecto. Puedes copiar y pegar este contenido directamente en tu archivo `README.md`.

```markdown
# API REST en Python con Flask y SQLite

## Descripción
Esta API REST permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos SQLite que almacena elementos. Se ha desarrollado utilizando Flask, un microframework de Python.

## Requisitos
- Python 3.x
- Flask
- SQLite

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <tu-repositorio-url>
   cd <nombre-del-repositorio>
   ```

2. **Instala las dependencias:**
   ```bash
   pip install Flask
   ```

## Estructura del Proyecto
```
/tu-proyecto
│
├── app.py
├── requirements.txt
└── README.md
```

## Código de la API

Crea un archivo llamado `app.py` y copia el siguiente código:

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla si no existe
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO items (name) VALUES (?)', (new_item['name'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item created"}), 201

@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()
    conn.close()
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(dict(item))

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    updated_item = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE items SET name = ? WHERE id = ?', (updated_item['name'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item updated"})

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    init_db()  # Crear la base de datos y la tabla
    app.run(debug=True)
```

## Ejecución
1. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

2. **Haz solicitudes a la API:**
   Puedes usar herramientas como Postman o cURL para realizar solicitudes a la API.

## Rutas de la API

### Obtener todos los elementos
- **Método:** `GET`
- **Ruta:** `/items`
- **Descripción:** Recupera una lista de todos los elementos almacenados en la base de datos.

#### Ejemplo de solicitud
```bash
GET http://localhost:5000/items
```

#### Ejemplo de respuesta
```json
{
    "items": [
        {
            "id": 1,
            "name": "Elemento 1"
        },
        {
            "id": 2,
            "name": "Elemento 2"
        }
    ]
}
```

### Crear un nuevo elemento
- **Método:** `POST`
- **Ruta:** `/items`
- **Descripción:** Crea un nuevo elemento en la base de datos.

#### Ejemplo de solicitud
```bash
POST http://localhost:5000/items
Content-Type: application/json

{
    "name": "Nuevo Elemento"
}
```

#### Ejemplo de respuesta
```json
{
    "message": "Item created"
}
```

### Obtener un elemento específico
- **Método:** `GET`
- **Ruta:** `/items/<id>`
- **Descripción:** Recupera un elemento específico según su ID.

#### Ejemplo de solicitud
```bash
GET http://localhost:5000/items/1
```

#### Ejemplo de respuesta
```json
{
    "id": 1,
    "name": "Elemento 1"
}
```

### Actualizar un elemento
- **Método:** `PUT`
- **Ruta:** `/items/<id>`
- **Descripción:** Actualiza los detalles de un elemento específico.

#### Ejemplo de solicitud
```bash
PUT http://localhost:5000/items/1
Content-Type: application/json

{
    "name": "Elemento Actualizado"
}
```

#### Ejemplo de respuesta
```json
{
    "message": "Item updated"
}
```

### Eliminar un elemento
- **Método:** `DELETE`
- **Ruta:** `/items/<id>`
- **Descripción:** Elimina un elemento específico de la base de datos.

#### Ejemplo de solicitud
```bash
DELETE http://localhost:5000/items/1
```

#### Ejemplo de respuesta
```json
{
    "message": "Item deleted"
}
```

## Ejemplos de Respuestas
- **200 OK:** La operación fue exitosa (por ejemplo, al obtener o actualizar un elemento).
- **201 Created:** Se creó un nuevo recurso.
- **404 Not Found:** El recurso solicitado no existe (por ejemplo, al intentar obtener o eliminar un elemento que no está en la base de datos).
- **400 Bad Request:** La solicitud es incorrecta, por ejemplo, si falta un campo requerido.

## Errores Comunes
- **No se pudo conectar a la base de datos:** Asegúrate de que la base de datos SQLite esté creada y accesible.
- **ID no válido:** Asegúrate de que el ID proporcionado en la URL sea un número válido.

## Notas Adicionales
- Asegúrate de que el servidor esté en ejecución para realizar solicitudes a la API.
- Para más información sobre cómo ejecutar la aplicación, consulta la documentación.
