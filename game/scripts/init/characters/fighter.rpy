#-----------------------------
# Fighter
#-----------------------------
init:
    $crt_fighter = GameCharacter("Crasher", "Daggermaw", crr_fighter, Character("crt_fighter.name", dynamic = True, color = "#5ca75c"), renpy.image("fighter", "characters/fighter.png"), False, True, "fighterTN.png")
    $crt_fighter.addPreference(CharacterPreference("savage", True, "Ha ha, it would be better if there was more blood!"))
    $crt_fighter.addPreference(CharacterPreference("running", True, "I'll race you!"))
    $crt_fighter.addPreference(CharacterPreference("combat", True, "This is what I like! Bring on the challenegers!"))
    $crt_fighter.addPreference(CharacterPreference("intelligence", False, "Pfft, that's for those with weak muscles."))
    $crt_fighter.addPreference(CharacterPreference("dull", False, "Ughhhhh, that is so boring."))
    $crt_fighter.addPreference(CharacterPreference("art", False, "Its a thing. Can I eat it? Can I smash it? No? Its useless."))
    define f = crt_fighter.c