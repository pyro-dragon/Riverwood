#-----------------------------
# Mechanic
#-----------------------------
init: 
    $crt_mechanic = GameCharacter("Maria", "Coppertail", crr_mechanic, Character("crt_mechanic.name", dynamic = True, color = "#5ca75c"), renpy.image("mechanic", "characters/maria.png"), False, True, "mariaTN.png")
    $crt_mechanic.addPreference(CharacterPreference("making", True, "I love to create stuff."))
    $crt_mechanic.addPreference(CharacterPreference("buildings", True, "Just look at these amazing things!"))
    $crt_mechanic.addPreference(CharacterPreference("shooting", True, "Bang bang! Ha ha ha."))
    $crt_mechanic.addPreference(CharacterPreference("destruction", False, "Its all broken. What a shame."))
    $crt_mechanic.addPreference(CharacterPreference("dull", False, "I am so bored now."))
    $crt_mechanic.addPreference(CharacterPreference("savage", False, "Wow, jsut look at that. Its shameful!"))
    define m = crt_mechanic.c