import random

area = 35

def skriv_ut_meny():
    print("Hej Micke!")
    print("Du kan välja mellan att:")
    print("Sova")
    print("Träna")
    print("Titta på TV")

def hälsa(namn, ålder):
    print(f"Hello, {namn}. You are {ålder} years old!")

def pris_med_moms(pris):
    # moms = 0.25 * pris
    # totalt_pris = pris + moms
    if pris<0:
        return 0
    else:
        return 1.25 * pris

def main():
    # Hälsa på användaren
    skriv_ut_meny()
    val = input("Vad heter du? ")
    age = input("Hur gammal är du? ")

    pris = float(input("Vad kostar en liter mjölk (utan moms)? "))
    totalpris = pris_med_moms(pris)
    print(f"Priset med moms är: {totalpris}")

    hälsa(val, age)
    hälsa(val, age)
    hälsa(val, age)

# Egendefinierade testfall
# Bra att testa olika troliga varianter
# plus "edge case" som skulle kunna vara fel
assert pris_med_moms(16)==20
assert pris_med_moms(10)==12.5
assert pris_med_moms(0)==0 # Vad händer vid 0?
assert pris_med_moms(-10)==0 # Vad händer vid negativa tal?

    
main()




