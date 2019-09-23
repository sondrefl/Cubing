import curses
import time

"""
-------------------------------------------
"""
def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): 
                break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)
"""
-------------------------------------------
"""

times = []
cube = curses.initscr()
solves = 2

for i in range(205):
    if solves > 2:
        new = input_char("Presing space for new solve:  \n")
        
    start = input_char("Start by presing space:  \n")

    if start == "q":
        break

    if start == " ":
        tid = time.time()

    stop = input_char("Press space to stop timer:\n")

    if stop == " ":
        tid1 = time.time()
        final_time = tid1 - tid
        if int(final_time) > 5:
            times.append(f"{final_time:.2f}")

        if solves < 22:
            cube.addstr(solves, 0, f"{solves-1}. {final_time:.2f}")

        if solves > 21 and solves <= 41:
            cube.addstr(solves-20, 12, f"{solves-1}. {final_time:.2f}")

        if solves > 41 and solves <= 61:
            cube.addstr(solves-40, 24, f"{solves-1}. {final_time:.2f}")

        if solves > 61 and solves <= 81:
            cube.addstr(solves-60, 36, f"{solves-1}. {final_time:.2f}")

        if solves > 81:
            cube.addstr(solves-80, 48, f"{solves-1}. {final_time:.2f}")

        if solves == 101:
            for i in range(100):
                stop = input_char("End of secion, press q to stop secion")
                if stop == "q":
                    break
            break
        solves = solves + 1


read = input("\nwould you like to add this times to a file? [y/n]: ")
if read == "y":
    read2 = input("would you like to overright the file? [y/n]: ")
    if read2 == "y":
        f = open("times_from_timer.txt", "w")
        for i in range(len(times)):
            f.write(f"{times[i]}\n")
        f.close()
    if read2 == "n":
        f = open("times_from_timer.txt", "a")
        for i in range(len(times)):
            f.write(f"{times[i]}\n")
        f.close()
