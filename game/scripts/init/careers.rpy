#-------------------------------------------------------------------------------
# This is where all the careers are defined
#-------------------------------------------------------------------------------

init: 
    python: 
        class Career: 
            
            # Constructor
            def __init__(self, name, keyAttr, primarySkill, secondarySkill, keywords):
                self.name = name                        # The career name
                self.keyAttr = keyAttr                  # The main attribute for the career
                self.primarySkill = primarySkill        # The primary career skill
                self.secondarySkill = secondarySkill    # The secondary career skill
                self.keywords = keywords                # A list of career keywords
                
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