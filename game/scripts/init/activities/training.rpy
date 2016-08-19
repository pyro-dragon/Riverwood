#-------------------------------------------------------------------------------
# The activity mapper for the training activity
#-------------------------------------------------------------------------------

init: 
    $trainingLessonCount = 0

# Entry point for the training activity
label training:
    
    if trainingLessonCount == 0: 
        call training1
        
    scene black with fade
    $player.changeSkillBonus("training", 1)
    "..."
    "... ..."
    
    $trainingLessonCount = trainingLessonCount +1
            
    return
    
# The intro to the training activity
label training1:
    $game.setLocation(arena)
    
    show Marrack with dissolve 
    
    M "So, you guys are here for a sample of what the Daggermaws can offter?"
    M "I don't think we are for just anyone."
    M "If you want to take some lessons from us they are going to be hard, brutal."
    M "But for those that don't shy away from a challenge then we can offer you life skills- skills that will ensure you keep your life."
    
    if player.family == "Bloodrunner": 
        M "Though I guess you guys will be getting trained on some aspects of combat, I don't think Shana teaches much in the way of combat when its up close and personal."
        M "A bow is all very well and good when you can get a good clear shot at a target, but when you are surrounded by dense undergrowth and its teaming with rain an axe is your best friend."

    elif player.family == "Coppertail": 
        M "I would assume that many of you are thinking that your brains beat braun any day. And for some of you that might be right if you don't venture too far from your workshop."
        M "However a grounding in basic martial combat will help you feel a lot safer when conducting field work."

    elif player.family == "Gildclaw": 
        M "As representatives of Temesh's trade and diplomatic missions you will be required to travel to strange and far away lands."
        M "There are many out there that dislike our kind and will not hesitate to draw a blade on you. "
        M "Bandits, thieves and hunters are all out for you so you better get familier with a weapon if you want your career to be a long one."

    M "So then, with the introduction out of the way I want you all to take a training staff and find a sparing partner..."
    
    return
    