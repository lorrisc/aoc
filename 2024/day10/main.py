import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = [[int(char) for char in ligne] for ligne in content.split("\n")]

directions = {
    "nord": {"row": 1, "col": 0},
    "sud": {"row": -1, "col": 0},
    "est": {"row": 0, "col": 1},
    "ouest": {"row": 0, "col": -1},
}

# La fonction trouver_sentier() permet de trouver la suite d'un sentier dans une matrice
# Un sentier à une hauteur qui augmente de 1 à chaque case, et la case ne peux pas se situer en diagonale
# Le chantier est fini quand il arrive à 9
def trouver_sentier(lignes, valeur_a_trouver, current_row_idx, current_col_idx):

    positions_fin = []
    nb_chemins_distincts = 0

    for direction, val_direction in directions.items(): # Parcourir toutes les directions possibles pour les tester

        new_row_idx = current_row_idx + val_direction["row"]
        new_col_idx = current_col_idx + val_direction["col"]

        if new_row_idx >= 0 and new_row_idx < len(lignes) and new_col_idx >= 0 and new_col_idx < len(lignes[0]): # Nouvelle cellule calculé présent dans la matrice
            if lignes[new_row_idx][new_col_idx] == valeur_a_trouver:
                if valeur_a_trouver == 9: # Nous l'avons trouvé donc c'est fini, fin de sentier
                    positions_fin.append([new_row_idx, new_col_idx])
                    nb_chemins_distincts += 1
                else: # Continuer le sentier à partir de la nouvelle position
                    position_fin, nb_chemins_distincts_apres = trouver_sentier(lignes, valeur_a_trouver + 1, new_row_idx, new_col_idx)

                    nb_chemins_distincts += nb_chemins_distincts_apres

                    for pos_fin in position_fin:
                        if pos_fin not in positions_fin:
                            positions_fin.append(pos_fin)
    
    return positions_fin, nb_chemins_distincts

    
somme_score_sentier = 0
nb_de_sentier_distincts = 0

for idx_ligne, ligne in enumerate(lignes): # On parcourt chaque ligne
    for idx_char, char in enumerate(ligne): # On parcourt chaque char de la ligne
        if char == 0:
            positions_fin, nb_chemins_distincts = trouver_sentier(lignes, 1, idx_ligne, idx_char)
            somme_score_sentier += len(positions_fin)
            nb_de_sentier_distincts += nb_chemins_distincts

print("La somme des scores est de : ", somme_score_sentier)
print("Le nombre de chemin distinct est de : ", nb_de_sentier_distincts)