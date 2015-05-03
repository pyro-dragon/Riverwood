#-------------------------------------------------------------------------------
# The Quest object used to represent quest arcs the plater can go on
#-------------------------------------------------------------------------------

init: 
    python: 
        class Quest: 
            def __init__(self, name, questStages = []):
                self.name = name        # The name of the quest arc
                self.questStages = questStages
                self.currentStage = 0
                self.complete = False
                    
            # Discover the environment
            def CheckQuest(self):
                # Do quest checking things
                
            def AddQuestStage(self, stage)
                self.questStages.append(stage)
                
#  The quest stage object
        class QuestStage: 
            def __init__(self, name, stageLabel):
                self.name = name
                self.stageLabel = stageLabel