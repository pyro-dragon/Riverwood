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
                self.weekendLength = 2   # Number of days in a weekend
                self.monthLength = 4     # Number of weeks in a month
                self.yearLength = 12     # Number of months in a year
                
                self.weekend = False
                self.start = True        # Start of the week or weekend
                
                self.weekdayActivityChoices = [[Activity("hunting"), Activity("slacking")], [Activity("engineering"), Activity("slacking")], [Activity("reading"), Activity("slacking")], [Activity("training"), Activity("slacking")], [Activity("reading"), Activity("slacking")]]
                self.weekendActivityChoices = [["shopping", "converstion"], ["intelligenceTraining", "intelligenceTraining"]]
                
                self.eventList = [[] for x in range((self.monthLength * self.weekLength) * self.yearLength)]    # A list of events that may occur on any specific day. There may be multiple events here.
                self.eventWatchList = []                   # An array/list of events that may occure right now if their criteria are met
                self.callCount = 0
                
                self.suppressMenu = False       # Do not display the week planning menu (one time only)

            # A function to advance the day counters
            def advanceDayCounter(self):
                self.currentDay += 1
                
                # Check if this is a weekend
                if self.currentDay >= self.weekLength - self.weekendLength:
                    say("EDITOR", "Its the weekend!")
                    self.weekend = True         # It is the weekend
                    self.start = True           # Its the start of the weekend
                    self.currentWeekend += 1
                # Check if the weekend it over
                #elif self.currentDay > self.weekLength:
                #    say("EDITOR", "Week reset, not another manic Monday :(")
                #    self.start = True           # Its the start of a new week
                #    self.weekend = False        # The weekend is over :(
                #    self.currentDay = 0         # Reset
                #    self.currentWeekend = 0     # Reset
                #    self.currentWeekday = 0     # Reset
                # Just another regular week day
                else: 
                    say("EDITOR", "Working hard, or hardly working?")
                    self.currentWeekday += 1
                
            # Do all the things needed to get today ready to play though
            def prepareToday(self):
                # Create a new day
                day = Day()
                
                # Check for events that may start occuring on this day
                if len(self.eventList[self.currentDay]) > 0:
                    
                    # Add them to the watch list
                    for event in self.eventList[self.currentDay]:
                        self.eventWatchList.append(event)
                
                # Cycle through watch list
                for i in xrange(len(self.eventWatchList) - 1, -1, -1):       # Iterate over the list backwards

                    # Check for out-of-date events and remove them
                    if self.eventWatchList[i].expireryDate < self.currentDay:
                        say("", "Event expired: " + self.eventWatchList[i].label)
                        self.eventWatchList.remove(self.eventWatchList[i])
                        pass
                    
                    # Check if event criterias are met and add them to the right event slot
                    if self.eventWatchList[i].conditions(): 
                        if self.eventWatchList[i].timeslot == "morning": 
                            day.morningEvent = self.eventWatchList[i]
                        elif self.eventWatchList[i].timeslot == "afternoon":
                            day.afternoonEvent = self.eventWatchList[i]
                            
                        # Remove the event from the list
                        #say("", "Event dropped: " + self.eventWatchList[i].label)
                        self.eventWatchList.remove(self.eventWatchList[i])
                
                # Add the activities
                #say("", "Morning event: " + str(day.morningEvent))
                if day.morningEvent != None and day.morningEvent.override == True:
                    #say("", "morning activity skipped")
                    pass
                else:
                    say("EDITOR", "Current weekDay:" + str(self.currentWeekday))
                    day.morningActivity = self.weekdayActivityChoices[self.currentWeekday][0]
                    #say("", "++added morning activities")
                if day.afternoonEvent != None and not day.afternoonEvent.override: 
                    #say("", "++adding afternoon activities")
                    day.afternoonActivity = self.weekdayActivityChoices[self.currentWeekday][1]
                
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
            def setActivity(self, activity, day, period):
                self.weekdayActivityChoices[day][period] = activity
        
        # A complete day
        class Day: 
            
            def __init__(self, morningEvent = None, afternoonEvent = None, EveningEvent = None, morningActivity = None, afternoonActivity = None):
                self.morningEvent = morningEvent             # An event that can occure in the morning before anything else
                self.afternoonEvent = afternoonEvent           # An event that can occure in the afternoon between the morning and afternoon activity
                self.eveningEvent = EveningEvent             # An event that can occure in the evening after the afternoon event
                
                self.morningActivity = morningActivity          # An activity that can occure in the morning, this is mostly lessons
                self.afternoonActivity = afternoonActivity        # An activity that can occure in the afternoon, this is mostly leasure or training
                
            def callMorningEvent(self):
                if(self.morningEvent != None):
                    renpy.call(self.morningEvent.label)
                
            def callAfternoonEvent(self):
                if(self.afternoonEvent != None):
                    renpy.call(self.afternoonEvent.label)

            def callEveningEvent(self):
                if(self.eveningEvent != None):
                    renpy.call(self.eveningEvent.label)

            def callMorningActivity(self):
                if(self.morningActivity != None):
                    say("", "calling morning activity: " + self.morningActivity.label)
                    #say("", "calling morning activity: " + self.morningActivity)
                    renpy.call(self.morningActivity.label)

            def callAfternoonActivity(self):
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

label yearCycle:    
    $monthCount = 0
    while monthCount < game.gameLoop.yearLength: 

        $weekCount = 0
        while weekCount < game.gameLoop.monthLength: 
            
            #$dayCount = 0
            
            # Check if we need to suppress the menu
            if game.gameLoop.suppressMenu:
                $game.gameLoop.suppressMenu = False
            else: 
                call screen weekPlan
                    
            while game.gameLoop.currentDay < game.gameLoop.weekLength:
                
                call day
                
                #$dayCount += 1
            $weekCount += 1
        $monthCount += 1
        
    return
    
label day:
    "Day number is [game.gameLoop.currentDay]"
    $day = game.gameLoop.prepareToday()
    
    # call pre-morning event
    $day.callMorningEvent()
    
    "Morning activity"
    $day.callMorningActivity()
    
    #"Calling pre-afternoon event"
    $day.callAfternoonEvent()
    
    "Afternoon activity"
    $day.callAfternoonActivity()
    
    # call any event happening in the evening
    $day.callEveningEvent()
    
    $game.gameLoop.nextDay()
    
    return
