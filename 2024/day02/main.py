import sys
from pathlib import Path

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)

lines = [[int(el) for el in line.split(' ')] for line in content.split('\n')] # Créer un tableau de ligne puis un tableau d'élément


# Déterminer le sens de deux éléments
def determiner_sens(first, second):
    if first > second : return "desc"
    elif first < second : return "asc"
    else : return "plat"

# Déterminer si le dossier est safe
def is_safe_line(line):

    sens = determiner_sens(line[0], line[1])

    previous_elt = line[0]

    # Parcourir chaque élément de la ligne
    for elt in line[1:]:

        if abs(previous_elt - elt) > 3:
            return False
        
        if (previous_elt > elt and sens != "desc") \
            or (previous_elt < elt and sens != "asc") \
            or (previous_elt == elt):
            return False
        
        previous_elt = elt  

    return True


def part1():

    nb_safe = sum(1 if is_safe_line(line) else 0 for line in lines) # parcourir chaque ligne et 1 si le dossier est safe

    print("PART1 : Le nombre de dossier dit safe est de : ", nb_safe)


def part2():

    nb_safe = 0

    for line in lines:
        safe = is_safe_line(line)

        if not(safe): # Tester en enlevant tout les niveaux : brutforce :)
            for i in range(len(line)):

                # Créer une copie de la ligne et enlever le niveau i
                line_test = line[:]
                line_test.pop(i)
                
                safe = is_safe_line(line_test)

                if safe:
                    nb_safe += 1
                    break
        else : 
            nb_safe += 1

    print("PART2 : Le nombre de dossier dit safe est de : ", nb_safe)

part1()
part2()