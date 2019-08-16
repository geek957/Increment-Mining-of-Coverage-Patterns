import sys
import time



def scan_database(filename):
	count = 0
	f = open(filename,'r')
	out = []
	for line in f:
		count += 1
		line = line.strip('\n')
		items = line.split(',')
		if len(items[-1]) == 0:
			items.pop()
		out.append(items)
	return out,count 


if __name__ == '__main__':
	f = open(sys.argv[4],'a')
	inpfile_old = sys.argv[1]
	inpfile_new = sys.argv[2]
	minRF = float(sys.argv[3])
	maxOR = float(sys.argv[6])
	
	DB, old_db_size = scan_database(inpfile_old)
	db, new_db_size = scan_database(inpfile_new)

	# size one
	total_db_size = new_db_size
	new_flist = {}
	old_flist = {}
	for row in DB:
		for i in row:
			if i in old_flist:
				old_flist[i] += 1
			else:
				old_flist[i] = 1

	for row in db:
		for i in row:
			if i in new_flist:
				new_flist[i] += 1
			else:
				new_flist[i] = 1

	new_flist = {key:val for key, val in new_flist.items() if val>=minRF*total_db_size}
	old_flist = {key:val for key, val in old_flist.items() if val>=minRF*old_db_size}

	new_flist = sorted(new_flist.items(), key=lambda x:(-x[1], x[0]))
	old_flist = sorted(old_flist.items(), key=lambda x:(-x[1], x[0]))
	n = len(new_flist)

	# print "final",new_flist
	# print "old",old_flist
	# print "size",n

	new = []
	old = []
	for i in old_flist:
		old.append(i[0])
	for i in new_flist:
		new.append(i[0])

	print new
	print old
	ans = 0.0
	newans = 0
	deno = ((2**n)-n-1)
	# print deno

	for i in range(len(new)):
		new_set = set(new[:i])
		old_set = []
		for j in old:
			if(j!=new[i]):
				old_set.append(j)
			else:
				break
		old_set = set(old_set)
		commset = new_set.intersection(old_set)
		# print new_set,commset
		# print i,len(commset)
		val = (2**i)-(2**len(commset))
		newans += val
		# print "val",val
		ans += val*1.0/deno
		# print i,ans
	print str(sys.argv[5])+","+str(1-maxOR*ans)+","+str(int(maxOR*newans))
	f.write(str(sys.argv[5])+","+str(1-maxOR*ans)+","+str(int(maxOR*newans))+"\n")
	f.close()