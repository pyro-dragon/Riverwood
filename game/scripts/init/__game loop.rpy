#------------------------------------------------------------------------------
# The main game cycle
#------------------------------------------------------------------------------

init:
    python:
        
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
                
                self.weekdayActivityChoices = [["engineering", "slacking"], ["engineering", "chatting"], ["hunting", "strengthTraining"], ["diplomacy", "chatting"], ["engineering", "slacking"]]
                self.weekendActivityChoices = [["shopping", "converstion"], ["intelligenceTraining", "intelligenceTraining"]]
                
                self.eventList = [[] for x in range((self.monthLength * self.weekLength) * self.yearLength)]    # A list of events that may occur on any specific day. There may be multiple events here.
                self.eventWatchList = []                   # An array/list of events that may occure right now if their criteria are met
                self.callCount = 0
                
                self.suppressMenu = False       # Do not display the week planning menu (one time only)

            # A function to advance the day counters
            def advanceDayCounter(self):
                self.currentDay += 1
                
                # Check if this is a weekend
                if self.currentWeekday >= self.weekLength - self.weekendLength:
                    self.weekend = True         # It is the weekend
                    self.start = True           # Its the start of the weekend
                    self.currentWeekend += 1
                
                # Check if we have finished a week
                if self.currentWeekday > self.weekLength: 
                    self.start = True           # Its the start of a new week
                    self.weekend = False        # The weekend is over :(
                    self.currentWeekend = 0     # Reset
                    self.currentWeekday = 0     # Reset
                
            # Things to do when we advance to the next day
            def nextDay(self): 

                # Advance the day counter
                self.advanceDayCounter()
                
                # Create a new day
                day = Day()

                say("", "Today is day: " + str(self.currentDay))
                say("", "Todays event list size: " + str(len(self.eventList[self.currentDay])))
                
                # Check for events that may start occuring on this day
                if len(self.eventList[self.currentDay]) > 0:
                    
                    # Add them to the watch list
                    for event in self.eventList[self.currentDay]:
                        say("", "Adding event: \n" + str(event.label) + "\n" + str(event.timeslot) + "\n" + str(event.expireryDate) + "\n" + str(event.override) + "\n" + str(event.conditions));
                        self.eventWatchList.append(event)
                
                # Cycle through watch list
                # Note: Can't remove while mid cycle- It messes up the order of things (there is no next one to go onto
                say("", "Watchlist size: " + str(len(self.eventWatchList)))
                for event in self.eventWatchList: 
                    say("", "Event: " + str(event.label))

                    # Check for out-of-date events and remove them
                    if event.expireryDate < self.currentDay:
                        say("", "Event expired")
                        #self.eventWatchList.remove(event)
                        pass
                    
                    # Check if event criterias are met and add them to the right event slot
                    if event.conditions(): 
                        if event.timeslot == "morning": 
                            day.morningEvent = event
                            say("", "Morning event added: " + str(day.morningEvent))
                        elif event.timeslot == "afternoon":
                            day.afternoonEvent = event
                            say("", "Afternoon event added: " + str(day.afternoonEvent))
                        else: 
                            day.afternoonEvent = event
                            
                        # Remove the event from the list
                        #self.eventWatchList.remove(event)
                        #say("", "Event still there?: " + str(day.afternoonEvent))
                
                # Add the activities
                if day.morningEvent != None and not day.morningEvent.override:
                    day.morningActivity = self.weekdayActivityChoices[self.currentWeekday][0]
                if day.afternoonEvent != None and not day.afternoonEvent.override: 
                    day.afternoonActivity = self.weekdayActivityChoices[self.currentWeekday][1]
                
                return day
               
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
                    renpy.say("", "Morning event time: " + self.morningEvent.label)
                    renpy.call(self.morningEvent.label)
                    #self.morningEvent = None
                
            def callAfternoonEvent(self):
                say("", "Afternoon event: " + str(self.afternoonEvent))
                if(self.afternoonEvent != None):
                    renpy.say("", "Afternoon event time: " + self.afternoonEvent.label)
                    renpy.call(self.afternoonEvent.label)
                    #self.afternoonEvent = None

            def callEveningEvent(self):
                if(self.eveningEvent != None):
                    renpy.say("", "Evening event time")
                    renpy.call(self.eveningEvent.label)
                    #self.eveningEvent = None

            def callMorningActivity(self):
                if(self.morningActivity != None):
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
            
            $dayCount = 0
            
            # Check if we need to suppress the menu
            if game.gameLoop.suppressMenu:
                $game.gameLoop.suppressMenu = False
            else: 
                call screen weekPlan
                    
            while dayCount < game.gameLoop.weekLength:
                
                call day
                "Day: [dayCount]\nWeek: [weekCount]\nMonth: [monthCount]\n"
                    
                $dayCount += 1
            $weekCount += 1
        $monthCount += 1
        
    return
    
label day:
    $day = game.gameLoop.nextDay()
    
    $day.callMorningEvent()
    
    $day.callMorningActivity()
    
    "Calling afternoon event"
    $day.callAfternoonEvent()
    
    $day.callAfternoonActivity()
    
    $day.callEveningEvent()
    
    return
