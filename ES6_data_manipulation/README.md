# Data manipulation

![Static Badge](https://img.shields.io/badge/javascript-blue?logo=javascript)
![Static Badge](https://img.shields.io/badge/nodejs-12.22.12-blue?logo=nodedotjs)
![Static Badge](https://img.shields.io/badge/npm-6.14.16-green?logo=npm)

<!-- ![Javascript](https://assets-global.website-files.com/606a802fcaa89bc357508cad/61143444834cd54b9b0a88b3_2-p-2600.png) -->

## Array

Un array es una estructura de datos en JavaScript que puede contener una colección de elementos. Los elementos de un array se organizan en posiciones numeradas llamadas índices, comenzando desde 0.

### Propiedades:

- **length**: Devuelve o establece la cantidad de elementos en el array.

### Métodos:

- **concat()**: Combina dos o más arrays.
- **copyWithin()**: Copia elementos dentro del array.
- **entries()**: Devuelve un nuevo objeto Array Iterator que contiene pares clave/valor para cada índice en el array.
- **every()**: Verifica si todos los elementos cumplen una condición.
- **fill()**: Rellena todos los elementos con un valor estático.
- **filter()**: Crea un nuevo array con los elementos que pasan la prueba de una función.
- **find()**: Devuelve el primer elemento que cumple una condición.
- **findIndex()**: Devuelve el índice del primer elemento que cumple una condición.
- **forEach()**: Ejecuta una función para cada elemento del array.
- **includes()**: Verifica si un array contiene un elemento determinado.
- **indexOf()**: Devuelve el primer índice en el que se encuentra un elemento dado.
- **join()**: Une todos los elementos de un array en una cadena.
- **lastIndexOf()**: Devuelve el último índice en el que se encuentra un elemento dado.
- **map()**: Crea un nuevo array con los resultados de aplicar una función a cada elemento del array.
- **pop()**: Elimina el último elemento del array y lo devuelve.
- **push()**: Añade uno o más elementos al final del array y devuelve la nueva longitud.
- **reduce()**: Aplica una función a un acumulador y a cada elemento del array (de izquierda a derecha) para reducirlo a un único valor.
- **reduceRight()**: Aplica una función a un acumulador y a cada elemento del array (de derecha a izquierda) para reducirlo a un único valor.
- **reverse()**: Invierte el orden de los elementos del array.
- **shift()**: Elimina el primer elemento del array y lo devuelve.
- **slice()**: Extrae una sección del array y devuelve un nuevo array.
- **some()**: Verifica si al menos un elemento cumple una condición.
- **sort()**: Ordena los elementos del array.
- **splice()**: Cambia el contenido de un array eliminando elementos existentes y/o agregando nuevos elementos.
- **toString()**: Devuelve una cadena que representa al array.
- **unshift()**: Añade uno o más elementos al inicio del array y devuelve la nueva longitud.
- **valueOf()**: Devuelve el valor primitivo del array.

### Ejemplo

```javascript
let miArray = [1, 2, 3, 4, 5];
console.log(miArray[2]); // Imprime: 3

// Casos de Uso Comunes:
// - Almacenar una lista de elementos similares.
// - Recorrer y manipular datos estructurados.

// Propiedades y Métodos Importantes:
console.log(miArray.length); // Propiedad: Longitud del array
miArray.push(6); // Método: Agrega un elemento al final
miArray.pop(); // Método: Elimina el último elemento
miArray.forEach((item) => console.log(item)); // Método: Itera sobre cada elemento
```

## Typed Array (Array Tipado):

Los Typed Arrays proporcionan una forma de manejar datos binarios de forma más eficiente en JavaScript. Estos arrays tienen un tamaño fijo y están diseñados para almacenar elementos de un tipo específico.

### Propiedades:

- **buffer**: Devuelve el ArrayBuffer asociado con el Typed Array.
- **byteLength**: Devuelve la longitud en bytes del Typed Array.
- **byteOffset**: Devuelve el byte inicial del Typed Array en el ArrayBuffer.

### Métodos:

- **copyWithin()**
- **entries()**
- **every()**
- **fill()**
- **filter()**
- **find()**
- **findIndex()**
- **forEach()**
- **includes()**
- **indexOf()**
- **join()**
- **keys()**
- **lastIndexOf()**
- **map()**
- **reduce()**
- **reduceRight()**
- **reverse()**
- **set()**
- **slice()**
- **some()**
- **sort()**
- **subarray()**
- **values()**

### Ejemplo

```javascript
let miTypedArray = new Int32Array([1, 2, 3, 4, 5]);
console.log(miTypedArray[2]); // Imprime: 3

// Casos de Uso Comunes:
// - Manipulación eficiente de datos binarios como imágenes o audio.
// - Trabajo con datos de bajo nivel como píxeles de imagen o bytes de red.

// Propiedades y Métodos Importantes:
console.log(miTypedArray.length); // Propiedad: Longitud del Typed Array
miTypedArray.set([10, 20, 30], 2); // Método: Establece valores en una ubicación específica
```

## Set (Conjunto):

Un conjunto es una colección de elementos únicos en JavaScript. Esto significa que no puede haber duplicados en un conjunto.

### Propiedades:

- **size**: Devuelve la cantidad de elementos en el Set.

### Métodos:

- **add()**: Añade un nuevo elemento al Set.
- **clear()**: Elimina todos los elementos del Set.
- **delete()**: Elimina un elemento específico del Set.
- **entries()**: Devuelve un nuevo objeto Iterator que contiene los pares [valor, valor] de cada elemento del Set.
- **forEach()**: Ejecuta una función para cada valor del Set.
- **has()**: Verifica si un valor específico existe en el Set.
- **keys()**: Devuelve un nuevo objeto Iterator que contiene los valores de cada elemento del Set.
- **values()**: Igual que keys(), para compatibilidad con los Map.

### Ejemplo

```javascript
let miSet = new Set([1, 2, 3, 4, 5, 1, 2]);
console.log(miSet); // Imprime: Set {1, 2, 3, 4, 5}

// Casos de Uso Comunes:
// - Eliminar duplicados de una lista.
// - Verificar la existencia de elementos únicos.

// Propiedades y Métodos Importantes:
console.log(miSet.size); // Propiedad: Tamaño del conjunto
miSet.add(6); // Método: Agrega un elemento al conjunto
miSet.delete(3); // Método: Elimina un elemento del conjunto
```

## WeakMap (Mapa Débil):

Un WeakMap es una colección de pares clave-valor donde las claves son objetos y los valores pueden ser de cualquier tipo. A diferencia de los Map, las referencias a las claves en un WeakMap son débiles, lo que significa que no impiden que las claves sean eliminadas por el recolector de basura si no hay otras referencias a ellas.

### Métodos:

- **delete()**: Elimina el elemento asociado a la clave proporcionada.
- **get()**: Devuelve el valor asociado a la clave proporcionada.
- **has()**: Verifica si existe un valor asociado a la clave proporcionada.
- **set()**: Asigna un valor a la clave proporcionada.

### Ejemplo

```javascript
let miWeakMap = new WeakMap();
let clave = { nombre: 'Ejemplo' };
miWeakMap.set(clave, 123);
console.log(miWeakMap.get(clave)); // Imprime: 123

// Casos de Uso Comunes:
// - Asociar datos privados con objetos sin exponerlos globalmente.
// - Evitar fugas de memoria al permitir que los objetos sean eliminados por el recolector de basura.

// Propiedades y Métodos Importantes:
// Los WeakMap no tienen métodos para recorrer o limpiar manualmente. Las claves débiles se eliminan automáticamente.
```

## Map (Mapa):

Un Map es una colección de pares clave-valor donde las claves pueden ser de cualquier tipo, incluidos los objetos y los valores pueden ser de cualquier tipo.

### Propiedades:

- **size**: Devuelve la cantidad de elementos en el Map.

### Métodos:

- **clear()**
- **delete()**
- **entries()**
- **forEach()**
- **get()**
- **has()**
- **keys()**
- **set()**
- **values()**

### Ejemplo

```javascript
let miMapa = new Map();
miMapa.set('clave', 'valor');
console.log(miMapa.get('clave')); // Imprime: valor

// Casos de Uso Comunes:
// - Mantener relaciones entre datos de diferentes tipos.
// - Realizar búsquedas rápidas utilizando claves personalizadas.

// Propiedades y Métodos Importantes:
console.log(miMapa.size); // Propiedad: Tamaño del mapa
miMapa.has('clave'); // Método: Verifica si una clave existe en el mapa
miMapa.clear(); // Método: Elimina todos los elementos del mapa
```
