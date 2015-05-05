#-----------------------------
# Player
#-----------------------------
init:
    $playerCompanion = "none"
    $peopleKnown = 2
    $discoveredPlaces = 0
    #$crt_mechanic = GameCharacter("Maria", "Coppertail", crr_mechanic, Character("crt_mechanic.name", dynamic = True, color = "#5ca75c"), "characters/maria.png", False, True, "mariaTN.png")
    #$player = GameCharacter("Unnamed Player", "", "", Character("player.name", dynamic = True, color = "#848484"), "", True, False, "")
    $player = GameCharacter("Unnamed Player", "Daggermaw", crr_mechanic, Character("player.name", dynamic = True, color = "#848484"), "", True, False, "")
    define P = player.c

    $playerCompanion = "none"