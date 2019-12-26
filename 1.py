from masses import masses

fuelRequired = 0

for mass in masses:
    fuelRequired += (mass // 3) - 2

print(fuelRequired)
