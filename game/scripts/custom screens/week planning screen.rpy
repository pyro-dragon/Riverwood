#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""

    python:
        activityArray = [[], [], [], [], []]
    
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
                
screen selectLesson(day, dayNum):
    default lessonType = ""
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for lesson in game.lessons: 
                if lesson["available"]:
                    textbutton lesson["name"] action SetVariable("activityArray", lesson["lesson"]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

screen selectActivities(day, dayNum):
    default activityType = ""
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for activity in game.activities: 
                if activity["available"]:
                    textbutton activity["name"] action SetScreenVariable("activityType", activity["activity"]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

