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
    S "The remaining two days will be spend training with the Bloodrunners."
    S "Now then, it is a fine, Spring day that we have been blessed with and I see no reason not to finish early and let you all enjoy it."
    S "But before I do I must make a request for any volenteers to help perform important Bloodrunner duties this weekend."
    
    menu:
        "Volenteer":
            P "I'd like to volenteer please."
            S "Ah, thank you very much [player.name]."
            S "Now, is there anyone else?"
            S "..."
            S "Anyone?"
            hide Shana with dissolve
            
            show crt_hunter.image with dissolve
            h "Ugh, I guess I had better volenteer then."
            hide crt_hunter.image with dissolve
            
            show Shana with dissolve
            S "Bless you [crt_hunter.name]!"
    
        "Stay silent":
            S "..."
            S "Anyone?"
            S "I would have hoped you would all be eager to demonstrate your family loyalties."
            S "But, alas, the draw of the weekend is strong. "
            S "In that case I will choose."
            S "[crt_hunter.name]"
            hide Shana
            
            show crt_hunter.image
            h "Me??"
            hide crt_hunter.image
            
            show Shana 
            S "And, [player.name]."
            
    S "Please meet me here at the Glade at first light tomorrow."
    S "Thank you again, your loyalty to your family will be noted."
    hide Shana
    
    show crt_hunter.image
    h "Whatever."
    hide crt_hunter.image
    
    show Shana
    S "Now you all may go, see you all next week."
    hide Shana with dissolve
        
    return

label coppertailsEndOfWeek1: 
    return
    
label daggermawEndOfWeek1: 
    return
    
label gildclawEndOfWeek1: 
    return