infile = open('complex_cave.txt')
cave = infile.read()
infile.close()
cave = cave.split('\n') ## Splits input file into list of rows
watertiles = int(cave.pop(0)) ## Sets the variable for how much water to fill in

cave = [list(x) for x in cave if x] ## Turns every row into a modifiable list and deletes completely empty rows
    
cavecols = []
startpos = False
for t in range(0, len(cave[0])): ## Sets cavecols to a list of the columns, left to right
    cavecols.append(''.join([x[t] for x in cave]))
for xpos, x in enumerate(cavecols): ## Sets the start position of water
    if '~' in x:
        startpos = [xpos, cavecols[xpos].index('~')]

def putWater(x, y):
    """Puts a water tile on cave[y][x]"""
    global cave
    cave[y][x] = '~'

def checkWater(x, y):
    """Checks for what the next square to place water on is, starting from x, y"""
    try:
        if cave[y + 1][x] == ' ': ## If there's empty space under the water, fill that in
            return x, y + 1
        elif cave[y][x + 1] == ' ': ## If there's empy space to the right of the water, fill that in
            return x + 1, y
        ypos = y ## Lets the code modify a copy of y later
        xpos = len(cavecols) ## xpos starts at the right
        for row in cave[y - 1::-1]:
            ypos -= 1
            for column in cavecols[::-1]:
                xpos -= 1
                if column[ypos] == ' ' and row[xpos - 1] == '~': ##Checks for cases where water should start at the previous row
                    return xpos, ypos
    except IndexError: ## The water can pour down into the abyss!
        return False

def flow(numflows, pos=startpos):
    """Fills in cave using checkWater and putWater."""
    for turn in range(numflows):
        pos = checkWater(*pos)
        if not pos:
            return
        putWater(*pos)

flow(watertiles) ## Gotta call the function to use it!

cavecols = [] ## This whole time, cavecols hasn't been updated
for t in range(0, len(cave[0])): ## Update cavecols to contain water
    cavecols.append(''.join([x[t] for x in cave]))

def measureDepth(cols):
    """Measures the water depth of each column in 'cols'."""
    depths = []
    for col in cols:
        coldepth = 0
        for symbol in col:
            if symbol == '~': ## Every ~ adds one depth unit
                coldepth += 1
            elif symbol == ' ' and coldepth > 0: ## Sometimes water isn't done filling in a column
                coldepth = '~'
                break
        depths.append(coldepth) ## Returns a list of depths, from left to right
    return depths

depthstring = ' '.join([str(x) for x in measureDepth(cavecols)]) ## Write-friendly version of depths

output = open('complex_out-depths.txt', 'w')
output.write(depthstring)
output.close()      ## Mandatory closing
