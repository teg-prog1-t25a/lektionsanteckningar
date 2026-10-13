lexikon = ["Micke", "Felix", "William", "Stella", "Jovan"]
lottorad = [12, 23, 2, 5, 34, 14, 9]
vad_som_helst = ["Micke", 51, ["Sankt Paulsgatan 33A", "118 48 Stockholm"]]

for ord in lexikon:
    print(ord)

print(lexikon[3])

for ord in lexikon[1:3]:
    print(ord)

# Strängar är oföränderliga (immutable)
namn = "Micke"
namn + " Hemph" # ger en ny sträng, som vi måste stoppa in i en variable om vi vill använda den
print(namn)
namn = namn + " Hemph"
print(namn)

# Listor går att förändra (mutable)
lexikon.append("Edgar")
print("Nytt innehåll")
for ord in lexikon:
    print(ord)

# Bygga upp en lista
klassen = []
while True:
    namn = input("Ange ett namn (tomt avslutar): ")
    if namn=="":
        break
    klassen.append(namn)

print(f"Jag har {len(klassen)} vänner")

# klassen.remove("Micke")

print(f"Nu har jag {len(klassen)} vänner.")

for elev in klassen:
    print(f"{elev} är bäst")

# .append(värde) lägger till i en list
# .remove(värde) tar bort från listan
# .insert(plats, värde)

lexikon[1] = "Donald"
for ord in lexikon:
    print(ord)
