#-----------------------------
# Mechanic
#-----------------------------
init 1: 
    $crt_mechanic = GameCharacter("Maria", "Coppertail", "mechanic", Character("crt_mechanic.name", dynamic = True, color = "#5ca75c"), "characters/maria.png", False, True, "mariaTN.png")
    $crt_mechanic.addPreference(CharacterPreference("making", True, "I love to create stuff."))
    $crt_mechanic.addPreference(CharacterPreference("buildings", True, "Just look at these amazing things!"))
    $crt_mechanic.addPreference(CharacterPreference("shooting", True, "Bang bang! Ha ha ha."))
    $crt_mechanic.addPreference(CharacterPreference("destruction", False, "Its all broken. What a shame."))
    $crt_mechanic.addPreference(CharacterPreference("dull", False, "I am so bored now."))
    $crt_mechanic.addPreference(CharacterPreference("savage", False, "Wow, jsut look at that. Its shameful!"))
    define m = crt_mechanic.c
    
    # Special topics
    $crt_mechanic.addTopic(Topic("repeat", "repeat"))
    $crt_mechanic.addTopic(Topic("late", "late"))
    
    # Regualr topics
    $crt_mechanic.addTopic(Topic("How are you doing?", "howYouDoing", False))
    $crt_mechanic.addTopic(Topic("Do you like this place?", "thisPlace", False))
    $crt_mechanic.addTopic(Topic("What are you into?", "whatInto", False))
    
label mechanic_howYouDoing: 
    m "I'm alright, thanks!"
    m "How about you?"
    
    menu: 
        "I'm doing fine. Thanks for asking.": 
            m "Thats great to hear!"
            
        "Not so good really.": 
            m "Awr! Thats not good!"
            
    return
            
label mechanic_thisPlace:
    
    # Allow the player to talk about the new place
    
    # A loved place
    if game.currentLocation.name == "Forge": 
        m "I think its fantastic!"
        m "Look at all the cool stuff in here!"
        m "Honestly, I can't spend enough time here. I am so happy that our clan has a place like this."
        m "I have spent so much of my cubhood staring at Clarence's forge and helping out when I can and now I am finally part of it all!"
        $crt_mechanic.addRP(5)
        
        return
        
    # A hated place
    if game.currentLocation.name == "Glade":
        m "Umm, I am not too fond of this place actully."
        m "There is a feeling in the air that I don't like, it feels like... resentment."
        m "It was a bit of a long treck out to here too and there really isn't much to see."
        m "I'm sorry, I don't want to sound like I'm complaining, but you could have picked a better place."
        $crt_mechanic.addRP(-5)
        
        return
    
    # Everything else
    m "Its ok I guess. Nothing special really."
    
    return
    
label mechanic_whatInto: 
    m "Ooooo, thats a hard question."
    m "Building stuff, taking stuff appart."
    m "Bending stuff, welding stuff"
    m "Thats it, I think"
    
    return
    
label mechanic_repeat:
    m "I already told you that, silly."
    
label mechanic_late:
    m "Its getting really late. We should head back now."