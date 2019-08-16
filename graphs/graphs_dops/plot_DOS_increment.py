import sys
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
import numpy as np


color = ['b','g','r','c','m','y','k','w']
markers = ['o','s','D','X','1','2','3','4']

font = {'weight': 'normal',
        'size': 26,}

font1= {'family':'sans-serif',}

rc('axes', linewidth=2)
# rc('font', weight='bold')



def plot_graph(x, y, xx, xticks, y_ticks, title, x_label, y_label, xlim, ylim, filename):
    plt.plot(x, y, color[0], marker=markers[0],markersize = 20, mfc='none')
    # plt.plot(x, cppg_final, 'b-',marker = 'x',markersize = 10)
    plt.xticks(xx,xticks)
    plt.yticks(y_ticks)
    plt.tick_params(axis='both', which='major', labelsize=26)
    plt.tick_params(axis='both', which='minor', labelsize=26)
    
    axes = plt.gca()
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    axes.set_xlabel(x_label, fontdict = font)
    # axes.set_ylabel(y_label, fontdict = font)
    axes.set_ylabel(r'$\Psi$', fontdict = font1)
    axes.set_title(title)
    # plt.tight_layout(pad=5, w_pad=10, h_pad=10)
    plt.tight_layout()
    plt.savefig(filename, format='eps', dpi=1000)
    plt.show()


#bmspos
def plot1():
    f = open("bmspos_db.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1-float(y))*100)
    X = np.arange(5,101,5)
    XX = np.arange(0,101,5)
    print X
    print Y
    x_ticks = []
    for i in XX:
		if(i%20==0):
			x_ticks.append(str(i))
		else:
			x_ticks.append("")
    print x_ticks
    y_ticks = np.arange(0,21,5)
    title = ""
    # x_label = "db ("+r'$ \times 10^3$'+")"
    x_label = r'$ \Delta $'+" ("+r'$ \times 10^3$'+")"		    
    y_label = r'$ \Psi $'
    filename = "../images_final/bmspos_dops_db.eps"
    plot_graph(X, Y, XX, x_ticks, y_ticks, title, x_label, y_label, [0,100], [0, 20], filename)

#cabs120k08
def plot2():
    f = open("cabs120k08_db.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1-float(y))*100)
    X = np.arange(5,101,5)
    XX = np.arange(0,101,5)
    print X
    print Y
    x_ticks = []
    for i in XX:
		if(i%20==0):
			x_ticks.append(str(i))
		else:
			x_ticks.append("")
    print x_ticks
    y_ticks = np.arange(0,16,5)
    title = ""
    x_label = "db ("+r'$ \times 10^3$'+")"
    x_label = r'$ \Delta $'+" ("+r'$ \times 10^3$'+")"		
    y_label = r'$ \Psi $'
    filename = "../images_final/cabs120k08_dops_db.eps"
    plot_graph(X, Y, XX, x_ticks, y_ticks, title, x_label, y_label, [0,100], [0, 15], filename)

#synthetic
def plot3():
    f = open("synthetic_db.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1-float(y))*100)
    X = np.arange(5,51,5)
    XX = np.arange(0,51,5)
    print X
    print Y
    x_ticks = []
    for i in XX:
        if(i%10==0):
            x_ticks.append(str(i))
        else:
            x_ticks.append("")
    print x_ticks
    y_ticks = np.arange(0,11,5)
    title = ""
    x_label = "db ("+r'$ \times 10^3$'+")"
    x_label = r'$ \Delta $'+" ("+r'$ \times 10^3$'+")"		
    y_label = r'$ \Psi $'
    filename = "../images_final/synthetic_dops_db.eps"
    plot_graph(X, Y, XX, x_ticks, y_ticks, title, x_label, y_label, [0,50], [0, 10], filename)

if (__name__=='__main__'):
    plot1()
    plot2()
    plot3()