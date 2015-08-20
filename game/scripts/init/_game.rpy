#-------------------------------------------------------------------------------
# The overall game object. This is for holding global object structures
#-------------------------------------------------------------------------------

init: 
    python: 
        import os                        
        import json
                
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
                self.initialiseCharacters()
                self.initialiseLocations()
                self.initialiseHeadshots()
                True
               
            def addLocation(self, location):
                self.locations.append(location)
               
            # Generate a random colour hex value
            def generateColour(self):
                r = lambda: renpy.random.randint(0,255)
                return '#%02X%02X%02X' % (r(),r(),r())
                
            def getFileData(self, filename):
                True
                
            def getFolderData(self, foldername): 
                folderLocation = renpy.loader.transfn(foldername)
                
                extractedData = []
                
                for fname in os.listdir(folderLocation):

                    if fname.endswith("json"):
                        json_data = open(folderLocation + "/" + fname).read()
                        extractedData.append(json.loads(json_data))
                        
                return extractedData
                
            def initialiseHeadshots(self): 
                True
                
            def initialiseCharacters(self):
                True
                
            def initialiseLocations(self):
                True
                
                
    $game = Game()
    