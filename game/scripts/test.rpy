label test:
    "Checking for active quests..."
    $game.checkForActiveQuests()
    
    "Executing active quest stages..."
    $game.updateActiveQuests()