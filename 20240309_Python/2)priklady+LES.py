# seznam_cisel = [1,2,3,4,5,6,7,]

# soucet = 0 
# for cislo in seznam_cisel:
#     soucet = cislo + soucet

# print(soucet)

# nejvyssi_hodnota = 0
# for cislo in seznam_cisel:
#     if cislo > nejvyssi_hodnota:
#         nejvyssi_hodnota = cislo

# print(nejvyssi_hodnota)






# --------------------------------- TASK 01 ------------------------------------
# Napiš kód, který zpracuje seznam čísel a vypíše jejich součet
# (bez použití funkce sum()).
les = [4, 5, 6, 7]
kosik = 0

for houba in les:
    kosik += houba

print(kosik)

# --------------------------------- TASK 02 ------------------------------------
# Napiš kód, který zpracuje seznam čísel a vypíše největší prvek
# v tomto seznamu (bez použití funkce max()).
les = [4, 5, 78, 3, 4]
nejvyssi_strom = les[0]

for strom in les:
    if strom > nejvyssi_strom:
        nejvyssi_strom = strom

print(nejvyssi_strom)


# --------------------------------- TASK 03 ------------------------------------
# Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla
# z tohoto seznamu.
les = [4, 5, 6, 7]

for houba in les:
    if houba % 2 == 0:
        print(houba)



# --------------------------------- TASK 04 ------------------------------------
# Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam se sudými čísly
# a nový seznam s lichými čísly z původního seznamu.
les = [6, 8, 4, 55, 3, 0]
lichy_kosik = []
sudy_kosik = []

for houba in les:
    if houba % 2 == 0:
        sudy_kosik.append(houba)
    else:
        lichy_kosik.append(houba)

print(f"Sude cisla: {sudy_kosik} a liche cisla: {lichy_kosik}")

# --------------------------------- TASK 05 ------------------------------------
# Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů.
# Výsledné pořadí prvků musí být zachováno.
les = [5, 3, 5, 6, 7, 3, 7, 9]
kosik = []

for houba in les:
    if houba not in kosik:
        kosik.append(houba)

print(kosik)
