#-------------------------------------------------------------------------------
# The activity mapper for the reading activity
#-------------------------------------------------------------------------------

init: 
    $readingLessonCount = 0

# Entry point for the training activity
label reading:
    
    if readingLessonCount == 0: 
        call reading1
        
    scene black with fade
    $player.changeSkillBonus("reading", 1)
    "..."
    "... ..."

    return
            
return
    
# The intro to the reading activity
label reading1:
    $game.setLocation(tent)
    
    show Temesh with dissolve
    
    T "Welcome to the Gildclaw enclave."
    T "As some of you may know, we, the Riverwood clan are a world power."
    T "Our name is known as far away as the sandy deserts of XXXX and the dense, bustling cities of YYYY."
    T "It is here that we train our fine, young diplomats and traders wo go out into the world to negotiate deals, spread good relations and represent our clan."
    T "I am more than a little proud of my family and I a most grateful that you have chosen to take some lessons from me."
    
    if player.family == "Bloodrunner": 
        T "I am glad that some of you have chosen to take lessons from the Gildclaws. You are depended upon to attack or defend convoys. "
        T "Knowlege we give you on foreign relations and trade practices will help you pick out smugglers from legitimate traffic."

    elif player.family == "Coppertail": 
        T "Ever since your family was founded the Guildclaws and Coppertails have worked closely together. "
        T "A knowledge of trade and the price fluxuations in materials with serve you well in the decisions you make and engineers."
        T "For those persuing a more scientific career, our lessons can help you developed the more refined and delecate manorisms that demand respect in academic circles"

    elif player.family == "Daggermaw": 
        T "Some may find it strange that Daggermaws have chosen to spend time learning from the Gildclaws."
        T "However when we need guards to protect our traders or acompany diplomats on long missions, we always take Daggermaws. And Daggermaws with training in foreign relations are always the first to be chosen."

    T "Todays lesson will be a brief overview of the surrounding lands and who governs them."
    T "Now, let me start with Estansia. This is a land that has had a long history of peace with the Empire..."
    
    $readingLessonCount += 1
    
    return
    