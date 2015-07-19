#-------------------------------------------------------------------------------
# This is the start of chapter three and the place where the main game cycle 
# begins.
#-------------------------------------------------------------------------------

#---------------------------------------
# Set up the initial variables
#---------------------------------------
init:
    $lessons = {"bloodrunnerLesson" : 1,"coppertailLesson" : 1, "daggermawLesson" : 1, "gildclawLesson" : 1}
    #$[bloodrunnerLesson = 1
    #$coppertailLesson = 1
    #$daggermawLesson = 1
    #$gildclawLesson = 1

    $currentDay = 1
    $missionTree = 0
    $missionNumber = 0

#---------------------------------------
# The Chapter 3 start point
#---------------------------------------
label chapter3:
    # Set the mission tree based on the player family
    if player.family == "Bloodrunner": 
        $missionTree = bloodrunnerMissions
    elif player.family == "Coppertail":
        $missionTree = coppertailMissions
    elif player.family == "Daggermaw":
        $missionTree = daggermawMissions
    elif player,family == "Gildclaw":
        $missionTree = gildclawMissions
    
    #call screen activity

    # Pre-invasion story- Cycle throug the days, advancing the missions when needed
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
