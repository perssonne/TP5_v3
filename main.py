# Créé par Mikolai Szychowski et Enzo Sanchez Valero
# Créé le 22/02/2024
# TP5

# Importation des fonctions
import random
import arcade

import game_state
import attack_animation
import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

# Affichage de base

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
SCREEN_SUBTITLE_DEUX = "Sélectionner une image pour attaquer!"
SCREEN_SUBTITLE_UN = "Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!"
SCREEN_SUBTITLE_TROIS = "Vous avez gagné la partie! " \
                        " Appuyer sur 'ESPACE' pour débuter une nouvelle partie!"
SCREEN_SUBTITLE_QUATRE = "Vous avez perdu la partie! " \
                        " Appuyer sur 'ESPACE' pour débuter une nouvelle partie!"
SCREEN_SUBTITLE_CINQ = " L'ordinateur a gagné la ronde. " \
                        "Appuyer sur 'ESPACE' pour continuer à jouer!"
SCREEN_SUBTITLE_SIX = " Vous avez gagné la ronde. " \
                        "Appuyer sur 'ESPACE' pour continuer à jouer!"
SCREEN_SUBTITLE_SEPT = " Ronde nulle. " \
                        "Appuyer sur 'ESPACE' pour continuer à jouer!"

DEFAULT_LINE_HEIGHT = 40  # The default line height for text.


class MyGame(arcade.Window):

