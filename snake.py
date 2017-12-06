from upemtk import *
from time import sleep
from random import *

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases

def deplacement(pos, direction, signe):
    """
    Fonction qui recoit la position accompagné d'une diréction et renvoie
    la position actualisée
    """
    x, y = pos
    s, d = direction
    if signe == 1:
        nPos = (x + s, y + d)
    else:
        nPos = (x - s, y - d)
    return nPos
def case_vers_pixel(x):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la forme
    d'un couple d'entiers (ligne, colonne) et renvoyant les coordonnées du
    pixel se trouvant au centre de cette case. Ce calcul prend en compte la
    taille de chaque case, donnée par la variable globale taille_case.
    """
    i, j = x
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    x, y = case_vers_pixel(pommes)

    cercle(x, y, taille_case/2,
           couleur='darkred', remplissage='red')


def affiche_serpent(serpent, joueur):
    n = 0
    while n < len(serpent):
        x, y = case_vers_pixel(serpent[n])
        if joueur == 1:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Blue', remplissage='Blue')
        if joueur == 2:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Red', remplissage='Red')
        if joueur == 3:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Black', remplissage='Black')
        n += 1
def change_direction(direction, touche, joueur):
    """Permet de gérer le changement de direction"""
    if joueur == 1:
        if touche == 'Up':
            # flèche haut pressée
            return(0, -1)
        elif touche == 'Down':
            # flèche bas pressée
            return(0, 1)
        elif touche == 'Left':
            # flèche gauche pressée
            return(-1 , 0)
        elif touche == 'Right':
            # flèche droite pressée
            return(1, 0)
        else:
            # pas de changement !
            return direction
    elif joueur == 2:
        if touche == 'z':
            # flèche haut pressée
            return(0, -1)
        elif touche == 's':
            # flèche bas pressée
            return(0, 1)
        elif touche == 'q':
            # flèche gauche pressée
            return(-1 , 0)
        elif touche == 'd':
            # flèche droite pressée
            return(1, 0)
        else:
            # pas de changement !
            return direction

def ft_solo_mode():
    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 1)  # direction initiale du serpent
    posP = (40, 30)
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # boucle principale
    pas_pomme = True
    pos_S = [(21,15),(21,14),(21,13)]
    while True:
        # affichage des objets
        efface_tout()
        if pos_S[0] == posP:
            pas_pomme = True
            pos_S.append(deplacement(posP, direction, 0))

        if pas_pomme == True:
            px = randint(1, 38)
            py = randint(1, 28)
            pas_pomme = False
            posP = px, py
            while pos_S.count(posP) != 0:
                px = randint(1, 39)
                py = randint(1, 29)
                posP = px, py
        affiche_pommes(posP)# à modifier !
        pos_S.insert(0, (deplacement(pos_S[0], direction, 1)))
        pos_S.pop()
        collision = pos_S.count(pos_S[0])
        if collision != 1:
            break
        x, y = pos_S[0]
        print(pos_S)
        if x > largeur_plateau or x < 0 or y > hauteur_plateau or y < 0:
            break
        affiche_serpent(pos_S,3)  # à modifier !
        mise_a_jour()


        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Escape':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev), 1)

        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()

def ft_duo_mode():
    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (1, 0)  # direction initiale du serpent
    direction2 = (-1, 0)  # direction initiale du deuxiemme serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # boucle principale
    pas_pomme = True
    pos_S = [(1,1)]
    pos_S2 = [(38,28)]
    while True:
        # affichage des objets
        efface_tout()
        pos_S.insert(0, (deplacement(pos_S[0], direction, 1)))
        x, y = pos_S[0]
        pos_S2.insert(0, (deplacement(pos_S2[0], direction2, 1)))
        s, d = pos_S2[0]
        if x > largeur_plateau or x < 0 or y > hauteur_plateau or y < 0:
            break
        if s < 0 or s > largeur_plateau or y < 0 or y > hauteur_plateau:
            break
        collision1 = pos_S.count(pos_S2[0]) + pos_S2.count(pos_S2[0])
        if collision1 != 1:
            print("J2 désynchronisé")
            break
        collision2 = pos_S2.count(pos_S[0]) + pos_S.count(pos_S[0])
        if collision2 != 1:
            print("J1 désynchronisé")
            break
        affiche_serpent(pos_S,1)  # à modifier !
        affiche_serpent(pos_S2,2)
        mise_a_jour()


        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Escape':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev), 1)
            direction2 = change_direction(direction2, touche(ev), 2)
        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()



 #programme principal
if __name__ == "__main__":
    mode = "ok"
    while mode != "SOLO" and mode != "DUO":
        mode = input("Solo ou duo?:")
        mode = mode.upper()
    if mode == "SOLO":
        ft_solo_mode()
    else:
        ft_duo_mode()


