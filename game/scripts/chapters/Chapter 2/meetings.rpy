#-------------------------------------------------------------------------------
# This is the meetings stage. The player meets their family head and one member 
# of their family. They are then cycled around to meet one memeber in each 
# family.
#-------------------------------------------------------------------------------

#-----------------------------
# Introduce the player's 
# family.
#-----------------------------
label meetings:
    scene black
    
    "..."
    "... ..."
    "The new day dawns..."

    if player.family == "Bloodrunners":
        call meetTheBloodRunners
        
    elif player.family == "Coppertails":
        call meetTheCoppertails
        
    elif player.family == "Daggermaws":
        call meetTheDaggermaws
        
    elif player.family == "Gildclaws":
        call meetTheGildclaws
        
    call theOtherFamilies
    
    return

#-----------------------------
# Meet the Bloodrunners. 
#-----------------------------
label meetTheBloodRunners: 
    scene expression camp.name with fade
    
    show shana with dissolve
    S "Awaken my childeren, your training as Bloodrunners begins now."
    S "Now, there will be a structure to your education. You will choose a skill set to learn that is unique to your family."
    S "You will also be shown general skills that you will learn alongside other clan members."
    S "Now, you are going to have to decide which area you wish to specialise in."
    S "[player.name]! Come here, tell me which specialisation you wish to choose..."
    
    # Choose the players class
    call chooseClass

    S "You will be known as [player.name] the [player.career.name]."
    
    scene black with fade
    "You wait while the other young gnolls are sorted into their specialisation."
    S "Ok then come along with me to the Silent Grove. I'll give you a bit of an introduction to our family."

    scene expression grove.name with fade
    show shana with dissolve
    S "We are the second largest family in the clan. We are also, arguably the most important."
    S "As you know, we gnolls are quite adept at hunting. But this is something that our family excells at."
    S "But it is not just hunting that we do, not by a long way. We also know the best places and the right seasons in which to find all kinds of fruits, berries, roots and herbs too."
    S "Roots and herbs roots and herbs are particulally important to us. They form the basis for our medicines."
    S "In my younger days I used to travel from clan to clan, trading work for the secrets to the herbs that their elders kept."
    S "Eventually I met with Clarance with whom I worked to get it all written down. Now, this book..."
    hide shana with dissolve
    
    "You can't help but let your attention drift. You look around the grove, catching your eye on a small song bird, twittering away in one of the trees"
    
    show hunter with dissolve
    h "Are you bored too?"
    P "Huh?"
    P "Yeah I am."
    h "She does go on a bit doesn't she? I want to just start stalking elk!"
    $hunter.showName()
    $hunterMet = True
    h "I'm [hunter.name] by the way."
    h "Who are you?"
    P "I am [player.name]"
    hide hunter with dissolve
    
    show shana with dissolve
    S "Are you two listening over there?"
    hide shana with dissolve
    
    show hunter with dissolve
    h "Yes, of course Miss Shana. Sorry."
    hide hunter with dissolve

    show shana with dissolve
    S "I think that will enough for today. The rest of the day is yours."
    S "Tomorrow you will be seen by one of the other family heads."
    hide shana with dissolve
    
    show hunter with dissolve
    h "Please Miss Shana. I thought that we would be taught by you?"
    hide hunter with dissolve
    
    show shana with dissolve
    S "I will be guiding you through most of your training, yes. But every gnoll should know a little of everything and the other family heads are much better at showing you these things."
    S "Everyone gets cycled around a little. It helps keep things interesting and lets you meet the others."
    S "Gnolls should never get too insular. We are a clan and must work for the good of all of us, not just some of us."
    "Shana nods to everyone, dismissing them."
    hide shana with dissolve
    
    "You spot [hunter.name] walking away. What do you do?"
    menu: 
        "Run up to meet her": 
            $playerCompanion = hunter.name
            call greetHunter
            
        "Leave her alone": 
            call activityCycle

    return

#-----------------------------
# Player introduces themselves 
# to the hunter character. 
#-----------------------------
label greetHunter: 
    P "Hey [hunter.name]!"
    
    show hunter with dissolve
    h "Hey there [player.name]. Wouldn't wait to get away from that sitting around. I want to do something!"
    
    call activityCycle
    
    return
    
