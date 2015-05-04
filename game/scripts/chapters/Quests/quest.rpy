#-------------------------------------------------------------------------------
# The Quest object used to represent quest arcs the plater can go on
#-------------------------------------------------------------------------------

init 1: 
    python: 
        class Quest: 
            def __init__(self, name, startCondition, stages = []):
                self.name = name                        # The name of the quest arc
                self.startCondition = startCondition    # A lambda function describing the start of the quest
                self.stages = stages                    # A list of the quest stages
                self.currentStage = 0                   # The current quest stage
                self.complete = False                   # If the quest is complete or not
                    
            # Check if the conditions are right to start the quest
            def checkQuest(self):
                return self.startCondition()
                
            def addStage(self, stage):
                self.stages.append(stage)

#-------------------------------------------------------------------------------
#  The quest stage object
#-------------------------------------------------------------------------------
        class QuestStage: 
            def __init__(self, name, stageLabel, startCondition):
                self.name = name
                self.stageLabel = stageLabel
                self.startCondition = startCondition
                
            # Check if we can start this stage
            def checkStage(self):
                return self.startCondition()
                
            # Run the stage scene
            def runScene(self):
                renpy.say("None", "SCENE: " + self.stageLabel)
                renpy.jump(self.stageLabel)