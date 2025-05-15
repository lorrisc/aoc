import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import copy
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
lignes = content.split('\n')

# La fonction update_position_garde permet de mettre à jour la position du garde en fonction de son sens et s'il rencontre un obstacle
# Obstacle, on tourne de 90 deg
# Pas d'obstacle : on continu dans le même sens
def update_position_garde(lignes_fct, sens, current_row, current_col, new_row, new_col):
    current_lignes = lignes_fct.copy()

    if len(current_lignes) - 1 < new_row or len(current_lignes[new_row]) - 1 < new_col or new_row < 0 or new_col < 0:

        ligne_modifiable = list(current_lignes[current_row])
        ligne_modifiable[current_col] = "X"
        current_lignes[current_row] = ''.join(ligne_modifiable)

        return current_lignes, True

    if current_lignes[new_row][new_col] != "#":

        # Convertir la chaîne à la position new_row en une liste de caractères
        ligne_modifiable = list(current_lignes[new_row])
        # Modifier le caractère voulu
        ligne_modifiable[new_col] = sens
        # Reconstruire la chaîne et réassigner
        current_lignes[new_row] = ''.join(ligne_modifiable)

        ligne_modifiable = list(current_lignes[current_row])
        ligne_modifiable[current_col] = "X"
        current_lignes[current_row] = ''.join(ligne_modifiable)

    else:
        if sens == "^":
            new_sens = ">"
        elif sens == ">":
            new_sens = "v"
        elif sens == "v":
            new_sens = "<"
        elif sens == "<":
            new_sens = "^"

        ligne_modifiable = list(current_lignes[current_row])
        ligne_modifiable[current_col] = new_sens
        current_lignes[current_row] = ''.join(ligne_modifiable)      

    return current_lignes, False

# La fonction trouver_nombre_distinctes_position(lignes) permet de trouver le nombre de position distinctes qui ont été surveillés par le garde
def trouver_nombre_distinctes_position(lignes):
    nb_total = 0

    for ligne in lignes:
        for char in ligne:
            if char == "X":
                nb_total += 1

    return nb_total





# La fonction trouver_garde(lignes) permet de chercher le garde dans un ensemble de ligne puis de modifier sa position via update_position_garde(...)
def trouver_garde(lignes, partie2 = False):
    current_lignes = lignes.copy()
    garde_partis = False

    # Pour la P2 : vérifier si la position courante du garde + sens n'a pas déjà été visité
    pos_deja_surveille = set()
    all_pos = [] # Liste utile pour connaitre les celulles qui se sont trouvé sur le chemin, pour la P2 cela pourra permettre de se limiter a ces cellules pour tester les combinaisons d'obstacle

    while not garde_partis:
        stop = False
        for idx_row, ligne in enumerate(current_lignes):
            for idx_col, char in enumerate(ligne):
                if char in "^>v<":
                    if char == "^":
                        current_lignes, garde_partis = update_position_garde(current_lignes, "^", idx_row, idx_col, idx_row - 1, idx_col)
                    elif char == ">":
                        current_lignes, garde_partis = update_position_garde(current_lignes, ">", idx_row, idx_col, idx_row, idx_col + 1)
                    elif char == "v":
                        current_lignes, garde_partis = update_position_garde(current_lignes, "v", idx_row, idx_col, idx_row + 1, idx_col)
                    elif char == "<":
                        current_lignes, garde_partis = update_position_garde(current_lignes, "<", idx_row, idx_col, idx_row, idx_col - 1)

                    if [idx_row, idx_col] not in all_pos:
                        all_pos.append([idx_row, idx_col])

                    current_pos_str = f"{idx_row}_{idx_col}_{char}" # String de la position et sens

                    if current_pos_str in pos_deja_surveille: # Si déjà survéillés alors le garde est bloqué
                        return False, all_pos
                    pos_deja_surveille.add(current_pos_str) # Sinon l'append

                    stop = True
                    break  # Sortir de la boucle interne
            if stop:
                break  # Sortir de la boucle externe

    if not partie2:
        # Compter les positions surveillées une fois que le garde est parti
        nombre_positions_surveilles = trouver_nombre_distinctes_position(current_lignes)
        print("Le garde est parti en surveillant", nombre_positions_surveilles, "positions.")
    else:
        return True, all_pos




def part1():
    trouver_garde(lignes)


# Fonction pour tester une position comme obstacle
def tester_obstacle(pos_a_test, lignes):
    print(pos_a_test)
    current_lignes = copy.deepcopy(lignes)
    ligne_modifiable = list(current_lignes[pos_a_test[0]])
    ligne_modifiable[pos_a_test[1]] = "#"
    current_lignes[pos_a_test[0]] = ''.join(ligne_modifiable)

    status, _ = trouver_garde(current_lignes, True)
    return not status  # Renvoie True si le garde est bloqué


def part2():
    current_lignes = lignes.copy()
    
    status, all_pos = trouver_garde(current_lignes, True)
    obstacle_nb_pos = 0

    with ProcessPoolExecutor() as executor:
        # Créer des tâches parallèles pour tester les positions
        futures = [executor.submit(tester_obstacle, pos, current_lignes) for pos in all_pos
                   if current_lignes[pos[0]][pos[1]] not in "^>v<#"]

        # Récupérer les résultats
        results = [future.result() for future in futures]

        obstacle_nb_pos = sum(results)

    print("Il y a", obstacle_nb_pos, "positions d'obstacle possible")

if __name__ == "__main__":
    part1()
    part2()




