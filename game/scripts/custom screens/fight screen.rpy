#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""
    
screen fight():
    window:
        has hbox
        
        add "characters/enemy.png" xpos -50
        
        vbox xalign: 
            add "characters/player head.png"
            
            vbox:
                textbutton "Head" xminimum 0.9 #action jump testAttack(10)
                textbutton "Arms" xminimum 0.9 #action jump testAttack(7)
                textbutton "Body" xminimum 0.9 #action jump testAttack(2)
                textbutton "Legs" xminimum 0.9 #action jump testAttack(6)