# Meet the Coppertails. 
#-----------------------------
label meetTheCoppertails: 
    C "Rise and shine you young'uns. Today you wake as Coppertails and I need to start teaching you a thing or two."

    scene expression camp.name with fade
    
    show clarance with dissolve
    C "Yeah I know its early morning. Its good to get you young'uns in the habbit. You can get so much more done when you start early."
    C "When I started working at the clocks smiths, we would be up every morning at 5:55am so that we could test the alarms of the... "
    C "Now where was I... ?"
    hide clarance
    
    show mechanic
    m "Please sir, you were saying you wanted to teach us something."
    hide mechanic
    
    show clarance
    C "Oh yes. Thats right. But before we do that I am going to need to know what it is you young'uns actully want to be."
    C "I'll call you one at a time"
    C "[player.name]! Come here, tell me what you want to be..."
    
    # Choose the players class
    call chooseClass

    C "Alright! [player.name] you are now a trainee [player.career.name]."
    
    scene black with fade
    "You wait while the other young gnolls are sorted into their specialisation."
    C "Alright then. Lets head on over to the forge where I can talk you guys through what it is to be a Coppertail."

    scene expression forge.name with fade
    show clarance with dissolve
    C "Ok young'uns, welcome to the forge! Don't touch anything unless I say so. Many a young Coppertail has lost a finger or thumb through careless inattention. And you will need all of yours!"
    C "Using your hands is what being a Coppertail is all about. We make things, take things appart, repair things and see exactly how things work."
    C "We also look at things. I mean *really* look at things. Study things, learn things and find out new things about old things."
    C "Using your mind is what being a Coppertail is all about... "
    hide clarance
    
    show mechanic
    m "Sorry sir, but didn't you say that using our hands is what being a Coppertail is all about?"
    hide mechanic
    
    show clarance
    C "Umm, yes. Yes I did. Using a skilled hand controlled by a skilled mind is what being a Coppertail is all about."
    C "Err..."
    C "Yes. Anyways... "
    C "We are pretty much the smallest family in the Riverwood clan. Not a lot of gnolls have the brains or the inclination to become Coppertails. That makes us extra special."
    C "As a family we may not see eye-to-eye with a number of the other, the damned Daggermaws for one, but we are all in this clan together."
    C "Ok then. I have a little task for all of you, just to get you started and so I can asses everyone."
    C "There is a pile of wood scraps in the corner over there and the benches have hand tools in the rack next to them."
    C "I will split you into twos and each group will try to make something to impress me."
    C "Right, you and you. Go over there, you two, take the bench to the right."
    
    scene black with fade
    scene expression forge.name with fade
    
    show clarance with dissolve
    C "And you and you go on that last bench over there."
    hide clarance with dissolve
    
    "You wander over to the battered table with your partner"
    
    show mechanic with dissolve
    m "Well hello there!"
    P "Hello. So we have to try to make something impressive then?"
    $mechanic.showName()
    $mechanicMet = True
    m "I guess so. My name is [mechanic.name] by the way!"
    "She offers to shake your hand."
    P "I'm [player.name]."
    m "Nice! Well then, lets get started!"
    
    scene black with fade
    scene expression forge.name with fade
    
    show clarance with dissolve
    C "Well I think everyone did really well there! I am impressed with the variety. It looks like we have a real crafty bunch of young'uns this year!"
    C "I think we will knock it on the head for today. I'll see you all bright and early tomorrow before sending you to your next teacher."
    hide clarance with dissolve
    
    show mechanic
    m "But I thought you were going to be our teacher?"
    hide mechanic
    
    show clarance
    C "I will be for the most part, but we like our young gnolls to get a good round education in before specialising them further."
    C "It will be a good opportunity to meet the other gnolls and get a real understanding of where we fit in to everything."
    C "Ok, if there is nothing else I'll send you on your merry way."
    hide clarance
    
    "You spot [mechanic.name] walking away. What do you do?"
    menu: 
        "Run up to meet her": 
            $playerCompanion = mechanic.name
            call greetMechanic
            
        "Leave her alone": 
            call activityCycle

    return

#-----------------------------
# Player introduces themselves 
# to the mechanic character. 
#-----------------------------
label greetMechanic: 
    P "Hey [mechanic.name]!"
    
    show mechanic with dissolve
    m "Hey there [player.name]! It looks like the rest of the day is free. Do you want to do anything?"
    
    call activityCycle

    return

