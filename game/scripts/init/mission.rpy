#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

init: 
    python: 
        class Mission: 
            
            # Constructor
            def __init__(self, missionLabel, overrideAfternoon, condition, conditionPassLabel = "", conditionFailLabel = ""):
                self.missionLabel = missionLabel                # The lable for the mission scene to begin at
                self.overrideAfternoon = overrideAfternoon      # Whether or not the mission will allow afternoon activities
                self.condition = condition                      # An optional conditional. It is a function and should return true or false
                self.conditionPassLabel = conditionPassLabel    # The label to a scene to show when the mission is complete
                self.conditionFailLabe = conditionFailLabe      # The label to a scene to show when the mission is not passed yet