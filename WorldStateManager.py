class WorldStateManager:
    def __init__(self):
        self.inventory = []
        self.knownTricks = {}
        self.earliest = 0
        self.latest = 72
        self.worldState = {
            'cycle': 0,
            'clockTownDekuFlowerOpen': False,
            'AKquest': 0,
            'bombLadySaved': False
        }

    def state(self, opt):
        return self.worldState[opt]

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
        if 'zora' in self.inventory or 'goron' in self.inventory:
            maxH = max(maxH, 2)
        return height < maxH

    def postmanGame(self):
        # something like tricks['canTimeTen'] or have('bunnyHood')
        pass

    class timeObj(object):
        ## let's get a little info down about this one
        # so the state manager is for checking whether gates can be accessed, using as general conditions as possible
        #
        # obviously time is a factor in MM, so I figured there should be a check you can do to see if you can access
        # certain things
        # but since this is just a check for item placement, the only thing that (even possibly) matters is the earliest
        # time in the cycle it has to be (ex, if you got an item you can only get on the 2nd night, it has to be at
        # least the 2nd night)
        # so these checks look a little weird, and honestly might not even be necessary/useful
        # they could be used to generate how many cycles are expected to beat the seed, in which case, when a between
        # check is done, earliest is moved to the larger of the first arg or earliest (for example)
        # or when atLeast is done, earliest is moved to that time
        #
        # so yeah, maybe not necessary at all, but it's in there for now
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
