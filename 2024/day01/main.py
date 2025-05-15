import sys
from pathlib import Path

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)

# Créer la liste des nombres de gauche et de droite
left_numbers = []
right_numbers = []

for line in content.split("\n"):
    left, right = line.split("   ")
    left_numbers.append(int(left))
    right_numbers.append(int(right))


def part1():

    # Création de copie
    left = left_numbers[:] 
    right = right_numbers[:]

    distance_tot = 0

    # Parcourir la liste de gauche puis sommer la distance de chaque plus petit nombre puis le supprimer
    for i in range (0, len(left)):
        distance_tot += abs(min(left) - min(right))
        left.remove(min(left))
        right.remove(min(right))

    print("PART1 : La distance totale est de : ", distance_tot)


# Trouver le nombre d'occurence d'une valeur au sein d'une liste
def trouver_nb_occurences(val, list):

    nb_occurences = 0

    for elt in list:
        if elt == val: nb_occurences += 1

    return nb_occurences


def part2():

    left = left_numbers[:] 
    right = right_numbers[:]

    score_similaritude = 0

    for nb in left:
        score_similaritude += trouver_nb_occurences(nb, right) * nb

    print("PART2 : Le score de similaritude est de : ", score_similaritude)


part1()
part2()