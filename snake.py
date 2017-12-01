from upemtk import *
from time import sleep
from random import *

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases


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


def affiche_serpent(serpent):
    x, y = case_vers_pixel(serpent)  # à modifier !!!
    
    cercle(x, y, taille_case/2 + 1,
           couleur='White', remplissage='White')
def change_direction(direction, touche):
    """Permet de gérer le changement de direction"""
    if touche == 'Up':
        # flèche haut pressée
        return(0, -1)
    elif touche == 'Down':
        # flèche bas pressée
        return(0, 1)
    elif touche == 'Left':
        # flèche gauche pressée
        return(-1, 0)
    elif touche == 'Right':
        # flèche droite pressée
        return(1, 0)
    else:
        # pas de changement !
        return direction


# programme principal
if __name__ == "__main__":

    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 0)  # direction initiale du serpent
    posS = (0,0)
    posP = (40, 30)
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # boucle principale
    pas_pomme = True
    pos_S = [(0,0)]
    while True:
        # affichage des objets
        efface_tout()
        if posS == posP:
            nb_pomme.append(1)
            pas_pomme = True
        if pas_pomme == True:
            px = randint(0, 39)
            py = randint(0, 29)
            pas_pomme = False
            posP = px, py
        affiche_pommes((px,py))# à modifier !
        x, y = posS 
        s, d = direction
        posS = (x + s, y + d)
        affiche_serpent(pos_S)  # à modifier !
        mise_a_jour()


        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Quitte':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev))

        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()
