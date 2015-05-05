#-------------------------------------------------------------------------------
# The opening stage to the Mistaken Identity quest
#-------------------------------------------------------------------------------

# The root scene
label mi_raid:
    scene expression arena.name with fade
    
    show expression crt_fighter.imageName with dissolve
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
    else:
        scene black with dissolve
        "..."
        "... ..."
        
        scene expression arena.name with fade
        show expression crt_fighter.imageName with dissolve
        f "We could have really done with your help back there."
        crt_fighter.addRP(-2)
        f "We lost a few."
        f "But we do have this sweet prisoner. Seems like a price or something."
    
    scene black with dissolve

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
    scene expression forestRoad.name with fade
    
    show expression crt_fighter.imageName with dissolve
    f "Alright pipsqueek, we are going to hide down in this ditch." 
    f "There are a couple other guys over behind those fallen trees."
    hide expression crt_fighter.imageName
    
    show expression crt_hunter.imageName
    h "Hey, [player.name], I didn't know you were involved in this"
    h "Any good with a bow?"
    h "We could use another shooter."
    hide expression crt_hunter.imageName
    
    show expression crt_fighter.imageName with vpunch
    f "Oi! [crt_hunter.name]!" 
    f "[player.name] is with me!"
    hide expression crt_fighter.imageName
    
    show expression crt_hunter.imageName
    h "Perhaps, but it makes better sense if [player.name] goes to a position they think they are best at."
    hide expression crt_hunter.imageName
    
    show expression crt_fighter.imageName
    f "Fine, it makes sense. Well?"
    
    menu:
        "Stick with [crt_fighter.name] for a Close Combat attack":
            $mi_raid_attackChoice = "close"
            $playerCompanion = crt_fighter
            $playerCompanion.addRp(2)
        "Go with [crt_hunter.name] for a Ranged Combat attack":
            $mi_raid_attackChoice = "ranged"
            $playerCompanion = crt_hunter
            $playerCompanion.addRp(2)
    
    scene black with fade
    
    call mi_raid_action
    
    return
    
label mi_raid_action:
    "You wait in anticipation"
    "The sound of the approaching cart makes the adrenaline rise in your chest"
    "You spot the cart, it is magnificent and surrounded by a number of armed men on horseback."
    $playerCompanion.c("Get ready")
    
    show expression playerCompanion.imageName with hpunch
    $playerCompanion.c("Now!")
    
    "You and [playerCompanion.name] spring the ambush on the caravan."
    
    scene black with fade

    if(mi_raid_attackChoice == "close"):
        $mi_raid_success = player.skillTest("hand weapon", 20)
    else:
        $mi_raid_success = player.skillTest("archery", 20)
        
    if(mi_raid_success): 
        $playerCompanion.c("Nice one! Lets finish them off!")
    else:
        $playerCompanion.c("What the hell are you doing? Careful with that!")
        
    #call mi_raid_complete

    return
    
# The scene after the raid
label mi_raid_complete:
    scene expression forestRoad.name with fade
    show expression playerCompanion.imageName with dissolve
    
    if(mi_raid_attackChoice == "close"):
        if(mi_raid_success):
            $player.changeSkillBonus("hand weapon", 2)
            $playerCompanion.c("Whack! Slash! Stab!")
            $playerCompanion.c("You were a deamon out there!")
            P "Yeah! Did you see the look on that guys face as I went for his head?"
            $playerCompanion.c("Ha ha ha, yeah!")
            $playerCompanion.c("We really showed them! And we got a hostage too!")
            $playerCompanion.addRp(2)
        else:
            $player.changeSkillBonus("hand weapon", 1)
            $playerCompanion.c("You let us down.")
            $playerCompanion.c("I had to come in and save your ass a few times!")
            P "Yeah but they were in full armour and they were on horseback too."
            $playerCompanion.c("Yeah I supposed. We lost some of our guys, but we got a sweet hostage out of all of that.")
            $playerCompanion.addRp(1)
    else:
        if(mi_raid_success):
            $player.changeSkillBonus("archery", 2)
            $playerCompanion.c("Wow, you really showed them!")
            P "Yeah, did you see the way that guard was going for [fighter.name] and I got an arrow right between his eyes!"
            $playerCompanion.c("If it wans't for you we would have lost some for sure.")
            $playerCompanion.addRp(2)
        else:
            $player.changeSkillBonus("archery", 1)
            $playerCompanion.c("You really arn't very good with that bow yet are you?")
            P "I'm sorry, I'm not a fully fledged warrior yet."
            $playerCompanion.c("We lost some of our people but we managed to capture a high profile captive by the looks of things.")
            $playerCompanion.addRp(1)
        
    $playerCompanion.c("Come on, lets go get a drink.")    
    
    scene black with fade
    
    return