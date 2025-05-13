from GameEngine.game_interface import banner

class Menu:

    def __init__(self, *options, title="Menú de opciones"):
        self.__options = list(options)
        self.__title = title

    def choose(self):
        self.__print_menu()
        return self.__chosen_option()

    def __print_menu(self):
        print(self.__title)
        print()
        for n in range(len(self.__options)):
            print(f"{n + 1}. {self.__options[n]}")

    def __chosen_option(self):
        while True:
            try:
                option = int(input(f"\nIntroduce una opción (1 - {len(self.__options)}): "))
                if 1 <= option <= len(self.__options):
                    return option
                else:
                    print(f"Introduce un número entre 1 y {len(self.__options)}")
            except ValueError:
                print("Has introducido una opción incorrecta.")

main_menu = Menu("Cambiar nombre del jugador","Elegir dificultad del juego", "Elegir categoría de las preguntas", "Leer instrucciones",
                 "Ver la clasificación", "Empezar a jugar", "Salir", title = banner)

difficulty_menu = Menu("Dificultad Fácil", "Dificultad Media", "Dificultad Difícil",
                       title = "\nELIGE UNA DIFICULTAD")

category_menu = Menu("Programación", "Historia", "Cultura General",
                 "Geografía", "Deportes", "Videojuegos", title = "\nELIGE LA CATEGORÍA DE LAS PREGUNTAS")