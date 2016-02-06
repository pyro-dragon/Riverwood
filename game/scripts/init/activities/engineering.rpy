#-------------------------------------------------------------------------------
# The activity mapper for the engineering activity
#-------------------------------------------------------------------------------

init: 
    $engineeringLessonCount = 0

label engineering:
    
        if engineeringCount == 0: 
            call engineering1
            return
            
return
    
label engineering1:
    $game.setLocation(camp)
    
    show Clarence with dissolve
    
    C "Ah, welcome, welcome!"
    C "It is good to see all you youngsters"
    C "I am Clarance Coppertail and I am the head of the Coppertail family."
    C "As you may know already, we deal with the exciting field of technology and craftwork!"
    
    if player.family == "Bloodrunner": 
        C "Now some of you would be questioning what that has to do with you."
        C "You guys are Bloodrunners arn't you? You are all about understanding nature and making use of what she has to offer."
        C "Almost the polar opposite of us with our machines and tools and experimentation."
        C "In fact you will find we are very similar! We seek to understand nature and use it as best we can."
        C "To find the best metals we need to understand geology. To build strong buildings we need to understand how to grow strong timber."
        C "The Coppertails and Bloodrunners have a long history of working together on all kinds of projects."