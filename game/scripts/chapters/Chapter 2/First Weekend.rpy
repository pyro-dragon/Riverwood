#-------------------------------------------------------------------------------
# The first weekend the player experiances. 
# Tell them how weekends work and present them with the choice between relationships and duty. 
#-------------------------------------------------------------------------------

label firstWeekend:
    
    # Call the various weekend intros depending on family
    call firstWeekendIntro
    
    scene black with fade
    
    # Present the player with a choice
    menu:
        "Report for your duties with the [player.family]": 
            $renpy.call("weekendDuty" + player.family)
        "Sneak off to talk to [crt_ally.name]": 
            call allyWeekendTalk
            
    # Once everything has played out, let the player pick things for their weekend
    call planNewWeekend
    
    return
    
# Pick the right label for the right family. 
# Possibly replace this with variable name for the label.
label firstWeekendIntro: 
    if player.family == "Bloodrunner": 
        call firstWeekendBloodrunners
    elif player.family == "Coppertail": 
        call firstWeekendCoppertails
    elif player.family == "Daggermaw": 
        call firstWeekendDaggermaw
    elif player.family == "Gildclaw": 
        call firstWeekendGildclaw
    else:
        $renpy.say("DEBUG", "Error: No valid family selected.")

    return