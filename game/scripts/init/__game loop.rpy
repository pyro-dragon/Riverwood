#------------------------------------------------------------------------------
# The main game cycle
#------------------------------------------------------------------------------

init:
    python:

        from copy import deepcopy
        
        # The master game loop.
        class GameLoop:
            
            # Constructor
            def __init__(self): 
                self.currentDay = 0     # The current cycle
                self.currentWeekday = 0 # The number of days that have passed in the current week
                self.currentWeekend = 0 # The number of days that have passed in the current weekend

                self.weekLength = 7      # Number of days in a week
                self.weekdayLength = 5   # Number of days that are weekdays
                #self.weekendLength = 2   # Number of days in a weekend
                self.monthLength = 4     # Number of weeks in a month
                self.yearLength = 12     # Number of months in a year
                
                self.weekend = False
                self.start = True        # Start of the week or weekend
                
                self.weekdayActivityChoices = [
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    },
                    {
                        "lesson": Activity("nullActivity"), 
                        "activity": Activity("nullActivity")
                    }
                ]#[{"lesson": Activity("hunting"), "activity": Activity("slacking")}, {"lesson": Activity("hunting"), "activity": Activity("slacking")}, {"lesson": Activity("hunting"), "activity": Activity("slacking")}, {"lesson": Activity("hunting"), "activity": Activity("slacking")}, {"lesson": Activity("hunting"), "activity": Activity("slacking")}, {"morning": Activity("slacking"), "afternoon": Activity("slacking")}, {"morning": Activity("slacking"), "afternoon": Activity("slacking")}]
                self.weekendActivityChoices = [{"morning": Activity("slacking"), "afternoon": Activity("slacking")}, {"morning": Activity("slacking"), "afternoon": Activity("slacking")}]
                
                self.eventList = [[] for x in range((self.monthLength * self.weekLength) * self.yearLength)]    # A list of events that may occur on any specific day. There may be multiple events here.
                self.eventWatchList = []                   # An array/list of events that may occure right now if their criteria are met
                self.callCount = 0
                
                self.suppressMenu = False       # Do not display the week planning menu (one time only)

            # A function to advance the day counters
            def advanceDayCounter(self):
                self.currentDay += 1
                
                # Check if this is a weekend
                if self.currentDay > self.weekdayLength:
                    self.weekend = True         # It is the weekend
                    self.start = True           # Its the start of the weekend
                    self.currentWeekend += 1
                # Just another regular week day
                else: 
                    self.currentWeekday += 1
                
            # Do all the things needed to get today ready to play though
            def prepareToday(self):
                # Create a new day
                day = Day()
                
                # Check for events that may start occurring on this day
                if len(self.eventList[self.currentDay]) > 0:
                    
                    # Add them to the watch list
                    #for event in self.eventList[self.currentDay]:
                    #    self.eventWatchList.append(event)
                    self.eventWatchList = self.eventList[self.currentDay]
                
                # Cycle through watch list
                for i in xrange(len(self.eventWatchList) - 1, -1, -1):       # Iterate over the list backwards

                    # Check for out-of-date events and remove them
                    if self.eventWatchList[i].expireryDate < self.currentDay:
                        self.eventWatchList.remove(self.eventWatchList[i])
                        break
                    
                    # Check if event criterias are met and add them to the right event slot
                    if self.eventWatchList[i].conditions(): 
                        if self.eventWatchList[i].timeslot == "morning": 
                            day.morningEvents.append(self.eventWatchList[i])
                        elif self.eventWatchList[i].timeslot == "afternoon":
                            day.afternoonEvents.append(self.eventWatchList[i])
                        elif self.eventWatchList[i].timeslot == "evening":
                            day.eveningEvents.append(self.eventWatchList[i])
                            
                        # Remove the event from the list
                        self.eventWatchList.remove(self.eventWatchList[i])
                
                # Add the activities
                day.morningActivity = self.weekdayActivityChoices[self.currentDay % 7]["lesson"]
                day.afternoonActivity = self.weekdayActivityChoices[self.currentWeekday]["activity"]
                
                return day
            
            # Things to do when we advance to the next day
            def nextDay(self): 

                # Advance the day counter
                self.advanceDayCounter()
               
            # Add an event
            def addEvent(self, event, day):
                self.eventList[day].append(event)
                self.callCount += 1;

            # Add an activity
            def setActivity(self, activity, dayNum, type):
                self.weekdayActivityChoices[dayNum][type] = activity
        
        # A complete day
        class Day: 
            
            #def __init__(self, name="default", morningEvents =[], afternoonEvents = [], EveningEvents = [], morningActivity = None, afternoonActivity = None):
            def __init__(self):
                self.morningEvents = []              # An event that can occure in the morning before anything else
                self.afternoonEvents = []          # An event that can occure in the afternoon between the morning and afternoon activity
                self.eveningEvents = []              # An event that can occure in the evening after the afternoon event
                
                self.morningActivity = None          # An activity that can occure in the morning, this is mostly lessons
                self.afternoonActivity = None      # An activity that can occure in the afternoon, this is mostly leasure or training
                
                self.missMorningActivity = False                # A flag to miss the morning activity
                self.missAfternoonActivity = False              # A flag to miss the afternoon activity
                
            # Process the morning event
            def callMorningEvents(self):
                self.processOutEvents(self.morningEvents)
                            
                # Remove the morning events
                self.morningEvents = []
                
            # Process the afternoon event
            def callAfternoonEvents(self):
                self.processOutEvents(self.afternoonEvents)
                        
                # Remove events
                self.afternoonEvents = []

            # Process the evening event
            def callEveningEvents(self):
                self.processOutEvents(self.eveningEvents)
                            
                # remove events
                self.eveningEvents = []
                    
            def processOutEvents(self, eventList): 
                if len(eventList) > 0:
                    for j in xrange(len(eventList) - 1, -1, -1):       # Iterate over the list backwards
                        
                        # Check if the event has expired
                        if eventList[j].expireryDate >= game.gameLoop.currentDay:
                            renpy.call_in_new_context(eventList[j].label)
                            
                return []

            # Process the morning activity
            def callMorningActivity(self):
                
                # Check if we have a morning event and that it is overriding
                if len(self.morningEvents) > 0 and day.missMorningActivity == True:
                    pass
                # There is no event or the event does not override so proceed with the activity
                else:
                    # Make sure we have an activity to do
                    if(self.morningActivity != None):
                        renpy.call(self.morningActivity.label)

            # Process the afternoon activity
            def callAfternoonActivity(self):
                
                # Check if we have a morning event and that it is overriding
                if len(self.afternoonEvents) > 0 and day.missAfternoonActivity == True:
                    pass
                # There is no event or the event does not override so proceed with the activity
                else: 
                    # Make sure we have an activity to do
                    if(self.afternoonActivity != None):
                        renpy.call(self.afternoonActivity.label)
        
        # An event. These may interrupt the day of the player
        class Event:

            # Constructor
            def __init__(self, label, timeslot, expireryDate, override, conditions):
                self.label = label                      # The label where this event happens
                self.timeslot = timeslot                # The timeslot this event happens in. morning, afternoon, evening
                self.expireryDate = expireryDate        # The day that this event expires and can no longer be activated
                self.override = override                # Determines if the following activity period does not happen
                self.conditions = conditions            # A lambda function of conditions that must be met before the event can occure
                
            # Check if the conditions have been met
            def checkValidity():
                return self.conditions()
                
            # Run the event
            def run():
                renpy.call(self.label)
                
        # An activity. These are the normal things that the player gets up to during the course of their day.
        class Activity: 
            
            # Constructor
            def __init__(self, label):
                self.label = label      # The label of the activity to run
                
            # Run the activity
            def run():
                renpy.call(self.label)
                
label mainCycle:

    while True:
        
        # Check for end of the week
        if game.gameLoop.currentDay % 7 == 0:
            if game.gameLoop.suppressMenu == False:
                call planNewWeek
            elif game.gameLoop.suppressMenu == True:
                $game.gameLoop.suppressMenu = False
            
        # Check for weekend
        if game.gameLoop.currentDay % 7 == 5: 
            if game.gameLoop.suppressMenu == False:
                call planNewWeekend
            elif game.gameLoop.suppressMenu == True:
                $game.gameLoop.suppressMenu = False
        
        call day
        
    return
    
label day:
    
    $day = game.gameLoop.prepareToday()
    
    $day.callMorningEvents()
    
    $day.callMorningActivity()
    
    $day.callAfternoonEvents()
    
    $day.callAfternoonActivity()
    
    $day.callEveningEvents()
    
    $game.gameLoop.nextDay()
    
    return
