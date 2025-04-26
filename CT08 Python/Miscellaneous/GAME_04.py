AuraColour = {
    "Chromatic":[]
}
Auras = {
    "Common":[],
    "Chromatic":[]
    }

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

def debugcolour():

    def print_six(row, format, end="\n"):
        for col in range(6):
            color = row*6 + col - 2
            if color>=0:
                text = "{:3d}".format(color)
                print (format(text,color), end=" ")
            else:
                print(end="    ")   # four spaces
        print(end=end)

    for row in range(0, 43):
        print_six(row, fg, " ")
        print_six(row, bg)

debugcolour()
# Simple usage: print(fg("text", 160))

print(fg("text",160))

print(fg("C",196) + fg("H",202) + fg("R",226) + fg("O",82) + fg("M",48) + fg("A",39) + fg("T",99) + fg("I",201) + fg("C",196))

import time
import math
import sys

# Colored text functions (using 256 colors)
fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"

text = "CHROMATIC"

# Time settings
duration = 5  # total seconds to run
fps = 30      # frames per second
frames = duration * fps
sleep_time = 1 / fps

# 256 color palette "rainbow" range
def rainbow_color(position, total):
    # position: current letter index
    # total: total number of letters
    hue = (position / total) * 360
    return hsv_to_256(hue)

def hsv_to_256(h):
    # Approximate HSV to 256 color (only rough!)
    # 0-360 hue to color
    if h < 60:
        return 196  # red
    elif h < 120:
        return 226  # yellow
    elif h < 180:
        return 46   # green
    elif h < 240:
        return 51   # cyan
    elif h < 300:
        return 21   # blue
    else:
        return 201  # pink/magenta

# Animate
start_time = time.time()
while (time.time() - start_time) < duration:
    output = ""
    now = time.time() - start_time
    for i, char in enumerate(text):
        offset = (now * 120) + (i * 40)  # time + letter offset
        color = hsv_to_256(offset % 360)
        output += fg(char, color)
    
    print("\r" + output, end="")
    sys.stdout.flush()
    time.sleep(sleep_time)

# Reset colors
print("\33[0m")
