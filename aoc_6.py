#advent of code

#Day 6

with open("aoc_input_6.txt") as file:
   data = file.read()

#data = 'ababababababcdababababab'

stringLength = 14
currentChars = ['-'] * (stringLength - 1)
filledNdx = 0
res = 0

for char in data:
    res = res + 1
    if filledNdx == 0:
        currentChars[0] = char
        filledNdx = filledNdx + 1
        continue
    
    if char in currentChars:
        charLoc = currentChars.index(char)
        currentChars = currentChars[charLoc + 1:] + ['-']  * (charLoc + 1)
        filledNdx = filledNdx - charLoc
        currentChars[filledNdx - 1] = char
    else:
       if filledNdx < stringLength - 1:
           currentChars[filledNdx] = char
           filledNdx = filledNdx + 1
       else:
           print(char)
           break
           
print(currentChars) 
print(res)
          