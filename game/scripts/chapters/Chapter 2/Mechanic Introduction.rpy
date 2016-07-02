label mechanicIntroduction:
    
    $ignoringMechanic = False
    
    scene black
    "You walk back from your first class, head spinning."
    "There was a lot to take in and you are trying to file it all away in your mind"

    "*CRASH*"

    m "Ouch!"
    
    $game.setLocation(camp)
    show expression crt_mechanic.image with hpunch
    m "Oh darn, are you ok?"
    "You rub your head where she crashed into you. "
    menu:
        "Yeah, I think so. How about yourself?":
            $player.changeSkillBonus("Social", 1)
            $crt_mechanic.addRP(2)
            m "Nothings broken."
            m "Gosh I am so sorry. I was carrying this big stack and just didn’t see where I was going."
        
        "Watch where the hell you are going!":
            $player.changeSkillBonus("Social", -1)
            $crt_mechanic.addRP(-3)
            m "Eeek!"
            m "I’m sorry, I’m {i}really{/i} sorry. I had this huge stack of-"
            m "I really didn’t mean to-"
        
    "You look around at all the long sheets of metal scattered on the ground."
    menu:
        "Ask about the metal sheets":
            $crt_mechanic.addRP(1)
            P "What are all these things anyway?"
            m "They are blades for the wind turbine we have over near the Overlook"
            m "Clarence says that repairing them would be a good first lesson for us [crt_mechanic.family]s"
            call mechanicIntroduction_mean_choice
        
        "Ignore the metal sheets, you have no interest in bits of metal":
            $ignoringMechanic = True;
            pass
    
    hide expression crt_mechanic.image with dissolve
    $crt_mechanic.showName()
    show Clarence with dissolve
    C "[crt_mechanic.name], there you are."
    C "I thought you had gotten lost."
    hide Clarence

    show expression crt_mechanic.image
    m "Oh, no, sorry sir."
    
    if ignoringMechanic == False:
        m "I just dropped them and [player.name] here was helping me pick them up."
        "You grin sheepishly at Clarence."
    else: 
        m "I just wasn't looking where I was going and ran into someone."
        m "I am so sorry, so, so sorry."
    
    hide expression crt_mechanic.image

    show Clarence
    C "Hmm, well you should get along to the forge, the really need those turbine blades."
    hide Clarence
    
    show expression crt_mechanic.image
    m "Yes, sit. I'll head off right away!"
    
    if ignoringMechanic == False:
        m "Thanks for your help [player.name]!"
    hide expression crt_mechanic.image
    
    show Clarence
    C "You are that young [player.family] ain’t you?"
    P "Yes I am, sir."
    C "How did you find your first lesson?"

    menu:
        "Very interesting, very engaging sir. I am enjoying my time with the [player.family]s.":
            C "Thats good to hear."

        "Well to be honest sir, its a little dull.":
            C "Ha ha ha!"
            C "The [player.family]s can get a little tedious at times!"
            C "You should have joined the [crt_mechanic.family]s."

    C "Well we should get back to the forge now."
    hide Clarence

    if ignoringMechanic == True:
        show expression crt_mechanic.image
        m "Thanks for helping me out!"
        m "It was nice meeting you."
        hide expression crt_mechanic.image
    
    return
    
label mechanicIntroduction_mean_choice:
    menu:
        "Help her pick them up.":
            $player.changeSkillBonus("Social", 1)
            $crt_mechanic.addRP(1)
            m "Thank you!"
            m "I can’t believe I just ran into you like that."
            P "Its ok. Say, what is this turbine for then?"
            m "Oh!"
            m "Umm…"
            m "All kinds of stuff!"
            m "Right now its hooked up to some grinding gear to pulverise some iron ore for one of Clarence’s experiments"
            m "Its really cool!"
            m "Just using a little bit of lime and charcoal he’s been making this really strong iron."
            m "But, like, you need to get the chemistry just right"
            m "And the heat too. He’s had to get a whole new furnace built and… "
            
        "I haven’t got time for this.":
            $crt_mechanic.addRP(-1)
            $ignoringMechanic = True
            pass
            
    return