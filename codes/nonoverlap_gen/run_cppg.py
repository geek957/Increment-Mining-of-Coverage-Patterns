import sys
import time
import cppg

t1=time.time()


#minrf=0.1
minRF=float(sys.argv[1])

#mincs=0.1
minCS=float(sys.argv[2])

#maxor=0.025
maxOR=float(sys.argv[3])

filepath = sys.argv[5] 
# creating an objectof class cppg
inpfile = sys.argv[4]
outfile = filepath+"_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".csv"
nonoverlap_file = filepath+"_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+"_nonoverlappatterns"+".csv"
print "filename---",nonoverlap_file

f = open(outfile,'w')

f.write("file_name,"+outfile+"\n")
f.write("minRF,"+sys.argv[1]+"\n")
f.write("minCS,"+sys.argv[2]+"\n")
f.write("maxOR,"+sys.argv[3]+"\n")
f.write("input_file,"+inpfile+"\n")
f.write("filepath,../nonoverlap_gen/"+"\n")
f.write("nonoverlap_patterns,"+nonoverlap_file+"\n")
f.close()

p = cppg.cppg(inpfile,outfile,nonoverlap_file,float(minRF),float(minCS),float(maxOR))
t3 = time.time()
print "data read",str(t3-t1)
p.getcoveragepatterns()


del p
t2 = time.time()
print "process done",str(t2-t1)
