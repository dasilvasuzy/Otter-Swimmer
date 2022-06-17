#-------------------------------------------------------------------------------
# Name:        class_Loutre
# Purpose:
#
# Author:      Suzy
#
# Created:     28/03/2020
# Copyright:   (c) Suzy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Sprite_Sheet_Fonction import *

class Loutre:
   def __init__(self, posx, posy, sheet) :
        self.sprite_sheet = sheet
        self.x = posx
        self.y = posy
        self.list_sprite = []
        self.sprite_actif = 0
        self.score = 0
        self.vie = 3
        self.rect = recup_sprite(self.sprite_sheet, 0, 200, 100).get_rect()

   def remplir_list_sprite(self, nb_sprite):
        for i in range (nb_sprite) :
            self.list_sprite.append(recup_sprite(self.sprite_sheet, i, 200, 100))
            self.list_sprite[i].set_colorkey((255,255,255))

   def sprite_actif_increment(self):
        self.sprite_actif += 1
        if self.sprite_actif == len(self.list_sprite):
            self.sprite_actif = 0

   def mv_up(self):
        if self.y > 20:
            self.y -= 8

   def mv_down(self):
        if self.y < 400:
            self.y += 8
