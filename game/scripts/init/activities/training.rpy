#-------------------------------------------------------------------------------
# The activity mapper for the training activity
#-------------------------------------------------------------------------------

init: 
    $trainingLessonCount = 0

# Entry point for the training activity
label training:
    
        if trainingCount == 0: 
            call training1
            return
            
        scene black with fade
        $player.changeSkillBonus("training", 1)
        "..."
        "... ..."

            
return
    
# The intro to the training activity
label training1:
    $game.setLocation(glade)
    
    show Marrack with dissolve
    
    M ""
    
    if player.family == "Bloodrunner": 
        M ""

    elif player.family == "Coppertail": 
        M ""

    elif player.family == "Gildclaw": 
        M ""

    M ""
    
    return
    