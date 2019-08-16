import sys
import os


minimum =  202776

for i in range(0,200000+1,20000):
    lines = minimum + i
    f = open(sys.argv[1],'r')
    size = 200 + (i/1000)
    fout = open(sys.argv[2]+"cabs120k08_"+str(size)+"K.txt",'w')
    count = 0
    for line in f:
        fout.write(line)
        count += 1
        if count >= lines:
            break
    fout.close()
    f.close()
