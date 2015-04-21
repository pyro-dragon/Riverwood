#-------------------------------------------------------------------------------
# This is a mission the player must perform with the Bloodrunner datable. 
# Succeeding at this improved their chances with this datable. 
#-------------------------------------------------------------------------------

label bloodrunnerMission: 
    scene bgSilentGrove with fade
    
    if playerFamily == "Bloodrunner": 
        h "Lets see if you are a true Bloodrunner after all."
        
    h "There is a big elk in these parts. If we can catch it we can offer it up to Shana and go down in Bloodrunner history."
    h "No one our age has managed to take on an elk and live to tell the tale."
    
    menu:
        "Hesitate. Say \"Maybe this isn't such a good idea...\"":
            h "Oh don't be such a worrier. We will be fine!"
        "Say \"Yeah! Lets go get it!\"": 
            h "Thats the spirit!"
            
    h "Now lets go... "
    h "Be very *very* quiet. We don't want to alert it."