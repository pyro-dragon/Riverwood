label test:
    $playerCompanion = crt_mechanic
    $playerCompanion.showName()
    $place = glade
    
    scene expression place.name with fade
    show expression playerCompanion.image with dissolve
    $game.currentLocation = place.name
    call screen conversation(playerCompanion)
    
    "END OF TEST"
