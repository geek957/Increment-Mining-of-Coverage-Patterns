import os
#bmspos
# for i in range(5,100,5):
#     minRF = i/1000.0
#     os.system("python get_DGS.py ../dataset/bmspos/bmspos_1.0L.txt ../dataset/bmspos/bmspos_1.25L.txt "+str(minRF)+" bmspos_minRF.csv "+str(minRF)+" 0.6")

# for i in range(105,201,5):
#     db = str(i/100.0)
#     os.system("python get_DGS.py ../dataset/bmspos/bmspos_1.0L.txt ../dataset/bmspos/bmspos_"+db+"L.txt 0.065 bmspos_db.csv "+str(i-100)+" 0.6")

#cabs120k08
# for i in range(5,100,5):
#     minRF = i/1000.0
#     os.system("python get_DGS.py ../dataset/cabs120k08/cabs120k08_100K.txt ../dataset/cabs120k08/cabs120k08_125K.txt "+str(minRF)+" cabs120k08_minRF.csv "+str(minRF)+" 0.4")

# for i in range(105,201,5):
#     db = str(i)
#     os.system("python get_DGS.py ../dataset/cabs120k08/cabs120k08_100K.txt ../dataset/cabs120k08/cabs120k08_"+db+"K.txt 0.035 cabs120k08_db.csv "+str(i-100)+" 0.4")

#synthetic
# for i in range(300,701,25):
#     minRF = i/10000.0
#     os.system("python get_DGS.py ../dataset/synthetic/synthetic_50K.txt ../dataset/synthetic/synthetic_75K.txt "+str(minRF)+" synthetic_minRF.csv "+str(minRF)+" 0.2")


for i in range(55,101,5):
    db = str(i)
    os.system("python get_DGS.py ../dataset/synthetic/synthetic_50K.txt ../dataset/synthetic/synthetic_"+db+"K.txt 0.045 synthetic_db.csv "+str(i-50)+" 0.2")

# kosarak
# for i in range(5,100,5):
#     minRF = i/1000.0
#     os.system("python get_DGS.py ../dataset/kosarak/kosarak_100K.txt ../dataset/kosarak/kosarak_125K.txt "+str(minRF)+" kosarak_minRF.csv "+str(minRF))

# for i in range(105,201,5):
#     db = str(i)
#     os.system("python get_DGS.py ../dataset/kosarak/kosarak_100K.txt ../dataset/kosarak/kosarak_"+db+"K.txt 0.015 kosarak_db.csv "+str(i-100))


# for i in range(5,100,5):
#     minRF = i/1000.0
#     os.system("python get_DGS.py ../dataset/synthetic/synthetic_50K.txt ../dataset/synthetic/synthetic_75K.txt "+str(minRF)+" synthetic_minRF.csv "+str(minRF))

# for i in range(55,101,5):
#     db = str(i)
#     os.system("python get_DGS.py ../dataset/synthetic/synthetic_50K.txt ../dataset/synthetic/synthetic_"+db+"K.txt 0.05 synthetic_db.csv "+str(i-50))
