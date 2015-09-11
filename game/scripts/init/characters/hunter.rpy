#-----------------------------
# Hunter
#-----------------------------
init 1:
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/hunter.json")
        
        # Create the player
        crt_hunter = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("crt_hunter.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            crt_hunter.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))
    
    # Add to datable list
    game.dateableCharacters.append(crt_hunter)
    
    # Create renpy character
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