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
   
    python: 
        def waitForEnemy(): 
            if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
                say(None, "[playerOpponent.name] fails to land the blow!")
            else: 
                damage = 0
                hitNum = renpy.random.randint(1, 4)
                if hitNum == 1: 
                    say(None, "[playerOpponent.name] hits you in the head, ouch!")
                    damage = 10
                elif hitNum == 2:
                    say(None, "[playerOpponent.name] throws a fist into your up-held arms.")
                    damage = 7
                elif hitNum == 3:
                    say(None, "[playerOpponent.name] slams you in the stomarch!")
                    damage = 2
                elif hit == 4: 
                    say(None, "[playerOpponent.name] sweeps your legs out from under you.")
                    damage = 6
                    
                say(None, "[playerOpponent.name] strikes for [damage]!")
                playerHealth -= damage
                
        def attackEnemy(diffilculty): 
            if player.skillTest("hand weapon", playerOpponent.getSkillTotal("dodge") + diffilculty):
                say(None, "[player.name] strikes for [diffilculty]!")
                opponentHealth -= diffilculty
            else: 
                say(None, "[player.name] fails to land the blow!")
                
        def defence():
            if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
                say(None, "[playerOpponent.name] fails to land the blow!")
            else: 
                damage = 0
                hitNum = renpy.random.randint(1, 4)
                if hitNum == 1: 
                    say(None, "[playerOpponent.name] hits you in the head, ouch!")
                    damage = 10
                elif hitNum == 2:
                    say(None, "[playerOpponent.name] throws a fist into your up-held arms.")
                    damage = 7
                elif hitNum == 3:
                    say(None, "[playerOpponent.name] slams you in the stomarch!")
                    damage = 2
                elif hit == 4: 
                    say(None, "[playerOpponent.name] sweeps your legs out from under you.")
                    damage = 6
                    
                say(None, "[playerOpponent.name] strikes for [damage]!")
                playerHealth -= damage
    
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
                    textbutton "Head" action Function(attackEnemy, 10) xminimum 0.9 #action Jump("testAttack", 10)
                    textbutton "Arms" action Function(attackEnemy, 7) xminimum 0.9 #action Jump("testAttack", 7)
                    textbutton "Body" action Function(attackEnemy, 2) xminimum 0.9 #action Jump("testAttack", 2)
                    textbutton "Legs" action Function(attackEnemy, 6) xminimum 0.9 #action Jump("testAttack", 6)

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
    