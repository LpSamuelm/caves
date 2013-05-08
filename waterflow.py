from sys import argv

argfile = False

try:
    argfile = argv[1]
except IndexError:
    af = raw_input("What file do you want to use for simulation? >")
while not argfile:
    try:
        infile = open(af, 'r')
        argfile = af
    except IOError:
        af = raw_input("That is not a valid file.\nWhat file do you want to use for simulation? >")
    
cave = infile.read()
infile.close()
cave = cave.split('\n')
watertiles = int(cave[0])

cave = cave[2:-1]
cave = [list(x) for x in cave]
    
cavecols = []
for t in range(0, len(cave[0])):
    cavecols.append(''.join([x[t] for x in cave]))
for xpos, x in enumerate(cavecols):
    if '~' in x:
        startpos = [xpos, cavecols[xpos].index('~')]

def putWater(x, y):
    global cave
    cave[y][x] = '~'

def checkWater(x, y):
    try:
        if cave[y + 1][x] == ' ':
            return x, y + 1
        elif cave[y][x + 1] == ' ':
            return x + 1, y
        ypos = y
        xpos = len(cavecols)
        for row in cave[y - 1::-1]:
            ypos -= 1
            for column in cavecols[::-1]:
                xpos -= 1
                if column[ypos] == ' ' and row[xpos - 1] == '~':
                    return xpos, ypos
    except IndexError:
        return False

def checkput(x, y):
    pos = checkWater(x, y)
    if pos:
        putWater(*pos)
        return pos
    else:
        return False

def flow(numflows, pos=startpos):
    for turn in range(numflows):
        pos = checkput(*pos)
        if not pos:
            return

flow(watertiles)
cavecols = []
for t in range(0, len(cave[0])):
    cavecols.append(''.join([x[t] for x in cave]))

def measureDepth(cols):
    depths = []
    for col in cols:
        coldepth = 0
        for symbol in col:
            if symbol == '~':
                coldepth += 1
            elif symbol == ' ' and coldepth > 0:
                coldepth = '~'
                break
        depths.append(coldepth)
    return depths

cavestring = '\n'.join([''.join(x) for x in cave])
depthstring = ' '.join([str(x) for x in measureDepth(cavecols)])

outfile = open('output.txt', 'w')
outfile.write(cavestring + '\n' + depthstring)
outfile.close()

Print "Successful!"
