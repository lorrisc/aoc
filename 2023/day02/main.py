import sys
from pathlib import Path
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split("\n")

def part1et2(lignes):

    supposition = {
        "red" : 12,
        "green" : 13,
        "blue" : 14,
    }

    id_sum = 0
    sum_p2 = 0

    for game in lignes: 

        game_split = game.split(': ')
        game_id = game_split[0].replace('Game ', '')
        game_pioches = game_split[1]
        
        possible = True

        max_colors = {}

        for pioche in game_pioches.split("; "):

            for color in pioche.split(', '):

                nb_color = int(color.split(" ")[0])
                name_color = color.split(" ")[1]

                if name_color not in supposition:
                    possible = False
                elif nb_color > supposition[name_color]:
                    possible = False

                if name_color not in max_colors:
                    max_colors[name_color] = nb_color
                elif max_colors[name_color] < nb_color:
                    max_colors[name_color] = nb_color

        calcul_p2 = 1
        for max_color in max_colors:
            calcul_p2 = calcul_p2 * max_colors[max_color]
        sum_p2 += calcul_p2

        if possible:
            id_sum += int(game_id)

    print(f"PARTIE 1 : La somme des ID possibles est {id_sum}")
    print(f"PARTIE 2 : La valeur  est {sum_p2}")

part1et2(lignes)