#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------

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
                
        textbutton "Start the week" action Return()
                
screen selectLesson(day, dayNum):
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for lesson in game.lessons: 
                if lesson["available"]:
                    # The second action here is purely to allow the correct buttons to show up as selected.
                    textbutton lesson["name"] action([Function(game.gameLoop.setActivity, lesson["lesson"], dayNum, 0), SetScreenVariable("lessonType" + day, lesson["name"] + day)]) xfill True
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
                    # The second action here is purely to allow the correct buttons to show up as selected.
                    textbutton activity["name"] action([Function(game.gameLoop.setActivity, activity["activity"], dayNum, 1), SetScreenVariable("activityType" + day, activity["name"] + day)]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

