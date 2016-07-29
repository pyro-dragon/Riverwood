#-------------------------------------------------------------------------------
# A screen used to pick activities for the weekend
#-------------------------------------------------------------------------------

init:
    python:
        weekEndPlan = [{"day": "Saturday", "morning": "", "afternoon": ""}, 
                    {"day": "Sunday", "morning": "", "afternoon": ""}]
            
label planNewWeekend:
    $weekendPlan = [{"day": "Saturday", "morning": "", "afternoon": ""}, {"day": "Sunday", "morning": "", "afternoon": ""}]
    
    call screen weekendPlanScreen
    
    # Set the activity chices
    python:
        for i, day in enumerate(weekendPlan):
            game.gameLoop.setActivity(Activity(day["morning"]), i + 5, "lesson")      #  + 5 for the offset from weekdays
            game.gameLoop.setActivity(Activity(day["afternoon"]), i + 5, "activity")
    
    return

screen weekendPlanScreen():
    
    window:
        xfill True
        yfill True
        has vbox:
            text "Morning Activities: "
            hbox xfill True:
                for i, day in enumerate(weekendPlan):
                    use selectMorning(day["day"], i)

            text "----"
                
            text "Afternoon activities: "
            hbox xfill True:
                for i, day in enumerate(weekendPlan):
                    use selectAfternoon(day["day"], i)
                    
        $allSet = 0
        for day in weekendPlan:
            if day["morning"] != "" and day["afternoon"] != "":
                $allSet = allSet + 1
                
        if allSet == 2:
            textbutton "Start the weekend!" action Return()
                
screen selectMorning(day, dayNum):
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for lesson in game.activities: 
                if lesson["available"]:
                    textbutton lesson["name"] action SetDict(weekendPlan[dayNum], "morning", lesson["activity"]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

screen selectAfternoon (day, dayNum):
    default activityType = ""
    
    frame:
        xsize 155
        
        vbox: 
            label day
            
            for activity in game.activities: 
                if activity["available"]:
                    textbutton activity["name"] action SetDict(weekendPlan[dayNum], "afternoon", activity["activity"]) xfill True
                else: 
                    textbutton "[[Hidden]" action False xfill True

