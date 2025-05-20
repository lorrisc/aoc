import sys
from pathlib import Path
import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *

content = read_file(Path(__file__).parent / "input.txt", True)
cards = content.split('\n')

def part1(cards):
    cards = [card.split(": ")[1].split(" | ") for card in cards]

    win_score = 0

    for card in cards:
        win = set(card[0].split())
        have = set(card[1].split())
        
        matches = len(win & have)

        win_score += 2 ** (matches - 1) if matches > 0 else 0

    print(f"PARTIE 1 : {win_score}")

part1(cards)

def part2(cards):
    nb_card_instances = {}
    for i in range(1, len(cards) + 1):
        nb_card_instances[i] = 1

    for card in cards:

        card_num, card_data = card.split(": ")
        card_num = int(card_num.split()[1])
        win, have = card_data.split(" | ")

        win = set(win.split())
        have = set(have.split())
        
        matches = len(win & have)

        for i in range(1, matches + 1):
            nb_card_instances[card_num + i] += nb_card_instances[card_num]

    nb_tot_cards = sum(nb_card_instances.values())

    print(f"PARTIE 2 : {nb_tot_cards}")
        
part2(cards)
    