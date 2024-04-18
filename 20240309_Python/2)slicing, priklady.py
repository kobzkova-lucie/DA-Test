import statistics

from audioop import avg


pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])

print(pohyby[2:])

print(len(pohyby))

print(max(pohyby), min(pohyby))

print(sum(pohyby))



S = [1,2,3,4,5,6,7,8,9,10]
print(statistics.mean(S))

range_S = max(S) - min(S)
print(f"Rozpětí: {range_S}")

