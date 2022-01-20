import re

def isNiceString1(inputString):
    rule1 = "[a|e|i|o|u].*[a|e|i|o|u].*[a|e|i|o|u]"
    rule2 = "(.)\\1"
    rule3 = "(ab|cd|pq|xy)"

    return (
        re.search(rule1, inputString) and
        re.search(rule2, inputString) and
        not re.search(rule3, inputString)
    )

def isNiceString2(inputString):
    rule1 = "(.{2}).*\\1"
    rule2 = "(.)(.)\\1"

    return (
        re.search(rule1, inputString) and
        re.search(rule2, inputString)
    )

def naughtyOrNice(inputFile, determiner):
    with open(inputFile) as names:
        niceStringsCount = 0
        for name in names:
            if determiner(name):
                niceStringsCount += 1

    return niceStringsCount

determiner = isNiceString2

print(naughtyOrNice("inputs/5.txt", determiner))
