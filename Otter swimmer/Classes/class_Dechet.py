#-------------------------------------------------------------------------------
# Name:        class_Dechet
# Purpose:
#
# Author:      Suzy
#
# Created:     30/03/2020
# Copyright:   (c) Suzy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Sprite_Sheet_Fonction import *

class Dechet:
    def __init__(self, posx, posy, sheet, index_dechet, vitesse):
        self.sprite_sheet = sheet
        self.x = posx
        self.y = posy
        self.img = recup_sprite(self.sprite_sheet, index_dechet, 70, 70)
        self.vitesse = vitesse
        self.rect = self.img.get_rect()

    def deplacement(self):
        self.x -= self.vitesse
