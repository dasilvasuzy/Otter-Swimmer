#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      Suzy
#
# Created:     15/03/2020
# Copyright:   (c) Suzy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame, time
from random import randint
from Sprite_Sheet_Fonction import *
from Classes.class_Loutre import Loutre
from Classes.class_Dechet import Dechet

pygame.init()

# Variables générales de jeux

Largeur_ecran = 500
Longueur_ecran = 1080

ecran = pygame.display.set_mode((Longueur_ecran,Largeur_ecran))
pygame.display.set_caption("° Otter Swimmer °")

sprite_sheet_loutre = pygame.image.load("Images/Loutre_sprite_sheet.png").convert_alpha()
sprite_sheet_dechet = pygame.image.load("Images/dechet_sprite_sheet.png").convert_alpha()
img_fond = pygame.image.load("Images/fond.png").convert_alpha()

# Textes
ecriture = pygame.font.Font("freesansbold.ttf", 30)
texte_fin_partie = ecriture.render("Perdu !", True, (58,84,216))
textRect = texte_fin_partie.get_rect()
textRect.center = (Longueur_ecran // 2, Largeur_ecran // 2)

ecriture = pygame.font.Font("freesansbold.ttf", 20)

# Sons
pygame.mixer.init(48000, -16, 2, 2048)
Whoosh = pygame.mixer.Sound("Sons/Whoosh.wav")

music = 'Sons/Hygeia.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.play()
pygame.event.wait()

# Instanciation du joueur
joueur_loutre = Loutre(50, 200, sprite_sheet_loutre)
joueur_loutre.remplir_list_sprite(7)

dechet_test = Dechet(1080, 200, sprite_sheet_dechet,1,10)

list_dechet = []
temps_nouveau_dechet = 0

def random_dechet ():
    """Créé un objet déchet avec une vitesse et une position aléatoire"""
    posy = randint (70, Largeur_ecran-70)
    num_sprite = randint (0,3)
    vitesse = randint(5,20)
    dechet = Dechet(1080, posy, sprite_sheet_dechet, num_sprite,vitesse)
    list_dechet.append(dechet)

random_dechet()

# Boucle de jeu
game = True
while game:

    # Mise à jour de l'écran
    ecran.blit(img_fond, (0,0))

    for i in range (len(list_dechet)):
        ecran.blit(list_dechet[i].img, (list_dechet[i].x,list_dechet[i].y))

    ecran.blit(joueur_loutre.list_sprite[joueur_loutre.sprite_actif], (joueur_loutre.x,joueur_loutre.y))
    joueur_loutre.sprite_actif_increment()

    # Affichage vie
    texte_vie = ecriture.render("vie: x" + str(joueur_loutre.vie), True, (99,177,245))
    textRect_vie = texte_fin_partie.get_rect()
    ecran.blit(texte_vie, textRect_vie)

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Gestion des touches
    clavier_input = pygame.key.get_pressed()
    if clavier_input[pygame.K_UP] == True :
        joueur_loutre.mv_up()
    if clavier_input[pygame.K_DOWN] == True :
        joueur_loutre.mv_down()


    # Gestion Collision
    longueur_list_dechet = len(list_dechet)
    for dechet in list_dechet:
        if (dechet.x >= 60 and dechet.x <= 240) and (dechet.y >= joueur_loutre.y and dechet.y <= joueur_loutre.y + 100) :
            pygame.mixer.Sound.play(Whoosh)
            joueur_loutre.vie -= 1
            list_dechet.remove(dechet)

    # Gestion fin de partie
    if joueur_loutre.vie == 0:
        ecran.blit(texte_fin_partie, textRect)
        pygame.time.delay(1000)
        game = False


    # Mise à jour des déplacements des déchets et des poissons
    for i in range (len(list_dechet)):
        list_dechet[i].deplacement()

    if temps_nouveau_dechet == 10:
        random_dechet()
        temps_nouveau_dechet = 0

    time.sleep(0.1)
    temps_nouveau_dechet += 1
    pygame.display.update()

pygame.quit()