import sys
import time


def compare(s1,s2):
    for i in range(min(len(s1),len(s2))):
        if new_flist_ordered[s1[i]] < new_flist_ordered[s2[i]]:
            return -1
        elif new_flist_ordered[s1[i]] > new_flist_ordered[s2[i]]:
            return 1
    return (len(s1)-len(s2))

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

def iteration_one_new(db, old_fitems):
	new_candidates = {}
	for row in db:
		for item in row:
			if item in old_fitems:
				old_fitems[item] += 1
			else:
				if item in new_candidates:
					new_candidates[item] += 1
				else:
					new_candidates[item] = 1

	return new_candidates, old_fitems

def check_SCP(pattern, diff_set):
	for i in diff_set:
		if(i==pattern[:-1] or i==pattern[:-2]+[pattern[-1]]):
			return True
	return False

def prune_patterns(temp_patterns, NOP, new_flist_ordered, prev_NOP):
	out = []
	old_NOP = []
	diff_set = []
	for i in prev_NOP:
		if i not in NOP:
			diff_set.append(i)

	for pattern in temp_patterns:
		if pattern[0][-1] not in new_flist_ordered:
			continue

		flag3 = False
		for i in pattern[0][:-1]:
			if i not in new_flist_ordered or new_flist_ordered[i]>new_flist_ordered[pattern[0][-1]]:
				flag3 = True
				break
			# elif new_flist_ordered[i]>new_flist_ordered[pattern[0][-1]]:
			# 	falg3 = True
			# 	break 
		
		if(flag3):
			continue
		
		flag1 = True
		if(check_SCP(pattern[0],diff_set)):
			flag1 = False
			continue
		# pattern[0] = order_pattern(pattern[0], new_flist_ordered)
		pattern[0] = sorted(pattern[0], key=lambda k:new_flist_ordered[k])
		if(flag1):
			old_NOP.append(pattern[0])
			out.append([pattern[0],pattern[1],pattern[3],pattern[4]])
	return out, old_NOP

def generate_candiate(NOP, temp_winners):
	out = []
	for i in range(len(NOP)):
		for j in range(i+1,len(NOP)):
			if (NOP[i][:-1] == NOP[j][:-1]):
				new_pattern = NOP[i] + [NOP[j][-1]]
				flag1 = True
				for k in temp_winners:
					if new_pattern == k[0]:
						flag1 = False
						break
				if(flag1):
					out.append([new_pattern,0,0,0])
			else:
				break
	return out

def update_values_new(temp_winners, candidate, db, pruned_items):
	temp_db = []
	for row in db:
		for i in range(len(temp_winners)):
			flag1 = False
			for item in temp_winners[i][0][:-1]:
				if item in row:
					temp_winners[i][1] += 1
					flag1 = True
					break
			if temp_winners[i][0][-1] in row:
				temp_winners[i][3] += 1
				if(flag1):
					temp_winners[i][2] += 1
				else:
					temp_winners[i][1] += 1

		for i in range(len(candidate)):
			flag1 = False
			for item in candidate[i][0][:-1]:
				if item in row:
					candidate[i][1] += 1
					flag1 = True
					break
			if candidate[i][0][-1] in row:
				candidate[i][3] += 1
				if(flag1):
					candidate[i][2] += 1
				else:
					candidate[i][1] += 1
		row = list(set(row)-set(pruned_items))
		if(len(row)!=0):
			temp_db.append(row)
	return temp_winners, candidate, temp_db

def get_temp_winners(f_patterns,size):
	out = []
	last_pos = f_patterns.tell()
	while 1:
		line = f_patterns.readline()
		if(line == ''):
			break
		x = line.rstrip("\n")
		x = "["+x+"]"
		x = eval(x)
		if(len(x[0])!=size):
			break
		else:
			out.append(x)
		last_pos = f_patterns.tell()
	f_patterns.seek(last_pos)
	return out, f_patterns

def already_checked(pattern, old_flist_ordered):
	if pattern[-1] not in old_flist_ordered:
		return False
	for i in pattern[:-1]:
		if i not in old_flist_ordered:
			return False
		if(old_flist_ordered[i] > old_flist_ordered[pattern[-1]]):
			return False
	return True

def update_values_old(candidate, DB, pruned_items):
	temp_DB = []
	for row in DB:
		for i in range(len(candidate)):
			flag1 = False
			for item in candidate[i][0][:-1]:
				if item in row:
					candidate[i][1] += 1
					flag1 = True
					break
			if candidate[i][0][-1] in row:
				candidate[i][3] += 1
				if(flag1):
					candidate[i][2] += 1
				else:
					candidate[i][1] += 1
		row = list(set(row)-set(pruned_items))
		if(len(row)!=0):
			temp_DB.append(row)
	return candidate,temp_DB

def update_row_one(row,prune_1):
	return list(set(row)-set(prune_1))

def get_pruned_items(pruned_items, temp_winners, candidate, size):
	new_check = {}
	if size>2:
		pruned_items = []
	for pattern in temp_winners:
		for i in pattern[0][:-1]:
			if i in new_check:
				new_check[i] += 1
			else:
				new_check[i] = 1
		new_check[pattern[0][-1]] = size+2

	for pattern in candidate:
		for i in pattern[0][:-1]:
			if i in new_check:
				new_check[i] += 1
			else:
				new_check[i] = 1
		new_check[pattern[0][-1]] = size+2

	for item in new_check:
		if(new_check[item] < size-1):
			pruned_items.append(item)

	return pruned_items

