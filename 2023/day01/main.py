import sys
from pathlib import Path
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split("\n")


def part1(lignes):
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

    calibs_sum = sum(calibs)

    print("PARTIE 1 : ")
    print(calibs_sum)

def part2(lignes):
    numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibs = []


    for ligne in lignes:
        all_find = {}
        for idx, char in enumerate(ligne):
            if char.isdigit():
                all_find[idx] = char

        for idx, char in enumerate(numbers_str):
            matches = re.finditer(char, ligne)

            for match in matches:
                all_find[match.start()] = idx + 1

        minval = all_find[min(all_find)]
        maxval = all_find[max(all_find)]
        calibs.append(int(str(minval) + str(maxval)))

    calibs_sum = sum(calibs)

    print("PARTIE 2 : ")
    print(calibs_sum)

part1(lignes)
part2(lignes)