#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

init: 
    python: 
        class Mission: 
            
            # Constructor
            def __init__(self, missionLabel, overrideAfternoon, condition, conditionPassLabel, conditionFailLabe):
                self.missionLabel = missionLabel                # The lable for the mission scene to begin at
                self.overrideAfternoon = overrideAfternoon      # Whether or not the mission will allow afternoon activities
                self.condition = condition                      # An optional conditional. It is a function and should return true or false
                self.conditionPassLabel = conditionPassLabel    # The label to a scene to show when the mission is complete
                self.conditionFailLabe = conditionFailLabe      # The label to a scene to show when the mission is not passed yet
                
        # Gildclaw careers
        crr_trader = Career("Trader", "cha", "negotiation", "performance", ["gold", "dull"])
        crr_diplomat = Career("Diplomat", "cha", "negotiation", "presentation", ["dull", "peace", "intelligence"])
        gildclawCareers = [crr_trader, crr_diplomat]
        
        # Bloodrunner careers
        crr_hunter = Career("Hunter", "dex", "tracking", "silent movement", ["hunting", "action"])
        crr_healer = Career("Healer", "int", "medicine", "investigation", ["dull", "peace"])
        bloodrunnerCareers = [crr_hunter, crr_healer]
        
        # Coppertail careers
        crr_mechanic = Career("Mechanic", "int", "engineering", "construction", ["making", "dull"])
        crr_researcher = Career("Researcher", "int", "investigation", "exploring", ["intelligence", "dull"])
        coppertailCareers = [crr_mechanic, crr_researcher]
        
        # Daggermaw careers
        crr_fighter = Career("Fighter", "str", "hand weapon", "archery", ["danger", "combat", "action"])
        crr_scout = Career("Scout", "dex", "investigation", "silent movement", ["exploring", "running"])
        daggermawCareers = [crr_fighter, crr_scout]