def smaklighet(mat):
    if mat=="spenat":
        return "Äckligt"
    elif mat=="godis":
        return "Gott"
    else:
        return "Vet inte"

assert smaklighet("spenat")=="Äckligt"

mat = input("Åt du spenat eller godis idag?")
smak = smaklighet(mat)
print(smak)


