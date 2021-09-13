from object_data.bonus_barrel_data import bonus_barrels, barrel_locations
import random

# Shuffle Bonus Barrels
def set_bonus_barrels(asm: str, post_data: dict):
    barrelGamesDK = [x for x in bonus_barrels if x.uses_dk == True]
    barrelGamesDiddy = [x for x in bonus_barrels if x.uses_diddy == True]
    barrelGamesLanky = [x for x in bonus_barrels if x.uses_lanky == True]
    barrelGamesTiny = [x for x in bonus_barrels if x.uses_tiny == True]
    barrelGamesChunky = [x for x in bonus_barrels if x.uses_chunky == True]

    barrelLocationsDK = [x for x in barrel_locations if x.uses_dk == True]
    barrelLocationsDiddy = [x for x in barrel_locations if x.uses_diddy == True]
    barrelLocationsLanky = [x for x in barrel_locations if x.uses_lanky == True]
    barrelLocationsTiny = [x for x in barrel_locations if x.uses_tiny == True]
    barrelLocationsChunky = [x for x in barrel_locations if x.uses_chunky == True]

    finalBarrelList = [ ]
    barrelSpoilerLog = [ ]

    logdata = str()
    logdata += "\n" + "\n"
    logdata += "Bonus Barrels:" + "\n"
    
    for x in barrelLocationsDK:
        pickRandomBarrelDK = random.choice(barrelGamesDK)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelDK.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelDK))

    for x in barrelLocationsDiddy:
        pickRandomBarrelDiddy = random.choice(barrelGamesDiddy)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelDiddy.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelDiddy))

    for x in barrelLocationsLanky:
        pickRandomBarrelLanky = random.choice(barrelGamesLanky)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelLanky.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelLanky))

    for x in barrelLocationsTiny:
        pickRandomBarrelTiny = random.choice(barrelGamesTiny)
        finalBarrelList.append(
            {
                "minigame_map_index": pickRandomBarrelTiny.map_index,
                "barrel_map_location": x.location_map,
                "bonus_id": x.object_id
            }
            )
        barrelSpoilerLog.append(str(x) + " - " + str(pickRandomBarrelTiny))

    for x in barrelLocationsChunky:
        pickRandomBarrelChunky = random.choice(barrelGamesChunky)
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