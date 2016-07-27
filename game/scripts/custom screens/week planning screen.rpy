#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------

init:
    python:
        weekPlan = [{"day": "Monday", "lesson": "", "activity": ""}, 
                    {"day": "Tuseday", "lesson": "", "activity": ""},
                    {"day": "Wednesday", "lesson": "", "activity": ""},
                    {"day": "Thursday", "lesson": "", "activity": ""},
                    {"day": "Friday", "lesson": "", "activity": ""}]
            
label planNewWeek:
    $weekPlan = [{"day": "Monday", "lesson": "", "activity": ""}, {"day": "Tuseday", "lesson": "", "activity": ""}, {"day": "Wednesday", "lesson": "", "activity": ""}, {"day": "Thursday", "lesson": "", "activity": ""}, {"day": "Friday", "lesson": "", "activity": ""}]
    
    call screen weekPlanScreen
    
    # Set the activity chices
    python:
        for i, day in enumerate(weekPlan):
            game.gameLoop.setActivity(Activity(day["lesson"]), i, "lesson")
            game.gameLoop.setActivity(Activity(day["activity"]), i, "activity")
            
    
    return

screen weekPlanScreen():
    default MondaySet = False
    default TusedaySet = False
    default WednesdaySet = False
    default ThursdaySet = False
    default FridaySet = False
    
    window:
        xfill True
        yfill True
        has vbox:
            text "Morning lessons: "
            hbox xfill True:
                for i, day in enumerate(weekPlan):
                    use selectLesson(day["day"], i)

            text "----"
                
            text "Afternoon activities: "
            hbox xfill True:
                for i, day in enumerate(weekPlan):
                    use selectActivities(day["day"], i)
        
        # pseudo validation
        #if weekPlan[0]["lesson"] != "" and weekPlan[1]["lesson"] != "" and weekPlan[2]["lesson"] != "" and weekPlan[3]["lesson"] != "" and weekPlan[4]["lesson"] != "":
        #python:
            #def checkAllSet():
        $allSet = 0
        for day in weekPlan:
            if day["lesson"] != "" and day["activity"] != "":
                $allSet = allSet + 1
                
        if allSet == 5:
            textbutton "Start the week" action Return()
                
screen selectLesson(day, dayNum):
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for lesson in game.lessons: 
                if lesson["available"]:
                    textbutton lesson["name"] action SetDict(weekPlan[dayNum], "lesson", lesson["name"]) xfill True
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
                    textbutton activity["name"] action SetDict(weekPlan[dayNum], "activity", activity["name"]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

