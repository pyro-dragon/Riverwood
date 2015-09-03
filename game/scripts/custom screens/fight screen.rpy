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
    $nextFunction = "test"
    $enemyHasAttacked = False
    $playerHasAttacked = False
    $screenChange = False
    #$opponentHealth = 100
    $statusText = ""
   
    python: 
                
        #**
        # Attack the enemy
        #
        def attackEnemy(diffilculty): 
            global opponentHealth
            global nextFunction
            global statusText
            global nextFunction
            global changeScreen
            global playerHasAttacked
            
            outputString = ""
            if player.skillTest("hand weapon", playerOpponent.getSkillTotal("dodge") + diffilculty):
                outputString += player.name + " strikes for " + str(diffilculty) + " !"
                opponentHealth -= diffilculty
            else: 
                outputString += player.name + " fails to land the blow!"
                
            if opponentHealth <= 0: 
                outputString = "Enemy defeted!"
                nextFunction = "close"
                return
            else: 
                statusText = outputString
                if enemyHasAttacked == True:
                    nextFunction = "choice"
                    changeScreen = True
                else: 
                    nextFunction = defence
                    changeScreen = False
            
            playerHasAttacked = True
            return
        
        #**
        # Defend against an attack
        #
        def defence():
            global playerHealth
            global nextFunction
            global statusText
            global nextFunction
            global changeScreen
            global enemyHasAttacked
            
            outputString = ""
            
            if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
                outputString += playerOpponent.name + " fails to land the blow!"
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
                    
                outputString += playerOpponent.name + " strikes for " + str(damage) + " !"
                playerHealth -= damage
            
            if playerHealth <= 0: 
                outputString = "You have been defeted!"
                nextFunction = "close"
                return
            else: 
                statusText = outputString
                if playerHasAttacked == True:
                    nextFunction = "choice"
                    changeScreen = True
                else: 
                    nextFunction = "target"
                    changeScreen = True
            
            enemyHasAttacked = True
            return
            
        #statusText = ""
    
screen fight():
    
    window:
        has hbox
        text "Health: " + str(opponentHealth)
        add "enterEnemy" #xpos -50
        
        vbox at screenSlide: 
            add "characters/player head.png"
            text "Health: " + str(playerHealth)
            
            if fightScreenMode == "intro": 
                text "An oponent arives!" yalign 0.5
                timer 1.5 action SetVariable("fightScreenMode", "choice")
                
            elif fightScreenMode == "choice":
                #$enemyHasAttacked = False
                #$playerHasAttacked = False
                #$screenChange = False
                vbox at screenSlide: 
                    textbutton "Attack" action SetVariable("fightScreenMode", "target") xminimum 0.9
                    textbutton "Wait" action [Function(defence), SetVariable("fightScreenMode", "results")] xminimum 0.9
                
            elif fightScreenMode == "target": 
                vbox:
                    textbutton "Head" action [Function(attackEnemy, 10), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 10)
                    textbutton "Arms" action [Function(attackEnemy, 7), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 7)
                    textbutton "Body" action [Function(attackEnemy, 2), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 2)
                    textbutton "Legs" action [Function(attackEnemy, 6), SetVariable("fightScreenMode", "results")] xminimum 0.9 #action Jump("testAttack", 6)
                    
            elif fightScreenMode == "results": 
                vbox: 
                    text "Status: [statusText]"
                    if nextFunction is "close":
                        timer 3 action Return(0)
                    else: 
                        if changeScreen is True:
                            text "Player has attacked: " + str(playerHasAttacked)
                            text "Enemy has attacked: " + str(enemyHasAttacked)
                            text "Next screen is: " + nextFunction
                            timer 3 action SetVariable("fightScreenMode", nextFunction)
                        else: 
                            timer 3 action Function(nextFunction)

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
    