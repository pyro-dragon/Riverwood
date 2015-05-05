#-----------------------------
# Rival
#-----------------------------
init 1:
    $crt_rival = GameCharacter("Charrd", "none", "none", Character("crt_rival.name", dynamic = True, color = "#9999e6"), "characters/charrd.png", True, False, "charrdTN.png")
    $crt_rival.rp = 9
    $crt_rival.addPreference(CharacterPreference("action", True, "Yeah! That looks fun."))
    $crt_rival.addPreference(CharacterPreference("danger", True, "Sounds like great fun!"))
    $crt_rival.addPreference(CharacterPreference("exploring", True, "Lets go looking for trouble."))
    $crt_rival.addPreference(CharacterPreference("peace", False, "So damn quiet!"))
    $crt_rival.addPreference(CharacterPreference("dull", False, "That is really dull!"))
    $crt_rival.addPreference(CharacterPreference("savage", False, "I like a bit of action but that is just crazy!"))
    define c = crt_rival.c