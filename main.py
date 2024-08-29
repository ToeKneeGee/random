import sys
import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#print(lower_letters[0])
#print(lower_letters[25])
#sys.exit()

print(lower_letters[0])
print(lower_letters.index("z"))
print(lower_letters[0:3])

for l in range(1,100):
  randnum = random.randint(0,25)
  lower_letter = lower_letters[randnum]
  print(f"lower_letter = {lower_letter}, loop - l = {l}, randnum = {randnum}")
  if randnum == 25:
    print(f"here is lower_letter: {lower_letter}")
    #sys.exit()

  letter = letters[random.randint(0,24)]
  if letter == "Z":
    print(letter)
    print(letter.index[z])

randnum = random.randint(0,3)
print(randnum)
randnum = random.randint(0,3)
print(randnum)
randnum = random.randint(0,3)
print(randnum)
randnum = random.randint(0,3)
print(randnum)
randnum = random.randint(0,3)
print(randnum)
