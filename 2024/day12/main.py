<<<<<<< HEAD
import sys
from pathlib import Path
from functools import cache

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = [ligne for ligne in content.split("\n")]

directions = {
    "nord": {"row": 1, "col": 0},
    "sud": {"row": -1, "col": 0},
    "est": {"row": 0, "col": 1},
    "ouest": {"row": 0, "col": -1},
}


regions = {}
parcelles_traites = []

def rechercher_region(idx_ligne, idx_col, char):

    for direction, val_direction in directions.items():

        new_row_idx = idx_ligne + val_direction["row"]
        new_col_idx = idx_col + val_direction["col"]

        if new_row_idx >= 0 and new_row_idx < len(lignes) and new_col_idx >= 0 and new_col_idx < len(lignes[0]): # Nouvelle cellule calculé présent dans la matrice
            
            str_new_parcelle = str(new_row_idx) + "_" + str(new_col_idx)
            
            if str_new_parcelle not in parcelles_traites and lignes[new_row_idx][new_col_idx] == char:
                region_parcelles_traites.append(str_new_parcelle)
                parcelles_traites.append(str_new_parcelle)
                rechercher_region(new_row_idx, new_col_idx, char)


        

for idx_ligne, ligne in enumerate(lignes): # Parcourir chaque lignes
    for idx_col, char in enumerate(ligne): # Parcourir chaque col

        str_parcelle = str(idx_ligne) + "_" + str(idx_col)

        if str_parcelle not in parcelles_traites: # La parcelle n'est pas déjà traité

            region_parcelles_traites = [str_parcelle]
            parcelles_traites.append(str_parcelle)

            rechercher_region(idx_ligne, idx_col, char)

            regions[str_parcelle] = region_parcelles_traites

            # print(char, str_parcelle, len(region_parcelles_traites), region_parcelles_traites)

# print(regions)

def calculer_perimetre(positions):
    # Convertir les positions en un ensemble de tuples pour faciliter les recherches
    cells = {tuple(map(int, pos.split('_'))) for pos in positions}
    perimeter = 0
    
    # Définir les directions adjacentes (haut, bas, gauche, droite)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for cell in cells:
        row, col = cell
        # Vérifier chaque côté de la cellule
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)
            # Si le voisin n'est pas dans la zone, ce côté est exposé
            if neighbor not in cells:
                perimeter += 1
    
    return perimeter

prix_total = 0

for region, vals_region in regions.items(): # Parcourir chaque région
    
    perimetre = calculer_perimetre(vals_region)
    prix_cloture = perimetre * len(vals_region)

    prix_total += prix_cloture

=======
import sys
from pathlib import Path
from functools import cache

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = [ligne for ligne in content.split("\n")]

directions = {
    "nord": {"row": 1, "col": 0},
    "sud": {"row": -1, "col": 0},
    "est": {"row": 0, "col": 1},
    "ouest": {"row": 0, "col": -1},
}


regions = {}
parcelles_traites = []

def rechercher_region(idx_ligne, idx_col, char):

    for direction, val_direction in directions.items():

        new_row_idx = idx_ligne + val_direction["row"]
        new_col_idx = idx_col + val_direction["col"]

        if new_row_idx >= 0 and new_row_idx < len(lignes) and new_col_idx >= 0 and new_col_idx < len(lignes[0]): # Nouvelle cellule calculé présent dans la matrice
            
            str_new_parcelle = str(new_row_idx) + "_" + str(new_col_idx)
            
            if str_new_parcelle not in parcelles_traites and lignes[new_row_idx][new_col_idx] == char:
                region_parcelles_traites.append(str_new_parcelle)
                parcelles_traites.append(str_new_parcelle)
                rechercher_region(new_row_idx, new_col_idx, char)


        

for idx_ligne, ligne in enumerate(lignes): # Parcourir chaque lignes
    for idx_col, char in enumerate(ligne): # Parcourir chaque col

        str_parcelle = str(idx_ligne) + "_" + str(idx_col)

        if str_parcelle not in parcelles_traites: # La parcelle n'est pas déjà traité

            region_parcelles_traites = [str_parcelle]
            parcelles_traites.append(str_parcelle)

            rechercher_region(idx_ligne, idx_col, char)

            regions[str_parcelle] = region_parcelles_traites

            # print(char, str_parcelle, len(region_parcelles_traites), region_parcelles_traites)

# print(regions)

def calculer_perimetre(positions):
    # Convertir les positions en un ensemble de tuples pour faciliter les recherches
    cells = {tuple(map(int, pos.split('_'))) for pos in positions}
    perimeter = 0
    
    # Définir les directions adjacentes (haut, bas, gauche, droite)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for cell in cells:
        row, col = cell
        # Vérifier chaque côté de la cellule
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)
            # Si le voisin n'est pas dans la zone, ce côté est exposé
            if neighbor not in cells:
                perimeter += 1
    
    return perimeter

prix_total = 0

for region, vals_region in regions.items(): # Parcourir chaque région
    
    perimetre = calculer_perimetre(vals_region)
    prix_cloture = perimetre * len(vals_region)

    prix_total += prix_cloture

>>>>>>> 150308a23a6a387280ce37ff0c7e87622ea5d43c
print("Le prix total est de : ", prix_total)