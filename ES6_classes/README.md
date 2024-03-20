# ES6 classes(Classes in ECMAScript 2015)

![Static Badge](https://img.shields.io/badge/javascript-blue?logo=javascript)
![Static Badge](https://img.shields.io/badge/nodejs-12.22.12-blue?logo=nodedotjs)
![Static Badge](https://img.shields.io/badge/npm-6.14.16-green?logo=npm)
![Javascript](https://assets-global.website-files.com/606a802fcaa89bc357508cad/61143444834cd54b9b0a88b3_2-p-2600.png)

ES6, también conocido como ECMAScript 2015, es una versión importante del estándar ECMAScript, que es la especificación subyacente de JavaScript. Una de las características principales introducidas en ES6 son las clases.

Las clases en ES6 proporcionan una sintaxis más clara y orientada a objetos para la programación en JavaScript. Antes de ES6, JavaScript utilizaba prototipos para implementar la herencia y la encapsulación de datos, lo que a menudo era menos intuitivo para los programadores que venían de otros lenguajes orientados a objetos.

Con la introducción de las clases en ES6, los desarrolladores pueden definir clases utilizando la palabra clave `class`, y luego definir métodos y propiagees dentro de esa clase. Esto hace que el código sea más estructurado y legible para aquellos que están familiarizados con la programación orientada a objetos en otros lenguajes.

## ¿Qué son las clases en ES6?

Las clases en ES6 proporcionan una forma más estructurada y orientada a objetos de definir objetos y su comportamiento en JavaScript. Anteriormente, en JavaScript se utilizaban prototipos para la herencia y la creación de objetos, lo que a menudo resultaba confuso para los programadores que venían de otros lenguajes orientados a objetos.

## Ejemplo básico

Aquí hay un ejemplo básico de cómo se definen las clases en ES6:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hola, soy ${this.name} y tengo ${this.age} años.`);
  }
}

// Crear una instancia de la clase Person
const person1 = new Person("Jhony", 30);
person1.greet(); // Salida: Hola, soy Jhony y tengo 30 años.
```

En este ejemplo, `Person` es una clase que tiene un constructor para inicializar el nombre y la edad, y un método `greet` que imprime un saludo utilizando los datos de la instancia. Las clases en ES6 ofrecen una forma más conveniente y familiar de trabajar con objetos y herencia en JavaScript.

## Ventajas de utilizar clases en ES6

- **Sintaxis más clara**: La sintaxis de las clases en ES6 es más familiar para los desarrolladores que provienen de lenguajes orientados a objetos.

- **Herencia simplificada**: Las clases permiten una forma más sencilla de implementar la herencia en JavaScript.

- **Encapsulación de datos**: Las clases permiten definir métodos y propiedades privadas, lo que facilita la encapsulación de datos.

## Conclusión

Las clases en ES6 son una característica poderosa que mejora la legibilidad y la estructura del código JavaScript. Al utilizar clases, los desarrolladores pueden escribir código más limpio y mantenible, lo que facilita el desarrollo de aplicaciones robustas y escalables.

## Nodejs

Antes de comenzar debemos instalar nodejs usando un administrador de paquetes.

## Qué es Nodejs?

Node.js es un entorno de ejecución de JavaScript de código abierto y multiplataforma que permite ejecutar código JavaScript fuera del navegador web. Fue creado por Ryan Dahl en 2009 y desde entonces ha experimentado un crecimiento significativo en popularidad y adopción.

Las características clave de Node.js incluyen:

1. **JavaScript en el lado del servidor**: Node.js permite ejecutar JavaScript en el servidor, lo que amplía las capacidades del lenguaje más allá del navegador web.

2. **Basado en el motor V8 de Google**: Node.js utiliza el motor V8 de Google Chrome, que es altamente eficiente y está optimizado para ejecutar código JavaScript de manera rápida y confiable.

3. **Modelo de E/S sin bloqueo y basado en eventos**: Node.js utiliza un modelo de E/S sin bloqueo y basado en eventos, lo que permite manejar múltiples solicitudes de manera eficiente sin bloquear el hilo de ejecución.

4. **NPM (Node Package Manager)**: NPM es el administrador de paquetes de Node.js, que permite a los desarrolladores instalar, compartir y administrar paquetes de código JavaScript de manera sencilla. Es una de las mayores colecciones de código abierto en el mundo, lo que facilita la reutilización de código y acelera el desarrollo de aplicaciones.

5. **Amplio ecosistema de herramientas y frameworks**: Node.js cuenta con un amplio ecosistema de herramientas, bibliotecas y frameworks que facilitan el desarrollo de una variedad de aplicaciones, desde aplicaciones web y API hasta aplicaciones de red y procesamiento de datos en tiempo real.

En resumen, Node.js es una plataforma poderosa y versátil que ha revolucionado el desarrollo web al permitir a los desarrolladores utilizar JavaScript tanto en el lado del cliente como en el lado del servidor, lo que facilita la creación de aplicaciones web escalables y de alto rendimiento.

### Instalar administrador de versión

Este video tutorial te ayudará si estas en windows.

- [npm-sitio oficial](https://www.npmjs.com/)
- [Cómo Instalar NodeJS, NPM y NVM en Windows](https://www.youtube.com/watch?v=Z-Ofqd2yBCc)
- [nvm-windows](https://github.com/coreybutler/nvm-windows?tab=readme-ov-file)
- [Node - sitio oficial](https://nodejs.org/en)

> [!NOTE]
> Posiblemente después de instalar una versión de nodejs, necesites agregar esta versión al `PATH`.
