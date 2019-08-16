import os

# #bmspos
# #increment
# for j in range(105,201,5):
# 	size = str(j/100.0)
# 	os.system("python cmine_new.py 0.065 0.5 0.6 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_final_"+size+"L.txt ./ bmspos")

# excel = open("./times_final_bmspos.csv",'a')
# excel.write("\n")
# excel.close()

# #maxOR
# for j in range(10,100,10):
# 	maxOR = str(j/100.0)
# 	os.system("python cmine_new.py 0.065 0.5 "+maxOR+" ../dataset/bmspos/bmspos_1.25L.txt bmspos_final_1.25L.txt ./ bmspos")

# excel = open("./times_final_bmspos.csv",'a')
# excel.write("\n")
# excel.close()

# #minRF
# for j in range(65,96,5):
# 	minRF = str(j/1000.0)
# 	os.system("python cmine_new.py "+minRF+" 0.5 0.6 ../dataset/bmspos/bmspos_1.25L.txt bmspos_final_1.25L.txt ./ bmspos")


# #cabs120k08
# #increment
# for j in range(105,201,5):
# 	size = str(j)
# 	os.system("python cmine_new.py 0.035 0.5 0.4 ../dataset/cabs120k08/cabs120k08_"+size+"K.txt cabs120k08_final_"+size+"K.txt ./ cabs120k08")

# excel = open("./times_final_cabs120k08.csv",'a')
# excel.write("\n")
# excel.close()

# #maxOR
# for j in range(5,51,5):
# 	maxOR = str(j/100.0)
# 	os.system("python cmine_new.py 0.035 0.5 "+maxOR+" ../dataset/cabs120k08/cabs120k08_125K.txt cabs120k08_final_125K.txt ./ cabs120k08")

# excel = open("./times_final_cabs120k08.csv",'a')
# excel.write("\n")
# excel.close()

# #minRF
# for j in range(35,61,5):
# 	minRF = str(j/1000.0)
# 	os.system("python cmine_new.py "+minRF+" 0.5 0.4 ../dataset/cabs120k08/cabs120k08_125K.txt cabs120k08_final_125K.txt ./ cabs120k08")


#synthetic
#increment
# for j in range(55,101,5):
# 	size=str(j)
# 	os.system("python cmine_new.py 0.045 0.3 0.2 ../dataset/synthetic/synthetic_"+size+"K.txt synthetic_"+size+"K.txt ./ synthetic")

# excel = open("./times_final_synthetic.csv",'a')
# excel.write("\n")
# excel.close()

# #maxOR
# for j in range(5,31,5):
# 	maxOR=str(j/100.0)
# 	os.system("python cmine_new.py 0.045 0.3 "+maxOR+" ../dataset/synthetic/synthetic_75K.txt synthetic_75K.txt ./ synthetic")

# excel = open("./times_final_synthetic.csv",'a')
# excel.write("\n")
# excel.close()

#minRF
for j in range(625,701,25):
	minRF=str(j/10000.0)
	os.system("python cmine_new.py "+minRF+" 0.3 0.2 ../dataset/synthetic/synthetic_75K.txt synthetic_75K.txt ./ synthetic")


# for i in range(65,100,5):
# 	minRF = str(i*1.0/1000)
# 	# for j in range(10,100,10):
# 	# 	maxOR = str(j/100.0)
# 	# 	os.system("python cmine_new.py "+minRF+" 0.5 "+maxOR+" ../dataset/bmspos/bmspos_1.25L.txt bmspos_1.25L.txt ./")
# 	for j in range(105,201,5):
# 		size=str(j/100.0)
# 		os.system("python cmine_new.py "+minRF+" 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_final_"+size+"L.txt ./")
# 		#os.system("python cmine_new.py "+minRF+" 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_final_"+size+"L.txt ./")

# 	excel = open("./times_final_bmspos.csv",'a')
# 	excel.write("\n")
# 	excel.close()

