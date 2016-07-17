#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------

init:
    python:
        testCount = 0
        
        weekPlan = [{"day": "Monday", "lesson": "", "activity": ""}, 
                    {"day": "Tuseday", "lesson": "", "activity": ""},
                    {"day": "Wednesday", "lesson": "", "activity": ""},
                    {"day": "Thursday", "lesson": "", "activity": ""},
                    {"day": "Friday", "lesson": "", "activity": ""}]

        def initialiseWeekPlan(): 
            weekPlan = [{"day": "Monday", "lesson": "", "activity": ""}, 
                    {"day": "Tuseday", "lesson": "", "activity": ""},
                    {"day": "Wednesday", "lesson": "", "activity": ""},
                    {"day": "Thursday", "lesson": "", "activity": ""},
                    {"day": "Friday", "lesson": "", "activity": ""}]
            
        

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

        text str(testCount)
        
        # pseudo validation
        if weekPlan[0]["lesson"] != "" and weekPlan[1]["lesson"] != "" and weekPlan[2]["lesson"] != "" and weekPlan[3]["lesson"] != "" and weekPlan[4]["lesson"] != "":
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

