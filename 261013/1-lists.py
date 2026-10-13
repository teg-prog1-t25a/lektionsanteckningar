namn = "Micke är bäst i världen"

def maskera_ord(ord):
    maskat_ord = ""
    for bokstav in ord:
        # print(bokstav, end="")
        if bokstav==" ":
            maskat_ord = maskat_ord + " "
        elif bokstav=="ä":
            maskat_ord = maskat_ord + bokstav
        else:
            maskat_ord = maskat_ord + "_"
    return maskat_ord

print(namn)
hemliga_ordet = maskera_ord(namn)
print(hemliga_ordet)


