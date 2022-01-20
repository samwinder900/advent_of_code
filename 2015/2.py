def wrappingPaper(inputFile):
    with open(inputFile) as giftSizes:
        totalPaper = 0
        for giftSize in giftSizes:
            l,w,h = sorted(
                [int(x) for x in giftSize.
                    strip().
                    split("x")
                ]
            )

            giftPaper = (
                2*(
                    l*w +
                    w*h +
                    l*h
                ) + l*w
            )

            totalPaper += giftPaper

        return totalPaper

def ribbon(inputFile):
    with open(inputFile) as giftSizes:
        totalRibbon = 0
        for giftSize in giftSizes:
            l,w,h = sorted([
                int(x) for x in giftSize.
                strip().
                split("x")
            ])

            totalRibbon += 2 * (
                l + w
            )

            totalRibbon += l * w * h

    return totalRibbon


wrappingPaper("inputs/2.txt")

print(ribbon("inputs/2.txt"))


