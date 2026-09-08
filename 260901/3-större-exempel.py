# Inmatning med input
# Typkonvertering från sträng till heltal med int()
year = int(input("Vilket år är du född? "))

# Logiska jämförelseoperatorer i Python: == <= >= !=   <   >

# == två likhetstecken används för likhet vid jämförelser
if year==2008:
    month = int(input("Vilken månad är du född? "))
    if month==9:
        print("Du får kanske rösta")
    elif month<9:
        # Elif körs enbart om inte något tidigare alternativt varit sant
        print("Du får rösta")
    else:
        # Else-alternativet utförs då INGET alternativ varit sant
        print("Du får inte rösta")
elif year<2008:
    print("Du får rösta i höst!")
else:
    print("Du får inte rösta!")

