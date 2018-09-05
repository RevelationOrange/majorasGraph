class WorldStateManager:
    def __init__(self):
        self.inventory = []
        self.knownTricks = {}
        self.earliest = 0
        self.latest = 72
        self.worldState = {
            'cycle': 0,
            'clockTownDekuFlowerOpen': False,
            'AJquest': 0
        }

    def haveItem(self, i):
        return i in self.inventory

    def canBeLink(self):
        # there's an assumption here that's it not randomized that you can take off your initial mask to become link
        # after the first cycle
        # probly a safe assumption, but this check will need to be changed if it's not
        return self.worldState['cycle'] > 0

    def canLeaveClockTown(self):
        return self.canBeLink() or 'goron' in self.inventory or 'zora' in self.inventory

    def heightTest(self, height, bypass=None):
        if bypass is not None:
            if self.worldState[bypass]:
                return True
        maxH = 0
        if self.canBeLink():
            maxH = 1
        for item in self.inventory:
            if item == 'zora':
                maxH = max(maxH, 2)
            if item == 'goron':
                maxH = max(maxH, 2)
        return height < maxH

    class timeObj(object):
        def __init__(self):
            self.earliest = 0

        def isFirstNight(self):
            return self.earliest < 24

        def isSecondNight(self):
            return self.earliest < 48

        def atLeast(self, x):
            return True

        def between(self, x, y):
            return self.earliest < y
