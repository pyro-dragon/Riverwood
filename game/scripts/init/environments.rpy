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
    
    # Family rooms
    $glade = Environment("Glade", "environments/silentGrove.jpg", 0, True, False, [])
    $forge = Environment("Forge", "environments/workshop.jpg", 0, True, False, [])
    $arena = Environment("Arena", "environments/provingGrounds.jpg", 0, True, False, [])
    $tent = Environment("Tent", "environments/tent.jpg", 0, True, False, [])
    
    # Quest locations
    $forestRoad = Environment("ForestRoad", "environments/forestRoad.jpg", 0, False, True, [])

    # Discoverable areas
    $forest = Environment("Forest", "environments/forest.jpg", 50, False, True, ["nature", "peace"])
    $river = Environment("River", "environments/river.jpg", 50, False, True, ["nature", "peace", "water"])
    $village = Environment("Village", "environments/village.jpg", 50, False, True, ["buildings"])
    $cave = Environment("Cave", "environments/cave.jpg", 50, False, True, ["dirt", "dark", "scary"])
    $lake = Environment("Lake", "environments/lake.jpg", 50, False, True, ["nature", "peace", "water"])
    $waterfall = Environment("Waterfall", "environments/waterfall.jpg", 50, False, True, ["water", "nature", ])
    $overlook = Environment("Overlook", "environments/overlook.jpg", 50, False, True, ["nature", "views"])
    $fields = Environment("Fields", "environments/fields.jpg", 50, False, True, ["peace"])
    $windmill = Environment("Windmill", "environments/windmill.jpg", 50, False, True, ["buildings", "action"])
    $monument = Environment("Monument", "environments/monument.jpg", 50, False, True, ["buildings", "art", "peace"])
    $ruins = Environment("Ruins", "environments/ruins.jpg", 50, False, True, ["buildings", "scary"])
    $junkyard = Environment("Junkyard", "environments/junkyard.jpg", 50, False, True, ["buildings" "scary"])
    
    # Mutable list for player discovery
    $discoverableAreas = [forest, river, village, cave, lake, waterfall, overlook, fields, windmill, monument, ruins, junkyard]

    #image bgCamp = "camp.jpg"
    #image bgSilentGrove = "silentGrove.jpg"
    #image bgWorkshop = "workshop.jpg"
    #image bgProvingGrounds = "provingGrounds.jpg"
    #image bgTent = "tent.jpg"