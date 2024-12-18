import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
content = content.split('\n\n')

regles = [regle.split("|") for regle in content[0].split("\n")]
dossiers = [dossier.split(",") for dossier in content[1].split('\n')]


# Tester une page d'un dossier par rapport à ses pages précédentes et suivante ainsi qu'aux règles définies
def tester_regles_page_dossier(previous_pages, next_pages, page):

    for previous_page in previous_pages: # Parcourir chaque page précédente
        for regle in regles: # Parcourir chaque regle
            if previous_page == regle[1] and regle[0] == page:
                return False
    for next_page in next_pages: # Parcourir chaque page suivante
        for regle in regles: # Parcourir chaque regle
            if next_page == regle[0] and regle[1] == page:
                return False
            
    return True


def move_element(lst, from_index, to_index):
    # Extraire l'élément de sa position d'origine
    element = lst.pop(from_index)
    # Insérer l'élément à la nouvelle position
    lst.insert(to_index, element)
    return lst


def tester_dossier(dossier):
    status = True
    for page_idx, page in enumerate(dossier):

        status = tester_regles_page_dossier(dossier[:page_idx], dossier[page_idx + 1:], page)
        if not status:
            return False
    return status # Soit True



# # Réoordonne un dossier, l'algo est fortement similaire à tester_regles_page_dossier
# def reordonneer_dossier(dossier):

#     dossier_upd = dossier

#     for page_idx, page in enumerate(dossier): # Parcourir les pages

#         move = False

#         previous_pages = dossier[:page_idx]
#         next_pages = dossier[page_idx + 1:]

#         for idx_previous_page, previous_page in enumerate(previous_pages): # Parcourir chaque page précédente
#             for regle in regles: # Parcourir chaque regle
#                 if previous_page == regle[1] and regle[0] == page and move == False:
#                     dossier = move_element(dossier, idx_previous_page, page_idx)
#                     move = True

#         if move:
#             break

#     if not tester_dossier(dossier):
#         dossier_upd = reordonneer_dossier(dossier)
#     else:
#         return dossier_upd
    
#     return dossier_upd
    

# def reordonneer_dossier(dossier):
#     """
#     Réordonne les pages d'un dossier en respectant un ensemble de règles.
#     """
#     while True:  # Utilisation d'une boucle itérative pour éviter la récursion
#         dossier_modifie = False  # Suivi des modifications

#         for page_idx, page in enumerate(dossier):  # Parcourir les pages
#             previous_pages = dossier[:page_idx]
#             next_pages = dossier[page_idx + 1:]

#             for idx_previous_page, previous_page in enumerate(previous_pages):  # Parcourir chaque page précédente
#                 for regle in regles:  # Parcourir chaque règle
#                     # Vérifie si une règle est applicable
#                     if previous_page == regle[1] and regle[0] == page:
#                         dossier = move_element(dossier, idx_previous_page, page_idx)
#                         dossier_modifie = True  # Indique que le dossier a été modifié
#                         break  # Sort de la boucle actuelle pour recommencer l'analyse
#                 if dossier_modifie:
#                     break
#             if dossier_modifie:
#                 break

#         # Si aucune modification n'a été faite, on teste si le dossier est valide
#         if not dossier_modifie:
#             if tester_dossier(dossier):
#                 return dossier  # Retourner le dossier validé
#             else:
#                 print('ERROR')
#                 raise ValueError("Impossible de réorganiser le dossier pour le rendre valide.")  # Gestion d'erreur


from collections import defaultdict, deque

def construire_graphe_et_indegrees(dossier, regles):
    graphe = defaultdict(list)
    indegrees = defaultdict(int)
    
    # Construire le graphe pour les pages du dossier uniquement
    pages_presentes = set(dossier)
    for regle in regles:
        x, y = regle
        if x in pages_presentes and y in pages_presentes:
            graphe[x].append(y)
            indegrees[y] += 1
            if x not in indegrees:  # Initialiser les pages sans prérequis
                indegrees[x] = 0
    
    return graphe, indegrees

def tri_topologique(dossier, regles):
    graphe, indegrees = construire_graphe_et_indegrees(dossier, regles)
    # Trouver les nœuds sans prérequis
    queue = deque([node for node in dossier if indegrees[node] == 0])
    ordre = []
    
    while queue:
        node = queue.popleft()
        ordre.append(node)
        
        # Réduire le degré entrant des voisins
        for voisin in graphe[node]:
            indegrees[voisin] -= 1
            if indegrees[voisin] == 0:
                queue.append(voisin)
    
    # Vérifier si l'on a réussi à trier toutes les pages
    if len(ordre) != len(dossier):
        raise ValueError("Impossible de réorganiser le dossier pour le rendre valide.")
    
    return ordre



# Récupérer le numéro de page du millieu de chaque dossier et faire la somme de ces numéros
def somme_page_millieu(dossiers):
    somme_tot = 0
    for dossier in dossiers:
        somme_tot += int(dossier[int(len(dossier) / 2)])

    return somme_tot


def part1et2():

    dossiers_corrects = []
    dossiers_incorrects = []

    for dossier in dossiers: # Parcourir chaque dossier
        status_dossier = True
        for page_idx, page in enumerate(dossier):

            # Pour chaque page :
            # 1 . Récupérer toutes les pages précédentes et vérifier qu'une règle inverse n'est pas présente
            # 2 . Récupérer toutes les pages suivantes et vérifier qu'une règle inverse n'est pas présente

            status_page = tester_regles_page_dossier(dossier[:page_idx], dossier[page_idx + 1:], page)
            if not status_page:
                status_dossier = False
                break
            

        if status_dossier:
            dossiers_corrects.append(dossier)
        else :
            try:
                dossier_reordonne = tri_topologique(dossier, regles)
                dossiers_incorrects.append(dossier_reordonne)
            except ValueError as e:
                print(f"Erreur avec le dossier {dossier}: {e}")

    # Partie 1
    somme_dossier_correct = somme_page_millieu(dossiers_corrects)
    print("Le total des numéros de pages du millieu additionnées est de : ", somme_dossier_correct)

    # Partie 2
    somme_dossier_incorrect = somme_page_millieu(dossiers_incorrects)
    print("Le total des numéros de pages du millieu additionnées est de : ", somme_dossier_incorrect)




part1et2()