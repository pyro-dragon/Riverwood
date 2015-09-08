#-------------------------------------------------------------------------------
# The overall game object. This is for holding global object structures
#-------------------------------------------------------------------------------

init: 
    python: 
        import os                        
        import json
        
        ## 
        # This is the master game class. It cointains all the ikmportant control variables for the game
        class Game: 
            dateableCharacters = []     # An array of all datable characters
            leaderCharacters = []       # An array of all leader characters
            playerCharacter = {}        # The player character
            headshots = []              # All of the background character portraits
            locations = []              # All of the locations in the game
            hiddenLocations = []        # All of the hidden locations
            currentLocation = None      # The current location
            daytime = True              # Is it day or night
            day = 1                     # The current day number
            
            # Possibly obsolete #
            questList = []
            
            ##
            # The game object constructor
            def __init__(self):
                True
               
            ## 
            # Add a location to the game
            # @param location (object) The location object
            def addLocation(self, location):
                self.locations.append(location)
                if location.discovered == False: 
                    self.hiddenLocations.append(location)
            
            ##
            # Generate a random colour hex value
            # @return (string) The colour code
            def generateColour(self):
                r = lambda: renpy.random.randint(0,255)
                return '#%02X%02X%02X' % (r(),r(),r())
                
            ##
            # Return the data in a single file
            # @param filename (string) The name of the file to read, including its file path.
            # @return (object) The data from a single file
            def getFileData(self, filename):
                
                # Get the full path
                fileLocation = renpy.loader.transfn(filename)
                
                # Pull out the data and convert it
                extractedData = {}
                if fileLocation.endswith("json"):
                    extractedData = json.loads(open(fileLocation).read())
                
                # Return the data
                return extractedData
                
            ##
            # Return all objects taken from a given folder location
            # @param foldername (string) The name of the folder and its path
            # @param joinData (boolean) If any of the files contain arrays, these should be joined with any individual item into one big array
            # @return (object) The folder content
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
            
            ## 
            # Advance time- if day, set to night. If night, set today and advance the day counter
            # @param days (int) The number of days to advance by. Zero means to just go from day to night.
            # @param maintainTime (boolean) If the time is advanced by a number of days, this controls if we should stay on the same day/night stage as we left
            def advanceTime(self, days = 0, maintainTime = False): 
                if days == 0:
                    self.daytime = not self.daytime
                    
                    # Check to see if we should advance the day counter
                    if self.daytime == True: 
                        self.day = self.day + 1
                        
                else: 
                    self.day = self.day + days
                    
                    # Check if we are maintaining the day time
                    if maintainTime == False: 
                        self.daytime = True
    
    # Create the game object
    $game = Game()
    