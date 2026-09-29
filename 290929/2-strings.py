string1 = "Hejsan"
string2 = "Micke"

# Konkatenerar strängar (string concatenation)
greeting = string1 + string2
print(greeting)

greeting = string1 + " " + string2
print(greeting)

greeting = f"{string1} {string2}!"
print(greeting)

namn = "Michael Hemph"
print(namn[1]) # Index 1 betyder 2:a tecknet. Börjar räkna på 0.
print(namn[2])
print(namn[3])
print(namn[-1]) # Första tecknet från slutet

length = len(namn)

for index in range(length-1,-1,-1):
    print(namn[index], end="")

print()

# En slice (en bit) av en sträng
print(namn[4:10]) # Femte till tionde bokstaven
print(namn[4:99]) # Femte till 99:onde (om den finns, inget fel)
print(namn[1:]) # Från andra bokstaven till slutet
print(namn[:4]) # Från början till bokstav 4

början = namn[:3]

förnamn = "Michael"
efternamn = "Hemph"

email = förnamn[:3] + efternamn[:3] + "@gmail.com"
print(email)


# Svårare, parametrarna fungerar som i range
print(namn[2:12:2]) # 2 steg i taget 
print(namn[12:2:-2]) # 2 steg bakåt i taget
# Från den andra bokstaven från slutet,
# till den åttonde bokstaven från slutet,
# ett steg i taget baklänges
print(namn[-2:-8:-1])
print(namn[::-1])

reversed = namn[::-1]

# Funktioner, t ex
# len() returnerar längden

# Metoder - ungefär funktioner, men anropas annorlunda
uppernamn = namn.upper()
print(uppernamn)
print(uppernamn[0].upper() + uppernamn[1:].lower())

# .upper() ger stora bokstäver (versaler)
# .lower() ger små (gemener)
# .strip() tar bort blanka tecken i början och slutet
print("    Micke     ".strip());
namn = input("Mata in ditt namn: ")
# Ta bort blanktecken och gör små bokstäver före jämförelse
if (namn.strip().lower()=="micke"):
    print("Hej")

# "micke".replace("mi", "xx") Ersätter mi med xx

hemligtord = "programmering"
bokstav = input("Mata in bokstav")

# in ger True om en sträng finns i en annan
print("x" in "Lax")
if bokstav.strip().lower() in hemligtord:
    print("Bokstaven finns i ordet!")









