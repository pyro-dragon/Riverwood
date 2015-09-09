label mechanicIntroduction:
    
    $ignoringMechanic = False
    
    scene black
    "You walk back from your first class, head spinning."
    "There was a lot to take in and you are trying to file it all away in your mind"

    "*CRASH*"

    m "Ouch!"

    scene expression camp.getBackgroundImage()
    show expression crt_mechanic.image with hpunch
    m "Oh mallets, are you ok?"
    "You rub your leg. You must have had your head so far up in the clouds that you did not see where you were going."
    menu:
        "Yeah thanks, how about yourself?":
            $player.changeSkillBonus("Social", 1)
            $crt_mechanic.addRP(2)
            m "Nothings broken."
            m "Gosh I am so sorry. I was carrying this big stack and just didn’t see where I was going."
        
        "Watch out where the hells you are walking!":
            $player.changeSkillBonus("Social", -1)
            $crt_mechanic.addRP(-3)
            m "Eeek!"
            m "I’m sorry, I’m sorry. I had this huge stack of-"
            m "I really didn’t mean to-"
        
    "You look around at all the long sheets of metal scattered on the ground. There is a slight curvature to their shape."
    menu:
        "What are all these things anyway?":
            $crt_mechanic.addRP(1)
            m "They are blades for the wind turbine we have over near the Overlook"
            m "Clarence says that repairing them would be a good first lesson for us [crt_mechanic.family]s"
        
        "Ignore the metal sheets, you have no interest in bits of metal":
            pass
    
    menu:
        "Let me help you pick them up.":
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
    
    hide expression crt_mechanic.image with dissolve
    $crt_mechanic.showName()
    show Clarence with dissolve
    C "[crt_mechanic.name], there you are."
    C "I thought you had gotten lost."
    hide Clarence

    show expression crt_mechanic.image
    m "Oh, no, sorry sir."
    m "I just dropped them and [player.name] here was helping me pick them up."
    "You grin sheepishly at Clarence."
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