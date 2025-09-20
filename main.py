from itertools import count
import random

def main():
    
    # ------ game toolbox
    choise_list = ("pierre", "feuille", "ciseaux")
    GAME_ROUNDS = 3
    
    # verif the player choise
    def verif_choise(choise):
        if choise == "p":
            return "pierre"
        elif choise == "f":
            return "feuille"
        elif choise == "c":
            return "ciseaux"
        else:
            return None
    
    # verif if the player win
    def verif_player_win(choise_player, choise_Ia):
        if choise_player == "pierre" and choise_Ia == "feuille":
            return False
        elif choise_player == "feuille" and choise_Ia == "ciseaux":
            return False
        elif choise_player == "ciseaux" and choise_Ia == "pierre":
            return False
        elif choise_player == choise_Ia:
            return None
        else:
            return True
    
    # play one round
    def play_round():
        choise_Ia = random.choice(choise_list)
        choise_player = input(
            "Choisir entre pierre, feuille, ciseaux ?\n"
            "Pour pierre taper p\n"
            "Pour feuille taper f\n"
            "Pour ciseaux taper c\n"
        )

        while verif_choise(choise_player) == None:
            print("Choix invalide, veuiller réessayer!")
            choise_player = input(
                "Choisir entre pierre, feuille, ciseaux ?\n"
                "Pour pierre taper p\n"
                "Pour feuille taper f\n"
                "Pour ciseaux taper c\n"
            )

        player_win = verif_player_win(verif_choise(choise_player), choise_Ia)
        return player_win, choise_Ia, choise_player
    
    # play part of the game
    def game_part():
        round_counter = 0
        score_player = 0
        score_Ia = 0
        
        while round_counter < GAME_ROUNDS:    
            print(f"\n--- Manche {round_counter + 1} ---")
            
            player_win, choise_Ia, choise_player = play_round()
            
            print(f"Vous aviez choisi {choise_player} et l'IA avait choisi {choise_Ia}")
            
            if player_win == True:
                print("Vous avez donc gagné cette manche !")
                score_player += 1
                round_counter += 1    
            elif player_win == False:
                print("L'IA a donc gagné cette manche !")
                score_Ia += 1
                round_counter += 1 
            else:
                print("Egalité ! personne ne marque de point !")
                pass
            
            print(f"Score actuel : Vous {score_player} - {score_Ia} IA")
        return score_player, score_Ia
    
    def game():    
        play = True
        
        print("Bienvenue dans le jeu Pierre Feuille Ciseaux !") 
        print(f"une partie se joue en {GAME_ROUNDS} manches contre l'ordinateur !")
        print("Vous pouvez jouer autant de partie que vous le souhaitez")
        # print("Vous pouvez quitter le jeu en tapant 'q'")
        print("Bonne chance !")
        
        while play:
            score_player, score_Ia = game_part()
        
            if score_player > score_Ia:
                print(f"Vous avez gagné la partie avec un score de {score_player} contre {score_Ia} ! Félicitations !")      
            else:
                print(f"L'IA a gagné la partie avec un score de {score_Ia} contre {score_player} ! Dommage !")
            play_again = input("Voulez-vous rejouer ? (o/n) : ")
            if play_again.lower() != 'o':
                play = False
                print("Merci d'avoir joué ! Au revoir !")          


    game()

if __name__ == "__main__":
    main()