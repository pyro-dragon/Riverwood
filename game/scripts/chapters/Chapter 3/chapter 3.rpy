#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

init:
    $lessons = {"bloodrunnerLesson" : 1,"coppertailLesson" : 1, "daggermawLesson" : 1, "gildclawLesson" : 1}
    #$[bloodrunnerLesson = 1
    #$coppertailLesson = 1
    #$daggermawLesson = 1
    #$gildclawLesson = 1

    $currentDay = 1
    $missionTree = 0
    $missionNumber = 0

label chapter3:
    if player.family == "Bloodrunner": 
        $missionTree = bloodrunnerMissions
    elif player.family == "Coppertail":
        $missionTree = coppertailMissions
    elif player.family == "Daggermaw":
        $missionTree = daggermawMissions
    elif player,family == "Gildclaw":
        $missionTree = gildclawMissions
    
    #call screen activity

    # Pre-invasion story
    while currentDay < 15:
        $allowAfternoon = True
        
        # Show mission screen
        call chapter("Day " + str(currentDay), missionTree[missionNumber].missionLabel)
        
        # Check if we can proceed with this mission or the player has missed a conditional
        if missionTree[missionNumber].condition() == True: 
            call expression missionTree[missionNumber].conditionPassLabel
            $allowAfternoon = missionTree[missionNumber].overrideAfternoon
            $missionNumber += 1
        else:
            call expression missionTree[missionNumber].conditionFailLabel
        
        # Check if the player is allowed an afternoon activity
        if allowAfternoon == True: 
            #call screen activity
            "### Activity Screen ###"
        
        # Progress to the next day
        $currentDay += 1
        
    return
        
label mainActivityCycle:
    # Call the appropriate lesson
    call expression (lessonTarget + str(lessons[lessonTarget]))
    
    # Advance the lesson count
    $lessons[lessonTarget] += 1
    
    # Perform todays activity
    call expression activityTarget
    
    # Check to see if we can make any quests active
    $game.checkForActiveQuests()
    
    # Perform quest updates
    $game.updateActiveQuests()
    
    jump chapter3