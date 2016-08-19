#-----------------------------
# Ally
#-----------------------------
init 1: 
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/ally.json")
        
        # Create the player
        crt_ally = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("crt_ally.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            crt_ally.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))
    
    # Add to datable list
    $game.dateableCharacters.append(crt_ally)
    
    # Create renpy character
    define a = crt_ally.c
    
    # Special topics
    $crt_ally.addTopic(Topic("repeat", "repeat"))
    $crt_ally.addTopic(Topic("late", "late"))
    
    # Regualr topics
    $crt_ally.addTopic(Topic("How are you doing?", "howYouDoing", False))
    $crt_ally.addTopic(Topic("Do you like this place?", "thisPlace", False))
    $crt_ally.addTopic(Topic("What are you into?", "whatInto", False))
    
    # Narative related topics
    $crt_ally.addTopic(Topic("Why did you choose a different family to me?", "whyDiffFam", False))
    $crt_ally.addTopic(Topic("How has your first week been?", "howHandlingWeek", False))
    
label ally_whyDiffFam: 
    a "Well, I kind of liked what the [crt_ally.family] family offered."
    a "You know I have been into that kind of stuff for a while."
    a "You don't mind do you?"
    
    menu: 
        "Not at all, we have our own lives to lead.": 
            a "Yeah. I'm still your best friend and you can always talk to me about anything."
            $ally_whyDiffFam_badchoice = False
            
        "Well, I thought we were supposed to be best friends": 
            $crt_ally.addRP(-1)
            a "I know we did everything together when we were growing up but we have our own life goals."
            $ally_whyDiffFam_badchoice = True
            
    
label ally_howHandlingWeek:
    a "Its been really crazy."
    a "I thought I would spend more time getting acustomed to the [crt_ally.family] family, but I've been mostly scooted around the other families."
    a "'Getting a taster' of everything else for the most part."
    a "I can't wait to get down to the real stuff."
    
label ally_hangOutMuch: 
    P "Do you think you will have much time to hang out like we used to?"
    
    if ally_whyDiffFam_badchoice == True:
        a "Well I don't know. I am going to be very busy working with the [crt_ally.family]s now."
    else: 
        a "I think so. I am sure we can get some time outside our new duties to hangout."
        a "And hey, we get the weekends off at least."
    
label ally_howYouDoing: 
    a "Kind of tired really, I've been doing a lot of things lately"
    a "How about you?"
    
    menu: 
        "I'm doing fine. Thanks for asking.": 
            h "Fair enough!"
            
        "Not so good really.": 
            h "Ehh, we all feel crappy sometimes"
            
    return
            
label ally_thisPlace:
    
    # Allow the player to talk about the new place
    
    # A loved place
    if game.currentLocation.name == "Glade": 
        h "It's alright I think."
        h "The fresh air, away from the smog and noise of the den feels good."
        h "It lets my senses really expand so I can smell scent trails and listen for prey."
        $crt_ally.addRP(5)
        
        return
        
    # A hated place
    if game.currentLocation.name == "Forge":
        h "I hate it. Why did you even bring me here?"
        h "Its noisy and dirty and so enclosed."
        $crt_ally.addRP(-5)
        
        return
    
    # Everything else
    h "I suppose its ok. I don't think its terrible."
    
    return
    
label ally_whatInto: 
    h "Into?"
    h "Well hunting is my primary skill. I love the stalking of prey, the wait for just the right moment."
    h "Or the running through the trees, dodging this way and that, using teamwork to bring down prey."
    h "It really gets my blood pumping."
    h "Outside of that I have an interest in herbs and medicine. "
    
    return
    
label ally_repeat:
    h "Ughh, don't make me repeat myself."
    
label ally_late:
    h "Its kinda getting late. I need to head off now."