import sys
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
import numpy as np

color = ['b','g','r','c','m','y','k','w']
markers = ['o','s','D','X','1','2','3','4']

font = {'weight': 'normal',
        'size': 26,}

rc('axes', linewidth=2)
# rc('font', weight='bold')



def plot_graph(x, y, xticks, y_ticks, title, x_label, y_label, xlim, ylim, filename):
    plt.plot(x, y, color[0], marker=markers[0],markersize = 20, mfc='none')
    # plt.plot(x, cppg_final, 'b-',marker = 'x',markersize = 10)
    plt.xticks(x,xticks)
    plt.yticks(y_ticks)
    plt.tick_params(axis='both', which='major', labelsize=26)
    plt.tick_params(axis='both', which='minor', labelsize=26)
    
    axes = plt.gca()
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    axes.set_xlabel(x_label, fontdict = font)
    axes.set_ylabel(y_label, fontdict = font)
    axes.set_title(title)
    plt.tight_layout()
    plt.savefig(filename, format='eps', dpi=1000)
    plt.show()

#bmspos
def plot1():
    f = open("bmspos_minRF.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1.0-float(y))*100)
    X = np.arange(65,96,5)
    # X = np.arange(300,701,25)
    x_ticks = []
    for i in X:
        if (i-5)%10==0:
            x_ticks.append(str(i))
        else:
            x_ticks.append("")
    y_ticks = np.arange(0,26,10)
    title = ""
    x_label="minRF ("+r'$ \times 10^{-3}$'+")"
    # x_label = "minRF(*10^-3)(DB=100K, db=25K, maxOR = 0.6)"
    y_label = "PAPF"
    filename = "../images_final/bmspos_dops_minRF.eps"
    print x_ticks, Y
    plot_graph(X, Y, x_ticks, y_ticks, title, x_label, y_label, [65,95], [0, 25], filename)


#cabs120k08
def plot2():
    f = open("cabs120k08_minRF.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1.0-float(y))*100)
    X = np.arange(35,61,5)
    # X = np.arange(300,701,25)
    x_ticks = []
    for i in X:
        if i%5==0:
            x_ticks.append(str(i))
        else:
            x_ticks.append("")
    y_ticks = np.arange(0,16,5)
    title = ""
    x_label="minRF ("+r'$ \times 10^{-3}$'+")"
    # x_label = "minRF(*10^-3)(DB=100K, db=25K, maxOR = 0.6)"
    y_label = "PAPF"
    filename = "../images_final/cabs120k08_dops_minRF.eps"
    print x_ticks, Y
    plot_graph(X, Y, x_ticks, y_ticks, title, x_label, y_label, [35,60], [0, 15], filename)

#synthetic
def plot3():
    f = open("synthetic_minRF.csv",'r')
    lines = f.readlines()
    X = []
    Y = []
    for i in range(1,len(lines),1):
        x = lines[i].split(",")[0]
        y = lines[i].split(",")[1]
        Y.append((1.0-float(y))*100)
    # X = np.arange(5,100,5)
    X = np.arange(450,601,25)
    x_ticks = []
    for i in X:
        if i%50==0:
            x_ticks.append(str(i))
        else:
            x_ticks.append("")
    y_ticks = np.arange(0,11,5)
    title = ""
    x_label="minRF ("+r'$ \times 10^{-4}$'+")"
    # x_label = "minRF(*10^-3)(DB=100K, db=25K, maxOR = 0.6)"
    y_label = "PAPF"
    filename = "../images_final/synthetic_dops_minRF.eps"
    print x_ticks, Y
    plot_graph(X, Y, x_ticks, y_ticks, title, x_label, y_label, [450,600], [0, 10], filename)


if (__name__=='__main__'):
    plot1()
    plot2()
    plot3()