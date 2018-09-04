

class Location(object):
    __uid = -1

    def __init__(self, name, region, exits, itemSpots=()):
        self.name = name
        self.region = region
        self.exits = exits
        self.itemSpots = itemSpots
        self.id = self.getNextId()

    def addItem(self):
        pass

    def getNextId(self):
        Location.__uid += 1
        return Location.__uid


class Gate(object):
    def __init__(self, name, tests=()):
        self.name = name
        self.tests = tests


class Exit(Gate):
    def __init__(self, name, goesTo, tests=(), bypass=()):
        super().__init__(name, tests)
        self.to = goesTo
        self.bypass = bypass


class ItemSpot(Gate):
    def __init__(self, name, tests=()):
        super().__init__(name, tests)
        self.contains = None

    def putItem(self, i):
        self.contains = i

    def removeItem(self):
        self.contains = None


class Item(object):
    itemObjs = {
        'heartPiece',
        'heartContainer',
        'rupees',
        'bombs',
        'bombchus',
        'arrows',
        'sticks',
        'nuts',
        'progBow',
        'fireArrow',
        'iceArrow',
        'lightArrow',
        'magicBean',
        'powderKeg',
        'picto',
        'lens',
        'hookshot',
        'fairySword',
        'bottle',
        'progSword',
        'hylianShield',
        'mirrorShield',
        'progWallet',
        'progBombBag',
        'boss0',
        'boss1',
        'boss2',
        'boss3',
        'progTitleDeed',
        'notebook',
        'roomKey',
        'kafeiLetter',
        'pendantOfMemories',
        'specDelivery',
        'moonTear',
        'postmanHat',
        'allNight',
        'blast',
        'stone',
        'greatFairy',
        'deku',
        'keaton',
        'bremen',
        'bunny',
        'donGero',
        'scents',
        'goron',
        'romani',
        'troupeLeader',
        'kafei',
        'couple',
        'truth',
        'zora',
        'kamaro',
        'gibdo',
        'garo',
        'captain',
        'giants',
        'fierceDeity'
    }

    def __init__(self, i, q=1):
        pass