# Classe du jeu
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       # Attributs d'initialisation

       self.rock = AttackAnimation(AttackType.ROCK)
       self.paper = AttackAnimation(AttackType.PAPER)
       self.scissors = AttackAnimation(AttackType.SCISSORS)
       self.rock_compy = AttackAnimation(AttackType.ROCK)
       self.paper_compy = AttackAnimation(AttackType.PAPER)
       self.scissors_compy = AttackAnimation(AttackType.SCISSORS)
       self.faceBeard = arcade.Sprite("assets/faceBeard.png")
       self.compy = arcade.Sprite("assets/compy.png")
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = None
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.game_state = GameState.NOT_STARTED


   def setup(self):

       #Réinitialisation de nouvelle partie

       # Sprites (et pas Coca Cola (idée de Mikolai))

       self.rock.center_x = 150
       self.rock.center_y = 150
       self.rock.scale = 0.5
       self.rock.draw()

       self.paper.center_x = 245
       self.paper.center_y = 145
       self.paper.scale = 0.5
       self.paper.draw()

       self.scissors.center_x = 345
       self.scissors.center_y = 145
       self.scissors.scale = 0.5
       self.scissors.draw()

       self.faceBeard.center_x = 245
       self.faceBeard.center_y = 250
       self.faceBeard.scale = 0.3
       self.faceBeard.draw()

       self.compy.center_x = 745
       self.compy.center_y = 250
       self.compy.scale = 1.4
       self.compy.draw()

       # Attributs

       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = None
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.game_state = GameState.NOT_STARTED


   def validate_victory(self):

       # Ronde nulle
       if self.player_attack_type == attack_animation.AttackType.ROCK and self.computer_attack_type == AttackType.ROCK:
           self.draw_round = True
           self.player_won_round = None
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.PAPER and self.computer_attack_type == AttackType.PAPER:
           self.draw_round = True
           self.player_won_round = None
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.SCISSORS and self.computer_attack_type == AttackType.SCISSORS:
           self.draw_round = True
           self.player_won_round = None
           self.game_state = GameState.ROUND_DONE

       # Victoire du joueur
       elif self.player_attack_type == attack_animation.AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
           self.player_won_round = True
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
           self.player_won_round = True
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
           self.player_won_round = True
           self.game_state = GameState.ROUND_DONE

       # Victoire de l'ordi
       elif self.player_attack_type == attack_animation.AttackType.ROCK and self.computer_attack_type == AttackType.PAPER:
           self.player_won_round = False
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS:
           self.player_won_round = False
           self.game_state = GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
           self.player_won_round = False
           self.game_state = GameState.ROUND_DONE

       else:
           pass

       # Mise à jour des scores

       if self.player_won_round == True:
           self.player_score += 1

           if self.player_score == 3:
               self.game_state = GameState.GAME_OVER


       elif self.player_won_round == False:
           self.computer_score += 1

           if self.computer_score == 3:
               self.game_state = GameState.GAME_OVER


   def draw_possible_attack(self):

       # Afficher les attaques possibles
       if self.player_attack_chosen == False:
           self.rock.draw()
           self.paper.draw()
           self.scissors.draw()

       else:
           if self.player_attack_type == attack_animation.AttackType.ROCK:
               self.rock.draw()

           elif self.player_attack_type == attack_animation.AttackType.PAPER:
               self.paper.draw()

           elif self.player_attack_type == attack_animation.AttackType.SCISSORS:
               self.scissors.draw()


   def draw_computer_attack(self):

       # Attaques possibles de l'ordi

       self.rock_compy.center_x = 745
       self.rock_compy.center_y = 150
       self.rock_compy.scale = 0.5

       self.paper_compy.center_x = 745
       self.paper_compy.center_y = 145
       self.paper_compy.scale = 0.5

       self.scissors_compy.center_x = 745
       self.scissors_compy.center_y = 145
       self.scissors_compy.scale = 0.5

   def draw_instructions(self):

       # Carrés rouges
       arcade.draw_rectangle_outline(145, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(245, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(345, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(745, 140, 70, 70,
                                     arcade.color.RED)

       # Affichage des scores
       arcade.draw_text("Le pointage du joueur est " + str(self.player_score),
                            0,
                            60,
                            arcade.color.AERO_BLUE,
                            20,
                            width = 500,
                            align = "center")

       arcade.draw_text("Le pointage de l'ordinateur est " + str(self.computer_score),
                            485,
                            60,
                            arcade.color.AERO_BLUE,
                            20,
                            width = 500,
                            align = "center")

       # Affichage des instructions
       if self.game_state == GameState.NOT_STARTED:
           arcade.draw_text(SCREEN_SUBTITLE_UN,
                                    0,
                                    SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                    arcade.color.AERO_BLUE,
                                    40,
                                    width=SCREEN_WIDTH,
                                    align="center")

       elif self.game_state == GameState.ROUND_ACTIVE:
           arcade.draw_text(SCREEN_SUBTITLE_DEUX,
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                            arcade.color.AERO_BLUE,
                            40,
                            width=SCREEN_WIDTH,
                            align="center")

       elif self.game_state == GameState.ROUND_DONE:
           if self.player_won_round == False:
               arcade.draw_text(SCREEN_SUBTITLE_CINQ,
                                0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                arcade.color.AERO_BLUE,
                                40,
                                width=SCREEN_WIDTH,
                                align="center")

           elif self.player_won_round == True:
               arcade.draw_text(SCREEN_SUBTITLE_SIX,
                                0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                arcade.color.AERO_BLUE,
                                40,
                                width=SCREEN_WIDTH,
                                align="center")

           elif self.player_won_round == None:
               arcade.draw_text(SCREEN_SUBTITLE_SEPT,
                                0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                arcade.color.AERO_BLUE,
                                40,
                                width=SCREEN_WIDTH,
                                align="center")

       elif self.game_state == GameState.VICTORY:
           arcade.draw_text(SCREEN_SUBTITLE_TROIS,
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                            arcade.color.AERO_BLUE,
                            40,
                            width=SCREEN_WIDTH,
                            align="center")

       elif self.game_state == GameState.GAME_OVER:
           arcade.draw_text(SCREEN_SUBTITLE_QUATRE,
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                            arcade.color.AERO_BLUE,
                            40,
                            width=SCREEN_WIDTH,
                            align="center")

       self.faceBeard.draw()
       self.compy.draw()


   def on_draw(self):

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       # Afficher l'attaque de l'ordinateur selon l'état de jeu
       if self.player_attack_chosen == True:
           if self.computer_attack_type == AttackType.ROCK:
               self.rock_compy.draw()

           elif self.computer_attack_type == AttackType.PAPER:
               self.paper_compy.draw()

           elif self.computer_attack_type == AttackType.SCISSORS:
               self.scissors_compy.draw()

       # Tout afficher
       self.draw_instructions()
       self.draw_possible_attack()
       self.draw_computer_attack()

   def on_update(self, delta_time):

       # Si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)

       if self.game_state == game_state.GameState.ROUND_ACTIVE:
           if self.player_attack_chosen == True:
               pc_attack = random.randint(0, 2)

               if pc_attack == 0:
                   self.computer_attack_type = AttackType.ROCK

               elif pc_attack == 1:
                   self.computer_attack_type = AttackType.PAPER

               elif pc_attack == 2:
                   self.computer_attack_type = AttackType.SCISSORS

               self.validate_victory()
               self.game_state = GameState.ROUND_DONE

       # Animation des sprites (et pas des Coca Cola)
       self.rock.on_update()
       self.scissors.on_update()
       self.paper.on_update()
       self.rock_compy.on_update()
       self.scissors_compy.on_update()
       self.paper_compy.on_update()

   def on_key_press(self, key, key_modifiers):

       # Changer l'état de jeu et setup
       if self.game_state == GameState.NOT_STARTED:
           self.game_state = game_state.GameState.ROUND_ACTIVE

       elif self.game_state == GameState.ROUND_DONE:
           if self.player_score >= 3:
               self.game_state = GameState.VICTORY

           elif self.computer_score >= 3:
               self.game_state = GameState.GAME_OVER

           else:
                self.reset_round()
                self.game_state = game_state.GameState.ROUND_ACTIVE

       elif self.game_state == GameState.GAME_OVER or GameState.VICTORY:
           self.setup()
           self.game_state = game_state.GameState.NOT_STARTED

   def reset_round(self):

       # Nouveau round

       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False

   def on_mouse_press(self, x, y, button, key_modifiers):

       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True

       if self.rock.collides_with_point((x, y)):
           self.player_attack_type = AttackType.ROCK
           self.player_attack_chosen = True

       elif self.paper.collides_with_point((x, y)):
           self.player_attack_type = AttackType.PAPER
           self.player_attack_chosen = True

       elif self.scissors.collides_with_point((x, y)):
           self.player_attack_type = AttackType.SCISSORS
           self.player_attack_chosen = True

       else:
           self.player_attack_chosen = False

def main():

   # Commencer le jeu

   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()