#-----------------------------
# Player
#-----------------------------
init:
    $playerCompanion = "none"
    $peopleKnown = 2
    $discoveredPlaces = 0
    $player = GameCharacter("Unnamed Player", "", "", Character("player.name", dynamic = True, color = "#848484"), "", True, False, "")
    define P = player.c

    $playerCompanion = "none"