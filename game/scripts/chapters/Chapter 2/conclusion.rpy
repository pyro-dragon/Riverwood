#-----------------------------------------------------------
# The conclusion to the first week
#-----------------------------------------------------------

label endOfFirstWeek: 
    
    # Pass time along into evening.
    #$game.advanceTime()
    
    # Show the camp
    $game.setLocation(camp)
    
    show expression crt_ally.image with dissolve
    
    a "Wow, what a week that was." 
    a "So many new things to learn, my head is spinning."
    a "how did you find it?"
    menu:
        "Whoa, yeah. That was one heck of a week.":
            a "ywah, wasn't it? Right?"
            a "I didn't think signing up for the [crt_ally.family] family would mean a complete tour of the others."
            
        "Oh, it was a breeze":
            $crt_ally.addRP(-1)
            a "It was huh?"
            a "Well I guess you must think you are something special."

    a "I am sorry I didn't get to down to you during the week, I was just so busy."
    a "How about we hang out tomorrow now the weekend is here. "
    a "We can have a good long chat about how its all been."
    a "I'll catch you later!"
    
    scene black with fade
    
    # Suppress the weekend menu. We will introduce it with an event instead
    $game.gameLoop.suppressMenu = True
    
    return
    
label endOfFirstWeekTaunt: 
    
    # Show the camp
    $game.setLocation(camp)
    
    show expression crt_rival.image with dissolve
    
    r "Hey there loser."
    r "Hows the [player.family] losers?"
    P "Well-"
    r "I don't even care."
    r "I've been busy with the [crt_rival.family]s."
    
    if crt_rival.family == "Bloodrunner": 
        r "I've been learning all about poisons and traps and things, all sorts of dangerous stuff."
        
    elif crt_rival.family == "Coppertail": 
        r "I've been building all kinds of things. Huge things covered in spikes that shoot flames."
        
    elif crt_rival.family == "Daggermaw": 
        r "I've been learning fifty different ways to kick your ass."
        
    elif crt_rival.family == "Gildclaws": 
        r "I've been trying amazing spices and foods from all kinds of exoticcand far away lands."
    
    r "I'd say you should ask to change your family choice but I don't think you have the substance for our family."
    r "I just hope you and your family don't end up dragging down the rest of the clan."
    
    r "Later."
    
    scene black with fade
    
    return
    