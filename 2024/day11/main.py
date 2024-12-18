import sys
from pathlib import Path
from functools import cache

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
pierres = [int(elt) for elt in content.split(" ")]

nb_iterrations = 75

@cache
def count(pierre, steps):
    if steps == 0:
        return 1
    if pierre == 0:
        return count(1, steps - 1)
    string = str(pierre)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    return count(pierre * 2024, steps - 1)


nb_pierres = 0
for pierre in pierres:
    nb_pierres += count(pierre, 75)

print("Le nombre de pierre est de : ", nb_pierres)