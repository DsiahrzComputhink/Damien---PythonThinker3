# --------------------------------------------------------------------
fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
LINE = fg("------------------------------",235)

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

egg_code = ['1UK42211','2FR9292','1UK29292','0NL24555','0NL93933']
valid = 0

print(LINE)
for i in range(len(egg_code)):
    check = 0
    if len(egg_code[i]) >= 7:
        check += 1
    if egg_code[i][0] in [valid]:
        check += 1
    if egg_code[i][1:3].isalpha:
        check += 1
    if egg_code[i][3:].isdigit:
        check += 1
    if check == 3:
        valid += 1

    # for visuals
    EggMethod = f"{fg(egg_code[i][0],69)}"
    EggCountry = f"{fg(egg_code[i][1:3],117)}"
    EggID = f"{fg(egg_code[i][3:],255)}"
    print(f"{EggMethod}{EggCountry}{EggID}")
print(LINE)

if valid == len(egg_code):
    print("Codes for the entire batch of eggs are valid.")
    # Collate the number of eggs sampled according to farm method
    farm_method_eggs = {}
    for j in range(len(egg_code)):
        farm_method_eggs[egg_code[j][0]] += 1
    farm_method = ['Organic','Free Range','Barn','Cage']
    for k in range(len(egg_code)):
        print("Number of {0} eggs: {1}".format(farm_method[k],farm_method_eggs[k]))
    # Collate the number of eggs sampled according to country of origin
    countries = ['UK', 'FR', 'NL']
    countries_eggs = [0,0,0]
    for m in range(len(egg_code)):
        for n in range(len(countries)):
            if egg_code[m][:2] == countries[n]:
                countries_eggs[m] += 1
    for p in range(len(countries_eggs)):
        print("Number of {0} eggs: {1}".format(countries[p], countries_eggs[p]))
else:
    print("Invalid egg codes found for this batch of eggs.")
    print("No data will be presented.")