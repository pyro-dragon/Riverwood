#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
init:
    # Available modes:
    # intro - Introduce the fight
    # choice - Present a choice to wait or attack
    # target - Choose the attack target
    # results - Print the results of the last action
    $fightScreenMode = "intro"
    #$opponentHealth = 100
    $statusText = ""
   
    python: 

        #**
        # Wait for the enemy to do something
        #
        def waitForEnemy(): 
            outputString = ""
            
            if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
                outputString += "[playerOpponent.name] fails to land the blow!"
            else: 
                damage = 0
                hitNum = renpy.random.randint(1, 4)
                if hitNum == 1: 
                    outputString += playerOpponent.name + " hits you in the head, ouch!"
                    damage = 10
                elif hitNum == 2:
                    outputString += playerOpponent.name + " throws a fist into your up-held arms."
                    damage = 7
                elif hitNum == 3:
                    outputString += playerOpponent.name + " slams you in the stomarch!"
                    damage = 2
                elif hit == 4: 
                    outputString += playerOpponent.name + " sweeps your legs out from under you."
                    damage = 6
                    
                outputString += playerOpponent.name + " strikes for " + damage + " !"
                playerHealth -= damage
            
            global statusText
            statusText = outputString
                
        #**
        # Attack the enemy
        #
        def attackEnemy(diffilculty): 
            global opponentHealth
            outputString = ""
            if player.skillTest("hand weapon", playerOpponent.getSkillTotal("dodge") + diffilculty):
                outputString += player.name + " strikes for " + diffilculty + " !"
                opponentHealth -= diffilculty
            else: 
                outputString += player.name + " fails to land the blow!"
            
            global statusText
            statusText = outputString
        
        #**
        # Defend against an attack
        #
        def defence():
            outputString = ""
            
            if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
                outputString += "[playerOpponent.name] fails to land the blow!"
            else: 
                damage = 0
                hitNum = renpy.random.randint(1, 4)
                if hitNum == 1: 
                    outputString += playerOpponent.name + " hits you in the head, ouch!"
                    damage = 10
                elif hitNum == 2:
                    outputString += playerOpponent.name + " throws a fist into your up-held arms."
                    damage = 7
                elif hitNum == 3:
                    outputString += playerOpponent.name + " slams you in the stomarch!"
                    damage = 2
                elif hit == 4: 
                    outputString += playerOpponent.name + " sweeps your legs out from under you."
                    damage = 6
                    
                outputString += playerOpponent.name + " strikes for [damage]!"
                playerHealth -= damage
            
            global statusText
            statusText = outputString
            
        #statusText = ""
    
screen fight():
    
    window:
        has hbox
        add "enterEnemy" #xpos -50
        
        vbox at screenSlide: 
            add "characters/player head.png"
            
            if fightScreenMode == "intro": 
                text "An oponent arives!" yalign 0.5
                timer 1.5 action SetVariable("fightScreenMode", "choice")
                
            elif fightScreenMode == "choice":
                vbox at screenSlide: 
                    textbutton "Wait" action Function(waitForEnemy) xminimum 0.9
                    textbutton "Attack" action SetVariable("fightScreenMode", "target") xminimum 0.9
                
            elif fightScreenMode == "target": 
                vbox:
                    textbutton "Head" action [Function(attackEnemy, 10), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 10)
                    textbutton "Arms" action [Function(attackEnemy, 7), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 7)
                    textbutton "Body" action [Function(attackEnemy, 2), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 2)
                    textbutton "Legs" action [Function(attackEnemy, 6), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 6)
                    
            elif fightScreenMode == "results": 
                vbox: 
                    text "Status: [statusText]"
                    timer 3 action SetVariable("fightScreenMode", "choice")

# Enemy slides in from the left
image enterEnemy: 
    "characters/enemy.png"
    xpos -490
    ease 0.45 xpos -50

# Slide meny, etc from the right
transform screenSlide:
    on start:
        xpos 900
        ease 0.45 xpos 0
    