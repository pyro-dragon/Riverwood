#------------------------------------------------------------------------------
# The main game cycle
#------------------------------------------------------------------------------

init:
    python:
        weekLength = 7
        monthLength = 4
        yearLength = 12
        elapsedDays = 0     # Possibly make this declared earlier
        elapsedWeeks = 0    # Same
        dayOfTheWeek = 0    # Counts up to the week length and resets
        weekend = False
        breakCycle = False
        start = True        # Start of the week or weekend
        weekdayLearning = ["engineering", "engineering", "hunting", "diplomacy", "engineering"]
        weekdayActivities = ["slacking", "chatting", "strengthTraining", "chatting", "slacking"]
        eventList = []      # An array/list of events that may occur on any specific day. There may be multiple events here.
        eventWatchList = [] # An array/list of events that may occure right now if their criteria are met
        morningEvent = None # An event that can occure in the morning before anything else
        afternoonEvent = None       # An event that can occure in the afternoon between the morning and afternoon activity
        eveningEvent = None # An event that can occure in the evening after the afternoon event
        morningActivity = None      # An activity that can occure in the morning, this is mostly lessons
        afternoonActivity = None    # An activity that can occure in the afternoon, this is mostly leasure or training
    
        #def nextPeriod(self): 
            
        
        def nextDay(self): 
            # Advance the weekly day count
            if dayOfTheWeek == weekLength -1:
                dayOfTheWeek = 0
            else:
                dayOfTheWeek += 1
            
            
            # Advance the overall day count
            elapsedDays += 1
            
            # Check for events that may start occuring on this day
            if eventList[elapsedDays].length > 0:
                
                # Add it to the watch list
                eventWatchList.append(eventList[elapsedDays])
            
            
            # Cycle through watch list
            for event in eventWatchList: 

                # Check for out-of-date events and remove them
                if event.expireryDate < elapsedDays:
                    eventWatchList.pop(event)
                
                # Check if event criterias are met and add them to the right event slot
                if event.criteriaMet(): 
                    if event.time == "morning": 
                        morningEvent = event
                    elif event.time == "afternoon":
                        afternoonEvent = event
                    else: 
                        afternoonEvent = event
                
        #def nextWeek(self):
        
        items = ["beans", "not beans", "bees"]

label yearCycle:    
    $monthCount = 0
    while monthCount < yearLength: 
        $weekCount = 0
        while weekCount < monthLength: 
            $dayCount = 0
            while dayCount < weekLength:
                call day
                "Day: [dayCount]\nWeek: [weekCount]\nMonth: [monthCount]\nElapsed Days: [elapsedDays]"
                $dayCount += 1
                $elapsedDays += 1
            $weekCount += 1
        $monthCount += 1
    
    python: 
        say("", "do a thing")
        renpy.call("anotherThing")
        
    python:
        say("", "all things done")
        renpy.return_statement()

label day:
    
    "Elapsed days: [elapsedDays]"
    
    # If morning event slot is filled then play the event
    if morningEvent != None:
        call expression morningEvent.name
    
    # If new weekend
    if weekend and start:
    
        # Display weekend activity screen
        screen weekendActivityScreen
        
    # If new week
    elif start:
        
        # Display week activity screen
        screen weekdayActivityScreen
    
    # Check if morning event has been overridden. Otherwise play it
    if morningEvent != None and not morningEvent.override:
        call expression morningActivity.name
            
    # If afternoon event slot is filled then play the event
    if afternoonEvent != None: 
        call expression afternoonEvent.name
    
    # Check if afternoon activity is overridden. Otherwise play it
    if afternoonEvent != None and not afternoonEvent.override: 
        call expression afternoonActivity.name
    
    # If evening event slot is filled then plat the event
    if eveningEvent != None: 
        call expression eveningEvent.name
    
    # Clean up
    $morningEvent = None
    $afternoonEvent = None
    $eveningEvent = None
    
    $start = False
    
    # Next day
    
    return
    