#-------------------------------------------------------------------------------
# The overall game object. This is for holding global object structures
#-------------------------------------------------------------------------------

init: 
    python: 
                
        class Game: 
            dateableCharacters = []
            leaderCharacters = []
            playerCharacter = []
            questList = []
            activeQuests = []
            completedQuests = []
            headshots = []
            
            locations = []
            currentLocation = None
            
            def __init__(self):
                initialiseCharacters()
                initialiseLocations()
                initialiseHeadshots()
               True
               
            def addLocation(self, location):
                self.locations.append(location)
               
            # Generate a random colour hex value
            def generateColour(self):
                r = lambda: renpy.random.randint(0,255)
                return '#%02X%02X%02X' % (r(),r(),r())
                
            def initialiseHeadshots(self): 
                
            def initialiseCharacters(self):
                
            def initialiseLocations(self):
                
                
    $game = Game()
    