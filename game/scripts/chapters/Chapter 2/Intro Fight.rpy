label introFight:
    scene expression arena.name with fade
    show expression crt_fighter.image with dissolve
    f "Alright there little one. You are about to get creamed!"
    $crt_fighter.showName()
    $playerOpponent = crt_fighter
    
    #while playerHealth > 75 | opponentHealth > 75:
    $knockout = False
    while knockout == False:
        menu:
            "Strike": 
                call attackMenu
                call testDefence
            "Wait": 
                call testDefence
                call attackMenu
                
                
        if playerHealth < 85:
            $knockout = True
        elif opponentHealth < 85: 
            $knockout = True
    return
    
label attackMenu:
    menu: 
        "Head":
            "You try to go for the head!"
            call testAttack(10)
        "Arms": 
            "You aim for [playerOpponent.name]'s rased arms."
            call testAttack(7)
        "Body":
            "You go for a body blow."
            call testAttack(2)
        "Legs":
            "You try to sweep [playerOpponent.name]'s legs from under them."
            call testAttack(6)
            
    return
            
label testAttack(diffilculty): 
    if player.skillTest("hand weapon", playerOpponent.getSkillTotal("dodge") + diffilculty):
        "[player.name] strikes for [diffilculty]!"
        $opponentHealth -= diffilculty
    else: 
        "[player.name] fails to land the blow!"
        
    return
    
label testDefence:
    if player.skillTest("dodge", playerOpponent.getSkillTotal("hand weapon")):
        "[playerOpponent.name] fails to land the blow!"
    else: 
        $damage = 0
        $hitNum = renpy.random.randint(1, 4)
        if hitNum == 1: 
            "[playerOpponent.name] hits you in the head, ouch!"
            $damage = 10
        elif hitNum == 2:
            "[playerOpponent.name] throws a fist into your up-held arms."
            $damage = 7
        elif hitNum == 3:
            "[playerOpponent.name] slams you in the stomarch!"
            $damage = 2
        elif hit == 4: 
            "[playerOpponent.name] sweeps your legs out from under you."
            $damage = 6
            
        "[playerOpponent.name] strikes for [damage]!"
        $playerHealth -= damage
        
    return