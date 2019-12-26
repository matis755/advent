from masses import masses

fuelRequired = 0
toAdd = 0

for mass in masses:
    toAdd = (mass // 3) - 2
    fuelRequired += toAdd

    while (toAdd > 8):
        toAdd = ((toAdd // 3) - 2)
        fuelRequired += toAdd

print(fuelRequired)
