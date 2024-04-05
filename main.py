"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import random

import arcade
from enum import Enum
from enum import Flag, auto

import attack_animation
import game_state
#import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
SCREEN_SUBTITLE_UN = "Appuyer sur une image pour faire une attaque!"
SCREEN_SUBTITLE_DEUX = "Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!"
SCREEN_SUBTITLE_TROIS = "Vous avez gagné la partie! \
                        La partie est terminée.  \
                        Appuyer sur 'ESPACE' pour débuter une nouvelle partie!"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
   """
   La classe principale de l'applicationz

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = arcade.Sprite("assets/srock.png")
       self.paper = arcade.Sprite("assets/spaper.png")
       self.scissors = arcade.Sprite("assets/scissors.png")
       self.rock_compy = arcade.Sprite("assets/srock.png")
       self.paper_compy = arcade.Sprite("assets/spaper.png")
       self.scissors_compy = arcade.Sprite("assets/scissors.png")
       self.faceBeard = arcade.Sprite("assets/faceBeard.png")
       self.compy = arcade.Sprite("assets/compy.png")
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = None
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = GameState
       self.pc_attack = None


   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

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

       pass


   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """

       if self.player_attack_type == attack_animation.AttackType.ROCK and self.computer_attack_type == AttackType.ROCK:
           game_state.GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.PAPER and self.computer_attack_type == AttackType.PAPER:
           game_state.GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.SCISSORS and self.computer_attack_type == AttackType.SCISSORS:
           game_state.GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
           self.player_won_round = True
           self.player_score += 1
           game_state.GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
           self.player_won_round = True
           self.player_score += 1
           game_state.GameState.ROUND_DONE

       elif self.player_attack_type == attack_animation.AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
           self.player_won_round = True
           self.player_score += 1
           game_state.GameState.ROUND_DONE




   def draw_possible_attack(self):

       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
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

           else:
               pass


   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """

       self.rock_compy.center_x = 745
       self.rock_compy.center_y = 150
       self.rock_compy.scale = 0.5

       self.paper_compy.center_x = 745
       self.paper_compy.center_y = 145
       self.paper_compy.scale = 0.5

       self.scissors_compy.center_x = 745
       self.scissors_compy.center_y = 145
       self.scissors_compy.scale = 0.5

       if self.player_attack_chosen == True:
           if self.computer_attack_type == AttackType.ROCK:
               self.rock_compy.draw()

           elif self.computer_attack_type == AttackType.PAPER:
               self.paper_compy.draw()

           else:
               self.scissors.center_x = 745
               self.scissors_compy.draw()

   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """

       arcade.draw_rectangle_outline(145, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(245, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(345, 140, 70, 70,
                                     arcade.color.RED)
       arcade.draw_rectangle_outline(745, 140, 70, 70,
                                     arcade.color.RED)

       arcade.draw_text("Le pointage du joueur est 0",
                            0,
                            60,
                            arcade.color.AERO_BLUE,
                            20,
                            width = 500,
                            align = "center")

       arcade.draw_text("Le pointage de l'ordinateur est 0",
                            485,
                            60,
                            arcade.color.AERO_BLUE,
                            20,
                            width = 500,
                            align = "center")

       if self.game_state == 1:
           arcade.draw_text(SCREEN_SUBTITLE_UN,
                                    0,
                                    SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                    arcade.color.AERO_BLUE,
                                    40,
                                    width=SCREEN_WIDTH,
                                    align="center")

       elif self.game_state == 2:
           arcade.draw_text(SCREEN_SUBTITLE_DEUX,
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                            arcade.color.AERO_BLUE,
                            40,
                            width=SCREEN_WIDTH,
                            align="center")

       elif self.game_state == 3:
           arcade.draw_text(SCREEN_SUBTITLE_TROIS,
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                            arcade.color.AERO_BLUE,
                            40,
                            width=SCREEN_WIDTH,
                            align="center")
       else:
           pass

       self.faceBeard.draw()
       self.compy.draw()


   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

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


       self.draw_instructions()
       self.draw_possible_attack()
       self.draw_scores()
       self.draw_computer_attack()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)

       if self.game_state == game_state.GameState.ROUND_ACTIVE:
           if self.player_attack_chosen == True:
               pc_attack = random.randint(0, 2)
               if pc_attack == 0:
                   self.computer_attack_type = AttackType.ROCK
               elif pc_attack == 1:
                   self.computer_attack_type = AttackType.PAPER
               else:
                   self.computer_attack_type = AttackType.SCISSORS

           else:
               pass
       else:
           pass



       pass

   def on_key_press(self, key, key_modifiers):

       """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """

       self.gamestate = Enum('GameState', ['NOT_STARTED', 'ROUND_ACTIVE', 'ROUND_DONE', 'GAME_OVER'])
       self.game_state += 1

       pass

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

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


       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True


def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()