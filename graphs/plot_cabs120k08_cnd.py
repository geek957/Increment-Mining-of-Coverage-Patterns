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
		print i,line1[7],float(line2[7])
		out1.append(float(line1[7])/1000.0)
		out2.append(float(line2[7])/1000.0)
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
# 	for i in range(35,61,5):
# 		minRF = i*1.0/1000
# 		lines1 = open("cmine_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		lines2 = open("cmine_increment_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		ratios = get_ratios(lines1,lines2,1,10,1)
# 		print "minRF",minRF
# 		print ratios
# 		y_plt.append(ratios)
# 	x_plt = np.arange(5,51,5)
# 	x_ticks = []
# 	for i in x_plt:
# 		x_ticks.append(i/100.0)
# 	# title = "Orignial Database=100K rows,Increment=25K rows,minCS=0.5"
# 	title = "test.csv"
# 	x_label = "maxOR (D = 100K, d = 25K)"
# 	y_label = "Execution time ratio"
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095')
# 	legends = ('minRF-0.035','minRF-0.04','minRF-0.045','minRF-0.05','minRF-0.055','minRF-0.06')
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095','minRF-0.1')
# 	filename = "images/cabs120k08_maxOR.eps"
# 	plot_graph(x_plt, y_plt, x_ticks, title, x_label, y_label, legends, [10,52], [0,8], filename)

def plot2(minRF):
	y_plt = []
	lines1 = open("cmine_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	lines2 = open("cmine_increment_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	cmine,increment = get_values(lines1,lines2,1,10,1)
	print "minRF",minRF
	y_plt.append(cmine)
	y_plt.append(increment)
	x_plt = np.arange(5,51,5)
	X_plt = np.arange(0,51,5)
	x_ticks = []
	for i in X_plt:
		if(i%10==0):
			x_ticks.append(i/100.0)
		else:
			x_ticks.append("")
	y_ticks = np.arange(0,21,5)
	title = "DB=100K ,db=25K, minRF=0.035, minCS=0.5"
	# title = "test.csv"
	# x_label = "maxOR (D = 100K, d = 25K)"
	x_label = "maxOR"
	y_label = "NC ("+r'$ \times 10^3$'+")"
	legends = ('CMine', 'IncCMine')
	filename = "images_final/cabs120k08_cnd_maxOR.eps"
	plot_graph(x_plt, y_plt, X_plt, x_ticks, y_ticks, title, x_label, y_label, legends, [0,50], [0,23], filename, 2)

# def plot3():
# 	y_plt = []
# 	for i in range(35,61,5):
# 		minRF = i*1.0/1000
# 		lines1 = open("cmine_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		lines2 = open("cmine_increment_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
# 		ratios = get_ratios(lines1,lines2,11,30,1)
# 		print "minRF",minRF
# 		print ratios
# 		y_plt.append(ratios)
# 	x_plt = np.arange(5,101,5)
# 	x_ticks = []
# 	for i in x_plt:
# 		x_ticks.append(str(i))
# 	# title = "Original database-100K transacions, minCS = 0.5, maxOR = 0.7"
# 	title = ""
# 	x_label = "Increment size-d (D = 100K transactions)"
# 	y_label = "Execution time ratio"
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095','minRF-0.1')
# 	# legends = ('minRF-0.065','minRF-0.07','minRF-0.075','minRF-0.08','minRF-0.085','minRF-0.09','minRF-0.095')
# 	legends = ('minRF-0.035','minRF-0.04','minRF-0.045','minRF-0.05','minRF-0.055','minRF-0.06')
# 	filename = "images/cabs120k08_increment.eps"
# 	plot_graph(x_plt, y_plt, x_ticks, title, x_label, y_label, legends, [5,101], [0, 20], filename)

def plot3(minRF):
	y_plt = []
	lines1 = open("cmine_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	lines2 = open("cmine_increment_cabs120k08_outputs/minRF_"+str(minRF)+".csv",'r').readlines()
	cmine,increment = get_values(lines1,lines2,11,30,1)
	print "minRF",minRF
	y_plt.append(cmine)
	y_plt.append(increment)
	x_plt = np.arange(5,101,5)
	X_plt = np.arange(0,101,5)
	x_ticks = []
	for i in X_plt:
		if(i%20==0):
			x_ticks.append(str(i))
		else:
			x_ticks.append("")
	y_ticks = np.arange(0,21,5)
	title = "DB-100K, minRF = 0.035, minCS = 0.5, maxOR = 0.4"
	# x_label = "Increment size-d (D = 100K transactions)"
	x_label = "db ("+r'$ \times 10^3$'+")"
	x_label = r'$ \Delta $' +" ("+r'$ \times 10^3$'+")"
	y_label = "NC ("+r'$ \times 10^3$'+")"
	legends = ('CMine','IncCMine')
	filename = "images_final/cabs120k08_cnd_increment.eps"
	plot_graph(x_plt, y_plt, X_plt, x_ticks, y_ticks, title, x_label, y_label, legends, [0,100], [0, 23], filename, 1)

if (__name__=='__main__'):
	# plot1()
	plot2(0.035)
	plot3(0.035)
	# print "ralla"
