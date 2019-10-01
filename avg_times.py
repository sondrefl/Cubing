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

    for i in range(0, len(times)-49, 50):
        sub1 = min(times[i : i + 49]) + max(times[i : i + 49])
        avg1 = (sum(times[i : i + 49]) - sub1) / 48

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

    if avg >= 60:
        minut = int(avg // 60)
        rest = avg-(minut*60)

    for i in range(2):
        #print(i)
        if avg < 60:
            timemin.append(f"{avg:.2f}")
            break
        else:
            timemin.append(f"{minut}:{rest:.2f}")
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