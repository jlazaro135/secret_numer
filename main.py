from fun import play_game
from fun import get_top_score

while True:
    options = input ("¿Qué te gustaría hacer? A) jugar una nueva partida, B)Ver el ranking o C)Salir: ")

    if options.upper() == "A":
        level = input("Nivel: A) Fácil o B) Difícil: ")
        if level.upper() == "A":
            play_game()
        elif level.upper() == "B":
            play_game("Hard")
    elif options.upper() == "B":
        ranking = input ("Ranking modo A) Fácil o B) Difícil: ")
        if ranking.upper() == "A":
            get_top_score("score_list.txt")
            for score_dict in get_top_score("score_list.txt"):
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        elif ranking.upper() == "B":
            get_top_score("score_list_hard.txt")
            for score_dict in get_top_score("score_list_hard.txt"):
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break



