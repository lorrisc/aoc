import sys
from pathlib import Path
from functools import cache

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
content_split = content.split("\n\n")

carte = [list(ligne) for ligne in content_split[0].split("\n")]
mouvements = content_split[1]

def afficher_carte(carte):
    for ligne in carte:
        print("".join(ligne))
    print("\n")

# afficher_carte(carte)

def trouver_robot(carte):
    for i, ligne in enumerate(carte):
        for j, col in enumerate(ligne):
            if carte[i][j] == "@":
                return i, j
            
pos_robot_x, pos_robot_y = trouver_robot(carte)

def deplacer_element(carte, element, current_x, current_y, increment_x, increment_y):
    new_x = current_x + increment_x
    new_y = current_y + increment_y

    global pos_robot_x
    global pos_robot_y

    if carte[new_x][new_y] == "#":
        return False
    elif carte[new_x][new_y] == "O":
        success = deplacer_element(carte, "O", new_x, new_y, increment_x, increment_y)
        if success:
            return deplacer_element(carte, element, current_x, current_y, increment_x, increment_y)
        else:
            return False
    elif carte[new_x][new_y] == ".":
        carte[new_x][new_y] = element
        carte[current_x][current_y] = "."
        if element == "@":
            pos_robot_x = new_x
            pos_robot_y = new_y
        return True

    return False

for mvt in mouvements: 
    if mvt == "^":
        deplacer_element(carte, "@", pos_robot_x, pos_robot_y, - 1, 0)
    elif mvt == "v":
        deplacer_element(carte, "@", pos_robot_x, pos_robot_y, 1, 0)
    elif mvt == "<":
        deplacer_element(carte, "@", pos_robot_x, pos_robot_y, 0, - 1)
    elif mvt == ">":
        deplacer_element(carte, "@", pos_robot_x, pos_robot_y, 0, 1)

    # afficher_carte(carte)

def get_sum_coordinates(carte):
    total = 0
    for i, row in enumerate(carte):
        for j, col in enumerate(row):
            if carte[i][j] == "O":
                total += 100 * i + j
    return total

print(get_sum_coordinates(carte))