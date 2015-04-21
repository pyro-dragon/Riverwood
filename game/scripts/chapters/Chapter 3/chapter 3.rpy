#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

init:
    $lessons = {"bloodrunnerLesson" : 1,"coppertailLesson" : 1, "daggermawLesson" : 1, "gildclawLesson" : 1}
    #$[bloodrunnerLesson = 1
    #$coppertailLesson = 1
    #$daggermawLesson = 1
    #$gildclawLesson = 1

    $daysPassed = 0

label chapter3:
    
    call screen activity

    while daysPassed < 6:
        "The day is [daysPassed]"
        $daysPassed += 1
        call screen activity
        
label mainActivityCycle:
    # Call the appropriate lesson
    call expression (lessonTarget + str(lessons[lessonTarget]))
    
    # Advance the lesson count
    $lessons[lessonTarget] += 1
    
    call expression activityTarget
    
    jump chapter3