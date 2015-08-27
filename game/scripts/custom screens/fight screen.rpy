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
                    textbutton "Attack" xminimum 0.9 action SetVariable("fightScreenMode", "target")
                    textbutton "Wait" xminimum 0.9
            elif fightScreenMode == "target": 
                vbox:
                    textbutton "Head" xminimum 0.9 #action Jump("testAttack", 10)
                    textbutton "Arms" xminimum 0.9 #action Jump("testAttack", 7)
                    textbutton "Body" xminimum 0.9 #action Jump("testAttack", 2)
                    textbutton "Legs" xminimum 0.9 #action Jump("testAttack", 6)

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
    