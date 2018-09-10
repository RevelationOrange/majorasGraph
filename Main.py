from WorldStateManager import WorldStateManager
from graph import Location, Exit, ItemSpot, Item


def main():
    wsm = WorldStateManager()
    ###
    ## if dealing with global stuff, like keaton mask or tingle maps, create the ItemSpots
    ## here I think and then put them in the appropriate Location
    ###
    globalItems = {
        'bigBombBag': ItemSpot('big bomb bag')
    }

    locs = [
        Location('south clock town', 'clock town', [
            Exit('sw', 'laundry pool'),
            Exit('w', 'west clock town'),
            Exit('nw', 'west clock town'),
            Exit('n', 'north clock town'),
            Exit('e', 'east clock town'),
            Exit('se', 'east clock town'),
            Exit('clock tower top', 'clock tower roof', lambda w: w.heightTest(1, 'clockTownDekuFlowerOpen') and w.time.atLeast(60)),
            Exit('clock tower ground', 'clock tower below'),
            Exit('s', 'termina field', lambda w: w.canLeaveClockTown())
        ], [
            ItemSpot('clock tower hp', lambda w: w.heightTest(1, 'clockTownDekuFlowerOpen')),
            ItemSpot('festival tower chest', lambda w: w.state('clockTownDekuFlowerOpen') or w.haveItem('hookshot')),
            ItemSpot('hookshot ledge chest', lambda w: w.haveItem('hookshot'))
        ]),
        Location('laundry pool', 'clock town', [
            Exit('e', 'south clock town'),
            Exit('n', 'kafei hideout', lambda w: w.state('AKquest') >= 3 and w.time.between(27, 30))
            # I need to actually look up the reqs for this quest, the values here are very rough guesses
            # like, it's on the second morning? and you have to be 3 steps into the quest? I forget
            # and you know, it's hard to find this part of the quest, I think it wasn't actually required or something
        ], [
            ItemSpot('guru guru confession', lambda w: w.canBeLink() and (w.time.isFirstNight() or w.time.isSecondNight())),
            ItemSpot('don gero frog', lambda w: w.canBeLink() and w.haveItem('donGero')).putItem(Item('donGeroFrog0'))
            # this don gero spot might not be needed, unless some maniac wants to throw it in the pool so that they beat
            # ghot or something, pick up the hc, and it's like 'thanks! i'm going to don gero!' or whatever
            # if we leave this in I'm calling it, pie would do it
        ]),
        Location('west clock town', 'clock town', [
            Exit('s door', 'curiosity shop', lambda w: (w.time.between(16, 24) or w.time.between(40, 48) or w.time.atLeast(64))),
            Exit('ssw door', 'trading post', lambda w: (not (w.time.between(15, 16) or w.time.between(39, 40) or w.time.between(63, 64)))),
            Exit('sw door', 'clock town bomb shop'),
            Exit('w', 'termina field', lambda w: w.canLeaveClockTown()),
            Exit('nw door', 'sword school'),
            Exit('ne door', 'post office', lambda w: (w.time.between(9, 18) or w.time.between(33, 42))),
            Exit('ne', 'south clock town'),
            Exit('se', 'south clock town')
        ], [
            ItemSpot('rosa sisters hp', lambda w: w.haveItem('kamaro')),
            ItemSpot('adult wallet from bank'),
            ItemSpot('5k rupee hp from bank')
        ]),
        Location('north clock town', 'clock town', [
            Exit('sw', 'deku scrub playground'),  # assumption here, that you can always access this. probly fair?
            Exit('w', 'clock town great fairy'),
            Exit('n', 'termina field', lambda w: w.canLeaveClockTown()),
            Exit('e', 'east clock town'),
            Exit('s', 'south clock town')
        ], [
            ItemSpot('bombers notebook', lambda w: w.canBeLink()),
            ItemSpot('blast mask', lambda w: w.canBeLink() and w.time.between(18, 18.5)),
            ItemSpot('tree hp'),
            # ItemSpot('tingle clock town map'), # not exactly sure how to deal with these, they might be rando'd,
            # ItemSpot('tingle woodfall map'),   # might not; if rando'd, must be changed in both places they appear
            ItemSpot('keaton hp')  # this might be global too? gotta figure out a way to track that
        ]),
        ###
        # stuff past here is probly sketchy, lots of work done while offline
        Location('east clock town', 'clock town', [
            Exit('sw', 'south clock town'),
            Exit('sw door', 'maze minigame', lambda w: w.time.between(0, 16) or w.time.between(24, 40) or w.time.between(48, 64)),
            Exit('w', 'south clock town'),
            Exit('w lower door', 'stock pot inn', lambda w: w.haveItem('roomKey') or w.time.between(2, 14.5) or w.time.between(26, 38.5) or w.time.between(50, 62.5)),
            Exit('w upper door', 'stock pot inn'), # any time I think
            Exit('nw', 'north clock town'),
            Exit('n', 'mayor residence', lambda w: w.time.between(4, 14) or w.time.between(28, 38) or w.time.between(52 ,62)),
            Exit('ne', 'bomber hideout', lambda w: w.haveItem('notebook')),
            Exit('e door', 'milk bar', lambda w: w.haveItem('romani') and (w.time.between(16, 24) or w.time.between(40, 48) or w.time.atLeast(64))),
            Exit('e', 'termina field', lambda w: w.canLeaveClockTown()),
            Exit('se door', 'bomb throwing minigame'),  # can't find times when it's open, but I'm pretty sure it's not always
            Exit('s door', 'town shooting gallery')  # same with this
        ], [
            ItemSpot('100 rupee chest', lambda w: w.canBeLink())  # as long as you're link, I think you can make those
            # jumps? might be some other reqs; possibly have the jumps be a trick so req jumps with bunny hood bypass
        ]),
        Location('clock tower roof', 'clock town', None, [ItemSpot('first cycle ocarina')]),
        Location('clock tower below', 'clock town', [
            Exit('door', 'south clock town')
        ], [
            ItemSpot('song of healing', lambda w: w.haveItem('ocarina') and w.canBeLink()),
            ItemSpot('deku', lambda w: w.haveItem('ocarina') and w.canBeLink())
        ]),
        Location('termina field', 'termina field', [
            # oh god so many exits I really need a map for this
            # todo later, because I haven't decided if I want to consider open grottos part of termina field
            Exit('n clock town entrance', 'north clock town'),
            Exit('s clock town entrance', 'south clock town'),
            Exit('e clock town entrance', 'east clock town'),
            Exit('w clock town entrance', 'west clock town'),
            Exit('n', 'mountain path'),
            Exit('s', 'swamp path'),
            Exit('e', 'ikana path'),
            Exit('w', 'beach'),  # plus various grottos and stuff
        ], [
            # very few actual checks here, just the kamaro mask and possibly some random chests
        ]),
        Location('kafei hideout', 'clock town', [
            Exit('door', 'laundry pool')
        ], [
            ItemSpot('whatever item kafei gives that advances the quest')  # no checks once you're inside probly?
            # also maybe two spots here, one for the item, one for advancing the quest?
            # or maybe it's a completely optional part of the quest?
        ]),
        Location('curiosity shop', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('all night mask', lambda w: w.state('bombLadySaved') and w.time.atLeast(64) and w.haveItem('giantWallet')),  # todo: check conditions here, probly missing smth
            # also maybe more spots?
            # it looks like just the big bomb bag if not bombLadySaved
            globalItems['bigBombBag'].setTest(lambda w: not w.state('bombLadySaved') and w.time.atLeast(64) and w.haveItem('adultWallet'))
        ]),
        Location('trading post', 'clock town', [
            Exit('door', 'west clock town')
        ]), # idek if there are any item spots to put here
        # yeah honestly maybe just don't have that as a location
        Location('clock town bomb shop', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('bomb bag')  # I think it's a good idea to randomize this lol
            # otherwise you can always just get bombs real easy every seed, no fun
        ]),
        Location('sword school', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('sword challenge hp', lambda w: w.canBeLink() and w.time.atMost(60))  # none of the other transform masks work here, right?
        ]),
        Location('post office', 'clock town', [
            Exit('door', 'west clock town')
        ], [
            ItemSpot('postman game hp', lambda w: w.postmanGame())
        ]),
        Location('deku scrub playground', 'clock town', [
            Exit('portal', 'north clock town')
        ], [
            ItemSpot('scrub playground hp', lambda w: w.time.atLeast(48))
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
            ItemSpot('chest', lambda w: w.haveItem('progBombBag') or w.haveItem('blast')),
            # ItemSpot()  # maybe put the song pierre gives here? if so, also in trading post -> make global
        ]),
        # Location('milk bar', 'clock town', ),
        # Location(),
    ]
    checkNames(locs)
    checkMade(locs)


def checkMade(locs):
    made = []
    exitsSansLocs = []
    for l in locs:
        made.append(l.name)
    for l in locs:
        if l.exits is not None:
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
