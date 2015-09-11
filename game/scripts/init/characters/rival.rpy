#-----------------------------
# Rival
#-----------------------------
init 1:
    python: 
        # Read in player data
        playerData = game.getFileData("resources/characters/rival.json")
        
        # Create the player
        crt_rival = GameCharacter(playerData["name"], 
                                    playerData["family"], 
                                    playerData["nick"], 
                                    Character("crt_rival.name", dynamic = True, color = playerData["textcolour"]), 
                                    playerData["image"], 
                                    playerData["met"], 
                                    playerData["hidename"], 
                                    playerData["imagetn"])
        # Add preference data
        for preference in playerData["preferences"]:
            crt_rival.addPreference(CharacterPreference(preference["keyword"], preference["type"], preference["response"]))

    # Add to datable list
    game.dateableCharacters.append(crt_rival)
    
    # Create renpy character
    define r = crt_rival.c