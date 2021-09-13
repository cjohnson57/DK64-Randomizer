"""Bonus Game Data"""
class BonusBarrel:
    def __init__(self, name, map_index=11, type=1, difficulty=1, **kwargs):
        self.name = name
        self.map_index = map_index
        self.type = type
        self.difficulty = difficulty
        self.shared_moves()
        self.kongs()
        self.category()
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise Exception("Attribute does not exist")
                
    def __str__(self):
        """Get the string.

        Returns:
            str: returns a string of the GB location.
        """
        return self.name

    def __repr__(self):
        """Get the string.

        Returns:
            str: returns a string of the GB location.
        """
        return self.name            
                
    def shared_moves(self, barrel=False, dive=False, gun=False, homing=False, orange=False, sniper=False, vine=False):
        self.barrel = barrel
        self.dive = dive
        self.gun = gun
        self.homing = homing
        self.orange = orange
        self.sniper = sniper
        self.vine = vine

    def kongs(self, dk=True, diddy=True, lanky=True, tiny=True, chunky=True):
        self.uses_dk = dk
        self.uses_diddy = diddy
        self.uses_lanky = lanky
        self.uses_tiny = tiny
        self.uses_chunky = chunky

    def category(self, batty=False, beaver=False, bash=False, barrage=False, klamour=False, kosh=False, maze=False, minecart=False, peril=False, seek=False, swing=False, splash=False, snatch=False, snoop=False, turtle=False, helm=False):
        self.batty = batty
        self.beaver = beaver
        self.bash = bash
        self.barrage = barrage
        self.klamour = klamour
        self.kosh = kosh
        self.maze = maze
        self.minecart = minecart
        self.peril = peril
        self.seek = seek
        self.swing = swing
        self.splash = splash
        self.snatch = snatch
        self.snoop = snoop
        self.turtle = turtle
        self.helm = helm
    
class BarrelLocation:
    def __init__(self, name, object_id=0, location_map=34, **kwargs):
        self.name = name
        self.object_id = object_id
        self.location_map = location_map
        self.kongs()
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise Exception("Attribute does not exist")

    def __str__(self):
        """Get the string.

        Returns:
            str: returns a string of the GB location.
        """
        return self.name

    def __repr__(self):
        """Get the string.

        Returns:
            str: returns a string of the GB location.
        """
        return self.name
    
    def kongs(self, dk=False, diddy=False, lanky=False, tiny=False, chunky=False):
        self.uses_dk = dk
        self.uses_diddy = diddy
        self.uses_lanky = lanky
        self.uses_tiny = tiny
        self.uses_chunky = chunky

