import sys
from pathlib import Path
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input.txt", True)
cards = content.split('\n')
cards = [card.split(": ")[1].split(" | ") for card in cards]

win_score = 0

for card in cards:
    win_numbers = card[0].split()
    card_numbers = card[1].split()
    win_occurences = 0

    for win_number in win_numbers:
        if win_number in card_numbers:
            win_occurences += 1

    win_score += 2 ** (win_occurences - 1) if win_occurences > 0 else 0

print(win_score)