import re
import sys
import os
from operator import itemgetter
# import numpy as np

allpatterns = []

def compar(s1,s2):
    return len(s1[0])-len(s2[0])   

class cppg:
    def __init__(self, inputfile, outputfile, nonoverlap_file, minRF, minCS, maxOR):
        self.minRF = minRF
        self.minCS = minCS
        self.maxOR = maxOR
        self.fp = open(outputfile,'a')
        self.fout = open(nonoverlap_file,'w')
        self.cnt = 0
        self.dataset = dict()
        self.nots = int(self.getlines(inputfile))
        #print self.nots
        [self.items] = self.dbscan(inputfile)

        sorteditems = sorted(self.items.items(), key = lambda a: (-a[1],a[0]))
        mintracs = self.minRF * 1.0 * self.nots
        freqitems = filter(lambda x: (x[1] >= mintracs), sorteditems)
        self.fp.write("freqent_items,"+str(freqitems)+"\n")
        one_size_coverage = filter(lambda x: (x[1] >= minCS*self.nots),freqitems)
        one_size_coverage = map(lambda x:x[0],one_size_coverage)
        #print map(lambda x: list([x[0],x[1]*1.0/self.nots]), freqitems)
        self.freqitems = map(lambda x: x[0], freqitems)
        #print self.freqitems
        # self.fp.write("freqent_items,"+str(freqitems)+"\n")
        # freqitems = singleton frquent items [b,a,c,..]
        print "frequent items:",self.freqitems
        f = open(inputfile, 'r')
        counter = 0
        for i in f:
            counter += 1
            i = i.rstrip('\n')
            l = i.split(",")
            if len(l[-1]) == 0:
                l.pop()
            l = filter(lambda x: (self.items[x] >= mintracs), l)
            l.sort(key = lambda x: (-self.items[x],x))
            if(len(l)) > 0:
                self.dataset[counter] = l
        f.close()
        #print self.dataset


    def compar(s1,s2):
        return len(s1[0])-len(s2[0])    

    def dbscan(self, db):
        f = open(db, 'r')
        a = {}
        counter = 0
        for i in f:
            counter += 1
            i = i.rstrip('\n')
            # print i
            x = i.split(',')
            if len(x[-1]) == 0:
                x.pop()
            # print x
            for j in x:
                if a.has_key(j):
                    a[j] += 1
                else:
                    a[j] = 1

        #bitpattern[-1]=bitpattern[self.nots-1]
        #bitpattern[self.nots]=bitpattern[0]
        return [a]

    def getlines(self,filename):
        with open(filename,"r") as f:
            return sum(1 for _ in f)

    def getcoveragepatterns(self):
        global allpatterns
        count=0
        datasetx = {}
        for key in self.dataset.iterkeys():
            datasetx[key] = 0
        for item in self.freqitems:
            global allpatterns
            print "item",item
            coverage_set = self.get_coverage_set(item)
            projds = self.noProjection(datasetx, [item])
            count += 1
            self.cppgrec([item],coverage_set, 1, projds)
            del projds
        self.fp.close()
        output = sorted(allpatterns,cmp=compar)
        for i in output:
            self.fout.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+"\n")   
        self.fout.close()

        print "patternschecked:",self.cnt

    def get_coverage_set(self,item):
        cov_set=set()
        for key, value in self.dataset.iteritems():
            if item in self.dataset[key]:
                cov_set.add(key)
        return cov_set

    def noProjection(self, datasetx, pattern):
        projdataset = dict()
        item = pattern[-1]

        for key, value in datasetx.iteritems():
            patternset = set(pattern)
            inputpattern = self.dataset[key][value:]
            if set(inputpattern).isdisjoint(patternset):
                index = value
                itemindex = self.freqitems.index(item)
                for j in inputpattern:
                    if self.freqitems.index(j) < itemindex:
                        index += 1
                if index < len(self.dataset[key]):
                    projdataset[key] = index
        return projdataset



    def getfqs(self, ds):
        items={}
        for key, value in ds.iteritems():
            pattern = self.dataset[key][value:]
            for w in pattern:
                if not(items.has_key(w)):
                    items[w] = 1
        fqs = []
        for key,value in items.iteritems():
            fqs.append(key)
        return fqs

    # def patterntolist(self, pattern):
    #     init = np.array([0]*self.nots)
    #     for i in pattern:
    #         init = np.bitwise_or(init, self.bitpattern[i])
    #     return init

    def cppgrec(self, pattern, coverage_set,length, projds):
        global allpatterns
        fqs = self.getfqs(projds)
        # print fqs
        fqs.sort(key=lambda x: self.freqitems.index(x))
        # print "pattern",pattern,fqs
        for i in fqs:
            # print i
            newpattern = pattern + [i]
            cov_set = self.get_coverage_set(i)
            self.cnt += 1
            # print newpattern
            # print "newpattern",newpattern,"\n"
            ovr_deno = cov_set
            ovr_nume = coverage_set.intersection(cov_set)
            # print newpattern,coverage_set,cov_set
            ovratio = len(ovr_nume)*1.0/len(ovr_deno)
            cs_nume = coverage_set.union(cov_set)
            if ovratio > self.maxOR:
                # self.fout.write(str(newpattern)+","+str(len(cs_nume))+","+str(self.nots)+","+str(len(ovr_nume))+","+str(len(ovr_deno))+",0\n")
                continue
            
            allpatterns.append([newpattern,len(cs_nume),self.nots,len(ovr_nume),len(ovr_deno)])            
            # self.fout.write(str(newpattern)+","+str(len(cs_nume))+","+str(self.nots)+","+str(len(ovr_nume))+","+str(len(ovr_deno))+"\n")
            newprojds = self.noProjection(projds, newpattern)
            self.cppgrec(newpattern, cov_set.union(coverage_set),length+1, newprojds)
            del newprojds
