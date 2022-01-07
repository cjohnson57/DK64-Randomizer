"""File that shuffles loading zone exits."""
from randomizer.Enums.Exits import Exits
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Levels import Levels


class ShufflableExit:
    """Class that stores data about an exit to be shuffled."""
    def __init__(self, region, reverse):
        self.region = region
        self.reverse = reverse
        # Here dest is the entrance to go to, rather than just the target region
        self.dest = None
        self.shuffled = False

ShufflableExits = {
    # Level Exits
    Exits.IslesToJapes: ShufflableExit(Regions.JungleJapesLobby, Exits.JapesToIsles),
    Exits.JapesToIsles: ShufflableExit(Regions.JungleJapesMain, Exits.IslesToJapes),
    Exits.IslesToAztec: ShufflableExit(Regions.AngryAztecLobby, Exits.AztecToIsles),
    Exits.AztecToIsles: ShufflableExit(Regions.AngryAztecStart, Exits.IslesToAztec),
    Exits.IslesToFactory: ShufflableExit(Regions.FranticFactoryLobby, Exits.FactoryToIsles),
    Exits.FactoryToIsles: ShufflableExit(Regions.FranticFactoryStart, Exits.IslesToFactory),
    Exits.IslesToGalleon: ShufflableExit(Regions.GloomyGalleonLobby, Exits.GalleonToIsles),
    Exits.GalleonToIsles: ShufflableExit(Regions.GloomyGalleonStart, Exits.IslesToGalleon),
    Exits.IslesToForest: ShufflableExit(Regions.FungiForestLobby, Exits.ForestToIsles),
    Exits.ForestToIsles: ShufflableExit(Regions.FungiForestStart, Exits.IslesToForest),
    Exits.IslesToCaves: ShufflableExit(Regions.CrystalCavesLobby, Exits.CavesToIsles),
    Exits.CavesToIsles: ShufflableExit(Regions.CrystalCavesMain, Exits.IslesToCaves),
    Exits.IslesToCastle: ShufflableExit(Regions.CreepyCastleLobby, Exits.CastleToIsles),
    Exits.CastleToIsles: ShufflableExit(Regions.CreepyCastleMain, Exits.IslesToCastle),
    Exits.IslesToHelm: ShufflableExit(Regions.HideoutHelmLobby, Exits.HelmToIsles),
    Exits.HelmToIsles: ShufflableExit(Regions.HideoutHelmStart, Exits.IslesToHelm),
    # DK Isles Exits
    Exits.IslesStartToMain: ShufflableExit(Regions.Start, Exits.IslesMainToStart),
    Exits.IslesMainToStart: ShufflableExit(Regions.IslesMain, Exits.IslesStartToMain),
    Exits.IslesMainToPrison: ShufflableExit(Regions.IslesMain, Exits.IslesPrisonToMain),
    Exits.IslesPrisonToMain: ShufflableExit(Regions.Prison, Exits.IslesMainToPrison),
    Exits.IslesMainToFairy: ShufflableExit(Regions.IslesMain, Exits.IslesFairyToMain),
    Exits.IslesFairyToMain: ShufflableExit(Regions.BananaFairyRoom, Exits.IslesMainToFairy),
    Exits.IslesMainToSnideRoom: ShufflableExit(Regions.CrocodileIsleBeyondLift, Exits.IslesSnideRoomToMain),
    Exits.IslesSnideRoomToMain: ShufflableExit(Regions.IslesSnideRoom, Exits.IslesMainToSnideRoom),
    Exits.IslesMainToJapesLobby: ShufflableExit(Regions.IslesMain, Exits.IslesJapesLobbyToMain),
    Exits.IslesJapesLobbyToMain: ShufflableExit(Regions.JungleJapesLobby, Exits.IslesMainToJapesLobby),
    Exits.IslesMainToAztecLobby: ShufflableExit(Regions.IslesMain, Exits.IslesAztecLobbyToMain),
    Exits.IslesAztecLobbyToMain: ShufflableExit(Regions.AngryAztecLobby, Exits.IslesMainToAztecLobby),
    Exits.IslesMainToFactoryLobby: ShufflableExit(Regions.CrocodileIsleBeyondLift, Exits.IslesFactoryLobbyToMain),
    Exits.IslesFactoryLobbyToMain: ShufflableExit(Regions.FranticFactoryLobby, Exits.IslesMainToFactoryLobby),
    Exits.IslesMainToGalleonLobby: ShufflableExit(Regions.IslesMain, Exits.IslesGalleonLobbyToMain),
    Exits.IslesGalleonLobbyToMain: ShufflableExit(Regions.GloomyGalleonLobby, Exits.IslesMainToGalleonLobby),
    Exits.IslesMainToForestLobby: ShufflableExit(Regions.CabinIsle, Exits.IslesForestLobbyToMain),
    Exits.IslesForestLobbyToMain: ShufflableExit(Regions.FungiForestLobby, Exits.IslesMainToForestLobby),
    Exits.IslesMainToCavesLobby: ShufflableExit(Regions.IslesMain, Exits.IslesCavesLobbyToMain),
    Exits.IslesCavesLobbyToMain: ShufflableExit(Regions.CrystalCavesLobby, Exits.IslesMainToCavesLobby),
    Exits.IslesMainToCastleLobby: ShufflableExit(Regions.IslesMain, Exits.IslesCastleLobbyToMain),
    Exits.IslesCastleLobbyToMain: ShufflableExit(Regions.CreepyCastleLobby, Exits.IslesMainToCastleLobby),
    Exits.IslesMainToHelmLobby: ShufflableExit(Regions.IslesMain, Exits.IslesHelmLobbyToMain),
    Exits.IslesHelmLobbyToMain: ShufflableExit(Regions.HideoutHelmLobby, Exits.IslesMainToHelmLobby),
    # Jungle Japes Exits
    Exits.JapesMainToMine: ShufflableExit(Regions.JungleJapesMain, Exits.JapesMineToMain),
    Exits.JapesMineToMain: ShufflableExit(Regions.Mine, Exits.JapesMainToMine),
    Exits.JapesMainToLankyCave: ShufflableExit(Regions.IslesMain, Exits.JapesLankyCaveToMain),
    Exits.JapesLankyCaveToMain: ShufflableExit(Regions.JapesLankyCave, Exits.JapesMainToLankyCave),
    Exits.JapesMainToCatacomb: ShufflableExit(Regions.JungleJapesMain, Exits.JapesCatacombToMain),
    Exits.JapesCatacombToMain: ShufflableExit(Regions.JapesCatacomb, Exits.JapesMainToCatacomb),
    Exits.JapesMainToTinyHive: ShufflableExit(Regions.JapesBeyondFeatherGate, Exits.JapesTinyHiveToMain),
    Exits.JapesTinyHiveToMain: ShufflableExit(Regions.TinyHive, Exits.JapesMainToTinyHive),
    Exits.JapesMineToCarts: ShufflableExit(Regions.Mine, Exits.JapesCartsToMine),
    Exits.JapesCartsToMine: ShufflableExit(Regions.JapesMinecarts, Exits.JapesMineToCarts),
    # Angry Aztec Exits
    Exits.AztecStartToTemple: ShufflableExit(Regions.AngryAztecStart, Exits.AztecTempleToStart),
    Exits.AztecTempleToStart: ShufflableExit(Regions.TempleStart, Exits.AztecStartToTemple),
    Exits.AztecMainToDonkey: ShufflableExit(Regions.AngryAztecMain, Exits.AztecDonkeyToMain),
    Exits.AztecDonkeyToMain: ShufflableExit(Regions.DonkeyTemple, Exits.AztecMainToDonkey),
    Exits.AztecMainToDiddy: ShufflableExit(Regions.AngryAztecMain, Exits.AztecDiddyToMain),
    Exits.AztecDiddyToMain: ShufflableExit(Regions.DiddyTemple, Exits.AztecMainToDiddy),
    Exits.AztecMainToLanky: ShufflableExit(Regions.AngryAztecMain, Exits.AztecLankyToMain),
    Exits.AztecLankyToMain: ShufflableExit(Regions.LankyTemple, Exits.AztecMainToLanky),
    Exits.AztecMainToTiny: ShufflableExit(Regions.AngryAztecMain, Exits.AztecTinyToMain),
    Exits.AztecTinyToMain: ShufflableExit(Regions.TinyTemple, Exits.AztecMainToTiny),
    Exits.AztecMainToChunky: ShufflableExit(Regions.AngryAztecMain, Exits.AztecChunkyToMain),
    Exits.AztecChunkyToMain: ShufflableExit(Regions.ChunkyTemple, Exits.AztecMainToChunky),
    Exits.AztecMainToRace: ShufflableExit(Regions.AngryAztecMain, Exits.AztecRaceToMain),
    Exits.AztecRaceToMain: ShufflableExit(Regions.AztecTinyRace, Exits.AztecMainToRace),
    Exits.AztecMainToLlama: ShufflableExit(Regions.AngryAztecMain, Exits.AztecLlamaToMain),
    Exits.AztecLlamaToMain: ShufflableExit(Regions.LlamaTemple, Exits.AztecMainToLlama),
    # Frantic Factory Exits
    Exits.FactoryRandDToRace: ShufflableExit(Regions.RandD, Exits.FactoryRaceToRandD),
    Exits.FactoryRaceToRandD: ShufflableExit(Regions.FactoryTinyRace, Exits.FactoryRandDToRace),
    Exits.FactoryChunkyRoomToPower: ShufflableExit(Regions.ChunkyRoomPlatform, Exits.FactoryPowerToChunkyRoom),
    Exits.FactoryPowerToChunkyRoom: ShufflableExit(Regions.PowerHut, Exits.FactoryChunkyRoomToPower),
    Exits.FactoryBeyondHatchToInsideCore: ShufflableExit(Regions.BeyondHatch, Exits.FactoryInsideCoreToBeyondHatch),
    Exits.FactoryInsideCoreToBeyondHatch: ShufflableExit(Regions.InsideCore, Exits.FactoryBeyondHatchToInsideCore),
    # Gloomy Galleon Exits
    Exits.GalleonLighthouseAreaToLighthouse: ShufflableExit(Regions.LighthouseArea, Exits.GalleonLighthouseToLighthouseArea),
    Exits.GalleonLighthouseToLighthouseArea: ShufflableExit(Regions.Lighthouse, Exits.GalleonLighthouseAreaToLighthouse),
    Exits.GalleonLighthousAreaToMermaid: ShufflableExit(Regions.LighthouseArea, Exits.GalleonMermaidToLighthouseArea),
    Exits.GalleonMermaidToLighthouseArea: ShufflableExit(Regions.MermaidRoom, Exits.GalleonLighthousAreaToMermaid),
    Exits.GalleonLighthouseAreaToSickBay: ShufflableExit(Regions.LighthouseArea, Exits.GalleonSickBayToLighthouseArea),
    Exits.GalleonSickBayToLighthouseArea: ShufflableExit(Regions.SickBay, Exits.GalleonLighthouseAreaToSickBay),
    Exits.GalleonShipyardToSeal: ShufflableExit(Regions.Shipyard, Exits.GalleonSealToShipyard),
    Exits.GalleonSealToShipyard: ShufflableExit(Regions.SealRace, Exits.GalleonShipyardToSeal),
    Exits.GalleonShipyardToSubmarine: ShufflableExit(Regions.Shipyard, Exits.GalleonSubmarineToShipyard),
    Exits.GalleonSubmarineToShipyard: ShufflableExit(Regions.Submarine, Exits.GalleonShipyardToSubmarine),
    Exits.GalleonShipyardToMechafish: ShufflableExit(Regions.Shipyard, Exits.GalleyonMechafishToShipyard),
    Exits.GalleyonMechafishToShipyard: ShufflableExit(Regions.Mechafish, Exits.GalleonShipyardToMechafish),
    Exits.GalleonShipyardToLanky: ShufflableExit(Regions.Shipyard, Exits.GalleonLankyToShipyard),
    Exits.GalleonLankyToShipyard: ShufflableExit(Regions.LankyShip, Exits.GalleonShipyardToLanky),
    Exits.GalleonShipyardToTiny: ShufflableExit(Regions.Shipyard, Exits.GalleonTinyToShipyard),
    Exits.GalleonTinyToShipyard: ShufflableExit(Regions.TinyShip, Exits.GalleonShipyardToTiny),
    Exits.GalleonShipyardToBongos: ShufflableExit(Regions.Shipyard, Exits.GalleonBongosToShipyard),
    Exits.GalleonBongosToShipyard: ShufflableExit(Regions.BongosShip, Exits.GalleonShipyardToBongos),
    Exits.GalleonShipyardToGuitar: ShufflableExit(Regions.Shipyard, Exits.GalleonGuitarToShipyard),
    Exits.GalleonGuitarToShipyard: ShufflableExit(Regions.GuitarShip, Exits.GalleonShipyardToGuitar),
    Exits.GalleonShipyardToTrombone: ShufflableExit(Regions.Shipyard, Exits.GalleonTromboneToShipyard),
    Exits.GalleonTromboneToShipyard: ShufflableExit(Regions.TromboneShip, Exits.GalleonShipyardToTrombone),
    Exits.GalleonShipyardToSaxophone: ShufflableExit(Regions.Shipyard, Exits.GalleonSaxophoneToShipyard),
    Exits.GalleonSaxophoneToShipyard: ShufflableExit(Regions.SaxophoneShip, Exits.GalleonShipyardToSaxophone),
    Exits.GalleonShipyardToTriangle: ShufflableExit(Regions.Shipyard, Exits.GalleonTriangleToShipyard),
    Exits.GalleonTriangleToShipyard: ShufflableExit(Regions.TriangleShip, Exits.GalleonShipyardToTriangle),
    Exits.GalleonTreasureToChest: ShufflableExit(Regions.TreasureRoom, Exits.GalleonChestToTreasure),
    Exits.GalleonChestToTreasure: ShufflableExit(Regions.TinyChest, Exits.GalleonTreasureToChest),
    # Fungi Forest Exits
    Exits.ForestMainToCarts: ShufflableExit(Regions.FungiForestStart, Exits.ForestCartsToMain),
    Exits.ForestCartsToMain: ShufflableExit(Regions.ForestMinecarts, Exits.ForestMainToCarts),
    Exits.ForestMainToLowerMushroom: ShufflableExit(Regions.GiantMushroomArea, Exits.ForestLowerMushroomToMain),
    Exits.ForestLowerMushroomToMain: ShufflableExit(Regions.MushroomLower, Exits.ForestMainToLowerMushroom),
    Exits.ForestLowerExteriorToLowerMushroom: ShufflableExit(Regions.MushroomLowerExterior, Exits.ForestLowerMushroomToLowerExterior),
    Exits.ForestLowerMushroomToLowerExterior: ShufflableExit(Regions.MushroomLower, Exits.ForestLowerExteriorToLowerMushroom),
    Exits.ForestLowerExteriorToUpperMushroom: ShufflableExit(Regions.MushroomLowerExterior, Exits.ForestUpperMushroomToLowerExterior),
    Exits.ForestUpperMushroomToLowerExterior: ShufflableExit(Regions.MushroomUpper, Exits.ForestLowerExteriorToUpperMushroom),
    Exits.ForestUpperExteriorToUpperMushroom: ShufflableExit(Regions.MushroomUpperExterior, Exits.ForestUpperMushroomToUpperExterior),
    Exits.ForestUpperMushroomToUpperExterior: ShufflableExit(Regions.MushroomUpper, Exits.ForestUpperExteriorToUpperMushroom),
    Exits.ForestExteriorToNight: ShufflableExit(Regions.MushroomNightExterior, Exits.ForestNightToExterior),
    Exits.ForestNightToExterior: ShufflableExit(Regions.MushroomNightDoor, Exits.ForestExteriorToNight),
    Exits.ForestExteriorToChunky: ShufflableExit(Regions.MushroomUpperExterior, Exits.ForestChunkyToExterior),
    Exits.ForestChunkyToExterior: ShufflableExit(Regions.MushroomChunkyRoom, Exits.ForestExteriorToChunky),
    Exits.ForestExteriorToZingers: ShufflableExit(Regions.MushroomUpperExterior, Exits.ForestZingersToExterior),
    Exits.ForestZingersToExterior: ShufflableExit(Regions.MushroomLankyZingersRoom, Exits.ForestExteriorToZingers),
    Exits.ForestExteriorToMushrooms: ShufflableExit(Regions.MushroomUpperExterior, Exits.ForestMushroomsToExterior),
    Exits.ForestMushroomsToExterior: ShufflableExit(Regions.MushroomLankyMushroomsRoom, Exits.ForestExteriorToMushrooms),
    Exits.ForestTreeToAnthill: ShufflableExit(Regions.HollowTreeArea, Exits.ForestAnthillToTree),
    Exits.ForestAnthillToTree: ShufflableExit(Regions.Anthill, Exits.ForestTreeToAnthill),
    Exits.ForestMainToChunkyMill: ShufflableExit(Regions.MillArea, Exits.ForestChunkyMillToMain),
    Exits.ForestChunkyMillToMain: ShufflableExit(Regions.MillChunkyArea, Exits.ForestMainToChunkyMill),
    Exits.ForestMainToTinyMill: ShufflableExit(Regions.MillArea, Exits.ForestTinyMillToMain),
    Exits.ForestTinyMillToMain: ShufflableExit(Regions.MillTinyArea, Exits.ForestMainToTinyMill),
    Exits.ForestMainToGrinder: ShufflableExit(Regions.MillArea, Exits.ForestGrinderToMain),
    Exits.ForestGrinderToMain: ShufflableExit(Regions.GrinderRoom, Exits.ForestMainToGrinder),
    Exits.ForestMainToRafters: ShufflableExit(Regions.MillArea, Exits.ForestRaftersToMain),
    Exits.ForestRaftersToMain: ShufflableExit(Regions.MillRafters, Exits.ForestMainToRafters),
    Exits.ForestMainToWench: ShufflableExit(Regions.MillArea, Exits.ForestWenchToMain),
    Exits.ForestWenchToMain: ShufflableExit(Regions.WenchRoom, Exits.ForestMainToWench),
    Exits.ForestMainToAttic: ShufflableExit(Regions.MillArea, Exits.ForestAtticToMain),
    Exits.ForestAtticToMain: ShufflableExit(Regions.MillAttic, Exits.ForestMainToAttic),
    Exits.ForestTinyMillToSpider: ShufflableExit(Regions.MillTinyArea, Exits.ForestSpiderToTinyMill),
    Exits.ForestSpiderToTinyMill: ShufflableExit(Regions.SpiderRoom, Exits.ForestTinyMillToSpider),
    Exits.ForestTinyMillToGrinder: ShufflableExit(Regions.MillTinyArea, Exits.ForestGrinderToTinyMill),
    Exits.ForestGrinderToTinyMill: ShufflableExit(Regions.GrinderRoom, Exits.ForestTinyMillToGrinder),
    Exits.ForestMainToBarn: ShufflableExit(Regions.ThornvineArea, Exits.ForestBarnToMain),
    Exits.ForestBarnToMain: ShufflableExit(Regions.ThornvineBarn, Exits.ForestMainToBarn),
    # Crystal Caves Exits
    Exits.CavesMainToRace: ShufflableExit(Regions.CrystalCavesMain, Exits.CavesRaceToMain),
    Exits.CavesRaceToMain: ShufflableExit(Regions.CavesLankyRace, Exits.CavesMainToRace),
    Exits.CavesMainToCastle: ShufflableExit(Regions.CrystalCavesMain, Exits.CavesCastleToMain),
    Exits.CavesCastleToMain: ShufflableExit(Regions.FrozenCastle, Exits.CavesMainToCastle),
    Exits.CavesIglooToDonkey: ShufflableExit(Regions.IglooArea, Exits.CavesDonkeyToIgloo),
    Exits.CavesDonkeyToIgloo: ShufflableExit(Regions.DonkeyIgloo, Exits.CavesIglooToDonkey),
    Exits.CavesIglooToDiddy: ShufflableExit(Regions.IglooArea, Exits.CavesDiddyToIgloo),
    Exits.CavesDiddyToIgloo: ShufflableExit(Regions.DiddyIgloo, Exits.CavesIglooToDiddy),
    Exits.CavesIglooToLanky: ShufflableExit(Regions.IglooArea, Exits.CavesLankyToIgloo),
    Exits.CavesLankyToIgloo: ShufflableExit(Regions.LankyIgloo, Exits.CavesIglooToLanky),
    Exits.CavesIglooToTiny: ShufflableExit(Regions.IglooArea, Exits.CavesTinyToIgloo),
    Exits.CavesTinyToIgloo: ShufflableExit(Regions.TinyIgloo, Exits.CavesIglooToTiny),
    Exits.CavesIglooToChunky: ShufflableExit(Regions.IglooArea, Exits.CavesChunkyToIgloo),
    Exits.CavesChunkyToIgloo: ShufflableExit(Regions.ChunkyIgloo, Exits.CavesIglooToChunky),
    Exits.CavesCabinToRotating: ShufflableExit(Regions.CabinArea, Exits.CavesRotatingToCabin),
    Exits.CavesRotatingToCabin: ShufflableExit(Regions.RotatingCabin, Exits.CavesCabinToRotating),
    Exits.CavesCabinToDonkey: ShufflableExit(Regions.CabinArea, Exits.CavesDonkeyToCabin),
    Exits.CavesDonkeyToCabin: ShufflableExit(Regions.DonkeyCabin, Exits.CavesCabinToDonkey),
    Exits.CavesCabinToDiddyLower: ShufflableExit(Regions.CabinArea, Exits.CavesDiddyLowerToCabin),
    Exits.CavesDiddyLowerToCabin: ShufflableExit(Regions.DiddyLowerCabin, Exits.CavesCabinToDiddyLower),
    Exits.CavesCabinToDiddyUpper: ShufflableExit(Regions.CabinArea, Exits.CavesDiddyUpperToCabin),
    Exits.CavesDiddyUpperToCabin: ShufflableExit(Regions.DiddyUpperCabin, Exits.CavesCabinToDiddyUpper),
    Exits.CavesCabinToLanky: ShufflableExit(Regions.CabinArea, Exits.CavesLankyToCabin),
    Exits.CavesLankyToCabin: ShufflableExit(Regions.LankyCabin, Exits.CavesCabinToLanky),
    Exits.CavesCabinToTiny: ShufflableExit(Regions.CabinArea, Exits.CavesTinyToCabin),
    Exits.CavesTinyToCabin: ShufflableExit(Regions.TinyCabin, Exits.CavesCabinToTiny),
    Exits.CavesCabinToChunky: ShufflableExit(Regions.CabinArea, Exits.CavesChunkyToCabin),
    Exits.CavesChunkyToCabin: ShufflableExit(Regions.ChunkyCabin, Exits.CavesCabinToChunky),
    # Creepy Castle Exits
    Exits.CastleMainToTree: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleTreeToMain),
    Exits.CastleTreeToMain: ShufflableExit(Regions.CastleTree, Exits.CastleMainToTree),
    Exits.CastleMainToLibrary: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleLibraryToMain),
    Exits.CastleLibraryToMain: ShufflableExit(Regions.Library, Exits.CastleMainToLibrary),
    Exits.CastleMainToBallroom: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleBallroomToMain),
    Exits.CastleBallroomToMain: ShufflableExit(Regions.Ballroom, Exits.CastleMainToBallroom),
    Exits.CastleMainToTower: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleTowerToMain),
    Exits.CastleTowerToMain: ShufflableExit(Regions.Tower, Exits.CastleMainToTower),
    Exits.CastleMainToGreenhouse: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleGreenhouseToMain),
    Exits.CastleGreenhouseToMain: ShufflableExit(Regions.Greenhouse, Exits.CastleMainToGreenhouse),
    Exits.CastleMainToTrash: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleTrashToMain),
    Exits.CastleTrashToMain: ShufflableExit(Regions.TrashCan, Exits.CastleMainToTrash),
    Exits.CastleMainToShed: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleShedToMain),
    Exits.CastleShedToMain: ShufflableExit(Regions.Shed, Exits.CastleMainToShed),
    Exits.CastleMainToMuseum: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleMuseumToMain),
    Exits.CastleMuseumToMain: ShufflableExit(Regions.Museum, Exits.CastleMainToMuseum),
    Exits.CastleMainToLower: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleLowerToMain),
    Exits.CastleLowerToMain: ShufflableExit(Regions.LowerCave, Exits.CastleMainToLower),
    Exits.CastleMainToUpper: ShufflableExit(Regions.CreepyCastleMain, Exits.CastleUpperToMain),
    Exits.CastleUpperToMain: ShufflableExit(Regions.UpperCave, Exits.CastleMainToUpper),
    Exits.CastleWaterfallToUpper: ShufflableExit(Regions.CastleWaterfall, Exits.CastleUpperToWaterfall),
    Exits.CastleUpperToWaterfall: ShufflableExit(Regions.UpperCave, Exits.CastleWaterfallToUpper),
    Exits.CastleBallroomToRace: ShufflableExit(Regions.Ballroom, Exits.CastleRaceToBallroom),
    Exits.CastleRaceToBallroom: ShufflableExit(Regions.CastleTinyRace, Exits.CastleBallroomToRace),
    Exits.CastleLowerToCrypt: ShufflableExit(Regions.LowerCave, Exits.CastleCryptToLower),
    Exits.CastleCryptToLower: ShufflableExit(Regions.Crypt, Exits.CastleLowerToCrypt),
    Exits.CastleLowerToMauseoleum: ShufflableExit(Regions.LowerCave, Exits.CastleMausoleumToLower),
    Exits.CastleMausoleumToLower: ShufflableExit(Regions.Mausoleum, Exits.CastleLowerToMauseoleum),
    Exits.CastleCryptToCarts: ShufflableExit(Regions.Crypt, Exits.CastleCartsToCrypt),
    Exits.CastleCartsToCrypt: ShufflableExit(Regions.CastleMinecarts, Exits.CastleCryptToCarts),
    Exits.CastleUpperToDungeon: ShufflableExit(Regions.UpperCave, Exits.CastleDungeonToUpper),
    Exits.CastleDungeonToUpper: ShufflableExit(Regions.Dungeon, Exits.CastleUpperToDungeon),
}
