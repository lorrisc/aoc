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

x_len = 101
y_len = 103

nb_cadrant_1 = 0
nb_cadrant_2 = 0
nb_cadrant_3 = 0
nb_cadrant_4 = 0


for ligne in lignes: 
    position, velocity = ligne.split(" ")

    valeurs_position = position.split("=")[1]
    pos_x, pos_y = map(int, valeurs_position.split(","))

    valeurs_velocity = velocity.split("=")[1]
    vel_x, vel_y = map(int, valeurs_velocity.split(","))

    for i in range(0, 100):
        pos_x = (pos_x + vel_x) % x_len
        pos_y = (pos_y + vel_y) % y_len

    # Déterminer quel est le cadran de la position pour incrémenter
    if pos_x < int(x_len / 2) and pos_y < int(y_len / 2):
        nb_cadrant_1 += 1
    elif pos_x > int(x_len / 2) and pos_y < int(y_len / 2):
        nb_cadrant_2 += 1
    elif pos_x < int(x_len / 2) and pos_y > int(y_len / 2):
        nb_cadrant_3 += 1
    elif pos_x > int(x_len / 2) and pos_y > int(y_len / 2):
        nb_cadrant_4 += 1


print(nb_cadrant_1 * nb_cadrant_2 * nb_cadrant_3 * nb_cadrant_4)