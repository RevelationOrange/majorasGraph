from WorldStateManager import WorldStateManager
from graph import Location, Exit, ItemSpot


def main():
    wsm = WorldStateManager()
    locs = [
        Location('south clock town', 'clock town', [
            Exit('sw', 'laundry pool'),
            Exit('w', 'west clock town'),
            Exit('nw', 'west clock town'),
            Exit('n', 'north clock town'),
            Exit('e', 'east clock town'),
            Exit('se', 'east clock town'),
            Exit('clock tower top', 'clock tower roof', [lambda world: world.heightTest(1, 'clockTownDekuFlowerOpen'), lambda world: world.time.atLeast(60)]),
            Exit('clock tower ground', 'clock tower below'),
            Exit('s', 'termina field', [lambda world: world.canLeaveClockTown()])
        ], [
            ItemSpot('clock tower hp', [lambda world: world.heightTest(1, 'clockTownDekuFlowerOpen')]),
            ItemSpot('festival tower chest', [lambda world: world.haveItem('hookshot', 'clockTownDekuFlowerOpen')]),
            ItemSpot('hookshot ledge chest', [lambda world: world.haveItem('hookshot')])
        ]),
        Location('laundry pool', 'clock town', [
            Exit('e', 'south clock town'),
            Exit('n', 'kafei hideout', [lambda world: world.AJquestState(3), lambda world: world.time.between(27, 30)])
            # I need to actually look up the reqs for this quest, the values here are very rough guesses
            # like, it's on the second morning? and you have to be 3 steps into the quest? I forget
        ], [
            ItemSpot('guru guru confession', [lambda world: world.canBeLink(), lambda world: (world.time.isFirstNight() or world.time.isSecondNight())]),
            ItemSpot('don gero frog', [lambda world: world.canBeLink(), lambda world: world.haveItem('donGero')])
        ]),
        Location('west clock town', 'clock town', [
            Exit('s door', 'curiosity shop'),
            Exit('ssw door', 'trading post'),
            Exit('sw door', 'clock town bomb shop'),
            Exit('w', 'termina field'),
            Exit('nw door', 'sword school'),
            Exit('ne door', 'post office'),
            Exit('ne', 'south clock town'),
            Exit('se', 'south clock town')
        ]),
    ]
    checkNames(locs)


def checkNames(locs):
    names = []
    with open('locationNames.txt') as namesfile:
        for line in namesfile:
            names.append(line[:-1])
    for l in locs:
        if l.name not in names:
            print(l.name)


if __name__ == '__main__':
    main()
