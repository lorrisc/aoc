import sys
from pathlib import Path

import re

# Ajouter le chemin racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Importer toutes les fonctions ou variables de fct_file
from tools.fct_file import *


content = read_file(Path(__file__).parent / "input_test.txt", True)

equations = content.split("\n")
equations = [equation.split(": ") for equation in equations]
equations = [[equation[0], equation[1].split(" ")] for equation in equations]

operateurs = ["+", "*"]

for equation in equations:
    # print(equation[0])
    # print(equation[1])
    print("\n")

    idx_test_op = 0
    while idx_test_op + 1 <= len(operateurs):
        calcul = ""
        for idx_nombre, nombre in enumerate(equation[1]):
            if idx_nombre < len(equation[1]) - 1:
                if idx_nombre == idx_test_op:
                    calcul += nombre + operateurs[idx_test_op]
                else:
                    if (len(operateurs) - 1 >= idx_test_op + 1):
                        calcul += nombre + operateurs[idx_test_op + 1]
                    elif (idx_test_op - 1 >= 0):
                        calcul += nombre + operateurs[idx_test_op - 1]
            else:
                calcul += nombre
        print(calcul)
            
        idx_test_op += 1



