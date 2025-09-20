from itertools import count
import random

def main():
    
    # ------ game toolbox
    choise_list = ("pierre", "feuille", "ciseaux")
    GAME_ROUNDS = 3
    game_counter = 1
    game_player_win = 0
    game_Ia_win = 0
    
    # verif the player choise
    def verif_choise(choise):
        if choise == "p":
            return "pierre"
        elif choise == "f":
            return "feuille"
        elif choise == "c":
            return "ciseaux"
        elif choise == "q":
            exit("Merci d'avoir joué ! Au revoir !")
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
            print("---------------")
            print("Choix invalide, veuiller réessayer!")
            choise_player = input(
                "\nChoisir entre pierre, feuille, ciseaux ?\n"
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
            
            print("--- Résultat ---")
            print(f"Vous aviez choisi {verif_choise(choise_player)} et l'IA avait choisi {choise_Ia}")
            
            if player_win == True:
                print("\nVous avez donc gagné cette manche !")
                score_player += 1
                round_counter += 1    
            elif player_win == False:
                print("\nL'IA a donc gagné cette manche !")
                score_Ia += 1
                round_counter += 1 
            else:
                print("\nEgalité ! personne ne marque de point !")
                pass
            
            print(f"\nScore actuel : Vous {score_player} - {score_Ia} IA")
        return score_player, score_Ia
    
    def game(game_counter, game_player_win, game_Ia_win):    
        play = True
        
        print("Bienvenue dans le jeu Pierre Feuille Ciseaux !") 
        print(f"une partie se joue en {GAME_ROUNDS} manches contre l'IA !")
        print("Vous pouvez jouer autant de partie que vous le souhaitez")
        print("Vous pouvez quitter le jeu en tapant 'q'")
        print("Bonne chance !")
        
        while play:
            score_player, score_Ia = game_part()
        
            if score_player > score_Ia:
                game_player_win += 1
                print(f"Vous avez gagné la partie avec un score de {score_player} contre {score_Ia} ! Félicitations !")    
            else:
                game_Ia_win += 1
                print(f"L'IA a gagné la partie avec un score de {score_Ia} contre {score_player} ! Dommage !")
                
            print(f"\nVous avez gagné {game_player_win} partie(s) et l'IA {game_Ia_win} partie(s) sur un total de {game_counter} partie(s) jouée(s).")  
            
            game_counter += 1
            
            play_again = input("Voulez-vous rejouer ? (o/n) : ")
            
            if play_again.lower() != 'o':
                play = False
                print("Merci d'avoir joué ! Au revoir !")          

    game(game_counter, game_player_win, game_Ia_win)

if __name__ == "__main__":
    main()