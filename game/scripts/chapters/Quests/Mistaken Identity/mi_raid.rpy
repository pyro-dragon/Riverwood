#-------------------------------------------------------------------------------
# The opening stage to the Mistaken Identity quest
#-------------------------------------------------------------------------------

# The root scene
label mi_raid:
    scene expression arena.name
    
    show fighter with dissolve
    f "Hey pipsqueak."
    f "The scouts say there's a caravan headed down the forest road."
    f "Its unregistered"
    P "Unregisterd?"
    f "Yeah, it means the Baron don't know its comming. Its free reign for us!"
    P "..."
    f "So, do you wanna come along? A couple of us are getting together for a bit of a raid."
    
    # Ask the player to attend
    menu:
        "Sure! I want to get in on some of this":
            $mi_raid_playerAttend = True
            call mi_raid_agree
        "I don't think so.":
            $mi_raid_playerAttend = False
            call mi_raid_disagree
    
    if mi_raid_playerAttend:
        call mi_raid_scene
        
    call mi_raid_complete
    
    return
    
# Player agrees to attend the raid
label mi_raid_agree:
    $ crt_fighter.addRp(2)
    f "Hey yeah!"
    f "Lets go along to the forest road, they are putting together an ambush there"
    return
    
# Player decides not to attend the raid
label mi_raid_disagree:
    $ crt_fighter.addRp(-2)
    f "Aww man, I thought you were cool."
    f "Well screw you, I'll see you later."
    f "Loser."
    return
    
# The scene in which the player attends the raid
label mi_raid_scene: 
    scene expression forestPath.name with fade
    
    show crt_fighter with dissolve
    f "Alright pipsqueek, we are going to hide down in this ditch." 
    f "There are a couple other guys over behind those fallen trees."
    hide crt_fighter
    
    show crt_hunter 
    h "Hey, [player.name], I didn't know you were involved in this"
    h "Any good with a bow?"
    h "We could use another shooter."
    hide crt_hunter
    
    show crt_fighter with vpunch
    f "Oi! [hunter.name]!" 
    f "[player.name] is with me!"
    hide crt_fighter
    
    show crt_hunter
    h "Perhaps, but it makes better sense if [player.name] goes to a position they think they are best at."
    hide crt_hunter
    
    show crt_fighter
    f "Fine, it makes sense. Well?"
    
    menu:
        "Stick with [fighter.name] for a Close Combat attack":
            $mi_raid_attackChoice = "close"
            $playerCompanion = fighter
        "Go with [hunter.name] for a Ranged Combat attack":
            $mi_raid_attackChoice = "ranged"
            $playerCompanion = hunter
    
    scene black with fade
    
    call mi_raid_action
    
label mi_raid_action:
    "You wait in anticipation"
    "The sound of the approaching cart makes the adrenaline rise in your chest"
    "You spot the cart, it is magnificent and surrounded by a number of armed men on horseback."
    $playerCompanion.c("Get ready")
    
# The scene after the raid
label mi_raid_complete: