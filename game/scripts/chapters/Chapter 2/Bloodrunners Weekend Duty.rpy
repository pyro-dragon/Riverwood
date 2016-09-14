#-------------------------------------------------------------------------------
# The first weekend duty for the Bloodrunnerss
#-------------------------------------------------------------------------------

label weekendDutyBloodrunner:
    "Bloodrunner duty"
    
    return
    
#-------------------------------------------------------------------------------
# The first weekend duty for the Coppertails
#-------------------------------------------------------------------------------

label weekendDutyCoppertail:
    "Coppertail duty"
    
    return
    
#-------------------------------------------------------------------------------
# The first weekend duty for the Daggermaws
#-------------------------------------------------------------------------------

label weekendDutyDaggermaw:
    "Daggermaw duty"
    
    return
    
#-------------------------------------------------------------------------------
# The first weekend duty for the Gildclaws
#-------------------------------------------------------------------------------

label weekendDutyGildclaw:
    "Gildclaw duty"
    
    return
    
label allyWeekendTalk:
    "Ally talk"
    
    a "Hey there [player.name]!"
    a "Glad you could make it!"
    a "did you have to weasel you way out of something today? I heard the family leaders have been hauling in people to work over the weekend."
    
    menu:
        "Yeah, i got asked to help out the [player.family]s":
            a "Oh no, I am so sorry, I hope you don't get into trouble about that."
            
        "No, its fine.":
         a "That's a relief, i don't want to think I've gotten you in trouble."
        "I don't weasel!":
            a "Alright, alright, clam down. You don't have to get so touchy."
            crt_ally.addRP(-1)
    
    return