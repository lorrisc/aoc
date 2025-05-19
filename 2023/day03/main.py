import sys
from pathlib import Path
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lines = content.split('\n')

# recherche un nombre dans une ligne à partir d'un index.
# renvoie le nombre, l'index de début et de fin.
def extract_number_from_pos(row, start_index):
    number = ""
    for j in range(start_index, len(row)):
        if row[j].isdigit():
            number += row[j]
        else:
            break
    return int(number), start_index, start_index + len(number) - 1

# Retour True si le caractère est spécial et différent de 0
def is_special(char):
    return not char.isalnum() and char != '.'

# Vérifie les cases adjacente à un nombre et cherche un caractère spécial
def has_adjacent_special_character(lines, row_idx, start_col, end_col):

    for i in range(row_idx - 1, row_idx + 2):
        if i < 0 or i >= len(lines):
            continue
        for j in range(start_col - 1, end_col + 2):
            if j < 0 or j >= len(lines[i]):
                continue
            if i == row_idx and start_col <= j <= end_col:
                continue  # On saute le nombre lui-même
            if is_special(lines[i][j]):
                return True
    return False


valid_numbers = []

for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        if line[j].isdigit():
            number, start, end = extract_number_from_pos(line, j)
            if has_adjacent_special_character(lines, i, start, end):
                valid_numbers.append(number)
            j = end + 1
        else:
            j += 1
    
print(f"PARTIE 1 : {sum(valid_numbers)}")