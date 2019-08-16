import os
for j in range(500,701,25):
	minRF = str(j/10000.0)
	print "minRF",minRF
	for i in range(5,31,5):
		maxOR = str(i/100.0)
		print "non_overlap_ratio",i/100.0
		os.system("python run_cppg.py "+minRF+" 0.3 "+maxOR+" ../dataset/T10I4D100K/synthetic_50K.txt ./outputs/synthetic/synthetic")
