infile = open('simple_cave.txt', 'r')
cave = infile.read()
infile.close()
cave = cave.split('\n')
watertiles = int(cave[0])
cave = cave[2:-1]
cave = [list(x) for x in cave]
for boob in cave:
    print boob
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
        for ypos in cave[y - 1::-1]:
            if ' ' in ypos:
                for xpos in cave[ypos][::-1]:
                    if cave[ypos][xpos - 1] == ' ' and xpos == ' ':
                        return xpos, ypos
                return False
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
print '\n'.join([''.join(x) for x in cave])