# Type 1 = Standard, 2 = Snides Only/Unused
# Difficulty 2 is a difficult bonus barrel, otherwise 1 is default
bonus_barrels = [
    BonusBarrel( "Batty Barrel Bandit [Slow Reel]", batty=True, map_index=32, ), # Factory Lanky - Slow Reel
    BonusBarrel( "Batty Barrel Bandit [Slow to Fast Reel]", batty=True, map_index=121, ), # Galleon Chunky - Slow to Fast Reel
    BonusBarrel( "Batty Barrel Bandit [Fast Reel, 40 secs]", batty=True, map_index=122, ), # Isles Diddy - Fast Reel, 40 secs
    BonusBarrel( "Batty Barrel Bandit [Fast Reel, 35 secs]", batty=True, map_index=123, type=2, ), # Snides - Fast Reel, 35 secs
    BonusBarrel( "Beaver Bother [Hit 12, Normal Beavers]", beaver=True, map_index=104, difficulty=2, ), # Factory Diddy - 12
    BonusBarrel( "Beaver Bother [Hit 15, Normal Beavers]", beaver=True, map_index=136, difficulty=2, ), # Castle Lanky, Castle Chunky - 15
    BonusBarrel( "Beaver Bother [Hit 15, Faster Beavers]", beaver=True, map_index=137, difficulty=2, type=2, ), # Snides - 15, Faster Beavers
    BonusBarrel( "Big Bug Bash [Hit 4]", bash=True, map_index=102, ), # Aztec Lanky - 4
    BonusBarrel( "Big Bug Bash [Hit 6]", bash=True, map_index=148, ), # Galleon Tiny - 6
    BonusBarrel( "Big Bug Bash [Hit 8]", bash=True, map_index=149, difficulty=2, ), # Isles Tiny - 8
    BonusBarrel( "Big Bug Bash [Hit 10]", bash=True, map_index=150, difficulty=2, ), # Castle Diddy, Snides - 10
    BonusBarrel( "Busy Barrel Barrage [45 Secs, 4 Spawns]", barrage=True, map_index=78, uses_lanky=False, ), # Aztec Chunky - 4 Spawns, 45 secs
    BonusBarrel( "Busy Barrel Barrage [45 Secs, 5 Spawns]", barrage=True, map_index=79, uses_lanky=False, ), # Forest Diddy - 5 Spawns, 45 secs
    BonusBarrel( "Busy Barrel Barrage [60 Secs, 6 Spawns]", barrage=True, map_index=131, uses_lanky=False, difficulty=2, ), # Caves DK - 6 Spawns, 60 secs
    BonusBarrel( "Krazy Kong Klamour [Hit 10, Ample Time]", klamour=True, map_index=101, ), # Tiny Factory - 10, Ample Time Between Hits
    BonusBarrel( "Krazy Kong Klamour [Hit 15, Ample Time]", klamour=True, map_index=141, ), # Galleon DK - 15, Ample Time Between Hits
    BonusBarrel( "Krazy Kong Klamour [Hit 5, Little Time]", klamour=True, map_index=142, difficulty=2, ), # Fungi Lanky, Caves Tiny - 5, Little Time Between Hits
    BonusBarrel( "Krazy Kong Klamour [Hit 10, Little Time]", klamour=True, map_index=143, difficulty=2, type=2, ), # Snides - 10, Little Time Between Hits
    BonusBarrel( "Kremling Kosh [Hit 18]", kosh=True, map_index=10, ), # Aztec Chunky - 18
    BonusBarrel( "Kremling Kosh [Hit 22]", kosh=True, map_index=115, ), # Galleon Tiny - 22
    BonusBarrel( "Kremling Kosh [Hit 25]", kosh=True, map_index=116, difficulty=2, ), # Castle Lanky - 25
    BonusBarrel( "Kremling Kosh [Hit 28]", kosh=True, map_index=117, difficulty=2, ), # Isles DK, Snides - 28
    BonusBarrel( "Mad Maze Maul [Hit 5, 60 Secs]", maze=True, map_index=68, ), # Japes Lanky - 5, 60 secs
    BonusBarrel( "Mad Maze Maul [Hit 7, 60 Secs]", maze=True, map_index=69, ), # Caves Diddy - 7, 60 secs
    BonusBarrel( "Mad Maze Maul [Hit 11, 120 Secs]", maze=True, map_index=66, difficulty=2, type=2, ), # Unused - 11, 120 secs
    BonusBarrel( "Mad Maze Maul [Hit 10, 125 Secs]", maze=True, map_index=124, difficulty=2, type=2, ), # Unused - 10, 125 secs
    BonusBarrel( "Minecart Mayhem [30 Secs, 1 TNT Barrel]", minecart=True, map_index=77, ), # Japes Chunky - 1 TNT, 30 secs
    BonusBarrel( "Minecart Mayhem [45 Secs, 2 TNT Barrels]", minecart=True, map_index=129, difficulty=2, ), # Fungi DK - 2 TNT, 45 secs
    BonusBarrel( "Minecart Mayhem [60 Secs, 2 TNT Barrels]", minecart=True, map_index=130, difficulty=2, ), # Castle Diddy - 2 TNT, 60 secs
    BonusBarrel( "Peril Path Panic [Save 6]", peril=True, map_index=144, ), # Factory Diddy - 6
    BonusBarrel( "Peril Path Panic [Save 8]", peril=True, map_index=145, ), # Fungi DK - 8
    BonusBarrel( "Peril Path Panic [Save 10]", peril=True, map_index=146, ), # Isles Diddy, Snides - 10
    BonusBarrel( "Peril Path Panic [Save 12]", peril=True, map_index=147, difficulty=2, type=2, ), # Unused - 12
    BonusBarrel( "Searchlight Seek [Hit 4]", seek=True, map_index=103, ), # Galleon Lanky - 4
    BonusBarrel( "Searchlight Seek [Hit 6]", seek=True, map_index=138, ), # Snides - 6
    BonusBarrel( "Searchlight Seek [Hit 8]", seek=True, map_index=139, ), # Caves Chunky - 8
    BonusBarrel( "Searchlight Seek [Hit 10]", seek=True, map_index=140, ), # Castle Chunky, Isles Lanky - 10
    BonusBarrel( "Speedy Swing Sortie [Get 9, 40 Secs]", swing=True, map_index=99, ), # Japes Lanky - 9, 40 secs
    BonusBarrel( "Speedy Swing Sortie [Get 14, 45 Secs]", swing=True, map_index=134, uses_dk=False, uses_diddy=False, uses_lanky=False, uses_chunky=False, ), # Fungi Tiny - 14, 45 secs
    BonusBarrel( "Speedy Swing Sortie [Get 6, 60 Secs]", swing=True, map_index=135, type=2, ), # Unused - 6, 60 secs
    BonusBarrel( "Splish Splash Salvage [Get 8]", splash=True, map_index=133, ), # Galleon Diddy - 8
    BonusBarrel( "Splish Splash Salvage [Get 10]", splash=True, map_index=96, ), # Japes Lanky - 10
    BonusBarrel( "Splish Splash Salvage [Get 15]", splash=True, map_index=132, type=2, ), # Unused - 15
    BonusBarrel( "Stash Snatch [Get 6, 60 Secs]", snatch=True, map_index=74, ), # Factory Chunky - 6, 60 secs
    BonusBarrel( "Stash Snatch [Get 16, 60 Secs]", snatch=True, map_index=67, type=2, ), # Unused - 16, 60 secs
    BonusBarrel( "Stash Snatch [Get 33, 120 Secs]", snatch=True, map_index=125, difficulty=2, type=2, ), # Unused - 33, 120 secs
    BonusBarrel( "Stash Snatch + Stealthy Snoop [Get 4, 120 Secs]", snatch=True, map_index=75, difficulty=2, type=2, ), # Unused - 4, 120 secs
    BonusBarrel( "Stealthy Snoop [50 Secs]", snoop=True, map_index=126, ), # Aztec DK - 50 secs
    BonusBarrel( "Stealthy Snoop [60 Secs]", snoop=True, map_index=127, ), # Galleon Diddy - 60 secs
    BonusBarrel( "Stealthy Snoop [70 Secs]", snoop=True, map_index=65, difficulty=2, type=2, ), # Unused - 70 secs, map 11 is the same but with no logo
    BonusBarrel( "Stealthy Snoop [90 Secs]", snoop=True, map_index=128, difficulty=2, type=2, ), # Unused - 90 secs
    BonusBarrel( "Teetering Turtle Trouble [45 Secs, Very Easy]", turtle=True, map_index=18, ), # Aztec Lanky - 45 secs
    BonusBarrel( "Teetering Turtle Trouble [45 Secs, Easy]", turtle=True, map_index=118, ), # Fungi Diddy - 45 secs
    BonusBarrel( "Teetering Turtle Trouble [60 Secs, Medium]", turtle=True, map_index=119, ), # Castle Tiny - 60 secs
    BonusBarrel( "Teetering Turtle Trouble [60 Secs, Hard]", turtle=True, map_index=120, type=2, ), # Snides - 60 secs
    BonusBarrel( "DK Helm Rambi", helm=True, map_index=212, type=4, ),
    BonusBarrel( "DK Helm Targets", helm=True, map_index=35, type=4, uses_diddy=False, uses_lanky=False, uses_tiny=False, uses_chunky=False, ),
    BonusBarrel( "Chunky Helm Shoot", helm=True, map_index=211, type=4, ),
    BonusBarrel( "Chunky Helm Crates", helm=True, map_index=209, type=4, uses_dk=False, uses_diddy=False, uses_lanky=False, uses_tiny=False, ),
    BonusBarrel( "Tiny Helm Mushrooms", helm=True, map_index=50, type=4, ),
    BonusBarrel( "Tiny Helm Boxes", helm=True, map_index=210, type=4, uses_dk=False, uses_diddy=False, uses_lanky=False, uses_chunky=False, ),
    BonusBarrel( "Lanky Helm Maze", helm=True, map_index=3, type=4, ),
    BonusBarrel( "Lanky Helm Shoot", helm=True, map_index=202, type=4, ),
    BonusBarrel( "Diddy Helm Rocketbarrel", helm=True, map_index=201, type=4, uses_dk=False, uses_lanky=False, uses_tiny=False, uses_chunky=False, ),
    BonusBarrel( "Diddy Helm Kremling", helm=True, map_index=165, type=4, ),

    # Not putting the training barrels in the pool for the time being
    # BonusBarrel( "Barrel", map_index=181, ),
    # BonusBarrel( "Orange", map_index=180, ),
    # BonusBarrel( "Swimming", map_index=177, ),
    # BonusBarrel( "Vine", map_index=182, ), 
]

