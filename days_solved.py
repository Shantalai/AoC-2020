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
