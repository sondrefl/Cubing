import sys
from scramblefromfile import (
    times,
    all_times,)
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
    sec_to_min(min(mo3), 0, "mo3")
    # print(f"Best Avgs:\n\nMo3: {min(mo3):.2f}")

    session = [5, 12]
    if len(times) >= 50:
        session = [5, 12, 50]
    if len(times) >= 100:
        session = [5, 12, 50, 100]

    for n in session:
        avg = []
        for i in range(len(times) - n):
            time = times[i : i + n]
            mami = max(time) + min(time)
            avgsum = (sum(time) - mami) / (n - 2)
            avg.append(round(avgsum, (n - 2)))

        sec_to_min(min(avg), n)
    print("---------------------")


def avg50s(times):
    n = len(times) // 50
    avg = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]


    print("---------------------")
    for i in avg[0:n]:
        sub1 = min(times[i : i + 49]) + max(times[i : i + 49])
        avg1 = (sum(times[i : i + 49]) - sub1) / 48

        hei = f"Avg({i+1}-{i+50}):"
        # print(f"Avg({i+1}-{i+50}): {avg1:.2f}")
        sec_to_min(avg1, 0, hei)
    print("---------------------")


def sub_n(y, num):
    sub = 0
    for i in y:
        if int(i) < int(num):
            sub = sub + 1
    print("Solves belove {}: {} ".format(num, sub))
    print("---------------------")


def sec_to_min(avg, n, name_avg="hei"):

    if name_avg == "mo3":
        if avg < 60:
            print(f"Best Avgs:\n\nMo3: {avg:.2f}")
        if avg > 60 and avg < 120:
            print(f"Best Avgs:\n\nMo3: 1:{(avg-60):.2f}")
        if avg > 120 and avg < 180:
            print(f"Best Avgs:\n\nMo3: 2:{(avg-120):.2f}")
        if avg > 180 and avg < 240:
            print(f"Best Avgs:\n\nMo3: 3:{(avg-180):.2f}")
        if avg > 240 and avg < 300:
            print(f"Best Avgs:\n\nMo3: 4:{(avg-240):.2f}")

    if len(name_avg) > 8:
        if avg < 60:
            print(f"{name_avg} {avg:.2f}")
        if avg > 60 and avg < 120:
            print(f"{name_avg} 1:{(avg-60):.2f}")
        if avg > 120 and avg < 180:
            print(f"{name_avg} 2:{(avg-120):.2f}")
        if avg > 180 and avg < 240:
            print(f"{name_avg} 3:{(avg-180):.2f}")
        if avg > 240 and avg < 300:
            print(f"{name_avg} 4:{(avg-240):.2f}")

    else:
        if avg < 60:
            print(f"avg{n}: {avg:.2f}")
        if avg > 60 and avg < 120:
            print(f"avg{n}: 1:{(avg-60):.2f}")
        if avg > 120 and avg < 180:
            print(f"avg{n}: 2:{(avg-120):.2f}")
        if avg > 180 and avg < 240:
            print(f"avg{n}: 3:{(avg-180):.2f}")
        if avg > 240 and avg < 300:
            print(f"avg{n}: 4:{(avg-240):.2f}")


if __name__ == "__main__":

    if len(sys.argv) == 3:
        cube = all_times[(int(sys.argv[2])-3)]
        avgs(cube)
        avg50s(cube)

    else:
        avgs(times)
        avg50s(times)