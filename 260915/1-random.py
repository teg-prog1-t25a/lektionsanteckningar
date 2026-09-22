import random

# "Hej" och "Micke" är argument till funktionen print
print("Hej", "Micke")

# En seed "väljer" vilken slumpsekvens vi ska använda
# random.seed(4576)

for _ in range(5):
    # randint är en funktion i modulen random
    tärningsslag = random.randint(1,6)
    print(f"Du slog {tärningsslag}")

# Randrange väljer ett slumpmässigt tal från en range (typ)
# där argumenten som vanligt är start, slut och steglängd
udda_tal = random.randrange(5,100,25)
print(udda_tal)


antal_sexor = 0
antal_slag = 10000000
for _ in range(antal_slag):
    tärningsslag = random.randint(1,6)
    if tärningsslag==6:
        antal_sexor += 1
print(f"Antalet sexor var {antal_sexor}")