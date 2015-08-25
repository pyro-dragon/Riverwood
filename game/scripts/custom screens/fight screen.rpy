#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""
    
screen fight():
    window:
        hbox:
            add enemyBody
            
        vbox: 
            add playerBody 
            
            vbox: 
                
                textbutton "Head" action(call testAttack(10))
                textbutton "Arms" action(call testAttack(7))
                textbutton "Body" action(call testAttack(2))
                textbutton "Legs" action(call testAttack(6))
