label test:
    
    scene black
    
    scene expression "environments/Forge.jpg" with fade
    "derp"
    
    #$renpy.scene()
    #$renpy.show("bg", what=Image("environments/Forge.jpg"))
    
    $game.setLocation(camp)
    "camp"
    scene black
    "black"
    
    $game.showCurrentLocation()
    
    ## Daylight Rave
    #while True:
    
        #scene expression camp.getBackgroundImage()
        
        #$game.advanceTime()
        
        #scene expression camp.getBackgroundImage() with dissolve
    
    "END OF TEST"
 