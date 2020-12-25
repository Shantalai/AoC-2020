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

#day 3

import math
f = open("/Users/shantalaika/Desktop/this.txt", "r")
inp = [line.rstrip() for line in f]

i = 0
c = 0
for x in inp:
    l = len(x)
    if i >= l:
        i -= l
    if (x[i] == '#'):
            c += 1
    i += 3

print("Solution : ", c)

import math
f = open("/Users/shantalaika/Desktop/this.txt", "r")
inp = [line.rstrip() for line in f]
slopes = [1,3,5,7]
count = 0
total = 1
linecount = 0 
countlist = []
for slope in slopes:
    i = 0
    count = 0
    for x in inp:
        l = len(x)
        if i >= l:
            i -= l
        if (x[i] == '#'):
            count += 1
        i += slope
    countlist.append(count)
    total *= count
    print(count,countlist)
count = 0
i =0 
for x in inp:
    linecount += 1
    if linecount % 2 == 0:
        l = len(x)
        if i >= l:
            i -= l
        if (x[i] == '#'):
            count += 1
        i += 1
countlist.append(count)
total *= count
print(count, countlist) 
print("Solution : ", total)

