from LogicClasses import Region, Location, Event, Exit
from Enums.Events import Events
from Enums.Regions import Regions

LogicRegions = {
    Regions.FranticFactoryStart: Region("Frantic Factory Start", False, [], [
        Event(Events.FactoryEntered, lambda l: True),
    ], [
        Exit(Regions.FranticFactoryLobby, lambda l: True),
        Exit(Regions.Testing, lambda l: Events.TestingGateOpened in l.Events),
        Exit(Regions.BeyondHatch, lambda l: l.Slam),
    ]),

    Regions.Testing: Region("Testing", True, [
        Location("Factory Donkey Number Game", lambda l: l.Slam and l.isdonkey),
        Location("Factory Diddy Block Tower", lambda l: l.spring and l.isdiddy),
        Location("Factory Lanky Batty Barrel Bandit", lambda l: l.balloon and l.islanky),
        Location("Factory Tiny Dartboard", lambda l: Events.DartsPlayed in l.Events and l.istiny),
        Location("Factory Chunky Kasplat", lambda l: l.ischunky),
        Location("Factory Banana Fairy by Counting", lambda l: l.camera),
        Location("Factory Banana Fairy by Funky", lambda l: l.camera and Events.DartsPlayed in l.Events),
    ], [
        Event(Events.DartsPlayed, lambda l: l.Slam and l.mini and l.feather),
    ], [
        Exit(Regions.RandD, lambda l: True),
        Exit(Regions.Snide, lambda l: True),
        Exit(Regions.Funky, lambda l: Events.DartsPlayed in l.Events),
        Exit(Regions.FactoryBossLobby, lambda l: True),
    ]),

    Regions.RandD: Region("R&D", True, [
        Location("Factory Diddy R&D", lambda l: l.guitar and l.charge and l.isdiddy),
        Location("Factory Lanky R&D", lambda l: l.trombone and l.Slam and l.islanky),
        Location("Factory Chunky R&D", lambda l: l.triangle and l.punch and l.hunkyChunky and l.ischunky),
        Location("Factory Lanky Kasplat", lambda l: l.islanky),
        Location("Factory Battle Arena", lambda l: l.grab),
    ], [], [
        Exit(Regions.FactoryTinyRace, lambda l: l.mini and l.istiny),
        Exit(Regions.ChunkyRoomPlatform, lambda l: True),
        Exit(Regions.FactoryBossLobby, lambda l: True),
    ]),

    Regions.FactoryTinyRace: Region("Factory Tiny Race", False, [
        Location("Factory Tiny Car Race", lambda l: l.istiny),
    ], [], []),

    Regions.ChunkyRoomPlatform: Region("Chunky Room Platform", False, [
        Location("Factory Diddy Beaver Bother", lambda l: l.Slam and l.isdiddy),
    ], [], [
        Exit(Regions.PowerHut, lambda l: True),
        Exit(Regions.BeyondHatch, lambda l: True),
    ]),

    Regions.PowerHut: Region("Power Hut", False, [
        Location("Factory Donkey Power Hut", lambda l: Events.MainCoreActivated in l.Events and l.isdonkey),
    ], [
        Event(Events.MainCoreActivated, lambda l: l.coconut and l.grab and l.isdonkey),
    ], [
        Exit(Regions.ChunkyRoomPlatform, lambda l: True),
    ]),

    Regions.BeyondHatch: Region("Beyond Hatch", True, [
        Location("Chunky Kong", lambda l: l.handstand and l.Slam and l.islanky),
        Location("Nintendo Coin", lambda l: Events.ArcadeLeverSpawned in l.Events and l.grab),
        Location("Factory Donkey DK Arcade", lambda l: Events.ArcadeLeverSpawned in l.Events and l.grab),
        Location("Factory Lanky Free Chunky", lambda l: l.handstand and l.Slam and l.islanky),
        Location("Factory Tiny by Arcade", lambda l: l.mini and l.istiny),
        Location("Factory Chunky Dark Room", lambda l: l.punch and l.Slam and l.ischunky),
        Location("Factory Chunky Stash Snatch", lambda l: l.punch and l.ischunky),
        Location("Factory Tiny Kasplat", lambda l: l.istiny),
    ], [
        Events(Events.ArcadeLeverSpawned, lambda l: l.blast and l.isdonkey),
        Events(Events.TestingGateOpened, lambda l: l.Slam),
        Events(Events.DiddyCoreSwitch, lambda l: l.Slam and l.isdiddy),
        Events(Events.LankyCoreSwitch, lambda l: l.Slam and l.islanky),
        Events(Events.TinyCoreSwitch, lambda l: l.Slam and l.istiny),
        Events(Events.ChunkyCoreSwitch, lambda l: l.Slam and l.ischunky),
    ], [
        Exit(Regions.InsideCore, lambda l: Events.MainCoreActivated in l.Events),
        Exit(Regions.MainCore, lambda l: Events.MainCoreActivated in l.Events),
        Exit(Regions.Cranky, lambda l: True),
        Exit(Regions.Candy, lambda l: True),
        Exit(Regions.FactoryBossLobby, lambda l: True),
    ]),

    Regions.InsideCore: Region("Inside Core", False, [
        Location("Factory Donkey Crusher Room", lambda l: l.strongKong and l.isdonkey),
    ], [], [
        Exit(Regions.BeyondHatch, lambda l: True),
    ]),

    Regions.MainCore: Region("Main Core", True, [
        Location("Factory Diddy Production Room", lambda l: Events.DiddyCoreSwitch in l.Events and l.spring and l.isdiddy),
        Location("Factory Lanky Production Room", lambda l: Events.LankyCoreSwitch in l.Events and l.handstand and l.islanky),
        Location("Factory Tiny Production Room", lambda l: Events.TinyCoreSwitch in l.Events and l.twirl and l.istiny),
        Location("Factory Chunky Production Room", lambda l: Events.ChunkyCoreSwitch in l.Events and l.ischunky),
    ], [], []),

    Regions.FactoryBossLobby: Region("Factory Boss Lobby", False, [], [], [
        # 200 bananas
        Exit(Regions.FactoryBoss, lambda l: l.istiny),
    ]),

    Regions.FactoryBoss: Region("Factory Boss", False, [
        Location("Factory Boss Key", lambda l: l.twirl and l.istiny),
    ], [], []),
}
