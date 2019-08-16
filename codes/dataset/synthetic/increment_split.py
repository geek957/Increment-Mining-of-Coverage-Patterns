import sys

for i in range(5,51,5):
	rows = i*1000
	f = open("shuffled.txt",'r')
	fout = open("increment_"+str(i)+"K.txt",'w')
	j = 1
	while(j<=50000+rows):
		line = f.readline()
		if(j>50000):
			fout.write(line)
		j += 1

