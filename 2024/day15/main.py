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

def trouver_robot(carte):
    for i, ligne in enumerate(carte):
        for j, col in enumerate(ligne):
            if carte[i][j] == "@":
                return i, j
            

def deplacer_element_p1(carte, element, current_x, current_y, increment_x, increment_y):
    new_x = current_x + increment_x
    new_y = current_y + increment_y

    global pos_robot_x
    global pos_robot_y

    if carte[new_x][new_y] == "#":
        return False
    elif carte[new_x][new_y] == "O":
        success = deplacer_element_p1(carte, "O", new_x, new_y, increment_x, increment_y)
        if success:
            return deplacer_element_p1(carte, element, current_x, current_y, increment_x, increment_y)
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

def get_sum_coordinates_p1(carte):
    total = 0
    for i, row in enumerate(carte):
        for j, col in enumerate(row):
            if carte[i][j] == "O":
                total += 100 * i + j
    return total


def part1():
    carte_p1 = [row.copy() for row in carte]
    x, y = trouver_robot(carte_p1)

    global pos_robot_x, pos_robot_y
    pos_robot_x, pos_robot_y = x, y

    for mvt in mouvements:
        if mvt == "^":
            deplacer_element_p1(carte_p1, "@", pos_robot_x, pos_robot_y, -1, 0)
        elif mvt == "v":
            deplacer_element_p1(carte_p1, "@", pos_robot_x, pos_robot_y, 1, 0)
        elif mvt == "<":
            deplacer_element_p1(carte_p1, "@", pos_robot_x, pos_robot_y, 0, -1)
        elif mvt == ">":
            deplacer_element_p1(carte_p1, "@", pos_robot_x, pos_robot_y, 0, 1)

    print("PARTIE 1 - SOMME COORDONNEES :")
    print(get_sum_coordinates_p1(carte_p1))

def deplacer_element_p2(carte, element, current_x, current_y, increment_x, increment_y):

    carte_copie = [row.copy() for row in carte]

    new_x = current_x + increment_x
    new_y = current_y + increment_y

    global pos_robot_x
    global pos_robot_y

    def restaurer_carte():
        for i in range(len(carte)):
            for j in range(len(carte[i])):
                carte[i][j] = carte_copie[i][j]

    if carte[new_x][new_y] == "#":
        return False
    elif carte[new_x][new_y] == "]":
        success = deplacer_element_p2(carte, carte[new_x][new_y], new_x, new_y, increment_x, increment_y)
        success2 = True
        if increment_x == - 1 or increment_x == 1:
            success2 = deplacer_element_p2(carte, carte[new_x][new_y - 1], new_x, new_y - 1, increment_x, increment_y)
        if success and success2:
            return deplacer_element_p2(carte, element, current_x, current_y, increment_x, increment_y)
        else:
            restaurer_carte()
            return False
    elif carte[new_x][new_y] == "[":
        success = deplacer_element_p2(carte, carte[new_x][new_y], new_x, new_y, increment_x, increment_y)
        success2 = True
        if increment_x == - 1 or increment_x == 1:
            success2 = deplacer_element_p2(carte, carte[new_x][new_y + 1], new_x, new_y + 1, increment_x, increment_y)
        if success and success2:
            return deplacer_element_p2(carte, element, current_x, current_y, increment_x, increment_y)
        else:
            restaurer_carte()
            return False
    elif carte[new_x][new_y] == ".":
        carte[new_x][new_y] = element
        carte[current_x][current_y] = "."
        if element == "@":
            pos_robot_x = new_x
            pos_robot_y = new_y
        return True

    restaurer_carte()
    return False

def aggrandir_carte(carte):
    for i, row in enumerate(carte):
        new_row = []
        for col in row:
            if col == "#": # Ajouter un nouveau #
                new_row.append("#")
                new_row.append(col)
            elif col == "O":
                new_row.append("[")
                new_row.append("]")
            elif col == ".":
                new_row.append(".")
                new_row.append(".")
            elif col == "@":
                new_row.append("@")
                new_row.append(".")
        carte[i] = new_row

    return carte

def get_sum_coordinates_p2(carte):
    total = 0
    for i, row in enumerate(carte):
        for j, col in enumerate(row):
            if carte[i][j] == "[":
                total += 100 * i + j
    return total

def part2():
    carte_p2 = [row.copy() for row in carte]
    carte_p2 = aggrandir_carte(carte_p2)

    x, y = trouver_robot(carte_p2)

    global pos_robot_x, pos_robot_y
    pos_robot_x, pos_robot_y = x, y

    # afficher_carte(carte_p2)

    for mvt in mouvements:
        if mvt == "^":
            deplacer_element_p2(carte_p2, "@", pos_robot_x, pos_robot_y, -1, 0)
        elif mvt == "v":
            deplacer_element_p2(carte_p2, "@", pos_robot_x, pos_robot_y, 1, 0)
        elif mvt == "<":
            deplacer_element_p2(carte_p2, "@", pos_robot_x, pos_robot_y, 0, -1)
        elif mvt == ">":
            deplacer_element_p2(carte_p2, "@", pos_robot_x, pos_robot_y, 0, 1)

        # afficher_carte(carte_p2)

    print("PARTIE 2 - SOMME COORDONNEES :")
    print(get_sum_coordinates_p2(carte_p2))

part1()
part2()