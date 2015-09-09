#-------------------------------------------------------------------------------
# This is where all the location settings are defines
#-------------------------------------------------------------------------------

init: 
    python: 
        ##
        # The class used to describe locations
        # @param name (string) The name of the location
        # @param dayImagePath (string) The path to the daytime image
        # @param nightImagePath (string) The path to the night time image
        # @param discoveryScore (int) The score needed to find the location
        # @param discovered (boolean) If the location starts off discovered or not
        # @param visitable (boolean) If the location is visitable or not
        # @param keyWords (array) An array of keywords associated with the location
        class Location: 
            def __init__(self, name, dayImagePath, nightImagePath, discoveryScore, discovered, visitable, keyWords):
                self.name = name                        # The name of the environment
                self.dayImage = dayImagePath            # The path to the daytime image
                self.nightImage = nightImagePath        # The path to the nighttime image
                self.discoveryScore = discoveryScore    # The score needed to discover the land
                self.discovered = discovered            # Wether the land has been discovered or not
                self.visitable = visitable              # If the land can be visited or not
                self.keyWords = keyWords                # A list of environment keywords
            
            ##
            # Discover the environment
            def discover(self):
                self.discovered = True
                game.hiddenLocations.remove(self)
                
            def getBackgroundImage(self, time=None):
                if time == None:
                    if game.daytime == True:
                        return self.dayImage
                    else: 
                        return self.nightImage
        
        # Create the camp
        landData = game.getFileData("resources/environments/camp.json")
        camp = Location(landData["name"], landData["day"], landData["night"], landData["concealment"], landData["discovered"], landData["visitable"], landData["keywords"])
        game.addLocation(camp)
        
        # Family rooms
        landData = game.getFileData("resources/environments/grove.json")
        glade = Location(landData["name"], landData["day"], landData["night"], landData["concealment"], landData["discovered"], landData["visitable"], landData["keywords"])
        game.addLocation(glade)
        landData = game.getFileData("resources/environments/forge.json")
        forge = Location(landData["name"], landData["day"], landData["night"], landData["concealment"], landData["discovered"], landData["visitable"], landData["keywords"])
        game.addLocation(forge)
        landData = game.getFileData("resources/environments/arena.json")
        arena = Location(landData["name"], landData["day"], landData["night"], landData["concealment"], landData["discovered"], landData["visitable"], landData["keywords"])
        game.addLocation(arena)
        landData = game.getFileData("resources/environments/tent.json")
        tent = Location(landData["name"], landData["day"], landData["night"], landData["concealment"], landData["discovered"], landData["visitable"], landData["keywords"])
        game.addLocation(tent)
        
        # Explorable areas
        landData = game.getFolderData("resources/environments/explorable")
        
        for land in landData: 
            game.addLocation(Location(land["name"], 
                                         land["day"], 
                                         land["night"],
                                         land["concealment"], 
                                         land["discovered"], 
                                         land["visitable"], 
                                         land["keywords"]))
    
    # Quest locations
    #$forestRoad = Environment("ForestRoad", "environments/forestRoad.jpg", 0, False, True, [])
    #$game.addLocation(forestRoad)

    # Discoverable areas
    #$forest = Environment("Forest", "environments/forest.jpg", 50, False, True, ["nature", "peace"])
    #$game.addLocation(forest)
    #$river = Environment("River", "environments/river.jpg", 50, False, True, ["nature", "peace", "water"])
    #$game.addLocation(river)
    #$village = Environment("Village", "environments/village.jpg", 50, False, True, ["buildings"])
    #$game.addLocation(village)
    #$cave = Environment("Cave", "environments/cave.jpg", 50, False, True, ["dirt", "dark", "scary"])
    #$game.addLocation(cave)
    #$lake = Environment("Lake", "environments/lake.jpg", 50, False, True, ["nature", "peace", "water"])
    #$game.addLocation(lake)
    #$waterfall = Environment("Waterfall", "environments/waterfall.jpg", 50, False, True, ["water", "nature", ])
    #$game.addLocation(waterfall)
    #$overlook = Environment("Overlook", "environments/overlook.jpg", 50, False, True, ["nature", "views"])
    #$game.addLocation(overlook)
    #$fields = Environment("Fields", "environments/fields.jpg", 50, False, True, ["peace"])
    #$game.addLocation(fields)
    #$windmill = Environment("Windmill", "environments/windmill.jpg", 50, False, True, ["buildings", "action"])
    #$game.addLocation(windmill)
    #$monument = Environment("Monument", "environments/monument.jpg", 50, False, True, ["buildings", "art", "peace"])
    #$game.addLocation(monument)
    #$ruins = Environment("Ruins", "environments/ruins.jpg", 50, False, True, ["buildings", "scary"])
    #$game.addLocation(ruins)
    #$junkyard = Environment("Junkyard", "environments/junkyard.jpg", 50, False, True, ["buildings" "scary"])
    #$game.addLocation(junkyard)
    
    # Mutable list for player discovery
    #$discoverableAreas = [forest, river, village, cave, lake, waterfall, overlook, fields, windmill, monument, ruins, junkyard]

    #image bgCamp = "camp.jpg"
    #image bgSilentGrove = "silentGrove.jpg"
    #image bgWorkshop = "workshop.jpg"
    #image bgProvingGrounds = "provingGrounds.jpg"
    #image bgTent = "tent.jpg"