from colorama import Fore, Style
import os
import time

banner = (
    Fore.YELLOW + r"   ___         _        " +
    Fore.BLUE   + r"___       _    __  __         _           " + "\n" +

    Fore.YELLOW + r"  / __|___  __| |___   " +
    Fore.BLUE   + r"/ _ \ _  _(_)__|  \/  |__ _ __| |_ ___ _ _ " + "\n" +

    Fore.YELLOW + r" | (__/ _ \/ _` / -_) " +
    Fore.BLUE   + r"| (_) | || | |_ / |\/| / _` (_-<  _/ -_) '_|" + "\n" +

    Fore.YELLOW + r"  \___\___/\__,_\___|  " +
    Fore.BLUE   + r"\__\_\\_,_|_/__|_|  |_\__,_/__/\__\___|_|  " + Style.RESET_ALL
)

banner_number3 = (Fore.YELLOW + r"""
  ____ 
 |__ /  
  |_ \
 |___/
""")

banner_number2 = (Fore.BLUE + r"""
  ___ 
 |_  )
  / / 
 /___|
""")

banner_number1 =(Fore.YELLOW + r"""
  _ 
 / |
 | |
 |_|
""")

banner_go = (Fore.BLUE + r"""
   ___  ___    _ 
  / __|/ _ \  | |
 | (_ | (_) | |_|
  \___|\___/  (_)  
""" + Style.RESET_ALL)

def instrucciones():
    print(f"""

   INSTRUCCIONES DEL JUEGO
   ═══════════════════════

   1. 🏁  Objetivo:
      Debes responder correctamente a 10 preguntas de opción múltiple.

   2. 🎯  Elección de dificultad:
      Tendrás que elegir antes de empezar cada partida la dificultad que tendrán las preguntas:
      · 🔴  Difícil
      · 🟠  Media
      · 🟢  Fácil

   3. 🗂️  Elección de categoría:
      Al igual que con la dificultad, debes elegir la categoría de las preguntas:
      · 💻  Programación
      · 🌐  Cultura General
      · 📜  Historia
      · 🗺️   Geografía
      · ⚽  Deportes
      · 🎮  Videojuegos

   4. 🎲  Mecánica de juego:
      · Cada pregunta tiene 4 opciones.
      · Solo hay una opción correcta.
      · Deberás poner el número de la opción que elijas.

   5. ❤️  Vidas y 'Ayudas':
      · Empezarás con 3 vidas.
      · Puedes tener 3 pistas para ayudarte en las preguntas (si lo necesitas).
   """)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def counter_start():
    banners = [banner_number3, banner_number2, banner_number1, banner_go]
    
    for banner in banners:
        clear_terminal()
        print(banner)
        time.sleep(1)
    
    clear_terminal()