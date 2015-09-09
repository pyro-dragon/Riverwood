label daggermawIntroduction:

    show Marrack with vpunch
    M "Get up you worms!"
    M "In the name of the Seven Hells I have never seen such a bunch of welps in all my years."
    M "Get yourselves down to the Arena ASAP!"
    M "Come one, move move! The sun is shining, the birds are singing and I’ll bite off the tail of the last welp to get there!"
    hide Marrack with dissolve

    "You head out with the other young [player.family]s across the den site grounds and into the ancient ruins of an arena."
    "You gaze around the crumbling and overgrown stone floor and tied seating. The eroded remains of statues line the outer ring of the main grounds."

    scene expression arena.getBackgroundImage() with dissolve
    show Marrack
    M "Get up in line!"
    M "Come on, I don’t have all day!"
    M "You there! What is your name?"
    hide Marrack

    show expression crt_fighter.image
    $crt_fighter.showName();
    f "[crt_fighter.name], Marrack, sir, ma’am!"
    hide expression crt_fighter.image

    show Marrack
    M "Is that so? Well I only know two things with a name like that-"
    M "-fairies, and daisies."
    M "I don’t see any wings on you recruit!"
    hide Marrack

    "You glance over at [crt_fighter.name] out the corner of your eye. He might not have any petels but he seems rooted to the spot."
    "Marrack wanders over to you, glaring at you almost muzzle to muzzle."

    show Marrack
    M "I see you eyeballing our flowery friend over there."
    M "And who might you be young pup?"

    menu:
        "I, err. I-I’m [player.name].":
            M "Sound off! I can’t hear you."
            P "[player.name]."
            M "Well, what a cute name you have there."
            M "Lets see if we can toughen you up a bit."

        "[player.name]!":
            "Confident there are you?"
            "We’ll see just how confident you are after a few weeks of seven mile runs at sunrise!"
    
    "Marrack wanders up and down the line, eyeing up each of the fresh new [player.family]s."
    
    M "..."
    M "Ok then you lot. I am Marrack [player.family] and I will be your worst nightmare."
    M "You have joined the [player.family]s. We are one of the oldest families. We are the biggest family."
    M "And it will be my job to get you sacks of manure up to the kind of standard that the [player.family]s exemplify."
    M "We are at a basic level all warriors."
    M "From the time you spoke our name last night you have been sworn to protect and fight for the Riverwood clan and its interests."
    hide Marrack

    show expression crt_fighter.image
    f "Excuse me ma’am."
    f "When do we get given weapons?"
    hide expression crt_fighter.image

    show Marrack
    M "[crt_fighter.name] is it?"
    hide Marrack

    show expression crt_fighter.image
    f "Yes ma’am."
    hide expression crt_fighter.image

    show Marrack
    M "Well [crt_fighter.name], while I appreciate your eagerness but…"
    M "… YOU WILL NOT INTERRUPT ME OR SPEAK WITHOUT BEING DIRECTLY ADDRESSED."
    hide Marrack

    show expression crt_fighter.image
    f "Yes ma-"
    hide expression crt_fighter.image

    show Marrack with hpunch
    M "DID I SAY YOU COULD SPEAK?"
    hide Marrack

    show expression crt_fighter.image
    f "…"
    hide expression crt_fighter.image

    show Marrack
    M "Good. You are learning. That is going to be a very important thing to do in this family."
    M "Right. Before I was interrupted I was going to give you runts a quick run through some of our history."
    M "Try and impress upon you some reasons to feel proud to be a [player.family] and something to think back to when it starts getting tough."
    M "And it will get tough."
    M "So…"
    M "As I said, we are one of the first founding families. The other is Temesh’s Gildclaws."
    M "The clan, as it is now was formed some twenty two years ago when we rose up against the tyrany of OLD LEADER."
    M "It was a great battle and a great many good warriors were lost that night."
    M "The clan was formed from the survivors of that fight. We came to this site and founded a new clan."
    M "Temesh lead the efforts to establish us diplomatically while I took charge of securing our new den site from those still loyal to OLD LEADER and the roving Orc tribes."
    M "The division of roles here was formalised in the founding of our families."
    M "Since then we have split only once- when the Bloodrunners were formed."
    M "Our core duty since the clans first founding has been to protect it." 
    M "And we have always been exceedingly good at that."
    M "So much so that the Baron has himself on occasion has hired us out for protection and escort missions within the Barony."
    M "…"

    M "Well that is enough history for now. I think its about time to try something a little more practical."
    M "I want you to all pair up. Square up to each other."
    hide Marrack

    show expression crt_fighter.image
    f "Alright there [player.name]."
    f "put them up."
    hide expression crt_fighter.image

    show Marrack
    M "This is simple."
    M "Try to get your partner on the floor. I want to see what what you are made of."
    M "Ready…"
    M "Go!"
    hide Marrack

    call introFight

    show Marrack
    if playerWins:
        $player.changeSkillBonus("hand weapon", 2)
        M "Well [player.name], you can fight after all! I am impressed."
    else:
        $player.changeSkillBonus("hand weapon", 1)
        M "[crt_fighter.name], I thought you might win out."

    M "Ok, everyone stop."
    M "STOP I said!"
    M "Good. I think that was an excellent display of just how much work I have to turn you lot into true [player.family]s"
    M "Tomorrow we will start work on shaping you up with some actual training."
    M "For now you should go get yourselves cleaned up and have an early night."
    M "Dismissed!"
    hide Marrack

    if playerWins:
        "You spot [crt_fighter.name] wandering off, his nose bloody."
    else:
        "You see [crt_fighter.name] wander off with a smug look on his face."

    menu:
        "Head over to him.":
            P "Hey, you were pretty good back there."
            
            show expression crt_fighter.image
            f "You think so?"
            P "Yeah, I almost never stood a chance."
            f "That’s right! Ha ha."
            P "Wanna go hang out for a bit?"
            f "Why not? What did you have in mind?"
            $playerCompanion = crt_fighter

        "Leave him alone.":
            pass

    return