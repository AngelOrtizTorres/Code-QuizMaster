from GameEngine.game_interface import *
from GameEngine.menu import *
from GameEngine.player import Player
from Questions.question import Question
from GameEngine.game import Game
from Classification.ranking import Ranking
import time

clear_terminal()
name = input("\nPara empezar escribe tu nombre: ")

while True:
    main_option = main_menu.choose()
    clear_terminal()
    match main_option:
        case 1:
            name = input("\nEscribe aquí tu nombre: ")

        case 2:
            selected_difficulty = Game.set_difficulty()

            print(f"\nHas elegido dificultad: {selected_difficulty}")
            time.sleep(1.5)
            clear_terminal()

        case 3:
            selected_category = Game.set_category()

            print(f"\nHas elegido categoría: {selected_category}")
            time.sleep(1.5)
            clear_terminal()            

        case 4:
            instrucciones()
            input("Pulsa ENTER para volver al menú principal...")     
            clear_terminal()

        case 5: 
            print("Dificultad Fácil\n" + "-" * 16)
            top3 = Game.get_top3_players("Classification/EasyMode.json")
            for line in top3:
                print(line)

            print("\nDificultad Media\n" + "-" * 16)
            top3 = Game.get_top3_players("Classification/MediumMode.json")
            for line in top3:
                print(line)

            print("\nDificultad Difícil\n" + "-" * 18)
            top3 = Game.get_top3_players("Classification/HardMode.json")
            for line in top3:
                print(line)
            input("\nPulsa ENTER para volver al menú principal...")    
            clear_terminal()

        case 6:
            player = Player(name, selected_difficulty, selected_category)
            counter_start()

            question_manager = Question(selected_difficulty, selected_category)

            game = Game(player, question_manager, selected_difficulty)

            questions = game.get_question_data()

            for question_ in questions:
                print(f"{question_['pregunta']}\n")
                for i, opcion in enumerate(question_['opciones'], 1):
                    print(f"  {i}. {opcion}")
                print()

                use_hint = input("¿Quieres usar una pista? (S/N): ").upper()
                
                hint_feedback = game.consume_hint(use_hint, player, question_)
                print(hint_feedback)

                user_answer = input("¿Cuál es la respuesta correcta? ")
                
                if game.evaluate_answer(user_answer, question_) == "correct":
                    print("\nCORRECTO")
                else:
                    print(f"\nINCORRECTO. La respuesta correcta era: {question_['respuesta']}")

                print(f"{question_["explicacion"]}\n")
                print(f"{name} actualmente tienes {player.score} pts y {player.lives} vidas\n")
                
                if player.lives.lives == 0:
                    print("¡Game Over!")
                    input("Pulsa ENTER para volver al menú principal...")     
                    clear_terminal()
                    break
                
                input("Pulsa ENTER para pasar a la siguiente pregunta...")     
                clear_terminal()

            if player.lives.lives != 0:
                save_results = input("¿Quieres guardar tus resultados? (S/N): ").strip().upper()
                if save_results == "S":
                    ranking_player = Ranking(player, selected_difficulty, selected_category)
                    ranking_player.append_to_leaderboard()
                    print("Resultados guardados.")
                    time.sleep(1.5)
                    clear_terminal()

                elif save_results == "N":
                    print("Resultados no guardados.")
                    time.sleep(1.5)
                    clear_terminal()

                else:
                    print("Opción no válida. Resultados no guardados.")

        case 7:
            print(f"\n¡Nos vemos en la próxima {name}!\n")
            exit()

        case _:
            print("Opción no válida")