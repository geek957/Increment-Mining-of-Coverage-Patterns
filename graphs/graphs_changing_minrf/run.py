import os

data = ['bmspos','cabs120k08','synthetic']

for i in data:
    os.system("python plot_"+i+"_cnd.py")
    os.system("python plot_"+i+".py")
