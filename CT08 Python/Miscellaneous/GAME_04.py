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

print(fg("C",196) + fg("H",208)+ fg("R",220)+ fg("O",154)+ fg("M",46)+ fg("A",27)+ fg("T",99)+ fg("I",200)+ fg("C",196))