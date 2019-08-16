import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
import matplotlib.gridspec as gridspec


color = ['b','g','r','c','m','y','k','w']
markers = ['o','x','1','2','3','4']

font = {'weight': 'normal',
        'size': 24,}

rc('axes', linewidth=2)
# rc('font', weight='bold')

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
def plot_graph1(x, y, xx, xticks, yticks, title, x_label, y_label, legends, xlim, xlim2, ylim, filename, legend_pos):
	# y = range(2,20,2) 
	xlimratio = (xlim[1]-xlim[0])/(xlim2[1]-xlim2[0]+xlim[1]-xlim[0])
 	xlim2ratio = (xlim2[1]-xlim2[0])/(xlim2[1]-xlim2[0]+xlim[1]-xlim[0])
	gs = gridspec.GridSpec(1, 2, width_ratios=[xlimratio, xlim2ratio])
	fig = plt.figure()
	ax = fig.add_subplot(gs[0])
 	ax2 = fig.add_subplot(gs[1])
	for i in range(len(y)):
		ax2.plot(x, y[i], color[i], marker=markers[i],markersize = 20, mfc='none')
	# plt.plot(x, cppg_final, 'b-',marker = 'x',markersize = 10)
	ax2.legend(legends, loc = legend_pos, frameon=False, prop={'size': 24, 'weight':'normal'})
	plt.xticks(xx,xticks)
	plt.yticks(yticks)
	# ax2.set_xticklabels(xx,xticks)
	ax2.set_yticklabels([])
	# ax.set_yticklabels(yticks)
	ax2.tick_params(axis='both', which='major', labelsize=26)
	ax2.tick_params(axis='both', which='minor', labelsize=26)
	ax2.tick_params(axis='y', which='both', length=0)

	# ax.set_yticklabels(yticks)
	ax.tick_params(axis='both', which='major', labelsize=26)
	ax.tick_params(axis='both', which='minor', labelsize=26)

	plt.subplots_adjust(wspace=0)
	# plt.label("bhvabkca")
	# plt.yticks(y,y)
	# axes = plt.gca()
	ax.set_xlim(xlim)
	ax2.set_xlim(xlim2)
	ax.set_ylim(ylim)
	ax2.set_ylim(ylim)
	ax2.set_xlabel(x_label, fontdict = font)
	ax2.xaxis.set_label_coords(0.55, 0.07, transform=fig.transFigure)
	ax.set_ylabel(y_label, fontdict = font)

	ax.spines['right'].set_visible(False)
	ax2.spines['left'].set_visible(False)
	# ax.yaxis.tick_left()
	# ax.tick_params(labelright='off')
	ax2.yaxis.tick_left()


	d = .009
	kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
	ax.plot((1-d,1+d), (-d,+d), **kwargs)
	ax.plot((1-d,1+d),(1-d,1+d), **kwargs)

	kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
	ax2.plot((-d,+d), (1-d,1+d), **kwargs)
	ax2.plot((-d,+d), (-d,+d), **kwargs)

	# axes.set_title(title)
	plt.tight_layout()
	plt.savefig(filename, format='eps', dpi=1000)
	plt.show()



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


def plot1():
	y_plt = []
	lines1 = open("cabs120K08_cmine.csv",'r').readlines()
	lines2 = open("cabs120K08_increment.csv",'r').readlines()
	cmine,increment = get_values(lines1,lines2,1,6,1)
	# print ratios
	y_plt.append(cmine)
	y_plt.append(increment)
	x_plt = np.arange(35,61,5)
	X_plt = np.arange(35,61,5)
	x_ticks = []
	for i in X_plt:
		x_ticks.append(i)
	y_ticks = np.arange(0,21,5)
	title = "DB=100K rows,db=25K rows, minCS=0.5, maxOR=0.4"
	# title = "minrf = "+str(minRF)+" minCS = 0.5"
	# x_label = "minRF (DB = 100K, db = 25K)"
	x_label = "minRF ("+r'$ \times 10^{-3}$'+")"
	y_label = "NC ("+r'$ \times 10^3$'+")"
	legends = ('CMine','IncCMine')
	filename = "../images_final/cabs120k08_cnd_minRF.eps"
	plot_graph1(x_plt, y_plt, X_plt, x_ticks, y_ticks, title, x_label, y_label, legends, [0.0,5], [33,60], [0,21], filename, 1)

if (__name__=='__main__'):
	plot1()
