import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)

mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
domul_pattern = r"do\(\)"
dontmul_pattern = r"don't\(\)"


def part1():
    muls = re.findall(mul_pattern, content)
    nombre_final = 0

    for mul in muls:
        mul = mul.replace("mul(", "").replace(")", "")
        numbers = [int(number) for number in mul.split(",")]
        nombre_final += numbers[0] * numbers[1]

    print("PART1 : La somme est de : ", nombre_final)



def part2():

    content_p2 = content[:] # Copie

    # Trouver les do() et trier
    # Le trie est probablement optionnel car déjà trié par ordre de find ?
    matches_domul = re.finditer(domul_pattern, content_p2)
    indices_domul = [match.start() for match in matches_domul]
    indices_domul.sort()

    # Trouver les don't() et trier
    matches_dontmul = re.finditer(dontmul_pattern, content_p2)
    indices_dontmul = [match.start() for match in matches_dontmul]
    indices_dontmul.sort()

    previous_domul = -1
    nb_chars_rm = 0 # Il ne faut pas oublier de prendre en compte les précédentes suppresions dans le content pour les futurs test/suppression
    for indice_dontmul in indices_dontmul: # Parcourir chaque indice de dontmul
        for indice_domul in indices_domul: # Parcourir chaque indice de mul
            if indice_domul - nb_chars_rm > indice_dontmul - nb_chars_rm and previous_domul - nb_chars_rm < indice_dontmul - nb_chars_rm: # Si le domul est supérieur au dontmul alors supprimer la partie entre les deux indices
                content_p2 = content_p2[:indice_dontmul - nb_chars_rm] + content_p2[indice_domul - nb_chars_rm:]

                nb_chars_rm += indice_domul - indice_dontmul


                previous_domul = indice_domul
                break


    # Trouver les mul dans le nouveau texte puis traiter comme p1
    nombre_final = 0
    muls = re.findall(mul_pattern, content_p2)

    for mul in muls:
        mul = mul.replace("mul(", "").replace(")", "")
        numbers = [int(number) for number in mul.split(",")]
        nombre_final += numbers[0] * numbers[1]

    print("PART2 : Le somme est de : ", nombre_final)

    

part1()
part2()
