from input import integers

integers[1] = 65
integers[2] = 33

for i in range(0, len(integers)//4):
    if(integers[4*i] == 1):
        integers[integers[4*i+3]] = integers[integers[4*i+1]] + integers[integers[4*i+2]]
    elif(integers[4*i] == 2):
        integers[integers[4*i+3]] = integers[integers[4*i+1]] * integers[integers[4*i+2]]
    elif(integers[4*i] == 99):
        break;

print(integers)
