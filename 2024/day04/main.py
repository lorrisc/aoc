import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split('\n')




sens = {
    "droite": [0, 1],
    "gauche": [0, -1],
    "haut": [-1, 0],
    "bas": [1, 0],
    "diag_bas_droite": [1, 1],
    "diag_bas_gauche": [1, -1],
    "diag_haut_droite": [-1, 1],
    "diag_haut_gauche": [-1, -1]
}

def rechercher_mot(lignes, idx_row, idx_col, mot_recherche, idx_lettre = 0, pas_horizontal = 0, pas_vertical = 0):

    trouve = None

    if idx_row + 1 <= len(lignes) and idx_row >= 0: 
        if idx_col + 1 <= len(lignes[idx_row]) and idx_col >= 0:
            if lignes[idx_row][idx_col] == mot_recherche[idx_lettre]: # Lettre trouvé

                if idx_lettre + 1 < len(mot_recherche): # Si le mot n'est pas fini chercher la lettre suivante
                    trouve = rechercher_mot(lignes, idx_row + pas_horizontal, idx_col + pas_vertical, mot_recherche, idx_lettre + 1, pas_horizontal, pas_vertical)
                else:
                    trouve = True

    return trouve


def part1():
    mot_recherche = ["X", "M", "A", "S"]

    nb_mots_trouves = 0

    for idx_row, ligne in enumerate(lignes): # Parcourir chaque ligne
        for idx_col, char in enumerate(ligne): # Parcourir chaque colonne
            if char == mot_recherche[0]: # Si la première lettre et trouvé alors rechercher le mot pour chaque sens

                for sens_nom, sens_val in sens.items():
                    mot_trouve = rechercher_mot(lignes, idx_row + sens_val[0], idx_col + sens_val[1], mot_recherche, 1, sens_val[0], sens_val[1])
                    if mot_trouve: # Si le mot est trouvé incrémenter
                        nb_mots_trouves += 1

    print("Le nombre de XMAS est de : ", nb_mots_trouves)

def part2():
    mot_recherche = ["M", "A", "S"]

    sens_possible = {'diag_bas_droite', 'diag_bas_gauche', 'diag_haut_droite', 'diag_haut_gauche'}
    sens_p2 = {cle: sens[cle] for cle in sens_possible if cle in sens}

    nb_mots_trouves = 0
    pos_trouves = [] # Contient des tableaux avec la position de début et de fin de mot

    for idx_row, ligne in enumerate(lignes): # Parcourir chaque ligne
        for idx_col, char in enumerate(ligne): # Parcourir chaque colonne
            if char == mot_recherche[0]: # Si la première lettre et trouvé alors rechercher le mot pour chaque sens

                for sens_nom, sens_val in sens_p2.items():
                    mot_trouve = rechercher_mot(lignes, idx_row + sens_val[0], idx_col + sens_val[1], mot_recherche, 1, sens_val[0], sens_val[1])
                    if mot_trouve: # Si le mot est trouvé stocké sa pos

                        # Stocké la position de début et de fin du mot trouvé ; ex : [0, 1], [2, 3]
                        pos_trouves.append([
                            [idx_row, idx_col], 
                            [idx_row + (len(mot_recherche) - 1) * sens_val[0], 
                            idx_col + (len(mot_recherche) - 1) * sens_val[1]]
                        ])

    idx_deja_traite = [] # Index déjà traité pour ne pas compte double les memes croix

    for pos_trouve_idx, pos_trouve in enumerate(pos_trouves): # Parcourir chaque position trouvé

        if pos_trouve_idx not in idx_deja_traite: # Pas encore traité 

            # Calculer les coordonnées de l'autres diagonal pour compléter la croix
            pos1 = [pos_trouve[0][0], pos_trouve[1][1]]
            pos2 = [pos_trouve[1][0], pos_trouve[0][1]]

            for pos_trouve_recherche_idx, pos_trouve_recherche in enumerate(pos_trouves): # Parcourir chaque position trouvé pour recherché les coordonnées calculés
                if pos_trouve_recherche[0] == pos1 and pos_trouve_recherche[1] == pos2 or pos_trouve_recherche[0] == pos2 and pos_trouve_recherche[1] == pos1: # Coordonnées présent
                    idx_deja_traite.append(pos_trouve_recherche_idx) # Stocker l'idx
                    nb_mots_trouves += 1 # Incrémenter car la croix est complete

    print("Le nombre de X-MAS est de : ", nb_mots_trouves)

part1()
part2()