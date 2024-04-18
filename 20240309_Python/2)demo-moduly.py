# Author: Adela Bierska

import math
from math import floor, ceil
import statistics

print(math.floor(8.6))
print(ceil(3.1))

print(statistics.mean([1, 2, 3, 4, 5, 6]))
print(statistics.median([1, 2, 3, 4, 5, 6]))


# --------------------------------- TASK 01 ------------------------------------
# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše
# toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným
# Pythonovským zaokrouhlováním.

user_input = float(input("Zadej desetinne cislo: "))

print(math.ceil(user_input))
print(math.floor(user_input))
print(round(user_input))


# ------------------------------ BONUS TASK 02 ---------------------------------
# Uvažujme vysvědčení studenta, které máme uložené jako seznam:
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru.
# Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk,
# matematika a fyzika. Vypočítej průměr studenta z daných předmětů s využitím
# modulu statstics. Na začátku vytvoř prázdný seznam a následně pomocí cyklu
# vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů. Nakonec použij
# metodu statistics.mean() k výpočtu průměru. Dále zkus využít funkce, které
# jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů.

subjects = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
marks = []

for subject_mark in school_report:
    if subject_mark[0] in subjects:
        marks.append(subject_mark[1])

marks_mean = statistics.mean(marks)
print(f"Prumer: {marks_mean}")


# ------------------------------ BONUS TASK 03 ---------------------------------
# Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu
# v datech. V modulu statistics existuje funkce mode(), která umí modus
# spočítat. Funkce mode() má navíc vychytávku, umí pracovat i s řetězci.

votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
]

# Můžeš se podívat i na popis funkce v dokumentaci,
# která obsahuje i příklad s použitím řetězců.
