# a och b är två heltal
a = 11
b = 9

# Vi kan göra en jämförelse och stoppa in svaret i en variabel
a_är_större_än_b = a>b

# Variabeln blir då booelsk (boolean/bool) med värdet True eller False
print(a_är_större_än_b)

# Ett värde som är True eller False kan styra vilken kod som körs
if a_är_större_än_b:
    print("A är större än B")

# Vi kan också göra jämförelsen direkt i if-satsen
if a>b:
    print("A är störst")
    
if b>a:
    print("B är störst")

print("Klar!")
