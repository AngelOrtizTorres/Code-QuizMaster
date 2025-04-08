# Code QuizMaster

## Introducción

Este proyecto tiene como finalidad crear un programa en el que se realice un juego de Quiz. En él responderás preguntas de diferentes categorías y dificultades para obtener la máxima puntuación.

## Objetivos

**Objetivo General:**

- Desarrollar un juego de Quiz interactivo utilizando Python.

**Objetivos Específicos:**

- Implementar un sistema de preguntas y respuestas.

- Crear una interfaz en la consola para interactuar con el juego.

- Almacenar las respuestas del usuario y calcular el puntaje al final.

- Almacenar los puntajes para crear una clasificación.

- Proporcionar retroalimentación sobre la respuesta correcta o incorrecta después de cada pregunta.

## Alcance del proyecto

Este juego incluirá:

- Un menú inicial para poder configurar la dificultad y la categoría de las preguntas.

- Un sistema de puntuación en el que se guardarán los resultados para crear una clasificación.

- Uso de diccionarios y librerías

Este juego no incluirá:

- Una interfaz gráfica (se realizará a través de la consola)

## Ejemplo

```
------------------------------------------------------
  ¡Bienvenido al Quiz de Preguntas y Respuestas!
------------------------------------------------------
1. Elegir Dificultad
2. Elegir Categoría
3. Ver clasificación
4. Borrar clasificación
5. Empezar a jugar
6. Salir
------------------------------------------------------
Elige una opción válida para comenzar... 
```
```
Elige una opción válida para comenzar... 1

----------------------------------
  Dificultad del juego
----------------------------------
1. Fácil
2. Medio
3. Difícil

Elige una opción: 
```
```
Elige una opción válida para comenzar... 2

----------------------------------
  Categorías de las preguntas
----------------------------------
1. Historia
2. Programación
3. Deportes
4. Geografía
5. Cine
3. Todas

Elige una opción: 
```
```
Elige una opción válida para comenzar... 3

----------------------------------
  Clasificación
----------------------------------

Dificultad Fácil:
-----------------
1. Jugador: Pepe | Puntuación: 25/50
2. Jugador: Ángel | Puntuación: 20/50
3. Jugador: Beñat | Puntuación: 10/50

Dificultad Medio:
-----------------
1. Jugador: Alejandro | Puntuación: 25/50
2. Jugador: Vicente | Puntuación: 13/50
3. Jugador: Jesús | Puntuación: 8/50

Dificultad Difícil:
-----------------
1. Jugador: Andrea | Puntuación: 30/50
2. Jugador: Adrián | Puntuación: 10/50
3. Jugador: Patricia | Puntuación: 3/50

Volver al menú pulsa Enter...
```
```
Elige una opción válida para comenzar... 4

¿Realmente quieres borrar las clasificaciones?(Sí/No)
```
```
Elige una opción válida para comenzar... 5

Primera pregunta:
------------------
¿Quién escribió la obra "Cien años de soledad"?

a) Julio Cortázar

b) Gabriel García Márquez

c) Mario Vargas Llosa

d) Pablo Neruda

Elige una opción: b
CORRECTO!

Segunda pregunta:
-----------------
¿En qué año comenzó la Revolución Francesa?

a) 1789

b) 1776

c) 1804

d) 1812

Elige una opción: a
CORRECTO!

Tercera pregunta:
------------------
¿Cuál es el instrumento musical tradicional de Japón?

a) Guitarra

b) Piano

c) Shamisen

d) Violín

Elige una opción: a
INCORRECTO!
----------------------------------
Has acertado 2/3 preguntas. 
¿Quieres guardar tu resultado?(Sí/No) Sí
¿Cuál es tu nombre? Ángel

Resultado guardado.
```