#-----------------------------
# Player
#-----------------------------
init:
    $playerCompanion = "none"
    $peopleKnown = 2
    $discoveredPlaces = 0
    $player = GameCharacter("Rodger", "Coppertail", crr_mechanic, Character("player.name", dynamic = True, color = "#848484"), renpy.image("hunter", "characters/hunter.png"), True, False, "hunterTN.png")
    define P = player.c

    $playerCompanion = "none"