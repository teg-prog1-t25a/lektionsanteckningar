
# Summa är en ackumulator, den "samlar in"
# totala värdet av talen i loopen

# Sätt ett startvärde innan loopen
summa = 0
for tal in range(1,101):
    # Öka värdet inuti loopen
    summa += tal

print(summa)