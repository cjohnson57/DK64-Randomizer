from object_data.loading_zone_data import loading_zones, map_list
import random

def set_loading_zones(asm: str, post_data: dict):
    loadingzonesCopy = [x for x in loading_zones]
    finalLoadingZoneList = [ ]
    loadingzonesSpoilerLog = [ ]

    logdata = str()
    logdata += "\n" + "\n"
    logdata += "Loading Zones:" + "\n"

    remainingLoadingZones = [x for x in loadingzonesCopy]

    for x in loadingzonesCopy:
        pickRandomLoadingZone = random.choice(remainingLoadingZones)
        remainingLoadingZones.remove(pickRandomLoadingZone)
        loadingzonesSpoilerLog.append(str(x) + " - " + str(pickRandomLoadingZone))

    loadingzonesSpoilerLog.sort()
    for x in loadingzonesSpoilerLog:
        logdata += str(x) + "\n"

    return asm, logdata