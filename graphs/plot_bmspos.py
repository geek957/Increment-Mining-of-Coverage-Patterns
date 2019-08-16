import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams

color = ['b','g','r','c','m','y','k','w']
markers = ['o','x','1','2','3','4']

font = {'weight': 'normal',
        'size': 24,}

rc('axes', linewidth=2)
# rc('font', weight='bold')


# def get_ratios(lines1, lines2, strt_line, end_line, incr):
# 	out = []
# 	for i in range(strt_line, end_line+1, incr):
# 		line1 = lines1[i].split(",")
# 		line2 = lines2[i].split(",")
# 		print i,line1[8],float(line2[9])
# 		out.append(round(float(line1[8])/float(line2[9]),2))
# 	return out

def get_values(lines1, lines2, strt_line, end_line, incr):
	out1 = []
	out2 = []
	for i in range(strt_line, end_line+1, incr):
		line1 = lines1[i].split(",")
		line2 = lines2[i].split(",")
		print i,line1[8],float(line2[9])
		out1.append(float(line1[8])/100.0)
		out2.append(float(line2[9])/100.0)
		# out.append(round(float(line1[8])/float(line2[9]),2))
	return out1, out2

def plot_graph(x, y, xx, xticks, yticks, title, x_label, y_label, legends, xlim, ylim, filename, legend_pos):
	# y = range(2,20,2) 
	for i in range(len(y)):
		plt.plot(x, y[i], color[i], marker=markers[i],markersize = 20, mfc='none')
	# plt.plot(x, cppg_final, 'b-',marker = 'x',markersize = 10)
	plt.legend(legends, loc = legend_pos, frameon=False, prop={'size': 24, 'weight':'normal'})
	plt.xticks(xx,xticks)
	plt.yticks(yticks)
	plt.tick_params(axis='both', which='major', labelsize=26)
	plt.tick_params(axis='both', which='minor', labelsize=26)

	# plt.label("bhvabkca")
	# plt.yticks(y,y)
	axes = plt.gca()
	axes.set_xlim(xlim)
	axes.set_ylim(ylim)
	axes.set_xlabel(x_label, fontdict = font)
	axes.set_ylabel(y_label, fontdict = font)
	# axes.set_title(title)
	plt.tight_layout()
	plt.savefig(filename, format='eps', dpi=1000)
	plt.show()

# def plot1():
# 	y_plt = []
# 	for i in range(65,100,5):
# 		minRF = i*1.0/1000
# 		lines1 = open("cmine_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		lines2 = open("cmine_increment_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		ratios = get_ratios(lines1,lines2,1,9,1)
# 		print "minRF",minRF
# 		print ratios
# 		y_plt.append(ratios)
# 	x_plt = np.arange(10,100,10)
# 	x_ticks = []
# 	for i in x_plt:
# 		x_ticks.append(i/100.0)
# 	title = "Orignial Database=100K rows,Increment=25K rows,maxOR=0.6"
# 	x_label = "minCS"
# 	y_label = "speedupratio(cmine/Increment_cmine)"
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095','minRF-0.1')
# 	legends = ('minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095')
# 	filename = "Changing_minCS.eps"
# 	plot_graph(x_plt, y_plt, x_ticks, title, x_label, y_label, legends,[1,4], filename)
# 	# for i in y_outs:
# 		# print i
# 	# print y_outs
# def plot2():
# 	y_plt = []
# 	for i in range(65,100,5):
# 		minRF = i*1.0/1000
# 		lines1 = open("cmine_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		lines2 = open("cmine_increment_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		ratios = get_ratios(lines1,lines2,1,9,1)
# 		print "minRF",minRF
# 		print ratios
# 		y_plt.append(ratios)
# 	x_plt = np.arange(10,100,10)
# 	x_ticks = []
# 	for i in x_plt:
# 		x_ticks.append(i/100.0)
# 	# title = "Orignial Database=100K rows,Increment=25K rows,minCS=0.5"
# 	title = "test.csv"
# 	x_label = "maxOR (DB = 100K, db = 25K)"
# 	y_label = "Execution time ratio"
# 	legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095')
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095','minRF-0.1')
# 	filename = "images/bmspos_maxOR.eps"
# 	plot_graph(x_plt, y_plt, x_ticks, title, x_label, y_label, legends, [10,90], [0,8], filename)

def plot2(minRF):
	y_plt = []
	lines1 = open("cmine_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	lines2 = open("cmine_increment_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	cmine,increment = get_values(lines1,lines2,1,9,1)
	print "minRF",minRF
	# print ratios
	y_plt.append(cmine)
	y_plt.append(increment)
	x_plt = np.arange(10,100,10)
	X_plt = np.arange(0,100,10)
	x_ticks = []
	for i in X_plt:
		if (i%20==0):
			x_ticks.append(i/100.0)
		else:
			x_ticks.append("")
	
	y_ticks = np.arange(0,151,40)
	title = "DB=100K rows,db=25K rows,minRF = 0.065, minCS=0.5"
	# title = "minrf = "+str(minRF)+" minCS = 0.5"
	# x_label = "maxOR (DB = 100K, db = 25K)"
	x_label = "maxOR"
	y_label = "ET ("+r'$ \times 10^2$'+")"
	legends = ('CMine','IncCMine')
	filename = "images_final/bmspos_maxOR.eps"
	plot_graph(x_plt, y_plt, X_plt, x_ticks, y_ticks, title, x_label, y_label, legends, [0,90], [0,150], filename, 2)


def plot3(minRF):
	y_plt = []
	lines1 = open("cmine_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	lines2 = open("cmine_increment_bmspos_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	cmine,increment = get_values(lines1,lines2,10,29,1)
	print cmine
	print "minRF",minRF
	y_plt.append(cmine)
	y_plt.append(increment)
	x_plt = np.arange(5,101,5)
	x_new_plt = np.arange(0,101,5)
	x_ticks = []
	for i in x_new_plt:
		if(i%20==0):
			x_ticks.append(str(i))
		else:
			x_ticks.append("")
	y_ticks= np.arange(0,26,5)
	title = "DB-100K transacions, minRF = 0.065, minCS = 0.5, maxOR = 0.6"
	# x_label = "Increment size-db (DB = 100K transactions)"
	x_label = "db ("+r'$ \times 10^3$'+")"
	x_label = r'$ \Delta $'+" ("+r'$ \times 10^3$'+")"
	y_label = "ET ("+r'$ \times 10^2$'+")"
	legends = ('CMine','IncCMine')
	filename = "images_final/bmspos_increment.eps"
	plot_graph(x_plt, y_plt, x_new_plt, x_ticks, y_ticks, title, x_label, y_label, legends, [0,100], [0, 25], filename, 1)

if (__name__=='__main__'):
	# plot1()
	plot2(0.065)
	plot3(0.065)
	# print "ralla"
