from object_data.bonus_barrel_data import bonus_barrels, barrel_locations
import random

# Shuffle Bonus Barrels
def set_bonus_barrels(asm: str, post_data: dict):
    bonusBarrelsCopy = [x for x in bonus_barrels]
    finalBarrelList = [ ]
    barrelSpoilerLog = [ ]

    logdata = str()
    logdata += "\n" + "\n"
    logdata += "Bonus Barrels:" + "\n"
    
    barrelLocationsDK = [x for x in barrel_locations if x.uses_dk == True]
    barrelGamesDK = [x for x in bonusBarrelsCopy if x.uses_dk == True]

    for x in barrelLocationsDK:
        pickRandomBarrelDK = random.choice(barrelGamesDK)
        barrelGamesDK.remove(pickRandomBarrelDK)
        bonusBarrelsCopy.remove(pickRandomBarrelDK)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelDK.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelDK))

    barrelLocationsDiddy = [x for x in barrel_locations if x.uses_diddy == True]
    barrelGamesDiddy = [x for x in bonusBarrelsCopy if x.uses_diddy == True]

    for x in barrelLocationsDiddy:
        pickRandomBarrelDiddy = random.choice(barrelGamesDiddy)
        barrelGamesDiddy.remove(pickRandomBarrelDiddy)
        bonusBarrelsCopy.remove(pickRandomBarrelDiddy)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelDiddy.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelDiddy))

    barrelLocationsLanky = [x for x in barrel_locations if x.uses_lanky == True]
    barrelGamesLanky = [x for x in bonusBarrelsCopy if x.uses_lanky == True]

    for x in barrelLocationsLanky:
        pickRandomBarrelLanky = random.choice(barrelGamesLanky)
        barrelGamesLanky.remove(pickRandomBarrelLanky)
        bonusBarrelsCopy.remove(pickRandomBarrelLanky)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelLanky.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelLanky))

    barrelLocationsTiny = [x for x in barrel_locations if x.uses_tiny == True]
    barrelGamesTiny = [x for x in bonusBarrelsCopy if x.uses_tiny == True]

    for x in barrelLocationsTiny:
        pickRandomBarrelTiny = random.choice(barrelGamesTiny)
        barrelGamesTiny.remove(pickRandomBarrelTiny)
        bonusBarrelsCopy.remove(pickRandomBarrelTiny)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelTiny.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelTiny))

    barrelLocationsChunky = [x for x in barrel_locations if x.uses_chunky == True]
    barrelGamesChunky = [x for x in bonusBarrelsCopy if x.uses_chunky == True]

    for x in barrelLocationsChunky:
        pickRandomBarrelChunky = random.choice(barrelGamesChunky)
        barrelGamesChunky.remove(pickRandomBarrelChunky)
        bonusBarrelsCopy.remove(pickRandomBarrelChunky)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelChunky.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelChunky))
    
    barrelSpoilerLog.sort()
    for x in barrelSpoilerLog:
        logdata += str(x) + "\n"

    return asm, logdata