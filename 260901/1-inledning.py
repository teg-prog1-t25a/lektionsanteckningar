# Print är en funktion som vi skickar in strängen "Hello, World!" till
print("Hello, World!")

# Olika variabler med olika datatyp
heltal = 10
decimaltal = 3.14
idag_är_det_helg = False

# Input väntar på inmatning från användaren
namn = input("Vad heter du? ")
print(f"Mitt favorittal är {decimaltal} och jag heter {namn}.")

# Sätta ihop strängar
dubbelnamn = namn + "-" + namn
print(f"Du skulle kunna heta {dubbelnamn}!")

# Inmatning med input ger strängar
ålder_str = input("Hur gammal är du? ")
tid_str = input("Hur lång tid passerar? ")

# Typkonvertering - input ger en sträng men vi vill räkna med tal
ålder = int(ålder_str)
tid = int(tid_str)

ålder_senare = ålder + tid
print(f"Om {tid} år är du {ålder_senare} år gammal.")

# Vi kan konvertera till andra datatyper
# Ett tal (eller annat) till en sträng
ålder_senare_str = str(ålder_senare)
# Ett sträng till ett decimaltal
decimaltal = float("3.14")

# Det går att nästla funktioner
ålder = int(input("Hur gammal är du?"))

