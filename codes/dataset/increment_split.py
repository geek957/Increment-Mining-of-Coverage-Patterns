import sys

startline  = 202776
for i in range(0,200000+1,20000):
	f = open(sys.argv[1],'r')
	fout = open(sys.argv[2]+"Increment_"+str((i)/1000)+"K.txt",'w')
	cnt = 0
	while cnt < startline:
		x = f.readline()
		# fout.write(x)
		cnt += 1
	while cnt < startline+i:
		x = f.readline()
		fout.write(x)
		cnt += 1
	fout.close()
	f.close()
