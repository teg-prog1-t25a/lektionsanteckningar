# Konkatenera strängar
namn = "Michael Sebastian Hemph"
ålder = 51
min_sträng = namn + " är " + str(ålder)
min_sträng = f"{namn} är {ålder}"

print(min_sträng[12])
print(min_sträng[12:18])
print(min_sträng[:-5:-1])

print(namn.lower())
print(namn)
namn = namn.lower()
print(namn)

print(len(namn))
# Skriver ut micke utan en ny rad efteråt
print("micke", end="")

# Skriv ut "0, 1, 2, 3," på en rad
for idx in range(4):
    print(f"{idx}, ", end="")
print()

vokaler = "aeiouåäö"
for index in range(len(namn)):
    if namn[index] in vokaler:
        print(f"{namn[index]} är en vokal")
    else:
        print(f"{namn[index]} är en konsonant") 

hemligt_ord = "programmering"
gissning = "a"
if gissning in hemligt_ord:
    print("Du gissade rätt")

gissade_bokstäver = "rgm"
# Hur skriver vi ut den "maskade" strängen, dvs
# _ r _ g r _ m m _ r _ _ g

# Förslag på uppgifter
# 1. Be användaren om gissningar och bygg upp en sträng
#    med alla gissningar hittills
# 2. Skriv ut valfritt maskat ord givet det hemliga ordet
#    och en sträng med gissade bokstäver
# 3. Gör en FUNKTION som tar ett hemligt ord och gissade
#    bokstäver och returnerar en maskad sträng 
# 4. Kontrollera om ordet är helt färdiggissat
# 5. Räkna antalet gissningar (är gubben "hängd"?)

