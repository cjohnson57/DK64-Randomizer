from enum import Enum

# Enum for kongs to avoid excessive string comparisons
class Kongs(Enum):
    donkey = 1
    diddy = 2
    lanky = 3
    tiny = 4
    chunky = 5

# A shufflable location at which a random item can be placed
class Location:
    def __init__(self, name, logic):
        self.name = name
        self.logic = logic # Lambda function for accessibility
        self.item = None

    def PlaceItem(self, item):
        self.item = item

# Event within a region
# Events act as statically placed items
# For example, if Lanky must press a button in region x to open something in region y,
# that can be represented as a button press event in region x which is checked for
# in region y.
class Event:
    def __init__(self, name, logic):
        self.name = name
        self.logic = logic # Lambda function for accessibility

# Exit from one region to another
class Exit:
    def __init__(self, dest, logic):
        self.dest = dest
        self.logic = logic # Lambda function for accessibility

# Region contains shufflable locations, events, and exits to other regions
class Region:
    def __init__(self, name, tagbarrel, locations, events, exits):
        self.name = name
        self.tagbarrel = tagbarrel
        self.locations = locations
        self.events = events
        self.exits = exits

        # Initially assume no access from any kong
        self.donkeyAccess = False
        self.diddyAccess = False
        self.lankyAccess = False
        self.tinyAccess = False
        self.chunkyAccess = False

    # Set that given kong has access to this region
    def UpdateAccess(self, kong, logicVariables):
        # If this region contains a tag barrel, all owned kongs also have access
        if self.tagbarrel:
            self.donkeyAccess = logicVariables.donkey
            self.diddyAccess = logicVariables.diddy
            self.lankyAccess = logicVariables.lanky
            self.tinyAccess = logicVariables.tiny
            self.chunkyAccess = logicVariables.chunky
        else:
            if kong == Kongs.donkey:
                self.donkeyAccess = True
            elif kong == Kongs.diddy:
                self.diddyAccess = True
            elif kong == Kongs.lanky:
                self.lankyAccess = True
            elif kong == Kongs.tiny:
                self.tinyAccess = True
            else:
                self.chunkyAccess = True
    
    # Check if given kong has access through this area
    # Used if a kong has access through a tag barrel only
    def HasAccess(self, kong):
        if kong == Kongs.donkey:
            return self.donkeyAccess
        elif kong == Kongs.diddy:
            return self.diddyAccess
        elif kong == Kongs.lanky:
            return self.lankyAccess
        elif kong == Kongs.tiny:
            return self.tinyAccess
        else:
            return self.chunkyAccess
