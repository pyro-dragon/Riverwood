#-------------------------------------------------------------------------------
# The overall game object. This is for holding global object structures
#-------------------------------------------------------------------------------

init: 
    python: 
        class Game: 
            dateableCharacters = []
            leaderCharacters = []
            playerCharacter = []
            questList = []
            activeQuests = []
            completedQuests = []
            
            def __init__(self):
                True
                
            # Check for quests that can be made active
            def checkForActiveQuests(self):
                for quest in self.questList:            # Cycle through all idle quests
                    if quest.checkQuest():              # Check if the quest can start
                        self.activeQuests.append(quest)      # Make quest active
                        self.questList.remove(quest)         # Remove from idle list
                        
            # Update active quests
            def updateActiveQuests(self):
                for quest in self.activeQuests:                         # Cycle through all active quests
                    if quest.stages[quest.currentStage].checkStage():   # Check if the stage can start
                        quest.stages[quest.currentStage].runScene()     # Run the stage scene. TODO: Add to a stack so that multiple stages can be run, one at a time. 
                        
            # Remove completed quests
            def checkForInactiveQuests(self):
                for quest in self.activeQuests:            # Cycle through all active quests
                    if quest.complete:                     # Check if the quest has finished
                        self.completedQuests.append(quest)      # Make quest inactive
                        self.activeQuests.remove(quest)         # Remove from active list
                        
    $game = Game()