#day 1

import math

f = open("/Users/shantalaika/Desktop/this.txt", "r")
count = 1
lines = f.readlines()
for line in lines:
    num = int(line.rstrip())
    print("Checking num ", num," count ", count)
    for x in lines[count:]:
        print("Check X ", x.rstrip())
        if num+int(x.rstrip()) == 2020:
            print("Found sum", num, x.rstrip())
            print("mult ",num*int(x.rstrip()))
            break
    else:
        count = count+1
        continue
        
    break
    
#day 2 part 1
import math

f = open("/Users/shantalaika/Desktop/this.txt", "r")
count = 0
#lines = f.readlines()
for line in f:
    passList = line.split()
    limits = passList[0].split("-")
    letter = passList[1][:1]
    counter = passList[2].count(letter)
    if int(limits[0])<= counter <= int(limits[1]):
        count = count + 1

print(count)

#day 2 part 2

import math
f = open("/Users/shantalaika/Desktop/this.txt", "r")
count = 0
#lines = f.readlines()
for line in f:
    passList = line.split()
    limits = passList[0].split("-")
    letter = passList[1][:1]
    word = passList[2]
    if word[int(limits[0])-1] == letter:
        if word[int(limits[1])-1] != letter:
            count = count + 1
    elif word[int(limits[1])-1] == letter:
        count = count + 1
print(count)