# for i in range(425,701,25):
# 	minRF = str(i*1.0/10000)
# 	for j in range(5,31,5):
# 		maxOR = str(j/100.0)
# 		os.system("python cmine_new.py "+minRF+" 0.3 "+maxOR+" ../dataset/synthetic/synthetic_75K.txt synthetic_75K.txt ./")
# 	for j in range(55,101,5):
# 		size=str(j)
# 		os.system("python cmine_new.py "+minRF+" 0.3 0.2 ../dataset/synthetic/synthetic_"+size+"K.txt synthetic_"+size+"K.txt ./")
# 		#os.system("python cmine_new.py "+minRF+" 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_final_"+size+"L.txt ./")

# 	excel = open("./times_final_synthetic.csv",'a')
# 	excel.write("\n")
# 	excel.close()


# for i in range(325,580,50):
# 	minRF = str(i*1.0/10000)
# 	for j in range(25,210,25):
# 		maxOR = str(j/1000.0)
# 		print "minRF",minRF,"maxOR",maxOR
# 		os.system("python cmine_new.py "+minRF+" 0.25 "+maxOR+" ../dataset/T10I4D100K/synthetic_75K.txt final_synthetic_out.txt ./")
# 	for j in range(50,101,5):
# 		size=str(j)
# 		print "minRF",minRF,"size",size
# 		os.system("python cmine_new.py "+minRF+" 0.25 0.1 ../dataset/T10I4D100K/synthetic_"+size+"K.txt final_out.txt ./")

# 	excel = open("./times_final_synthetic.csv",'a')
# 	excel.write("\n")
# 	excel.close()

# for k in range(450,701,25):
# 	minRF = str(k/10000.0)
# 	print "minRF",minRF
# 	for i in range(5,31,5):
# 		maxOR = str(i/100.0)
# 		print "maxOR",maxOR
# 		os.system("python cmine_new.py "+minRF+" 0.5 "+maxOR+"  ../dataset/T10I4D100K/synthetic_75K.txt synthetic_75K.txt ./")
# 	for i in range(50,101,5):
# 		size = str(i)
# 		print "size",size
# 		os.system("python cmine_new.py "+minRF+" 0.5 0.7 ../dataset/T10I4D100K/synthetic_"+size+"K.txt synthetic_new_"+size+"K.txt ./")

# 0.09
# for i in range(10,100,10):
# 	maxOR = str(i/100.0)
# 	os.system("python cmine_new.py 0.09 0.5 "+maxOR+"  ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(10,100,10):
# 	minCS = str(i/100.0)
# 	os.system("python cmine_new.py 0.09 "+minCS+" 0.7 ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(5,101,5):
# 	size = str((i+100)/100.0)
# 	print size
# 	os.system("python cmine_new.py 0.09 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_new_"+size+"L.txt ./")

# # 0.095
# for i in range(10,100,10):
# 	maxOR = str(i/100.0)
# 	os.system("python cmine_new.py 0.095 0.5 "+maxOR+"  ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(10,100,10):
# 	minCS = str(i/100.0)
# 	os.system("python cmine_new.py 0.095 "+minCS+" 0.7 ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(5,101,5):
# 	size = str((i+100)/100.0)
# 	print size
# 	os.system("python cmine_new.py 0.095 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_new_"+size+"L.txt ./")

# # 0.1
# for i in range(10,100,10):
# 	maxOR = str(i/100.0)
# 	os.system("python cmine_new.py 0.1 0.5 "+maxOR+"  ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(10,100,10):
# 	minCS = str(i/100.0)
# 	os.system("python cmine_new.py 0.1 "+minCS+" 0.7 ../dataset/bmspos/bmspos_1.25L.txt bmspos_new_1.25L.txt ./")

# for i in range(5,101,5):
# 	size = str((i+100)/100.0)
# 	print size
# 	os.system("python cmine_new.py 0.1 0.5 0.7 ../dataset/bmspos/bmspos_"+size+"L.txt bmspos_new_"+size+"L.txt ./")	
