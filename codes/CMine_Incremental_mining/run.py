import os


#bmspos
#increment
for j in range(5,101,5):
	INC = str(j)
	os.system("python increment.py ../nonoverlap_gen/outputs/bmspos/bmspos_1L_0.065_0.5_0.6.csv test_out.txt ../dataset/bmspos_1L/increment_"+INC+"K.txt "+INC+" bmspos")

excel = open("./time_increment_bmspos.csv",'a')
excel.write("\n")
excel.close()

#maxOR
for j in range(10,100,10):
	maxOR = str(j/100.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/bmspos/bmspos_1L_0.065_0.5_"+maxOR+".csv test_out.txt ../dataset/bmspos_1L/increment_25K.txt 25 bmspos")


excel = open("./time_increment_bmspos.csv",'a')
excel.write("\n")
excel.close()

# minRF
for j in range(65,96,5):
	minRF = str(j/1000.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/bmspos/bmspos_1L_"+minRF+"_0.5_0.6.csv test_out.txt ../dataset/bmspos_1L/increment_25K.txt 25 bmspos")





# #cabs120k08
# #increment
for j in range(5,101,5):
	INC = str(j)
	os.system("python increment.py ../nonoverlap_gen/outputs/cabs120k08/cabs120k08_100K_0.035_0.5_0.4.csv test_out.txt ../dataset/cabs120k08/increment_"+INC+"K.txt "+INC+" cabs120k08")

excel = open("./time_increment_cabs120k08.csv",'a')
excel.write("\n")
excel.close()

#maxOR
for j in range(5,51,5):
	maxOR = str(j/100.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/cabs120k08/cabs120k08_100K_0.035_0.5_"+maxOR+".csv test_out.txt ../dataset/cabs120k08/increment_25K.txt 25 cabs120k08")

excel = open("./time_increment_cabs120k08.csv",'a')
excel.write("\n")
excel.close()

#minRF
for j in range(35,61,5):
	minRF = str(j/1000.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/cabs120k08/cabs120k08_100K_"+minRF+"_0.5_0.4.csv test_out.txt ../dataset/cabs120k08/increment_25K.txt 25 cabs120k08")





#synthetic
#increment
for j in range(5,51,5):
	INC=str(j)
	os.system("python increment.py ../nonoverlap_gen/outputs/synthetic/synthetic_50K_0.045_0.3_0.2.csv test_out.txt ../dataset/synthetic/synthetic_increment_"+INC+"K.txt "+INC+" synthetic")

excel = open("./time_increment_synthetic.csv",'a')
excel.write("\n")
excel.close()

#maxOR
for j in range(5,31,5):
	maxOR=str(j/100.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/synthetic/synthetic_50K_0.045_0.3_"+maxOR+".csv test_out.txt ../dataset/synthetic/synthetic_increment_25K.txt 25 synthetic")

excel = open("./time_increment_synthetic.csv",'a')
excel.write("\n")
excel.close()

#minRF
for j in range(401,701,25):
	minRF=str(j/10000.0)
	os.system("python increment.py ../nonoverlap_gen/outputs/synthetic/synthetic_50K_"+minRF+"_0.3_0.2.csv test_out.txt ../dataset/synthetic/synthetic_increment_25K.txt 25 synthetic")

