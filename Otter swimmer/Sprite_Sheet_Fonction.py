#-------------------------------------------------------------------------------
# Name:        Sprite_Sheet_Fonction.py
# Purpose:
#
# Author:      Suzy
#
# Created:     18/03/2020
# Copyright:   (c) Suzy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame

pygame.init()

def recup_sprite(sprite_sheet, frame_numero, longueur, largeur):
    """Renvoie le sprite correspondant à frame_numero sur la sprite_sheet,
    longueur et largeur sont les dimensions de chaque sprite"""
    img = pygame.Surface((longueur,largeur), pygame.SRCALPHA)
    img.blit(sprite_sheet, (0,0), ((frame_numero*longueur), 0, longueur, largeur))
    return img