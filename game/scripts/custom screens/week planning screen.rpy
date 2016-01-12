#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""

    python:
        weekPlanArray = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
    
screen weekPlan():
    window:
        xfill True
        yfill True
        has vbox:
            text "Morning lessons: "
            hbox xfill True:
                use selectLesson("Monday", 0)
                use selectLesson("Tuseday", 1)
                use selectLesson("Wednesday", 2)
                use selectLesson("Thursday", 3)
                use selectLesson("Friday", 4)

            text "----"
                
            text "Afternoon activities: "
            hbox xfill True:
                use selectActivities("Monday", 0)
                use selectActivities("Tuseday", 1)
                use selectActivities("Wednesday", 2)
                use selectActivities("Thursday", 3)
                use selectActivities("Friday", 4)
                
        textbutton "Start the week" action Return(weekPlanArray)
                
screen selectLesson(day, dayNum):
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            text weekPlanArray[dayNum][0]
            
            for lesson in game.lessons: 
                if lesson["available"]:
                    # The second action here is purely to allow the correct buttons to show up as selected.
                    textbutton lesson["name"] action([SetDict(weekPlanArray, [dayNum][0], [lesson["lesson"], weekPlanArray[dayNum][1]]),SetScreenVariable("lessonType" + day, lesson["name"] + day)]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

screen selectActivities(day, dayNum):
    default activityType = ""
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            text weekPlanArray[dayNum][1]
            
            for activity in game.activities: 
                if activity["available"]:
                    #textbutton activity["name"] action SetDict(weekPlanArray, [dayNum][0], [weekPlanArray[dayNum][0], activity["activity"]]) xfill True
                    textbutton activity["name"] action([SetDict(weekPlanArray, [dayNum][0], [weekPlanArray[dayNum][0], activity["activity"]]),SetScreenVariable("activityType" + day, activity["name"] + day)]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

