# Konkatenera strängar
namn = "Michael Sebastian Hemph"
ålder = 51
min_sträng = namn + " är " + str(ålder)
min_sträng = f"{namn} är {ålder}"

# Använda index och slices för att ta delar av
# och vända på strängar
print(min_sträng[12])
print(min_sträng[12:18])
print(min_sträng[:-5:-1])

# Använd metoder (ungefär funktioner) för att göra
# t ex en ny sträng men med bara små bokstäver
print(namn.lower())
print(namn)
namn = namn.lower()
print(namn)

# Räkna tecken i en sträng
print(len(namn))

# Loopa igenom strängen
# Skriv ut ordet med komma mellan bokstäverna
for idx in range(len(namn)):
    # Lägger vi till end="" i print så får vi
    # ingen automatisk ny rad
    print(f"{idx}, ", end="")

# Vi kan göra en ny rad genom en tom print()
print()

# Definiera en sträng med alla vokaler
vokaler = "aeiouåäö"

# Loopa igenom indexet för varje bokstav i namnet
for index in range(len(namn)):
    # Kolla om bokstaven på den platsen finns bland vokalerna
    if namn[index] in vokaler:
        print(f"{namn[index]} är en vokal")
    else:
        print(f"{namn[index]} är en konsonant") 

# Om vi vill göra ett hänga gubbe-spel behöver vi ett
# hemligt ord
hemligt_ord = "programmering"

# Kontrollera om en (ny) gissning ingår i ordet
gissning = "a"
# in kollar om den första strängen finns i den andra
if gissning in hemligt_ord:
    print("Bokstaven finns med i ordet")

# Ta en sträng med alla gissade bokstäver
gissade_bokstäver = "rgm"
# Hur skriver vi nu ut det "maskade" ordet, dvs
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

