import pandas as pd
import sys


# cmine = pd.read_csv(sys.argv[1], chunksize=1, sep=',', dtype=None)
print sys.argv[1]
f = open(sys.argv[1],'r')
lines = f.readlines()
# cmine_increment = pd.read_csv("cmine_increment.csv", sep=',', dtype=None)
# cppg = pd.read_csv("cppg.csv", sep=',',  dtype=None)
# cppg_increment = pd.read_csv("cppg_increment.csv", sep=',',  dtype=None)

dct = {}
for i in range(400,701,25):
	minRF = i/10000.0
	f = open(sys.argv[2]+"minRF_"+str(minRF)+".csv",'w')
	f.write(lines[0])
	dct[str(minRF)] = f



for i in range(1,len(lines)):
	line = lines[i]
	print i, line
	if line=="\n":
		continue
	split = line.split(',')
	# print split[1]
	if split[1]=='':
		continue
	# dct[str(0.075)].write("helloi")
	dct[str(split[1])].write(line)
	# print lines[i]

for i in dct:
	dct[i].close()