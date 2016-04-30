#-------------------------------------------------------------------------------
# The activity mapper for the reading activity
#-------------------------------------------------------------------------------

init: 
    $readingLessonCount = 0

# Entry point for the training activity
label reading:
    
        if readingLessonCount == 0: 
            call reading1
            return
            
        scene black with fade
        $player.changeSkillBonus("reading", 1)
        "..."
        "... ..."

            
return
    
# The intro to the reading activity
label reading1:
    $game.setLocation(glade)
    
    show Temesh with dissolve
    
    T ""
    
    if player.family == "Bloodrunner": 
        T ""

    elif player.family == "Coppertail": 
        T ""

    elif player.family == "Gildclaw": 
        T ""

    T ""
    
    return
    