import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)

representations_strs = ""
index_fichier = 0

print(1)

for idx_char, char in enumerate(content): # on parcourt chaque char
    if idx_char % 2 == 0: # C'est une longueur de fichier
        for i in range(0, int(char)):
            representations_strs += str(index_fichier)
        index_fichier += 1
    else: # C'est une longueur d'espace vide
        for i in range(0, int(char)):
            representations_strs += "."

print(2)

# Vider les espaces vides par les chars (en partant des chars non vide de la droite)

# La fonction rechercher_idx_premier_vide(strs) prend en parametre une chaine de caractère et renvoie le premier index vide (qui est caractérisé par un point)
def rechercher_idx_premier_vide(chaine):
    for idx_char, char in enumerate(chaine):
        if char == ".":
            return idx_char
    return None
print(3)

# Convertir la chaîne en liste pour des modifications plus rapides
representations_list = list(representations_strs)
i = len(representations_list) - 1

while i > 0:  # Parcourir à l'envers la chaîne
    idx_first_empty = rechercher_idx_premier_vide(representations_list)

    if idx_first_empty is not None and idx_first_empty < i:  # Existe et est inférieur à l'index courant
        # Effectuer les modifications directement sur la liste
        representations_list[idx_first_empty], representations_list[i] = representations_list[i], "."

    i -= 1

# Calcul de la somme
somme_p1 = 0
print(4)

for idx_char, char in enumerate(representations_list):
    if char == ".": break
    somme_p1 += idx_char * int(char)


print(somme_p1)