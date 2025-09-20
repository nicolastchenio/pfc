import random

class Game:
    def __init__(self, game_counter=1, game_player_win=0, game_Ia_win=0):
        self.game_counter = game_counter
        self.game_player_win = game_player_win
        self.game_Ia_win = game_Ia_win 
        self.choise_list = ["pierre", "feuille", "ciseaux"]
        self.GAME_ROUNDS = 3
        
    # verif the player choise
    def __verif_choise(self, choise):
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
    def __verif_player_win(self, choise_player, choise_Ia):
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
    def __play_round(self):
        choise_Ia = random.choice(self.choise_list)
        choise_player = input(
            "Choisir entre pierre, feuille, ciseaux ?\n"
            "Pour pierre taper p\n"
            "Pour feuille taper f\n"
            "Pour ciseaux taper c\n"
        )

        while self.__verif_choise(choise_player) == None:
            print("---------------")
            print("Choix invalide, veuiller réessayer!")
            choise_player = input(
                "\nChoisir entre pierre, feuille, ciseaux ?\n"
                "Pour pierre taper p\n"
                "Pour feuille taper f\n"
                "Pour ciseaux taper c\n"
            )

        player_win = self.__verif_player_win(self.__verif_choise(choise_player), choise_Ia)
    
        return player_win, choise_Ia, choise_player
    
    def __game_part(self):
        round_counter = 0
        score_player = 0
        score_Ia = 0
        
        while round_counter < self.GAME_ROUNDS:
            print(f"\n--- Manche {round_counter + 1} ---")
            
            player_win, choise_Ia, choise_player = self.__play_round()
            
            print("--- Résultat ---")
            print(f"Vous aviez choisi {self.__verif_choise(choise_player)} et l'IA avait choisi {choise_Ia}")
            
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
            
            print(f"\nScore actuel : Vous {score_player} - {score_Ia} IA")
        return score_player, score_Ia
    
    def game(self):    
        play = True
        
        print("Bienvenue dans le jeu Pierre Feuille Ciseaux !") 
        print(f"une partie se joue en {self.GAME_ROUNDS} manches contre l'IA !")
        print("Vous pouvez jouer autant de partie que vous le souhaitez")
        print("Vous pouvez quitter le jeu en tapant 'q'")
        print("Bonne chance !")
        
        while play:
            score_player, score_Ia = self.__game_part()
        
            if score_player > score_Ia:
                self.game_player_win += 1
                print(f"Vous avez gagné la partie avec un score de {score_player} contre {score_Ia} ! Félicitations !")    
            else:
                self.game_Ia_win += 1
                print(f"L'IA a gagné la partie avec un score de {score_Ia} contre {score_player} ! Dommage !")
                
            print(f"\nVous avez gagné {self.game_player_win} partie(s) et l'IA {self.game_Ia_win} partie(s) sur un total de {self.game_counter} partie(s) jouée(s).")  
            
            self.game_counter += 1
            
            play_again = input("Voulez-vous rejouer ? (o/n) : ")
            
            if play_again.lower() != 'o':
                play = False
                print("Merci d'avoir joué ! Au revoir !")
    
    