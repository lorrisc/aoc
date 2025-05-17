import sys
from pathlib import Path

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split("\n")

calibs = []

for ligne in lignes:

    first_dgt = None
    last_dgt = None

    for char in ligne:
        if char.isdigit():
            first_dgt = char
            break

    for char in reversed(ligne):
        if char.isdigit():
            last_dgt = char
            break

    calib_val = first_dgt + last_dgt

    calibs.append(int(calib_val))

calibs_sum = 0
for val in calibs:
    calibs_sum += val

print(calibs_sum)