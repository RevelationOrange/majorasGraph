class WorldStateManager:
    def __init__(self):
        self.inventory = []
        self.knownTricks = {}
        self.worldState = {
            'cycle': 0,
            'clockTownDekuFlowerOpen': False,
            'AJquest': 0
        }

    def haveItem(self, i):
        return i in self.inventory

    def canBeLink(self):
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
