AuraColour = {
    "Chromatic":[]
}
Auras = {
    "Common":[],
    "Chromatic":[]
    }

#-
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

print(
    fg("C",196) +  # Bright Red
    fg("H",202) +  # Orange
    fg("R",226) +  # Yellow
    fg("O",82)  +  # Green (was 154, now 82 is more vivid green)
    fg("M",48)  +  # Teal / Light Green (was 46, 48 looks better)
    fg("A",39)  +  # Bright Blue (same)
    fg("T",99)  +  # Purple-ish
    fg("I",201) +  # Magenta/Pink
    fg("C",196)    # Red again
)