if __name__ == '__main__':
	time_start = time.clock()

	info={}
	outfile = sys.argv[2]
	inpfile_new = sys.argv[3]
	increment_size = int(sys.argv[4])
	data = sys.argv[5]
	print "increment_size",increment_size

	f = open(sys.argv[1],'r')
	for i in f:
		i = i.rstrip('\n')
		i = i.split(",")
		if len(i) == 2:
			info[i[0]]=i[1]
		else:
			x=i[1]
			for k in range(2,len(i)):
				x = x+","+i[k]
			info[i[0]] = x
	# print info
	minRF = float(info['minRF'])
	minCS = float(info['minCS'])
	maxOR = float(info['maxOR'])
	old_fitems = info['freqent_items']
	filepath = info['filepath']
	old_fitems = eval(old_fitems)
	inpfile_old = filepath+info['input_file']
	nonoverlap_file = filepath+info['nonoverlap_patterns']
	outfile = "./outputs/"+data+"/"+data+"_"+str(increment_size)+"_"+str(minRF)+"_"+str(minCS)+"_"+str(maxOR)+"_"+outfile 
	print "minCS",minCS,"maxOR",maxOR,"increment_size",increment_size
	fout = open(outfile,'w')


	prev_NOP = []
	old_flist = {}
	old_flist_ordered = {}
	k = 1
	for i in old_fitems:
		old_flist[i[0]] = i[1]
		old_flist_ordered[i[0]] = k
		prev_NOP.append([i[0]])
		k += 1

	# loading databases
	DB, old_db_size = scan_database(inpfile_old)
	db, new_db_size = scan_database(inpfile_new)


	# size one
	total_db_size = old_db_size + new_db_size
	temp_candidate_1, old_fitems_updated = iteration_one_new(db, old_flist)
	new_flist = {}
	NOP = []
	CP = []
	candidate_1 = {}
	prune_1 = []


	n_cand_new = len(temp_candidate_1)
	n_cand_old = 0

	for item in old_fitems_updated:
		if (old_fitems_updated[item]>=minRF*total_db_size):
			new_flist[item] = old_fitems_updated[item]
			if(old_fitems_updated[item]>=minCS*total_db_size):
				CP.append(item)
		else:
			prune_1.append(item)
	
	for item in temp_candidate_1:
		if(temp_candidate_1[item]>=minRF*new_db_size):
			candidate_1[item] = temp_candidate_1[item]
		else:
			prune_1.append(item)

	n_cand_old += len(candidate_1)

	temp_DB = []
	for row in DB:
		row = update_row_one(row,prune_1)
		for item in candidate_1:
			if item in row:
				candidate_1[item] += 1
		if(len(row)!=0):
			temp_DB.append(row)

	DB = temp_DB
	for item in candidate_1:
		if (candidate_1[item]>=minRF*total_db_size):
			new_flist[item] = candidate_1[item]
			if(candidate_1[item]>=minCS*total_db_size):
				CP.append(item)
		else:
			prune_1.append(item)

	temp_new_flist = sorted(new_flist.items(), key=lambda x:(-x[1], x[0]))
	new_flist = {}
	new_flist_ordered = {}
	
	k = 1
	for i in temp_new_flist:
		new_flist[i[0]] = i[1]
		new_flist_ordered[i[0]] = k
		NOP.append([i[0]])
		k += 1

	f_patterns = open(nonoverlap_file,'r')
	print "old",old_flist_ordered 
	print "new",new_flist_ordered 

	print "new flist",sorted(new_flist.items(), key=lambda x:(-x[1], x[0]))
	print "old_flist",sorted(old_flist.items(), key=lambda x:(-x[1], x[0]))
	size = 2
	# greater than size 2
	pruned_items = prune_1 
	while 1:
		temp_NOP = []
		if(len(NOP) == 0):
			break
		temp_winners, f_patterns = get_temp_winners(f_patterns, size)
		temp_winners, prev_NOP = prune_patterns(temp_winners, NOP, new_flist_ordered, prev_NOP)
		candidate = generate_candiate(NOP, temp_winners)

		n_cand_new += len(candidate)
		print "temp_winners",len(temp_winners)

		pruned_items = get_pruned_items(pruned_items, candidate, temp_winners, size)

		# print "temp_winners",temp_winners
		# print "candiate",candidate
		temp_winners, temp_candidate, db = update_values_new(temp_winners, candidate, db, pruned_items)
		candidate = []

		for i in temp_winners:
			if(i[2]*1.0/i[3]*1.0 <= maxOR):
				temp_NOP.append(i[0])
				if(i[1]*1.0 >= minCS*total_db_size):
					CP.append(i[0])

		for i in temp_candidate:
			if (already_checked(i[0], old_flist_ordered) == False):
				candidate.append(i)
			elif (i[2]*1.0/i[3]*1.0 <= maxOR):
				candidate.append(i)

		n_cand_old += len(candidate)
		candidate, DB = update_values_old(candidate, DB, pruned_items)
		print len(candidate)
		for i in candidate:
			if(i[2]*1.0/i[3]*1.0 <= maxOR):
				temp_NOP.append(i[0])
				if(i[1]*1.0 >= minCS*total_db_size):
					CP.append(i[0])

		NOP = temp_NOP #sort NOP based on new flist
		NOP = sorted(NOP,cmp=compare)
		print "size",size
		# print NOP
		print "######################################################################"
		size += 1

	print "--------------------------------------------------------------------------"
	# print NOP
	print "***************************************************************************"
	# print CP

	time_end = time.clock()
	print time_end - time_start

	for i in CP:
		fout.write(str(i)+"\n")
	fout.close()

	excel = open("time_increment_"+data+".csv",'a')
	excel.write("cmine_increment,"+str(minRF)+","+str(minCS)+","+str(maxOR)+","+str(increment_size)+","+inpfile_new+","+outfile+","+str(n_cand_old)+","+str(n_cand_new)+","+str(time_end-time_start)+"\n")
	excel.close()

