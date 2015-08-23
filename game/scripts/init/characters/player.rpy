#-----------------------------
# Player
#-----------------------------
init:
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/player.json")
        
        # Create the player
        player = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("player.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            player.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))
            
    $playerCompanion = "none"
    $peopleKnown = 2
    $discoveredPlaces = 0
    define P = player.c

    $playerCompanion = None
    $playerOpponent = 0
    $playerHealth = 100
    $opponentHealth = 100