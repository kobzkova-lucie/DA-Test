import statistics

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

vitezna_aktivita = statistics.mode(votes)
print(vitezna_aktivita)