label test:
    
    scene black
    
    
    ## Daylight Rave
    while True:
    
        scene expression camp.getBackgroundImage()
        
        $game.advanceTime()
        
        scene expression camp.getBackgroundImage() with dissolve
    
    "END OF TEST"
 