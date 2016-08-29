#-------------------------------------------------------------------------------
# The end of week assesment by the family heads
#-------------------------------------------------------------------------------

label endOfWeekAssesment:
    if player.family == "Bloodrunner"; 
        call bloodrunnersEndOfWeek1
    elif player.family == "Coppertail": 
        call coppertailsEndOfWeek1
    elif player.family == "Daggermaw": 
        call daggermawEndOfWeek1
    elif player.family == "Gildclaw": 
        call gildclawEndOfWeek1
    else
        $renpy.say("DEBUG", "Error: No valid family selected.")

    return

label bloodrunnersEndOfWeek1: 
    
    $game.setLocation(glade)
    
    show Shana with dissolve

    S "Well here we are my young blossoms. The end of your first week of training."
    S "I hope you have all had an enlightening experiance and learned a lot so far."
    S "Next week it will be down to you to decide your destiny."
    S "You may choose to train with any of the other families at for least three days a week."
    
    return

label coppertailsEndOfWeek1: 
    return
    
label daggermawEndOfWeek1: 
    return
    
label gildclawEndOfWeek1: 
    return