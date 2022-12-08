#Harvey's prodject

#rock paper scisors (day 2)

with open("AOC imput 2") as file:
    data = file.read()
    

allResult = data.split('\n')
    

def startsWithA(myString):
    return myString.startswith('A')

listOfA = list(filter(startsWithA, allResult))


def startsWithB(myString):
    return myString.startswith('B')

listOfB = list(filter(startsWithB, allResult))


def startsWithC(myString):
    return myString.startswith('C')

listOfC = list(filter(startsWithC, allResult))





def endsWithX(myString):
    return myString.endswith('X')

listOfAX = list(filter(endsWithX, listOfA))


listOfBX = list(filter(endsWithX, listOfB))


listOfCX = list(filter(endsWithX, listOfC))




def endsWithY(myString):
    return myString.endswith('Y')

listOfAY = list(filter(endsWithY, listOfA))


listOfBY = list(filter(endsWithY, listOfB))


listOfCY = list(filter(endsWithY, listOfC))



def endsWithZ(myString):
    return myString.endswith('Z')

listOfAZ = list(filter(endsWithZ, listOfA))


listOfBZ = list(filter(endsWithZ, listOfB))


listOfCZ = list(filter(endsWithZ, listOfC))




#part 1

#AX = len(listOfAX) * 4

#AY = len(listOfAY) * 8

#AZ = len(listOfAZ) * 3

#BX = len(listOfBX) * 1

#BY = len(listOfBY) * 5

#BZ = len(listOfBZ) * 9

#CX = len(listOfCX) * 7

#CY = len(listOfCY) * 2

#CZ = len(listOfCZ) * 6


#part 2

#AX = len(listOfAX) * 3

#AY = len(listOfAY) * 4

#AZ = len(listOfAZ) * 8

#BX = len(listOfBX) * 1

#BY = len(listOfBY) * 5

#BZ = len(listOfBZ) * 9

#CX = len(listOfCX) * 2

#CY = len(listOfCY) * 6

#CZ = len(listOfCZ) * 7




score = AX + AY + AZ + BX + BY + BZ + CX + CY + CZ




print(score)




