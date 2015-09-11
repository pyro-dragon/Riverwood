#-----------------------------
# Ally
#-----------------------------
init 1: 
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/ally.json")
        
        # Create the player
        crt_ally = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("crt_ally.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            crt_ally.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))
    
    # Add to datable list
    $game.dateableCharacters.append(crt_ally)
    
    # Create renpy character
    define a = crt_ally.c
    