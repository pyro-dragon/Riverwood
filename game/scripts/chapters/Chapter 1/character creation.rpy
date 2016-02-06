#-------------------------------------------------------------------------------
# The character creation scene
#-------------------------------------------------------------------------------

#-----------------------------
# Index for a multi-part file
#-----------------------------
label characterCreation:
    call chooseFamily
    
    call setFamilyData
    
    call chooseName
    
    return

#-----------------------------
# Choose the players family
#-----------------------------
label chooseFamily: 

    T "Which family will you choose?"
    "Player family: [player.family]"
    menu:
        "I in tune with the ways of the Bloodrunners. (Nature, Hunters, Medicine)":
            $player.family = "Bloodrunner"
            
        "I have a great interest in joining the Coppertails. (Industry, Crafting, Science)":
            $player.family = "Coppertail"
                
        "The Daggermaws seem like the only family tough enough for me! (Fighting, Tactics, Scouting)":
            $player.family = "Daggermaw"
                
        "It will be an honour to join the Gildclaws. (Diplomacy, Trade, Economics)":
            $player.family = "Gildclaw"
    
    call checkFamily
            
    return
    
#-----------------------------
# Check that the player is ok
# with their choice of family.
#-----------------------------
label checkFamily:
    "Is that your final choice?"
    
    menu: 
        "Yes, I want to join the [player.family]!":
            pass
            
        "No, I want to know the choices again.":
            call chooseFamily
            
    return

#-----------------------------
# Set the rival and ally name
# and family data
#-----------------------------
label setFamilyData:
    if player.family == "Bloodrunner":
        $crt_ally.family = "Daggermaw"
        $crt_ally.trueName = "Scarah"
        $crt_rival.family = "Coppertail"
        $crt_rival.trueName= "Scorch"
        $game.gameLoop.weekdayActivityChoices = [["hunting", "slacking"], ["hunting", "slacking"], ["engineering", "slacking"], ["training", "slacking"], ["readting", "slacking"]]
    
    elif player.family == "Coppertail":
        $crt_ally.family = "Gildclaw"
        $crt_ally.trueName = "Deft"
        $crt_rival.family = "Daggermaw"
        $crt_rival.trueName = "Dirge"
        $game.gameLoop.weekdayActivityChoices = [["engineering", "slacking"], ["engineering", "slacking"], ["training", "slacking"], ["reading", "slacking"], ["huntinging", "slacking"]]
    
    elif player.family == "Daggermaw":
        $crt_ally.family = "Bloodrunner"
        $crt_ally.trueName = "Swift"
        $crt_rival.family = "Gildclaw"
        $crt_rival.trueName = "Silver"
        $game.gameLoop.weekdayActivityChoices = [["training", "slacking"], ["training", "slacking"], ["reading", "slacking"], ["hunting", "slacking"], ["engineering", "slacking"]]

    elif player.family == "Gildclaw":
        $crt_ally.family = "Coppertail"
        $crt_ally.trueName = "Spark"
        $crt_rival.family = "Bloodrunner"
        $crt_rival.trueName = "Shade"
        $game.gameLoop.weekdayActivityChoices = [["reading", "slacking"], ["reading", "slacking"], ["hunting", "slacking"], ["engineering", "slacking"], ["training", "slacking"]]

    return
            
#-----------------------------
# Choose how to decide the 
# player name. 
#-----------------------------
label chooseName:
    T "Excellent. I am sure you will be an asset to the [player.family]s."
    T "Now, you must take a name for yourself. You can either choose one yourself of have your new family suggest a name. Which would you like?"
    menu:
        "I'll choose my own name.":
            call makeName
            
        "I'll let my family pick for me": 
            call pickName
            
    return

#-----------------------------
# Type out the player name. 
#-----------------------------
label makeName:
    $player.name = renpy.input("Very well, what will your name be?")
    $player.name = player.name.strip()
    call checkName
    
    return

#-----------------------------
# Select the name from a list.
#-----------------------------
label pickName:
    "Ok, here is a list of names you can choose"
    if player.family == "Bloodrunner":
        menu: 
            "Moon Spirit":
                $player.name = "Moon Spirit"

            "Sharp Eye":
                $player.name = "Sharp Eye"

    elif player.family == "Coppertail":
        menu: 
            "Gelda":
                $player.name = "Gelda"
                
            "Rivet":
                $player.name = "Rivet"
                
    elif player.family == "Daggermaw":
        menu: 
            "Quick Fang":
                $player.name = "Quick Fang"
                
            "Ripper":
                $player.name = "Ripper"
                
    elif player.family == "Gildclaw":
        menu: 
            "Coin":
                $player.name = "Coin"
                
            "Gilt":
                $player.name = "Gilt"
          
    call checkName
    
    return
    
#-----------------------------
# Check that the player is ok
# with their choice of name. 
#-----------------------------
label checkName:
    T "So you want [player.name] to be your name?"
    
    menu: 
        "Yes! I shall be known as [player.name]!":
            pass
        "No, on second thoughts I want to pick again.":
            call chooseName
            
    return