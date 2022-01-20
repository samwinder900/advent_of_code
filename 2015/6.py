import re

def configureLights(inputFile, instructionSet):
    grid = [[0 for x in range(0,1000)] for y in range(0,1000)]

    structure = '([A-z ]*)([\d,]*)([A-z ]*)([\d,]*)'
    for line in inputFile:
        components = re.match(structure, line)
        instruction = instructionSet[
            components.group(1).strip()
        ]
        startX, startY = [int(value) for value in components.group(2).split(',')]
        endX, endY = [int(value) for value in components.group(4).split(',')]

        for x in range(startX, endX+1):
            for y in range(startY,endY+1):
                grid[x][y] = instruction(grid[x][y])

    total = sum(map(sum, grid))

    return total

instructionSet2 = {
    "turn on": lambda value : (value + 1),
    "turn off": lambda value : max((value - 1),0),
    "toggle": lambda value : (value + 2),
}

instructionSet1 = {
    "turn on": lambda _ : 1,
    "turn off": lambda _ : 0,
    "toggle": lambda value : (value + 1) % 2,
}

with open('inputs/6.txt') as inputFile:
    print(configureLights(inputFile, instructionSet2))
