venecky = [1, 2, 4, 1, 6, 0, 1]

print(sum(venecky[:5]))
print(sum(venecky[5:]))

print(len(venecky[:5]))
print(len(venecky[5:]))

print(sorted(venecky))


jmeno = "Lucie" + " " + "Kobzikova"
print(jmeno[:5])
print(jmeno[6:])
print(jmeno[-3:])
print(len(jmeno))

inzerat = "Na této pracovní pozici budete využívat Python a SQL"
if "Python" in inzerat:
    print("Je to pro mě!")