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
print(LINE)

if valid == len(egg_code):
    print("Codes for the entire batch of eggs are valid.")
    # Collate the number of eggs sampled according to farm method
    farm_method = {'Organic':0,'Free Range':0,'Barn':0,'Cage':0}
    for j in range(len(egg_code)):
        if egg_code[j][0] == "0":
            farm_method['']
    
    for k in range(len(egg_code)):
        print("Number of {1} eggs: {2}".format(farm_method[k],farm_method[k]))
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