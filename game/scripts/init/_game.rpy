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
                True
               
            def addLocation(self, location):
                self.locations.append(location)
               
            # Generate a random colour hex value
            def generateColour(self):
                r = lambda: renpy.random.randint(0,255)
                return '#%02X%02X%02X' % (r(),r(),r())
                
            def getFileData(self, filename):
                True
                
            ##
            # Return all objects taken from a given folder location
            # @param foldername (string) The name of the folder and its path
            # @param joinData (boolean) If any of the files contain arrays, these should be joined with any individual item into one big array
            def getFolderData(self, foldername, joinData = True): 
                
                # Get the path to the files
                folderLocation = renpy.loader.transfn(foldername)
                
                extractedData = []
                
                # Cycle through every file in the folder
                for fname in os.listdir(folderLocation):
                    
                    # Check that the file ends with a json extension
                    if fname.endswith("json"):
                        
                        # Open the file, extract the json
                        json_data = json.loads(open(folderLocation + "/" + fname).read())
                        
                        # Check if this is a list of items and joinData is true
                        if type(json_data).__name__ == "list" and joinData == True: 
                            
                            # Cycle round for each item in the list
                            for item in json_data:
                                extractedData.append(item)
                        else:
                            extractedData.append(json_data)
                        
                return extractedData
                
                
    $game = Game()
    