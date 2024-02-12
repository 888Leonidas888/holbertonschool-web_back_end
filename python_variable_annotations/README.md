# ANOTACIONES EN PYTHON PARA FUNCIONES

Las anotaciones en funciones en Python nos permiten añadir información sobre los argumentos de entrada y salida de una función. Estas anotaciones son comúnmente utilizadas para indicar el tipo que se espera para cada argumento (por ejemplo, `int`, `list`, `str`). A continuación, te proporciono un resumen sobre las anotaciones en funciones:

## 1. Sintaxis básica:

- Para especificar el tipo de los argumentos, se coloca el tipo seguido de dos puntos (`:`) antes del nombre del argumento.

- Para indicar el tipo de retorno, se utiliza la flecha (`->`) seguida del tipo de dato.

### Ejemplo

```python
def suma(a: int, b: int) -> int:
    return a + b
```

## 2. Uso opcional

- Es importante destacar que **Python ignora las anotaciones**. Son una mera nota en el código que indica el tipo esperado, pero no generan errores si no se cumplen.

- Sin embargo, existen herramientas como **mypy** que permiten realizar el **chequeo de tipos** basado en estas anotaciones.

## 3. Ejemplos de anotaciones

- Las anotaciones pueden ser accedidas usando `__annotations__`.
- Se pueden usar tipos de Python como `int`, `str`, `float`, o incluso clases definidas por nosotros.

### Ejemplo

```python
def filtrar_pares(salida: list = []) -> list:
    return [i for i in salida if i % 2 == 0]

print(filtrar_pares.__annotations__)

# Salida de la línea anterior:
{'salida': <class 'list'>, 'return': <class 'list'>}
```

## 4. Variables y clases

- Las anotaciones no están limitadas a las funciones. También se pueden asignar a variables que declaremos.

### Ejemplo

```
pi: float = 3.14
```

> [!NOTE]
En resumen, las anotaciones en funciones son una herramienta útil para documentar y especificar los tipos de datos esperados, aunque su uso es opcional.
