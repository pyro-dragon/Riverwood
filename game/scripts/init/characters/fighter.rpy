#-----------------------------
# Fighter
#-----------------------------
init 1:
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/fighter.json")
        
        # Create the player
        crt_fighter = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("crt_fighter.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            crt_fighter.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))

    # Add to datable list
    $game.dateableCharacters.append(crt_fighter)
    
    # Create renpy character
    define f = crt_fighter.c
    
    # Special topics
    $crt_fighter.addTopic(Topic("repeat", "repeat"))
    $crt_fighter.addTopic(Topic("late", "late"))
    
    # Regualr topics
    $crt_fighter.addTopic(Topic("How are you doing?", "howYouDoing", False))
    $crt_fighter.addTopic(Topic("Do you like this place?", "thisPlace", False))
    $crt_fighter.addTopic(Topic("What are you into?", "whatInto", False))
    
label fighter_howYouDoing: 
    f "Really pumped!"
    f "How about you, pipsqueek?"
    
    menu: 
        "I'm doing fine. Thanks for asking.": 
            f "Well thats good, tell me if you want to wrestle sometime and we will sort that right out!"
            
        "Not so good really.": 
            "Ohh, did wittle baby hurt themselves!"
            
    return
            
label fighter_thisPlace:
    
    # Allow the player to talk about the new place
    
    # A loved place
    if game.currentLocation.name == "Arena": 
        f "It gets me feeling pumped!"
        f "I take a look at this place and I can just feel the warriors from long ago when this place was first built."
        f "I can just feel the history of this place coursing though me, you know?"
        f "It makes me want to roar!"
        f "ROAGHHHHH!"
        $crt_fighter.addRP(5)
        
        return
        
    # A hated place
    if game.currentLocation.name == "Tent":
        f "Yeah, this place really isn't my style."
        f "Look at how gharish it is, what is that smell in the air?"
        f "Look at these tiny cups, I can't even get a finger throught the handle."
        f "Lets never go here again, ok?"
        
        $crt_fighter.addRP(-5)
        
        return
    
    # Everything else
    f "I like it. Not terrile."
    
    return
    
label fighter_whatInto: 
    f "Wbat do you think pipsqueek?"
    f "Getting ripped!"
    
    return
    
label fighter_repeat:
    f "What? Didn't you hear me the first time?"
    
label fighter_late:
    f "Damn, the suns getting low. I gotta head off now, busting some more PT at sunrise you know?"