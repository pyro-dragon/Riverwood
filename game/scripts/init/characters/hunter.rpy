#-----------------------------
# Hunter
#-----------------------------
init:
    $crt_hunter = GameCharacter("Kacela", "Bloodrunner", crr_hunter, Character("crt_hunter.name", dynamic = True, color = "#5ca75c"), renpy.image("hunter", "characters/hunter.png"), False, True, "hunterTN.png")
    $crt_hunter.addPreference(CharacterPreference("exploring", True, "I love to explore!"))
    $crt_hunter.addPreference(CharacterPreference("hunting", True, "I love hunting!"))
    $crt_hunter.addPreference(CharacterPreference("meat", True, "Nom! Lets eat meat!"))
    $crt_hunter.addPreference(CharacterPreference("peace", False, "Ugh, this is so boring."))
    $crt_hunter.addPreference(CharacterPreference("buildings", False, "I hate how they have ruined the natural landscape."))
    $crt_hunter.addPreference(CharacterPreference("vegetables", False, "Blegh! Meat is the only thing!"))
    $crt_hunter.addPreference(CharacterPreference("dull", False, "Ugh, this is so boring."))
    define h = crt_hunter.c