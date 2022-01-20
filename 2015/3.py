def deliverPresents(inputLocation):
    with open(inputLocation) as directions:
        x = 0
        y = 0
        deliveryLocations = set((x,y))
        while direction:=directions.read(1):
            if direction == "^":
                x+=1
            elif direction == "v":
                x-=1
            if direction == ">":
                y+=1
            elif direction == "<":
                y-=1

            if(direction in ("^","v",">","<")):
                deliveryLocations.add((x,y))

        return len(deliveryLocations)

def deliverPresentsRobo(inputLocation, *agentStartLocs):
    with open(inputLocation) as directions:
        agentLocations=[[0,0] for _ in range(0,len(agentStartLocs))]
        deliveryLocations = set()
        for startingLocation in agentStartLocs:
            deliveryLocations.add(
                tuple(startingLocation)
            )
        turn = 0

        while direction:=directions.read(1):
            if direction == "^":
                agentLocations[turn][0]+=1
            elif direction == "v":
                agentLocations[turn][0]-=1
            if direction == ">":
                agentLocations[turn][1]+=1
            elif direction == "<":
                agentLocations[turn][1]-=1

            if(direction in ("^","v",">","<")):
                deliveryLocations.add(
                    (
                        agentLocations[turn][0],
                        agentLocations[turn][1]
                    )
                )
                turn = (turn + 1) % len(agentStartLocs)

        return len(deliveryLocations)

print(deliverPresentsRobo("inputs/3.txt", [0,0], [0,0]))


