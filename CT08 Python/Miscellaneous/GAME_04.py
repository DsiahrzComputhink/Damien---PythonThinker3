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

# 24-bit RGB truecolor function
def rgb_fg(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def hsv_to_rgb(h, s=1, v=1):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = int(255 * v * (1 - s))
    q = int(255 * v * (1 - f * s))
    t = int(255 * v * (1 - (1 - f) * s))
    v = int(255 * v)
    if hi == 0:
        return v, t, p
    elif hi == 1:
        return q, v, p
    elif hi == 2:
        return p, v, t
    elif hi == 3:
        return p, q, v
    elif hi == 4:
        return t, p, v
    elif hi == 5:
        return v, p, q

# Your word
text = "CHROMATIC"

# Settings
duration = 5     # total seconds
fps = 30         # frames per second
frames = duration * fps
sleep_time = 1 / fps
spread = 180     # degrees of hue spread across the word

# Animation loop
start_time = time.time()
while (time.time() - start_time) < duration:
    now = time.time() - start_time
    base_hue = (now * 60) % 360  # hue shift speed
    output = ""
    for i, char in enumerate(text):
        # Calculate hue for this character
        hue = (base_hue + (i / (len(text)-1)) * spread) % 360
        r, g, b = hsv_to_rgb(hue)
        output += rgb_fg(r, g, b, char)
    
    print("\r" + output, end="")
    sys.stdout.flush()
    time.sleep(sleep_time)

# Reset
print("\033[0m")
print(WENOMEACHAINSAMA)