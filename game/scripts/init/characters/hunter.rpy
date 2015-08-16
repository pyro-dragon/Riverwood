#-----------------------------
# Hunter
#-----------------------------
init 1:
    $crt_hunter = GameCharacter("Kacela", "Bloodrunner", "hunter", Character("crt_hunter.name", dynamic = True, color = "#5ca75c"), "characters/hunter.png", False, True, "hunterTN.png")
    $crt_hunter.addPreference(CharacterPreference("exploring", True, "I love to explore!"))
    $crt_hunter.addPreference(CharacterPreference("hunting", True, "I love hunting!"))
    $crt_hunter.addPreference(CharacterPreference("meat", True, "Nom! Lets eat meat!"))
    $crt_hunter.addPreference(CharacterPreference("peace", False, "Ugh, this is so boring."))
    $crt_hunter.addPreference(CharacterPreference("buildings", False, "I hate how they have ruined the natural landscape."))
    $crt_hunter.addPreference(CharacterPreference("vegetables", False, "Blegh! Meat is the only thing!"))
    $crt_hunter.addPreference(CharacterPreference("dull", False, "Ugh, this is so boring."))
    define h = crt_hunter.c
    
    # Special topics
    $crt_hunter.addTopic(Topic("repeat", "repeat"))
    $crt_hunter.addTopic(Topic("late", "late"))
    
    # Regualr topics
    $crt_hunter.addTopic(Topic("How are you doing?", "howYouDoing", False))
    $crt_hunter.addTopic(Topic("Do you like this place?", "thisPlace", False))
    $crt_hunter.addTopic(Topic("What are you into?", "whatInto", False))
    
label hunter_howYouDoing: 
    h "Ok, I guess."
    h "How about you?"
    
    menu: 
        "I'm doing fine. Thanks for asking.": 
            h "Fair enough!"
            
        "Not so good really.": 
            h "Ehh, we all feel crappy sometimes"
            
    return
            
label hunter_thisPlace:
    
    # Allow the player to talk about the new place
    
    # A loved place
    if game.currentLocation.name == "Glade": 
        h "It's alright I think."
        h "The fresh air, away from the smog and noise of the den feels good."
        h "It lets my senses really expand so I can smell scent trails and listen for prey."
        $crt_hunter.addRP(5)
        
        return
        
    # A hated place
    if game.currentLocation.name == "Forge":
        h "I hate it. Why did you even bring me here?"
        h "Its noisy and dirty and so enclosed."
        $crt_hunter.addRP(-5)
        
        return
    
    # Everything else
    h "I suppose its ok. I don't think its terrible."
    
    return
    
label hunter_whatInto: 
    h "Into?"
    h "Well hunting is my primary skill. I love the stalking of prey, the wait for just the right moment."
    h "Or the running through the trees, dodging this way and that, using teamwork to bring down prey."
    h "It really gets my blood pumping."
    h "Outside of that I have an interest in herbs and medicine. "
    
    return
    
label hunter_repeat:
    h "Ughh, don't make me repeat myself."
    
label hunter_late:
    h "Its kinda getting late. I need to head off now."