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
    
    a "It's so wierd isn't it?"
    a "It seems like it was only yesterday tgat we were young cubs, running about the den with no cares in the world."
    a "Now here we are, already one week into your new lives, learning about all kinds of stuff, having to make our own way in the world."
    
    menu:
        "Quit pining, we have grown up now. We have to deal with things how they are now, not how they were."
            a "Well, I guess you are right. But you didn't need to put it quite like that."
            crt_ally.addRR(-1)
            
        "Yeah, I remember when we used to play around together."
            P "I remeber when you said you wanted to be a [crt_ally.career]. And now look at you, in the [crt_ally.family] family and learning to be a [crt_ally.career]!" 
            a "I remember, yeah! Life certainly moves on, and up."
            
     a "I wonder how the next year will work out for us."
     a "I hope I have what it takes to be a great [crt_ally.career]"
     
     menu:
         "You will be fine! I know you can do it!"
             a "Aww, than you for beliving in me."
             a "But I just wish that was al, it took hough"
             
    
    return