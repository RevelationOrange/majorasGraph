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
            Exit('clock tower top', 'clock tower roof', [lambda w: w.heightTest(1, 'clockTownDekuFlowerOpen'), lambda w: w.time.atLeast(60)]),
            Exit('clock tower ground', 'clock tower below'),
            Exit('s', 'termina field', [lambda w: w.canLeaveClockTown()])
        ], [
            ItemSpot('clock tower hp', [lambda w: w.heightTest(1, 'clockTownDekuFlowerOpen')]),
            ItemSpot('festival tower chest', [lambda w: w.haveItem('hookshot', 'clockTownDekuFlowerOpen')]),
            ItemSpot('hookshot ledge chest', [lambda w: w.haveItem('hookshot')])
        ]),
        Location('laundry pool', 'clock town', [
            Exit('e', 'south clock town'),
            Exit('n', 'kafei hideout', [lambda w: w.AJquestState(3), lambda w: w.time.between(27, 30)])
            # I need to actually look up the reqs for this quest, the values here are very rough guesses
            # like, it's on the second morning? and you have to be 3 steps into the quest? I forget
        ], [
            ItemSpot('guru guru confession', [lambda w: w.canBeLink(), lambda w: (w.time.isFirstNight() or w.time.isSecondNight())]),
            ItemSpot('don gero frog', [lambda w: w.canBeLink(), lambda w: w.haveItem('donGero')])
        ]),
        Location('west clock town', 'clock town', [
            Exit('s door', 'curiosity shop', [lambda w: (w.time.between(16, 24) or w.time.between(40, 48) or w.time.atLeast(64))]),
            Exit('ssw door', 'trading post', [lambda w: (not (w.time.between(15, 16) or w.time.between(39, 40) or w.time.between(63, 64)))]),
            Exit('sw door', 'clock town bomb shop'),
            Exit('w', 'termina field', [lambda w: w.canLeaveClockTown()]),
            Exit('nw door', 'sword school'),
            Exit('ne door', 'post office', [lambda w: (w.time.between(9, 18) or w.time.between(33, 42))]),
            Exit('ne', 'south clock town'),
            Exit('se', 'south clock town')
        ], [
            ItemSpot('rosa sisters hp', [lambda w: w.haveItem('kamaro')]),
            ItemSpot('adult wallet from bank'),
            ItemSpot('5k rupee hp from bank')
        ]),
        Location('north clock town', 'clock town', [
            Exit('sw', 'deku scrub playground'),  # assumption here, that you can always access this. probly fair?
            Exit('w', 'clock town great fairy'),
            Exit('n', 'termina field', [lambda w: w.canLeaveClockTown()]),
            Exit('e', 'east clock town'),
            Exit('s', 'south clock town')
        ], [
            ItemSpot('bombers notebook', [lambda w: w.canBeLink()]),
            ItemSpot('blast mask', [lambda w: w.canBeLink(), lambda w: w.time.between(24, 24.5)]),
            ItemSpot('tree hp'),
            # ItemSpot('tingle clock town map'), # not exactly sure how to deal with these, they might be rando'd,
            # ItemSpot('tingle woodfall map'),   # might not; if rando'd, must be changed in both places they appear
            ItemSpot('keaton hp')  # this might be global too? gotta figure out a way to track that
        ]),
        Location('east clock town', 'clock town', [
            Exit('sw', 'south clock town'),
            Exit('sw door', 'maze minigame'),  # probly only open at certain times
            Exit('w', 'south clock town'),
            Exit('w lower door', 'stock pot inn'), # only at certain times
            Exit('w upper door', 'stock pot inn'), # any time I think
            Exit('nw', 'north clock town'),
            Exit('n', 'mayor manor or something?'),  # some schedule, who knows
            Exit('ne', 'bomber hideout', [lambda w: w.haveItem('notebook')]),
            Exit('e door', 'milk bar'),  # certain times for sure
            Exit('e', 'termina field', [lambda w: w.canLeaveClockTown()]),
            Exit('se door', 'bomb throwing minigame'),
            # Exit('', ''), # maybe this is a thing? south door? not sure
        ], [
            ItemSpot('rupee chest', [lambda w: w.canBeLink()])  # as long as you're link, I think you can make those
            # jumps? might be some other reqs; possibly have the jumps be a trick so req jumps with bunny hood bypass
        ]),
        Location('clock tower roof', 'clock town', (), [ItemSpot('first cycle ocarina')]),
        Location('clock tower below', 'clock town', [
            Exit('door', 'south clock town')
        ], [
            ItemSpot('song of healing', [lambda w: w.haveItem('ocarina') and w.canBeLink()]),
            ItemSpot('deku', [lambda w: w.haveItem('ocarina') and w.canBeLink()])
        ]),
        Location('termina field', 'termina field', [
            # oh god so many exits I really need a map for this
            Exit('n clock town entrance', 'north clock town'),
            Exit('s clock town entrance', 'south clock town'),
            Exit('e clock town entrance', 'east clock town'),
            Exit('w clock town entrance', 'west clock town'),
            Exit('n', 'mountain path'),
            Exit('s', 'swamp path'),
            Exit('e', 'ikana path'),
            Exit('w', 'beach'),  # plus various grottos and stuff
        ], [
            # actually maybe no items on this specific map
        ]),
        Location('kafei hideout', 'clock town', [
            Exit('door', 'laundry pool')
        ], [
            ItemSpot('whatever item kafei gives that advances the quest')  # no checks once you're inside probly?
            # also maybe two spots here, one for the item, one for advancing the quest?
        ]),
        Location('curiosity shop', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('all night mask', [lambda w: w.time.atLeast(54)])  # check conditions here, probly missing smth
            # also maybe more spots?
        ]),
        Location('trading post', 'clock town', [
            Exit('door', 'west clock town')
        ]), # idek if there are any item spots to put here
        Location('clock town bomb shop', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('some kind of bomb bag?', [lambda w: w.bombLadySaved()])  # this could be way off, look up what you
            # get at the bomb shop
        ]),
        Location('sword school', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('sword challenge hp', [lambda w: w.canBeLink()])  # none of the other transform masks work here, right?
        ]),
        Location('post office', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('postman game hp', [lambda w: w.postmanGame()])
        ]),
        Location('deku scrub playground', 'clock town', [
            Exit('portal', 'north clock town')
        ], [
            ItemSpot('scrub playground hp', [lambda w: w.time.atLeast(48)])
        ]),
        Location('clock town great fairy', 'clock town', [
            Exit('idk what to call it, empty door, whatever', 'north clock town')
        ], [
            ItemSpot('great fairy mask')
        ]),
        Location('maze minigame', 'clock town', [
            Exit('door', 'east clock town')
        ], [
            ItemSpot('maze minigame hp')  # totally don't remember how this works, gotta look it up
        ]),
        Location('stock pot inn', 'clock town', [
            Exit('lower door', 'east clock town'),
            Exit('upper door', 'east clock town')  # might be some times these doors are closed and you're stuck inside?
        ], [
            ItemSpot('toilet hand deed thingy? whatever it is')  # at least this, probly more; gotta look up the times this works
        ]),
        Location('mayor manor or something?', 'clock town', [
            Exit('door', 'east clock town')
        ]),
        Location('bomber hideout', 'clock town', [
            Exit('hallway', 'east clock town'),
            Exit('observatory door', 'termina field fenced area')
        ], [
            ItemSpot('chest', [lambda w: w.haveItem('progBombBag') or w.haveItem('blast')]),
            # ItemSpot()  # maybe put the song pierre gives here? if so, also in trading post -> make global
        ]),
        Location('milk bar', 'clock town', ),
        Location(),
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
