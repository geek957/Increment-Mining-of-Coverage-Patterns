import os

for i in range(650,951,50):
	minRF = str(i*1.0/10000)
	for j in range(10,100,10):
		maxOR = str(j/100.0) 
		os.system("python run_cppg.py "+minRF+" 0.5 "+maxOR+" ../dataset/bmspos/bmspos_250K.txt ./outputs/bmspos/bmspos_250K")

for i in range(350,601,50):
	minRF = str(i*1.0/10000)
	for j in range(5,51,5):
		maxOR = str(j/100.0)
		os.system("python run_cppg.py "+minRF+" 0.5 "+maxOR+" ../dataset/cabs120k08/cabs120k08_200K.txt ./outputs/cabs120k08/cabs120k08_200K")
