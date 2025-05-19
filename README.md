# Code-QuizMaster

## ¿Qué es *Code QuizMaster*?

*Code QuizMaster* es un juego de preguntas y respuestas por terminal en el que el jugador debe responder correctamente a 10 preguntas de opción múltiple. Puedes elegir la dificultad y categoría de las preguntas, obtener pistas, y competir por la mejor puntuación.

---

## Ejecución del programa

Para poder ejecutar de este juego debes hacer lo siguiente:

1. Debes clonar el repositorio de github a tu ordenador
```git
git clone https://github.com/AngelOrtizTorres/Code-QuizMaster
```
2. Accede al módulo main.py y ejecútalo.

Y ya podrías disfrutar de *Code QuizMaster*

---

## Menú Principal

El juego presenta el siguiente menú de opciones:

1. **Cambiar nombre del jugador**  
   Cambia el nombre actual del jugador.

2. **Elegir dificultad del juego**  
   Selecciona entre las dificultades:
   - Fácil
   - Media
   - Difícil

3. **Elegir categoría de las preguntas**  
   Categorías disponibles:
   - Programación
   - Historia
   - Cultura General
   - Geografía
   - Deportes
   - Videojuegos

4. **Leer instrucciones**  
   Muestra una guía sobre cómo jugar el juego.

5. **Ver la clasificación**  
   Muestra los 3 mejores jugadores de cada dificultad, ordenados por puntuación, vidas restantes y pistas usadas.

6. **Empezar a jugar**  
   Inicia una partida con las opciones seleccionadas.

7. **Salir**  
   Cierra el programa.

---

## Instrucciones del Juego

Puedes acceder a ellas desde el menú. Las reglas básicas son:

- Debes responder 10 preguntas.
- Cada pregunta tiene 4 opciones, solo una es correcta.
- Empiezas con 3 vidas.
- Tienes 3 pistas disponibles.
- Puedes ganar puntos por respuestas correctas y perder puntos por errores (según la dificultad).

---

## Pistas

Durante la partida, antes de responder a una pregunta, puedes elegir si deseas usar una pista escribiendo **S**. La pista se mostrará si te quedan disponibles.

- Tienes máximo 3 pistas por partida.
- Usar pistas no penaliza tu puntuación, pero se registra para el ranking.

---

## Puntuación y Penalizaciones

### Respuestas Correctas

- Suman **+5 puntos**.

### Respuestas Incorrectas

- Restan **1 vida**.
- Restan puntos según la dificultad:
  - Fácil: **-1 punto**
  - Media: **-2 puntos**
  - Difícil: **-3 puntos**

> Si pierdes todas las vidas, la partida termina.

---

## Sistema de Clasificación

Al terminar la partida (si ganaste el juego), te preguntará si quieres guardar tus resultados. Si la respuesta es sí, se guardan en un archivo según la dificultad.

Se guardan los datos:

- Nombre del jugador  
- Categoría elegida  
- Puntuación final  
- Vidas restantes  
- Pistas usadas  

El ranking muestra los 3 mejores jugadores, ordenados por:

1. Mayor puntuación  
2. Más vidas restantes  
3. Menos pistas usadas  

---

## Estructura del Proyecto

```
📂 Code-QuizMaster/
├── 📂 GameEngine/
│ ├── game_interface.py
│ ├── menu.py
│ ├── player.py
│ └── game.py
│
├── 📂 Questions/
│ ├── easy_questions.json
│ ├── medium_questions.json
│ ├── hard_questions.json
│ └── question.py
│
├── 📂 Classification/
│ ├── EasyMode.json
│ ├── MediumMode.json
│ ├── HardMode.json
│ └── ranking.py
│
└── main.py
```

