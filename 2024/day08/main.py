import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split('\n')

char_trouve = []
zones_blanches = set()
zones_blanches_p1 = set()

# renvoie un tableau contenant des tableaux [row, col] de chaque position de cet élément
def trouver_pos_char(lignes, char_recherche):
    positions = []
    for idx_ligne, ligne in enumerate(lignes):
        for idx_row, char in enumerate(ligne): 
            if char == char_recherche:
                positions.append([idx_ligne, idx_row])
    
    return positions


for ligne in lignes: # Parcourir chaque ligne
    for char in ligne: # Parcourir chaque colonne
        if char != "." and char not in char_trouve: # Si le char n'est pas un Point et n'a pas déjà été traité

            char_trouve.append(char)

            positions_antennes = trouver_pos_char(lignes, char) # On récupére la positions de l'ensembles des antennes

            for idx_pos1, position_antenne in enumerate(positions_antennes): # On parcourt chaque antenne
                for idx_pos2, position_antenne2 in enumerate(positions_antennes): # On reparcourt chaque antenne
                    if idx_pos1 < idx_pos2: # Si idx_pos1 est inférieur on la considere car le couple n'a pas encore été traité

                        # Positions des antennes (lignes et cols)
                        idx_ligne_a1 = positions_antennes[idx_pos1][0]
                        idx_ligne_a2 = positions_antennes[idx_pos2][0]
                        idx_colonne_a1 = positions_antennes[idx_pos1][1]
                        idx_colonne_a2 = positions_antennes[idx_pos2][1]

                        # Calcul de leur distance
                        distance_ligne = idx_ligne_a1 - idx_ligne_a2
                        distance_colonne = idx_colonne_a1 - idx_colonne_a2

                        # Nouvelles positions
                        new_row_a1 = idx_ligne_a1
                        new_row_a2 = idx_ligne_a2
                        new_col_a1 = idx_colonne_a1
                        new_col_a2 = idx_colonne_a2

                        # On ajoute pour la partie 1
                        zones_blanches_p1.add((idx_ligne_a1 + distance_ligne, idx_colonne_a1 + distance_colonne))
                        zones_blanches_p1.add((idx_ligne_a2 - distance_ligne, idx_colonne_a2 - distance_colonne))

                        # Une direction
                        while True:

                            # Condition de sortie
                            if new_row_a1 < 0 or new_col_a1 < 0 or new_row_a1 >= len(lignes) or new_col_a1 >= len(lignes[0]):
                                break  # On quitte la boucle quand on atteint les limites
                            else:
                                zones_blanches.add((new_row_a1, new_col_a1))
                                new_row_a1 += distance_ligne
                                new_col_a1 += distance_colonne

                        # Puis l'autre direction
                        while True:

                            if new_row_a2 < 0 or new_col_a2 < 0 or new_row_a2 + 1 > len(lignes) or new_col_a2 + 1 > len(lignes[0]):
                                break
                            else:
                                zones_blanches.add((new_row_a2, new_col_a2))
                                new_row_a2 -= distance_ligne
                                new_col_a2 -= distance_colonne


# Supprimer les zones blanche hors matrice pour la partie 1
for zone_blanche in zones_blanches_p1.copy():
    if zone_blanche[0] < 0 or zone_blanche[1] < 0 or zone_blanche[0] + 1 > len(lignes) or zone_blanche[1] + 1 > len(lignes[0]):
        zones_blanches_p1.remove(zone_blanche)

print("PARTIE 1 : Le nombre de zone blanche distincte est de : ", len(zones_blanches_p1))
print("PARTIE 2 : Le nombre de zone blanche distincte est de : ", len(zones_blanches))
