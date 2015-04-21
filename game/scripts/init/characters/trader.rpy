#-----------------------------
# Trader
#-----------------------------
init: 
    $crt_trader = GameCharacter("Denmar", "Gildclaw", crr_trader, Character("crt_trader.name", dynamic = True, color = "#5ca75c"), renpy.image("trader", "characters/trader.png"), False, True, "traderTN.png")
    $crt_trader.addPreference(CharacterPreference("art", True, "This is truely delightful!"))
    $crt_trader.addPreference(CharacterPreference("gold", True, "Oh my, my, my. Yes, yes, gold... "))
    $crt_trader.addPreference(CharacterPreference("peace", True, "Ah, this is so nice."))
    $crt_trader.addPreference(CharacterPreference("dirt", False, "This is a bit too grimy..."))
    $crt_trader.addPreference(CharacterPreference("action", False, "Thats too much for me I'm afrade."))
    $crt_trader.addPreference(CharacterPreference("scary", False, "That is too scary, I don't like it!"))
    define t = crt_trader.c