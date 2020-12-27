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

#Day 4 part 2

import math
import re

f = open("/Users/shantalaika/Desktop/this.txt", "r")
allf = [ passp.replace('\n', ' ') for passp in f.read().split('\n\n')]
count = 0 
for l in allf:
    if(re.search('(^| )byr:(19[2-9][0-9]|200[0-2])( |$)', l)):
        if(re.search('(^| )iyr:(201[0-9]|2020)( |$)', l)):
            if(re.search('(^| )eyr:(202[0-9]|2030)( |$)',l)):
                if(re.search('(^| )hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)( |$)',l)):
                    if(re.search('(^| )hcl:#([a-z0-9]{6})( |$)',l)):
                        if(re.search('(^| )ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)',l)):
                            if(re.search('(^| )pid:[0-9]{9}( |$)',l)):
                                count +=1
print(count)
