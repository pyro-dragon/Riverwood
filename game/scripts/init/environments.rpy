#-------------------------------------------------------------------------------
# This is where all the environment settings are defines
#-------------------------------------------------------------------------------

init: 
    python: 
        class Environment: 
            def __init__(self, name, background, discoveryScore, discovered, visitable, keyWords):
                self.name = name                        # The name of the environment
                self.background = background            # A path to the background image
                self.discoveryScore = discoveryScore    # The score needed to discover the land
                self.discovered = discovered            # Wether the land has been discovered or not
                self.visitable = visitable              # If the land can be visited or not
                self.keyWords = keyWords                # A list of environment keywords
                
                # Generate background image
                self.image = renpy.image(self.name, background)
                    
            # Discover the environment
            def discover(self):
                self.discovered = True
                
    $camp = Environment("Camp", "environments/camp.jpg", 0, True, False, [])
    $game.addLocation(camp)
    
    # Family rooms
    $glade = Environment("Glade", "environments/silentGrove.jpg", 0, True, False, [])
    $game.addLocation(glade)
    $forge = Environment("Forge", "environments/workshop.jpg", 0, True, False, [])
    $game.addLocation(forge)
    $arena = Environment("Arena", "environments/provingGrounds.jpg", 0, True, False, [])
    $game.addLocation(arena)
    $tent = Environment("Tent", "environments/tent.jpg", 0, True, False, [])
    $game.addLocation(tent)
    
    # Quest locations
    $forestRoad = Environment("ForestRoad", "environments/forestRoad.jpg", 0, False, True, [])
    $game.addLocation(forestRoad)

    # Discoverable areas
    $forest = Environment("Forest", "environments/forest.jpg", 50, False, True, ["nature", "peace"])
    $game.addLocation(forest)
    $river = Environment("River", "environments/river.jpg", 50, False, True, ["nature", "peace", "water"])
    $game.addLocation(river)
    $village = Environment("Village", "environments/village.jpg", 50, False, True, ["buildings"])
    $game.addLocation(village)
    $cave = Environment("Cave", "environments/cave.jpg", 50, False, True, ["dirt", "dark", "scary"])
    $game.addLocation(cave)
    $lake = Environment("Lake", "environments/lake.jpg", 50, False, True, ["nature", "peace", "water"])
    $game.addLocation(lake)
    $waterfall = Environment("Waterfall", "environments/waterfall.jpg", 50, False, True, ["water", "nature", ])
    $game.addLocation(waterfall)
    $overlook = Environment("Overlook", "environments/overlook.jpg", 50, False, True, ["nature", "views"])
    $game.addLocation(overlook)
    $fields = Environment("Fields", "environments/fields.jpg", 50, False, True, ["peace"])
    $game.addLocation(fields)
    $windmill = Environment("Windmill", "environments/windmill.jpg", 50, False, True, ["buildings", "action"])
    $game.addLocation(windmill)
    $monument = Environment("Monument", "environments/monument.jpg", 50, False, True, ["buildings", "art", "peace"])
    $game.addLocation(monument)
    $ruins = Environment("Ruins", "environments/ruins.jpg", 50, False, True, ["buildings", "scary"])
    $game.addLocation(ruins)
    $junkyard = Environment("Junkyard", "environments/junkyard.jpg", 50, False, True, ["buildings" "scary"])
    $game.addLocation(junkyard)
    
    # Mutable list for player discovery
    $discoverableAreas = [forest, river, village, cave, lake, waterfall, overlook, fields, windmill, monument, ruins, junkyard]

    #image bgCamp = "camp.jpg"
    #image bgSilentGrove = "silentGrove.jpg"
    #image bgWorkshop = "workshop.jpg"
    #image bgProvingGrounds = "provingGrounds.jpg"
    #image bgTent = "tent.jpg"