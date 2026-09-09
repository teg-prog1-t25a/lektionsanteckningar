
#.Räkna från 1 till 5 och skriv ut talen
for tal in range(1,6):
    print(f"Nu är talet {tal}.")
print("Klar")

räknare = 1
# Loopa så länge ett visst villkor gäller
while räknare*räknare<1000000:
    print(räknare*räknare)
    # Det måste finnas något i loopen som kan påverkade villkoret
    räknare = räknare + 1

