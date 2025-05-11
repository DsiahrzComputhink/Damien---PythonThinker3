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
    if egg_code[i][0] in [0,1,2,3]:
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
            farm_method['Organic'] += 1
        if egg_code[j][0] == "1":
            farm_method['Free Range'] += 1
        if egg_code[j][0] == "2":
            farm_method['Barn'] += 1
        if egg_code[j][0] == "3":
            farm_method['Cage'] += 1
    print(LINE)
    for k in farm_method:
        print("Number of {} eggs: {}".format(k,farm_method[k]))
    print(LINE)
    # Collate the number of eggs sampled according to country of origin
    countries = {'UK':0, 'FR':0, 'NL':0}
    for m in range(len(egg_code)):
        for n in countries:
            if egg_code[m][1:3] == n:
                countries[n] += 1
    for p in countries:
        print("Number of {0} eggs: {1}".format(p, countries[p]))
else:
    print("Invalid egg codes found for this batch of eggs.")
    print("No data will be presented.")