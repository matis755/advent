input = "152085-670283"
start = int(input.split("-")[0])
stop = int(input.split("-")[1])


listOfPasswords = []

for number in range(start, stop):
    if((int(str(number)[0]) <= int(str(number)[1])) & (int(str(number)[1]) <= int(str(number)[2])) & (int(str(number)[2]) <= int(str(number)[3])) & (int(str(number)[3]) <= int(str(number)[4])) & (int(str(number)[4]) <= int(str(number)[5]))):
        if((((int(str(number)[0]) == (int(str(number)[1])))) & (int(str(number)[1]) < (int(str(number)[2]))))|
        (((int(str(number)[1]) == (int(str(number)[2])))) & (int(str(number)[2]) < (int(str(number)[3]))) & (int(str(number)[1]) > (int(str(number)[0]))))|
        (((int(str(number)[2]) == (int(str(number)[3])))) & (int(str(number)[3]) < (int(str(number)[4]))) & (int(str(number)[2]) > (int(str(number)[1]))))|
        (((int(str(number)[3]) == (int(str(number)[4])))) & (int(str(number)[4]) < (int(str(number)[5]))) & (int(str(number)[3]) > (int(str(number)[2]))))|
        (((int(str(number)[4]) == (int(str(number)[5])))) & (int(str(number)[4]) > (int(str(number)[3]))))):
            listOfPasswords.append(number)
        
print(len(listOfPasswords))   