#-----------------------------
# Meet the Daggermaws. 
#-----------------------------
label meetTheDaggermaws: 
    M "Raaaaaaghhh!"
    
    scene expression camp.name with hpunch
    
    show marrack
    M "Good, you are awake. Now we can start turning you scrawny wasters into real Daggermaws."
    M "But before we do that I need to know what kind of Daggermaw you really want to be!"
    M "Form up!" 
    M "That means get into a line."
    M "Hurry, hurry, we havn't got all day."
    M "You!"
    M "What is it you want to be?"
    
    # Choose the players class
    call chooseClass

    M "Hmmmm you might just make it as a [player.career.name], if you work your butt off."
    M "Now, you what do you want to be... ?"
    
    scene black with fade
    "..."
    "... ..."
    M "Follow me, we are going to the proving grounds."
    scene expression arena.name with fade
    
    show marrack
    M "So this is a place that should become very familier to you. Much blood has been spilled on this ground and it has all been in the name of creating the finest warriors in the Barony."
    M "I am here to push you to be the best you can be."
    M "The Daggermaws *are* the finest warriors in this land. We have been ever since the Riverwood clan set up in the area."
    M "Temesh can speack about treaties and agreements all she wants but it is the fear of facing us that really keeps the Barran's men at bay."
    M "Now then. I am going to split you up into pairs. Get you sparing. See how much work you runts are going to take."
    hide marrack
    
    show fighter
    f "You there. Lets see what you're made of!"
    P "What the-"
    show fighter with hpunch
    "You dive asside as a fist flies at you"
    P "Hey, I'm not ready!"
    show fighter with vpunch
    f "Well you should have been ready!"
    "He throws another punch... "
    menu: 
        "Dodge it and throw a punch in the chest.": 
            "You twist out of the way and land a clean blow on the massive chest."
            "It does nothing."
            "As you are taken aback a blow comes from the side, laying you out."
            
        "Duck and land a kick in the neithers": 
            "You duck the punch and kick out hard."
            f "Ooooof!"
            "He goes cross-eyes and folds up slowly onto the ground"
    hide fighter
    
    show marrack
    M "Nice blow! That is the sort of thing the Daggermaws like to see."
    hide marrack
    
    "You both recover."
    
    show fighter
    f "You did ok there- for a begginer... "
    P "But we are both starting at the same level-"
    "You eye his muscles"
    f "I suppose so."
    f "So what is your name?"
    P "I'm [player.name]. What about you?"
    $fighter.showName()
    f "I am [fighter.name]. So, are you ready for another round?"
    
    scene black with fade
    "You spar with [fighter.name] for a few more rounds. Each becomming wise to eachothers moves."
    "..."
    
    scene expression arena.name with fade
    
    show marrack
    M "Right. Thats enough."
    M "Thats enough I said!"
    M "Good."
    M "Well I can see you all have a long way to go before you are Daggermaws in name alone."
    M "I see no one has any seriouse wounds..."
    M "... I am disapointed."
    M "You can go now. But I will see you all tomorrow morning bright and early."
    M "I want to make sure you are presentable before I pass you off to one of the other heads."
    M "And if it happens to be that Coppertail... well... "
    M "... just grin and bear it..."
    M "DISM-"
    hide marrack
    
    show fighter
    f "Why do we have to see other family heads? I thought we were going to learn fighting!"
    hide fighter
    
    show marrack with vpunch
    M "DON'T INTERRUPT ME WELP!"
    M "You need to see the others because although I can teach you to be the best fighters in the world, I cannot teach you how to be the best hunters."
    M "A good warrior knows many skills and the others will teach you them much better than I can"
    "Marrack lets a snear slide accross her face"
    M "And you can use the time to show just how powerful you are to the other young gnolls."
    M "Right then. Dismissed!"
    
    "You spot [fighter.name] walking away. What do you do?"
    menu: 
        "Run up to meet him": 
            $playerCompanion = fighter.name
            call greetFighter
            
        "Leave him alone": 
            call activityCycle

    return
            
#-----------------------------
# Player introduces themselves 
# to the fighter character. 
#-----------------------------
label greetFighter: 
    P "Oi, [fighter.name]!"
    
    show fighter with dissolve
    f "What do you want, runt?"
    P "Well we ain't got anything we should be doing now. Do you want to go find something to do?"
    f "Sure. What did you have in mind?"
    
    call activityCycle

    return

