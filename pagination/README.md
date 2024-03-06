# Paginación y HATEOAS en APIs REST

En el diseño de APIs REST, dos conceptos importantes son la paginación y HATEOAS (Hypertext As The Engine Of Application State). Estos conceptos son fundamentales para mejorar la eficiencia y la usabilidad de tu API al manejar grandes conjuntos de datos y proporcionar una navegación autodescriptiva.

## Paginación

La paginación es una técnica común utilizada en las APIs REST para manejar grandes conjuntos de datos al dividirlos en páginas más pequeñas. Esto ayuda a mejorar el rendimiento y la eficiencia de la transferencia de datos entre el servidor y el cliente.

### Implementación de la paginación

En una API REST, la paginación se puede implementar de varias formas. Una técnica común es incluir parámetros en las solicitudes HTTP para especificar el número de página y el tamaño de la página, lo que permite al cliente solicitar datos en bloques manejables.

```http
GET /resource?page=1&page_size=10

```

### Ventajas de la paginación

- Mejora el rendimiento al reducir la carga en el servidor.
- Permite una transferencia de datos eficiente entre el servidor y el cliente.
- Facilita la navegación y la visualización de grandes conjuntos de datos por parte del cliente.

## HATEOAS (Hypertext As The Engine Of Application State)

HATEOAS es un principio de diseño en las APIs REST que promueve la auto-descripción de la API mediante la inclusión de enlaces hipertextuales en las respuestas. Estos enlaces proporcionan al cliente la capacidad de descubrir y navegar de manera dinámica a través de los recursos relacionados.

### Implementación de HATEOAS

```json
{
  "id": 1,
  "name": "John Doe",
  "_links": {
    "self": { "href": "/users/1" },
    "edit": { "href": "/users/1/edit" },
    "delete": { "href": "/users/1/delete" }
  }
}
```

### Ventajas de HATEOAS

- Facilita la navegación y la interacción dinámica con la API.
- Reduce la dependencia del cliente en la documentación estática de la API.
- Mejora la mantenibilidad y la escalabilidad de la API al permitir cambios en los enlaces sin afectar a los clientes.

### Ejemplo de implementación

A continuación, se muestra un ejemplo de cómo implementar la paginación y HATEOAS en una API REST utilizando Python y Flask:

```python
from flask import Flask, jsonify, request
"""Nombre de este archivo app.py"""

app = Flask(__name__)

# Ejemplo de conjunto de datos
dataset = list(range(1, 101))


def paginate_with_links(data, page=1, page_size=10, base_url='/data'):
    total_items = len(data)
    total_pages = (total_items + page_size - 1) // page_size
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, total_items)

    result = {
        'page': page,
        'page_size': page_size,
        'total_items': total_items,
        'total_pages': total_pages,
        'data': data[start_idx:end_idx],
        '_links': {
            'self': f"{base_url}?page={page}&page_size={page_size}"
        }
    }

    if page > 1:
        result['_links']['first'] = f"{base_url}?page=1&page_size={page_size}"
        result['_links']['prev'] = f"{base_url}?page={page - 1}&page_size={page_size}"
    if page < total_pages:
        result['_links']['last'] = f"{base_url}?page={total_pages}&page_size={page_size}"
        result['_links']['next'] = f"{base_url}?page={page + 1}&page_size={page_size}"

    return result


@app.route('/data')
def get_data():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    paginated_data = paginate_with_links(dataset, page=page, page_size=page_size, base_url='/data')
    return jsonify(paginated_data)


if __name__ == '__main__':
    app.run(debug=True)

```

Ejecuta este ejemplo:

```python
python app.py

```

Ingrese al siguiente link generado en tu terminal y agrega la ruta /data:

```http
http://127.0.0.1:5000/data

```

En tu navegador debes tener una salida como la siguiente:

```json
{
  "_links": {
    "last": "/data?page=10&page_size=10",
    "next": "/data?page=2&page_size=10",
    "self": "/data?page=1&page_size=10"
  },
  "data": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
  ],
  "page": 1,
  "page_size": 10,
  "total_items": 100,
  "total_pages": 10
}

```

Ahora copia uno de los query parameters que nos han entregado y agregalo a tu ruta anterior, debe quedarte así:

```http
http://127.0.0.1:5000/data?page=2&page_size=10

```

Ahora debes tener una salida como la siguiente:

```json
{
  "_links": {
    "first": "/data?page=1&page_size=10",
    "last": "/data?page=10&page_size=10",
    "next": "/data?page=3&page_size=10",
    "prev": "/data?page=1&page_size=10",
    "self": "/data?page=2&page_size=10"
  },
  "data": [
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20
  ],
  "page": 2,
  "page_size": 10,
  "total_items": 100,
  "total_pages": 10
}
```

Este ejemplo utiliza Flask para crear una API REST simple. La función paginate_with_links es responsable de la paginación de los datos y la inclusión de enlaces HATEOAS en la respuesta. La ruta /data maneja las solicitudes GET para obtener los datos paginados.
