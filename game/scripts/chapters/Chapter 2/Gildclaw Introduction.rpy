label gildclawIntroduction:

    show Temesh with dissolve
    T "Welcome my young acolytes. Welcome to your first day as a full member of the [player.family] family."
    T "I trust you all slept well."
    T "Please, follow me..."
    hide Temesh with dissolve

    "You join your fellow [player.family]s and trail after Temesh through the den site."
    "You follow them over the bridge and into the [player.family] compound." 
    "The compound consists of an open yard half stocked with trade goods. To one side are the colourful tents where the Gildclaws gather to trade, to negotiate and to relax."
    "Temesh Leads you to one of the larger tents, through a side entrance."

    scene expression tent.getBackgroundImage() with fade
    "You enter a lushly decorated room. Around the walls are display cabinets showing strange items from exotic lands."
    "The main area is filled with cushions and short tables."

    show Temesh with dissolve
    T "Please be seated."
    T "This is our common room."
    T "Normally it is where you and your fellow family members come to unwind and meet informally."
    T "It is also used to instruct our young members in the skills that are required for our business."
    T "One of the most important skill that you need to know are interpersonal skills. They are the soul and centre of our family."
    T "Please, take a moment to introduce yourself to those around you."
    T "You will be spending a lot of time together in this room so it is important to find those you can work with."
    hide Temesh with dissolve

    "You look nervously at those seated around you."

    show expression crt_trader.image with dissolve
    t "H-hi there."
    "He looks pretty nervous too."
    $crt_trader.showName()
    t "I’m [crt_trader.name]. W-who are you?"

    menu:
        "I’m [player.name]. Its nice you meet you!":
            $player.changeSkillBonus("Social", 1)
            $crt_trader.addRP(1)
            "He blushes and extends a hand."
            t "This is really p-peculiar isn’t it?"
            t "I-I mean, just yesterday we were just c-cubs and now look at us."
            t "In the actual [crt_trader.family] compound with T-Temesh herself teaching us!"
            "[crt_trader.name]’s tail begins wagging excitedly."
        
        "None of your business!":
            $player.changeSkillBonus("Social", -1)
            $crt_trader.addRP(-3)
            "He shrinks back, lowering his head."
            t "I-I’m s-sorry."
            t "I-I didn’t m-mean to c-cause offence."
        
    P "Hey, what is with the stutter?"
    t "Y-you noticed it d-did you?"
    "[crt_trader.name]’s ears lower"
    t "I-it’s just s-something that happens when I’m n-nervous."
    t "W-which is unfortunately m-most of the t-time."
    t "They s-said I shouldn’t have j-joined the [crt_trader.family]s b-because of it."
    t "B-but Temesh s-said that if I have the desire to join, then I should."
    t "She s-said its better t-to follow your desires a-and struggle than s-settle for what you c-can d-do and be miserable."
    P "Wise words."
    P "So why-"
    hide expression crt_trader.image

    show Temesh
    T "I think we should draw this to a close now."
    T "I hope you have now got to know someone a little more than you did before."
    T "Now, I think it is time I tell you a little of our clan and the role this family plays."
    T "The Riverwood Clan as it stands today was formed some twenty-two years ago."
    T "The [player.family]s were one of the founding families of our clan. The other being the Daggermaws lead by my partner, Marrack."
    T "We were the ones to negotiate the land sharing arrangement with the Barron that brought an end to his attempts to eradicate us."
    T "We were the ones who reestablished trade negotiations with the river traders who supply us with much of our exotic goods."
    T "We are the family who maintain and develop our reputations in the immediate area of the Riverwood Barony and the wider world."
    T "Our name is known in places as far away as Heinreichesburg in the north, Al Alun in the south, New Warrick to the west and Koronovsk to the east."
    T "It is a proud family you have joined and as young members you will learn of the great things your family has achieved and begin to contribute to them in time."

    "Temesh begins to move around the room, handing bundles of papers out to each of the young gnolls"

    T "Now, before we proceed we need to run through some of the rules and regulations that govern the way trade and negotiates are conducted."
    T "Things are a little complex as we have our own regulations but there are also another set of regulations that must be adhered to that are put in place by the Riverwood government itself."
    hide Temesh with dissolve

    "You feel your head droop as trade tariffs, weights and measures and trade good adulteration penalties drift through the air."
    "This exciting new life has an awful lot of theory that needs to be covered it seems… "

    scene black with fade
    "…"
    "… …"

    scene expression tent.getBackgroundImage()
    show Temesh with dissolve
    T "I think we shall draw it to a close there for now."
    T "Please take the guide with you and read them through. There may be a test on them later"
    hide Temesh with dissolve
     
    "There is an audible groan from those around you."
    "You reach over to pick up the pamphlet and catch the eye of [crt_trader.name]."

    menu:
        "Wave goodby to him":
            pass
        
        "Approach him":
            show expression crt_trader.image with dissolve
            "Hey, do you want to hang out after?"
            t "R-really? Sure, w-what did you h-have in mind?"
            $playerCompanion = crt_trader

    return