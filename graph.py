

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
    def __init__(self, name, accessTest=None):
        self.name = name
        self.accessTest = accessTest


class Exit(Gate):
    def __init__(self, name, goesTo, accessTest=None):
        super().__init__(name, accessTest)
        self.to = goesTo


class ItemSpot(Gate):
    def __init__(self, name, accessTest=None):
        super().__init__(name, accessTest)
        self.contains = None

    def putItem(self, i):
        self.contains = i

    def removeItem(self):
        self.contains = None

    def setTest(self, f):
        self.accessTest = f
        return self


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
        'donGeroFrog0',
        'donGeroFrog1',
        'donGeroFrog2',
        'donGeroFrog3',
        'donGeroFrog4',
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
        if i in Item.itemObjs:
            self.what = i
            # self.type = Item.itemObjs[i]
        else:
            raise Exception('no such item')
