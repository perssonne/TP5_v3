import arcade
from enum import Enum

class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0

   def __init__(self):
       self.ROCK = 0
       self.PAPER = 1
       self.SCISSORS = 2

   def on_update(self, delta_time: float = 1 / 60):

       # Update the animation.
       self.current_texture += 1
       if self.current_texture < len(self.textures):
           self.set_texture(self.current_texture)
       else:
           self.current_texture = 0
           self.set_texture(self.current_texture)