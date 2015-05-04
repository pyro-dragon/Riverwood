#-------------------------------------------------------------------------------
# The warrior tells the player about a caravan that is coming up. It has no 
# registered passage and so it seen as fair game. The player is asked if they 
# want to go along to join the raid. The players presence will not have much of 
# an affect of the overall success of the raid. The raiders take the caravan 
# passenger hostage and haul him back to the den. First Marrack and then Temesh 
# question the prisoner and it becomes apparent that they are an important 
# dignitary with legitimate reasons for visiting the castle. 
# 
# The player learns through hearsay or the trader that the dignitary was an 
# important Empire official and did not appreciate being abducted by vagabonds. 
# He wants reparations and revenge on those that took him. Temesh is handling 
# things but it is in a delicate situation. For now all caravan raiding is 
# called off. 
# 
# The Daggermaws are outraged at this curtailing on their freedoms and duties. 
# 
# Temesh cools of the dignitary but he still wants to see those who took part in 
# the raid executed. 
#-------------------------------------------------------------------------------

init 10:
    # Declare quest
    $mistakenIdentity = Quest("Mistaken Identity", lambda: True if player.family == "Daggermaw" else False)
    
    # Add quest stages
    $mistakenIdentity.addStage(QuestStage("Raid", "mi_raid", lambda: True))
    $mistakenIdentity.addStage(QuestStage("Interview aftermath", "mi_aftermath", lambda: True))
    $mistakenIdentity.addStage(QuestStage("Baron's response", "mi_response", lambda: True))
    $mistakenIdentity.addStage(QuestStage("Daggermaw disgust", "mi_disgust", lambda: True))
    
    # Add quest to game
    $game.questList.append(mistakenIdentity)
    
    # Quest variables
    mi_raid_playerAttend = False        # If the player attended the raid or not
    mi_raid_attackChoice = "close"      # The form of attack the player makes