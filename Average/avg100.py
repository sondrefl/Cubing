import matplotlib.pyplot as plt
from math import ceil
import numpy as np
import sys

def extract_times(filename, cube=0):
    """
    extract times the cstimer export file, and collect them in a list
    """
    infile = open(filename,'r')
    data = infile.readlines()

    times = []
    for line in data:
        Type = line.split("[[")
        for i in Type:
            if i[0] == '[':
                i = i[1:]
            if i[0] == '0' and i[6] == ']':
                """for solves with four digits numbers"""
                j = int(i[2:6]) / 1000
                #print(j)
                times.append(j)
            elif i[0] == '0' and i[7] == ']':
                """for solves with five digits numbers"""
                j = int(i[2:7]) / 1000
                #print(j)
                times.append(j)
            elif i[0] == '0' and i[8] == ']':
                """for solves with six digits numbers"""
                j = int(i[2:8]) / 1000
                #print(j)
                times.append(j)

    infile.close()


    return times


def avgs(times):
    """calculating the different averages"""
    mo3 = []

    for i in range(len(times)-3):
        time = times[i:i+3]
        avgsum = sum(time)/3
        mo3.append(round(avgsum, 3))
    print("Best Avgs:\n\nMo3: {0:.2f}" .format(min(mo3)))

    session = [5,12]
    if len(times) >= 50:
        session = [5,12,50]
    if len(times) >= 100:
        session = [5,12,50,100]

    for n in session:
        tine = []
        for i in range(len(times)-n):
            time = times[i:i+n]
            mami = (max(time)+min(time))
            avgsum = (sum(time)- mami)/(n-2)
            tine.append(round(avgsum, (n-2)))
        print("avg{0:.0f}: {1:.2f}" .format(n, min(tine)))
    print("---------------------")


def avg50s(times):
    n = len(times)//50
    avg = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

    print("---------------------")
    for i in avg[0:n]:
        sub1 = min(times[i:i+49]) + max(times[i:i+49])
        avg1 = (sum(times[i:i+49]) - sub1)/48
        print("Avg({0:.0f}-{1:.0f}): {2:.2f}" .format(i+1, i+50, avg1))
    print("---------------------")


def sub_n(y, num):
    sub = 0
    for i in y:
        if int(i) < int(num):
            sub = sub + 1
    print("Solves belove {}: {} " .format(num,sub))
    print("---------------------")


def sort(times):
    y = sorted(times)

    for i in range(len(times)):
        print("{0:.0f}. {1:.2f}".format(i+1,y[i]))
        #print(y[i])


def plot_times(times):
    m = min(times)
    n = max(times)

    x = np.linspace(1,len(times),len(times))
    z = np.polyfit(x, times, 1)
    p = np.poly1d(z)
    plt.step(x, times, color = "c")
    plt.grid(axis = 'y', linestyle = '-', linewidth = 1)
    plt.plot(x,p(x),"--",color = "k")
    plt.show()

    xp = np.linspace(ceil(m)-1,ceil(n),round(ceil(n)-ceil(m)+2))
    #print(ceil(m)-1,ceil(n),round(ceil(n)-ceil(m)+2))
    plt.hist(times, xp, alpha = 1, width = .8)
    plt.xlim(m-1,n+1)
    plt.grid(axis = 'y', linestyle = '-', linewidth = 1)
    plt.show()


if __name__ == "__main__":
    filename = sys.argv[1]

    times = extract_times(filename)
    sort(times)

    plot_times(times)


    avg50s(times)

    avgs(times)

    if len(sys.argv) >= 4:
        sub_n(times, sys.argv[3])

    print("All over mean: {0:1.2f}" .format(sum(times)/len(times)))
