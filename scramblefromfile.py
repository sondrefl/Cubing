import sys

if len(sys.argv) < 2:
    print("You need to add a impute file")
    sys.exit()

filename = sys.argv[1]


def extract_times(filename):
    """
    extract times the cstimer export file, and collect them in a list
    """
    infile = open(filename, "r")
    data = infile.readlines()

    times = []
    scramble = []
    for line in data:
        if len(line) > 15:
            Type = line.split("[[")
            for i in Type:
                if i[0] == "[":
                    i = i[1:]
                if i[0] == "0" and i[6] == "]":
                    """for solves with four digits numbers"""
                    j = int(i[2:6]) / 1000
                    times.append(j)

                elif i[0] == "0" and i[7] == "]":
                    """for solves with five digits numbers"""
                    j = int(i[2:7]) / 1000
                    times.append(j)

                elif i[0] == "0" and i[8] == "]":
                    """for solves with six digits numbers"""
                    j = int(i[2:8]) / 1000
                    times.append(j)

            scram = line.split(",")
            for i in scram:
                # scramble.append(len(i))
                if len(i) > 40:
                    scramble.append(i)
        else:
            print("--------------------")
            print("wrong type of file")
            print("--------------------")
            exit()

        d = dict(zip(times, scramble))

    infile.close()

    return times, scramble, d


def from_timer_file(filename):

    infile = open(filename, "r")
    data = infile.readlines()

    times = []
    times2 = []

    for line in data:
        time = line
        if len(time) < 15:

            time = float(time)
            times.append(f"{time:.2f}")
        else:
            print("--------------------")
            print("wrong type of file")
            print("--------------------")
            exit()

    for i in range(len(times)):
        ti = float(times[i])
        times2.append(ti)

    return times2


time_format = input("timefile format: cstimer(press c), from timer (press t):")

if time_format == "c":

    times, scramble, d = extract_times(filename)
    time = sorted(times)

    time_scramb = []

    for i in range(len(time)):
        ti_scra = (time[i], d[time[i]])
        time_scramb.append(ti_scra)

if time_format == "t":
    times = from_timer_file(filename)


times_3x3 = []
times_4x4 = []
times_5x5 = []
times_6x6 = []
times_7x7 = []

all_times = (times_3x3, times_4x4, times_5x5, times_6x6, times_7x7)

for i in times:
    if i < 30:
        times_3x3.append(i)
    if (i > 30) and (i < 70):
        times_4x4.append(i)
    if (i > 70) and (i < 120):
        times_5x5.append(i)
    if (i > 120) and (i < 190):
        times_6x6.append(i)
    if i > 200:
        times_7x7.append(i)


if __name__ == "__main__":

    print("hei")
