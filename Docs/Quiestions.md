# Cuestionario

## **¿Qué es un _Coding Dojo_?**
Se trata de una reunión donde un gruop de codificadores/desarrolladores trabajan juntos en una tarea de dicha índole (programación). La idea de este concepto es mejorar e implementar habilidades (duras y blandas) entre cada uno de los programadores partícipes en dicha reunión. (Solano, 2012).
## **Diferencia entre requerimientos, criterios de aceptación y casos de prueba**
Durante la carrera de Ingeniería de Software, hemos visto los conceptos por separado de cada uno de los términos en cuestión. Sin embargo, es preciso diferenciarlos ya que estamos planteándolo desde un escenario laboral, menos conceptual y más práctico.


En esencia, los **requerimientos** son descripciones _grosso modo_ de las diferentes características que ha de tener el sistema. Sin embargo, debe existir un nivel de confiabilidad en ellas, a su vez que cierto rigor en la validación y especificación, esto se hace a partir de los **criterios de aceptación**. Estos criterios de aceptación no son lo suficientemente profundos como para analizar posibles casos específicos en donde se cumpla con los requerimientos, este nivel de profundidad en la validación se consigue a partir de los **escenarios de prueba** (Solano, 2017).

## **Dé dos ejemplos de requerimientos no-funcionales, y especifique cuál es su categoría (seguridad, performance, portabilidad, etc.)**

Este tipo de requerimientos de software son las restricciones o los requerimientos impuestos en el sistema. Estos son los indicadores principales de la calidad del software. Estos requerimientos tratan con problemas como escalabilidad, mantenibilidad, rendimiento, portabilidad, confiabilidad entre otros (GeeksforGeeks, 2020). Aquí los dos ejemplos:

* El sistema debe poseer una autenticación de seguridad en dos pasos. Este es un requerimiento de seguridad, correspondiente a las restricciones del rendimiento.
* El sistema debe tener una paleta de colores de azules y blancos. Esta es una restricción de interfaz.

## **¿Qué es TDD?**

Son las siglas en inglés de _Test Driven Development_. En desarrollo de software, se acercan a cuáles casos de prueba son desarrollados para especificar y validad lo que el código hará. En síntesis, cada funcionalidad se prueba col n su respectivo caso y, si pasa algún error, entonces se elabora un nuevo código libre de ese error de manera simple y efectiva (Hamilton, 2022).

El **ciclo** que define los TTD es:
1. Escribir una prueba.
2. Hacer que esta funcione.
3. Cambiar el código para corregir el posible error.
4. Repetir el proceso.

## **¿Qué son las pruebas unitarias automatizadas?**
Son un método de pruebas de software. Unidades hace referencia a secciones cortas del código que son rigurosamente validades en cuanto a funcionamiento. Cada sección de código puede ser reconstruida para probarse de manera individual. El objetivo de este método de prueba de software es demostrar que cada parte razonable (unidad, en este sentido) de software funciona correctamente o va acorde a los requisitos previamente establecidos. (Computer Hope, 2020).

## **¿Cuál fue el primer framework de pruebas unitarias y para cual lenguaje fue creado?**
El primer framework con el fin en cuestión fue Junit, nacido en 1997. Como se puede intuir, el framework fue creado para probar programas construidos en el lenguaje Java. Actualmente sigue en vigencia y su versión general actual es la quinta. (Wikipedia Contribuitors, 2022a).

## **Describa los componentes de xUnit**

Componentes de la arquitectura de xUnit:

* **_Test runner_**: es un programa ejecutable que corre las pruebas implementadas en un framework de xUnit, a la vez que reporta los resultados de prueba.

* **_Test case_**: es el componente más elemental. Todas las pruebas unitarias son heredadas de esta.
* **_Test Fixtures_**: también conocido como text context es un conjunto de precondiciones o algún estado que necesite correr una prueba.
* **_Test suites_**: es un conjunto de pruebas que comparten el mismo contexto. El orden de estas no es relevante, en este sentido.
* **_Test execution_**: contiene dos métodos, un setup y un teardown. En el primero se prepara un ambiente aislado. El segundo se trata de limpiar el ambiente para que no intercepte alguna otra prueba.
* **_Test result formatter_**: produce resultados en uno o varios formatos de salida. Utiliza XML producido por el propio framework que se produce como una salida.

* **_Assertions_**: es una función que verifica la sección de código o la unidad bajo revisión. Usualmente, expresa una condición lógica que se cumple cuando los resultados se corresponden con las estimaciones esperadas en un sistema bajo prueba correcto.

Todos estos componentes, en general, se congenian para formar una sinergia que hacen de este framework uno muy utilizado (Wikipedia contribuitors, 2022b).

## **Indique al menos tres desventajas de las pruebas unitarias automatizadas**
Según Kralj, 2022; las principales desventajas son:
* Reduce o previene que se envíen bugs o errores en los proyectos a producción. 
* Incrementa la productividad de los desarrolladores.
* Fortalece la programación modular o por módulos.

## **Indique al menos tres ventajas de las pruebas unitarias automatizadas**
Según Kralj, 2022; las principales ventajas son:
* Consume bastante tiempo en su elaboración.
* No puede ser evaluado todo el código de golpe, sino por partes (unidades).
* No garantiza la eliminación de todos los bugs posibles.

## **Referencias bibliográficas**
* Solano, L. (2012, 10 septiembre). What is Coding Dojo. Lorenzo Solano Martinez. https://lorenzosolano.com/what-is-coding-dojo/

* Solano, L. (2017, 18 junio). Requirements, Acceptance Criteria, and Scenarios. Lorenzo Solano Martinez. https://lorenzosolano.com/requirements-acceptance-criteria-and/

* GeeksforGeeks. (2020, 4 junio). Non-functional Requirements in Software Engineering. https://www.geeksforgeeks.org/non-functional-requirements-in-software-engineering/

* (TDD)? Tutorial with Example. Guru99. https://www.guru99.com/test-driven-development.html

* Computer Hope. (2020, 6 julio). What is Automated Unit Testing? https://www.computerhope.com/jargon/a/automated-unit-testing.htm

* Wikipedia contributors. (2022, 7 marzo). JUnit. Wikipedia. https://en.wikipedia.org/wiki/JUnit#:%7E:text=JUnit%20was%20born%20on%20a,of%20meta-circular%20geekery).

* Wikipedia contributors. (2022b, mayo 13). XUnit. Wikipedia. https://en.wikipedia.org/wiki/XUnit 

* Kralj, K. (2022, 23 febrero). What Are Advantages and Disadvantages of Unit Testing? MethodPoet. https://methodpoet.com/unit-testing-advantages-and-disadvantages/#:%7E:text=Advantages%20of%20unit%20testing%20are,won%27t%20catch%20all%20bugs

