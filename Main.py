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
            Exit('s door', 'curiosity shop', [lambda world: (world.time.between(16, 24) or world.time.between(40, 48) or world.time.atLeast(64))]),
            Exit('ssw door', 'trading post', [lambda world: (not (world.time.between(15, 16) or world.time.between(39, 40) or world.time.between(63, 64)))]),
            Exit('sw door', 'clock town bomb shop'),
            Exit('w', 'termina field', [lambda world: world.canLeaveClockTown()]),
            Exit('nw door', 'sword school'),
            Exit('ne door', 'post office', [lambda world: (world.time.between(9, 18) or world.time.between(33, 42))]),
            Exit('ne', 'south clock town'),
            Exit('se', 'south clock town')
        ], [
            ItemSpot('rosa sisters hp', [lambda world: world.haveItem('kamaro')]),
            ItemSpot('adult wallet from bank'),
            ItemSpot('5k rupee hp from bank')
        ]),
        Location('north clock town', 'clock town', [
            Exit('sw', 'deku scrub playground'),  # assumption here, that you can always access this. probly fair?
            Exit('w', 'clock town great fairy'),
            Exit('n', 'termina field', [lambda world: world.canLeaveClockTown()]),
            Exit('e', 'east clock town'),
            Exit('s', 'south clock town')
        ], [
            ItemSpot('bombers notebook', [lambda world: world.canBeLink()]),
            ItemSpot('blast mask', [lambda world: world.canBeLink(), lambda world: world.time.between(24, 24.5)]),
            ItemSpot('tree hp'),
            # ItemSpot('tingle clock town map'), # not exactly sure how to deal with these, they might be rando'd,
            # ItemSpot('tingle woodfall map'),   # might not; if rando'd, must be changed in both places they appear
            ItemSpot('keaton hp')  # this might be global too? gotta figure out a way to track that
        ]),
        Location('east clock town', 'clock town', [
            # Exit(),
        ])
    ]
    checkNames(locs)
    checkMade(locs)


def checkMade(locs):
    made = []
    exitsSansLocs = []
    for l in locs:
        made.append(l.name)
    for l in locs:
        for e in l.exits:
            if e.to not in made and e.to not in exitsSansLocs:
                exitsSansLocs.append(e.to)
    print('next up:', exitsSansLocs)


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
