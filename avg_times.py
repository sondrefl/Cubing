import sys
import matplotlib.pyplot as plt
from math import ceil
import numpy as np


def avgs(times):
    """calculating the different averages"""
    mo3 = []

    for i in range(len(times) - 3):
        time = times[i : i + 3]
        avgsum = sum(time) / 3
        mo3.append(round(avgsum, 3))
    # print(float(min(mo3)))
    min_time = sec_to_min(min(mo3))
    print(f"Best Avgs:\n\nMo3: {min_time}")

    session = [5]
    if len(times) > 11:
        session = [5, 12]
    if len(times) >= 50:
        session = [5, 12, 50]
    if len(times) >= 100:
        session = [5, 12, 50, 100]

    for n in session:
        avg = []
        for i in range(len(times) - (n-1)):
            time = times[i : i + n]
            mami = max(time) + min(time)
            avgsum = (sum(time) - mami) / (n - 2)
            avg.append(round(avgsum, (n - 2)))

        #print(avg)
        min_time = sec_to_min(min(avg))
        print(f"avg{n}: {min_time}")

    print("---------------------")


def avg50s(times):
    n = len(times) // 50
    avg = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]


    print("---------------------")
    for i in avg[0:n]:
        sub1 = min(times[i : i + 49]) + max(times[i : i + 49])
        avg1 = (sum(times[i : i + 49]) - sub1) / 48

        #hei = f"Avg({i+1}-{i+50}):"

        min_time = sec_to_min(avg1)
        print(f"Avg({i+1}-{i+50}): {min_time}")
    print("---------------------")


def sub_n(y, num):
    sub = 0
    for i in y:
        if int(i) < int(num):
            sub = sub + 1
    print("Solves belove {}: {} ".format(num, sub))
    print("---------------------")


def sec_to_min(avg):
    """
    convert seconds to min, limit of ten min.
    """
    timemin = []
    
    limits = [60,120,180,240,300,360,420,480,540] 

    for i in range(len(limits)-1):
        #print(i)
        if avg < 60 or avg > 600:
            timemin.append(f"{avg:.2f}")
            break
        if avg > limits[i] and avg < limits[i+1]:
            timemin.append(f"{i+1}:{(avg-limits[i]):.2f}")
            break

    #print(len(timemin[0]))
    if len(timemin[0]) == 6:
        min_time = timemin[0]
        min_time = timemin[0][:2] + "0" + timemin[0][2:]
        
        return min_time
    else:   
        return timemin[0]



if __name__ == "__main__":
    from scramblefromfile import (
    times,
    all_times,)

    if len(sys.argv) == 3:
        cube = all_times[(int(sys.argv[2])-3)]
        avgs(cube)
        avg50s(cube)

    else:
        avgs(times)
        avg50s(times)