barrel_locations = [
    BarrelLocation( "Japes 1st Cave [Lanky]", object_id=32, location_map=7, uses_lanky=True, ),
    BarrelLocation( "Japes 1st Cave [Tiny]", object_id=31, location_map=7, uses_tiny=True, ),
    BarrelLocation( "Japes Near Beehive [Chunky]", object_id=33, location_map=7, uses_chunky=True, ),
    BarrelLocation( "Japes Cave to Cranky's on Left [Lanky]", object_id=34, location_map=7, uses_lanky=True, ),
    BarrelLocation( "Aztec Behind Funky's [DK]", object_id=33, location_map=38, uses_dk=True, ),
    BarrelLocation( "Aztec 5 Door Temple [Lanky]", object_id=0, location_map=23, uses_lanky=True, ),
    BarrelLocation( "Aztec 5 Door Temple [Chunky]", object_id=0, location_map=24, uses_chunky=True, ),
    BarrelLocation( "Aztec Caged in 2nd Tunnel [Chunky]", object_id=35, location_map=38, uses_chunky=True, ),
    BarrelLocation( "Aztec In Llama Temple [Lanky]", object_id=2, location_map=20, uses_lanky=True, ),
    BarrelLocation( "Factory In Path Near Arcade [Chunky]", object_id=14, location_map=26, uses_chunky=True, ),
    BarrelLocation( "Factory Top of Production Room [Tiny]", object_id=16, location_map=26, uses_tiny=True, ),
    BarrelLocation( "Factory In Storage Room [Diddy]", object_id=13, location_map=26, uses_diddy=True, ),
    BarrelLocation( "Factory Top of Block Tower In Testing [Diddy]", object_id=0, location_map=26, uses_diddy=True, ),
    BarrelLocation( "Factory Above Door To R&D In Testing [Lanky]", object_id=15, location_map=26, uses_lanky=True, ),
    BarrelLocation( "Galleon 5 Door Ship [DK]", object_id=0, location_map=46, uses_dk=True, ),
    BarrelLocation( "Galleon 5 Door Ship [Diddy]", object_id=0, location_map=43, uses_diddy=True, ),
    BarrelLocation( "Galleon 5 Door Ship [Chunky]", object_id=1, location_map=43, uses_chunky=True, ),
    BarrelLocation( "Galleon Treasure Room [Diddy]", object_id=6, location_map=30, uses_diddy=True, ),
    BarrelLocation( "Galleon Treasure Room [Lanky]", object_id=7, location_map=30, uses_lanky=True, ),
    BarrelLocation( "Galleon Submarine [Tiny]", object_id=3, location_map=179, uses_tiny=True, ),
    BarrelLocation( "Galleon 2 Door Ship [Tiny]", object_id=0, location_map=47, uses_tiny=True, ),
    BarrelLocation( "Fungi Behind Night Gated Area In Barn [DK]", object_id=3, location_map=59, uses_dk=True, ),
    BarrelLocation( "Fungi Top of Giant Mushroom [Diddy]", object_id=18, location_map=48, uses_diddy=True, ),
    BarrelLocation( "Fungi Top of the Owl Tree [Diddy]", object_id=21, location_map=48, uses_diddy=True, ),
    BarrelLocation( "Fungi Room on Top of Giant Mushroom [Lanky]", object_id=0, location_map=63, uses_lanky=True, ),
    BarrelLocation( "Fungi Inside Giant Mushroom [Tiny]", object_id=8, location_map=64, uses_tiny=True, ),
    BarrelLocation( "Fungi Baboon Blast Course [DK]", object_id=22, location_map=188, uses_dk=True, ),
    BarrelLocation( "Caves Baboon Blast Course [DK]", object_id=19, location_map=186, uses_dk=True, ),
    BarrelLocation( "Caves In Waterfall by Funky's [Diddy]", object_id=6, location_map=72, uses_diddy=True, ),
    BarrelLocation( "Caves W3 Room [Tiny]", object_id=7, location_map=72, uses_tiny=True, ),
    BarrelLocation( "Caves 5 Door Cabin [Chunky]", object_id=0, location_map=90, uses_chunky=True, ),
    BarrelLocation( "Castle Top of the Castle [Diddy]", object_id=9, location_map=87, uses_diddy=True, ),
    BarrelLocation( "Castle Ballroom [Diddy]", object_id=1, location_map=88, uses_diddy=True, ),
    BarrelLocation( "Castle Dungeon Left Side in Basement [Lanky]", object_id=0, location_map=163, uses_lanky=True, ),
    BarrelLocation( "Castle Wind Room in Tower [Lanky]", object_id=0, location_map=105, uses_lanky=True, ),
    BarrelLocation( "Castle Basement Tunnel [Tiny]", object_id=0, location_map=151, uses_tiny=True, ),
    BarrelLocation( "Castle Crypt [Chunky]", object_id=0, location_map=112, uses_chunky=True, ),
    BarrelLocation( "Castle Tree [Chunky]", object_id=0, location_map=164, uses_chunky=True, ),
    BarrelLocation( "Isles Snide's Room [Diddy]", object_id=2, location_map=195, uses_diddy=True, ),
    BarrelLocation( "Isles Summit of DK Island [Diddy]", object_id=11, location_map=34, uses_diddy=True, ),
    BarrelLocation( "Isles Castle Lobby [Lanky]", object_id=2, location_map=193, uses_lanky=True, ),
    BarrelLocation( "Isles Aztec Lobby [Tiny]", object_id=1, location_map=173, uses_tiny=True, ),
    BarrelLocation( "Isles Helm Lobby [Chunky]", object_id=10, location_map=170, uses_chunky=True, ),
    BarrelLocation( "Helm DK's Room Left", object_id=15, location_map=17, uses_dk=True, ),
    BarrelLocation( "Helm DK's Room Right", object_id=16, location_map=17, uses_dk=True, ),
    BarrelLocation( "Helm Chunky's Room Left", object_id=14, location_map=17, uses_chunky=True, ),
    BarrelLocation( "Helm Chunky's Room Right", object_id=7, location_map=17, uses_chunky=True, ),
    BarrelLocation( "Helm Tiny's Room Left", object_id=12, location_map=17, uses_tiny=True, ),
    BarrelLocation( "Helm Tiny's Room Right", object_id=13, location_map=17, uses_tiny=True, ),
    BarrelLocation( "Helm Lanky's Room Left", object_id=10, location_map=17, uses_lanky=True, ),
    BarrelLocation( "Helm Lanky's Room Right", object_id=11, location_map=17, uses_lanky=True, ),
    BarrelLocation( "Helm Diddy's Room Left", object_id=8, location_map=17, uses_diddy=True, ),
    BarrelLocation( "Helm Diddy's Room Right", object_id=9, location_map=17, uses_diddy=True, ),
    
    # Not putting the training barrels in the pool for the time being
    # BarrelLocation( "Training - Bottom Left", object_id=4, location_map=176, ),
    # BarrelLocation( "Training - Top Left", object_id=3, location_map=176, ),
    # BarrelLocation( "Training - Top Right", object_id=5, location_map=176, ),
    # BarrelLocation( "Training - Bottom Right", object_id=6, location_map=176, ),
]