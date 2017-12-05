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


def affiche_serpent(serpent):
    n = 0
    while n < len(serpent):
        x, y = case_vers_pixel(serpent[n])

        cercle(x, y, taille_case/2 + 1,
               couleur='Black', remplissage='Black')
        n += 1
def change_direction(direction, touche,):
    """Permet de gérer le changement de direction"""
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

def ft_solo_mode():
    # initialisation du jeu
    i = 0
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 0)  # direction initiale du serpent
    posS = (0,0)
    posP = (40, 30)
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # boucle principale
    pas_pomme = True
    pos_S = [(21,15)]
    while True:
        # affichage des objets
        efface_tout()
        if pos_S[0] == posP:
            pas_pomme = True
            pos_S.append(deplacement(posP, direction, 0))
        collision = pos_S.count(pos_S[0])
        if collision != 1:
            break
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
        if len(pos_S) > 1:
            pos_S.insert(0, (deplacement(pos_S[0], direction, 1)))
            pos_S.pop()
        else:
            pos_S[0] = (deplacement(pos_S[0], direction, 1))
        x, y = pos_S[0]
        print(pos_S)
        if x > largeur_plateau or x < 0 or y > hauteur_plateau or y < 0:
            break
        affiche_serpent(pos_S)  # à modifier !
        mise_a_jour()


        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Escape':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev))

        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()


# programme principal
if __name__ == "__main__":
    ft_solo_mode()


