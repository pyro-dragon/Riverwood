#-----------------------------
# Ally
#-----------------------------
init 1: 
    $crt_ally = GameCharacter("Ellie", "none", "none", Character("crt_ally.name", dynamic = True, color = "#848484"), renpy.image("ellie", "characters/ellie.png"), True, False, "ellieTN.png")
    $crt_ally.rp = 45
    $crt_ally.addPreference(CharacterPreference("exploring", True, "I love looking around interesting places."))
    $crt_ally.addPreference(CharacterPreference("animals", True, "Aww, I just love cute animals."))
    $crt_ally.addPreference(CharacterPreference("peace", True, "This is really lovely."))
    $crt_ally.addPreference(CharacterPreference("destruction", False, "Thats terrible! Such a waste."))
    $crt_ally.addPreference(CharacterPreference("making", False, "I am really not very good at making things."))
    $crt_ally.addPreference(CharacterPreference("danger", False, "That is way too scary for me"))
    define e = crt_ally.c