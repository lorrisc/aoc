import sys
from pathlib import Path
from heapq import heappush, heappop

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
maze = [list(ligne) for ligne in content.split("\n")]

def afficher_maze(maze):
    for row in maze:
        print("".join(row))
    print("\n")

def trouver_depart(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "S":
                return i, j

def trouver_cible(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "E":
                return i, j
            
# Dijkstra pour éviter l'erreur de récursion
def chercher_chemin_dijkstra(maze, directions, start_x, start_y, cible, direction_init=(0, 1)):
    # Utilisons un min-heap pour simuler la priorité comme dans un Dijkstra
    # Pour assurer que nous prenons toujours le chemin de coût minimal
    from heapq import heappush, heappop
    
    # File de priorité - chaque élément : (coût, x, y, direction)
    pq = []
    heappush(pq, (0, start_x, start_y, direction_init))

    # État visité: (x, y, direction) → coût minimum pour y arriver ainsi
    visited = {}

    while pq:
        cost, x, y, prev_dir = heappop(pq)

        # Si on a déjà visité cet état avec un coût inférieur, on passe
        state = (x, y, prev_dir)
        if state in visited and visited[state] <= cost:
            continue
            
        # Mettre à jour le coût pour cet état
        visited[state] = cost
        
        # Si on a atteint la cible
        if (x, y) == cible:
            return cost

        # Essayer chaque direction
        for dir_key, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            new_dir = (dx, dy)

            # Vérifier si la nouvelle position est valide
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != "#":
                # Calculer le coût de rotation si on change de direction
                rotation_cost = 0
                if prev_dir != new_dir:
                    rotation_cost = 1000

                new_cost = cost + 1 + rotation_cost
                new_state = (new_x, new_y, new_dir)

                # Si cet état n'a pas été visité ou si on a trouvé un meilleur chemin
                if new_state not in visited or new_cost < visited[new_state]:
                    heappush(pq, (new_cost, new_x, new_y, new_dir))

    return None  # Pas de chemin trouvé

# Version DFS récursive originale (pour référence ou petits labyrinthes)
def chercher_chemin_dfs(maze, directions, x, y, already_visit, cible, direction):
    if (x, y) == cible:
        return 0  # Cible atteinte

    min_cout = float('inf')

    for dir in directions:
        incr_x, incr_y = directions[dir]
        new_x, new_y = x + incr_x, y + incr_y

        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]):
            if maze[new_x][new_y] != "#" and (new_x, new_y) not in already_visit:
                already_visit.add((new_x, new_y))
                cout = chercher_chemin_dfs(maze, directions, new_x, new_y, already_visit, cible, (incr_x, incr_y))
                if cout is not None:
                    cout_rotation = 0
                    if incr_x != direction[0] or incr_y != direction[1]:
                        cout_rotation = 1000
                    min_cout = min(min_cout, 1 + cout + cout_rotation)
                already_visit.remove((new_x, new_y))

    return min_cout if min_cout != float('inf') else None

# afficher_maze(maze)

# Trouver le départ et l'arrivée
dep_x, dep_y = trouver_depart(maze)
arr_x, arr_y = trouver_cible(maze)

directions = {
    "N": (-1, 0), 
    "S": (1, 0),
    "E": (0, 1),
    "O": (0, -1)
}

# Version DFS fonctionnels pour les petits problemes
# already_visit = set()
# already_visit.add((dep_x, dep_y))
# print("Tentative avec DFS...")
# cout_min_dfs = chercher_chemin_dfs(maze, directions, dep_x, dep_y, already_visit, (arr_x, arr_y), (0, 1))
# print("Coût minimal (DFS) :", cout_min_dfs)

# Utiliser Dijkstra qui fonctionne pour tous les labyrinthes
cout_min_dijkstra = chercher_chemin_dijkstra(maze, directions, dep_x, dep_y, (arr_x, arr_y))
print("Coût minimal (Dijkstra) :", cout_min_dijkstra)