#-----------------------------
# Meet the Gildclaws. 
#-----------------------------
label meetTheGildclaws: 
    scene expression camp.name with fade
    
    show temesh with dissolve
    T "I hope you all had a pleasant nights sleep. We should start early, there is much you need to learn as newly minted Gildclaws."
    T "We are the face of the clan. If anyone wishes to make a trade deal or negotiate territory then they will be speaking to a Gildclaw."
    T "It has been a long time since Marrack her Daggermaws were the first point of contact and we want to try to keep it that way."
    T "..."
    T "Now then it is time for you to chose the career you wish to persue. We offer a few to young Gildclaws."
    T "Let's sort that out now and I will then take you over to my tent to discuss this further."
    T "Come here young on. What career are you interested in."

    # Choose the players class
    call chooseClass

    T "A good choice [player.name]. If you truely wish to be a [player.career.name], you will need to work hard."
    T "Let us go to then next one then... "
    
    scene black with fade
    "..."
    "... ..."
    T "I think that is everyone. Let us head over to my tent."
    scene expression tent.name
    
    show temesh
    T "Please, make yourselves comfortable. Would anyone want some tea?"
    T "No?"
    T "Well ok then. As a Gildclaw, and as a diplomat in particular tea will be a central item in your meetings."
    T "Humans seem to favour it greatly, and I must admit, it does have a particularly pleasant taste."
    T "But to get back on track, being a Gildclaw is not as easy as some may make out."
    T "We must be on watch all the time, for the manorisms of others and yourself." 
    T "Much can be said about the way someone sits or how they hold themselves."
    T "Let us then, introduce ourselves to each other. Look at how your partner conducts themselves and try to read more than they are telling you verbally."
    T "Everyone found a partner? Good."
    hide temesh
    
    "A slender gnoll male turns to you, bowing"
    
    show trader
    t "Greetings there uhh..."
    t "..."
    t "What is your name?"
    P "It is [player.name]."
    menu: 
        "Offer your hand to shake.": 
            "Your partner takes your hand and shakes it, avoiding eye contact."
        "Bow to your partner":
            "You bow. Your partner looks flustered, unsure if he should bow again."
            "He settles on a half-bow."
    P "What about your name then?"
    $trader.showName()
    $traderMet = True
    $fighterMet = True
    t "I am [trader.name]. Trainee trader of the Gildclaws. "
    P "Well it is good to meet you [trader.name]."
    "The smile on [trader.name]'s face became glassy."
    t "Umm... "
    t "What do we do now?"
    P "I don't know."
    "..."
    t "So, you are a [trader.career] then?"
    P "Yeah."
    t "Looking forward to learning that kind of thing?"
    P "Sure"
    
    scene black with fade
    "..."
    "... ..."
    scene expression tent.name with fade
    
    show temesh
    "Temesh clapped her hands to bring the room to attention"
    T "Well we will bring this to a close now then."
    T "I hope you all learned something about each other. We will begin again tomorrow at dawn."
    T "The rest of the day is yours. But do not stay away too late, I want you alert and presentable for the other families."
    hide temesh
    
    show trader
    t "Excuse me please Temesh."
    hide trader
    
    show temesh
    T "Yes, [trader.name]?"
    hide temesh
    
    show trader
    t "We are going to be seeing the other families?"
    hide trader
    
    show temesh
    T "A good question."
    T "You are to learn your careers from me, this is true. However in order to be truely rounded individuals you must learn some of the other skills."
    T "I will not pretend that I am even close to competent enough to teach you those things."
    T "You will see one of the family heads tomorrow and join their teachings with the other young gnolls."
    T "But for now you have time to spend. Spend it well and I will see you tomorrow."
    hide temesh
    
    "You spot [trader.name] walking away. What do you do?"
    menu: 
        "Run up to meet him": 
            $playerCompanion = trader.name
            call greetTrader
            
        "Leave him alone": 
            call activityCycle

    return
            
#-----------------------------
# Player introduces themselves 
# to the trader character. 
#-----------------------------
label greetTrader: 
    P "Excuse me, [trader.name]. Before you go..."
    
    show trader with dissolve
    t "Yes?"
    P "Do you want to go and do something together?"
    t "Sure, what sort of something did you have in mind?"
    
    call activityCycle

    return
    
#-----------------------------
# Choose class
#-----------------------------
label chooseClass: 
    if player.family == "Bloodrunners":
        python:
            menuList = []
            for career in bloodrunnerCareers: 
                menuList.append((career.name, career))
            player.career = menu(menuList)
        call checkClass
    elif player.family == "Coppertails":
        python:
            menuList = []
            for career in coppertailCareers: 
                menuList.append((career.name, career))
            player.career = menu(menuList)
        call checkClass
    elif player.family == "Daggermaws":
        python:
            menuList = []
            for career in daggermawCareers: 
                menuList.append((career.name, career))
            player.career = menu(menuList)
        call checkClass
    elif player.family == "Gildclaws":
        python:
            menuList = []
            for career in gildclawCareers: 
                menuList.append((career.name, career))
            player.career = menu(menuList)
        call checkClass
    return

#-----------------------------
# Check that the player is ok
# with their class choice
#-----------------------------
label checkClass: 
    "Are you sure you want to be a [player.career.name]?"
    
    menu: 
        "I am sure.":
            return
            
        "No, I want to choose again.":
            jump chooseClass

#-----------------------------
# End of scene
#-----------------------------
return