
# Addera
def addera(tal1, tal2):
    resultat = tal1 + tal2
    return resultat

assert addera(12,13)==25
assert addera(12,-13)==-1
assert addera(0,1)==1

# Subtrahera

# Multiplicera

# Dividera

# Beräkningsfunktion
def calculate(tal1, tal2, operator):
    pass

# Huvudprogrammet
def main():
    # Mata in två tal
    a = float(input("Tal 1: "))
    b = float(input("Tal 2: "))
    # Mata in en operator
    operator = "+"

    # Beräkna resultatet
    resultat = addera(a,b)

    # Skriv ut resultatet
    print(f"Svaret blir {resultat}")

main()