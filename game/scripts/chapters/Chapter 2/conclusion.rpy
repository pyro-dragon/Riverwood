#-----------------------------------------------------------
# The conclusion to the first week
#-----------------------------------------------------------

label endOfFirstWeek: 
    
    # Pass time along into evening.
    $game.advanceTime()
    
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
    
    return