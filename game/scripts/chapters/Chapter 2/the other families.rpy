#-------------------------------------------------------------------------------
# This is where the player meets all the other families
#-------------------------------------------------------------------------------

label theOtherFamilies:
    if player.family == "Coppertail": 
        scene expression forge.name with fade
        show clarance with dissolve
        C "Ah, good morning young Coppertails."
        C "It is time to begin your second day as Coppertails and you will do that by going to a completely different family!"
        C "You will start with a visit to the Gildclaws I think."
        C "Hop along to Temesh's tent. I'll see you tomorrow"
        hide clarance
        
        call visitingTheGildclaws
        
        scene expression forge.name with fade
        show clarance with dissolve
        C "Morning Coppertails. Today I will be packing you off to see the fearsome Daggermaws."
        C "Try to take them seriously otherwise Marrack will come and have a word with me and she can be really scary."
        C "Off you go and grow to be more war-like!"
        hide clarance
        
        call visitingTheDaggermaws
        
        scene expression forge.name with fade
        show clarance with dissolve
        C "Well hello again, sorry to wake you so early but Shana does love dawn."
        C "She seems to think there is a 'magical vibe' to it."
        C "Anyways, head over to the glade and have fun!"
        hide clarance
        
        call visitingTheBloodrunners

        scene expression forge.name with fade
        show clarance with dissolve
        C "Greetings there chappies!"
        C "I hope you found your time with the other families enlightening!"
        C "The family heads will be running lessons for you young gnolls."
        C "As adults it is your decision as to which you choose to attend and which direction you wish to take your education."
        C "And if you should be having any issued you wish to disguss, any guidence needed I will be available to help you."
        C "With that it just leaves me to wish you all luck in the coming months." 
        
        scene black with fade
        "As you wander back to your bed your mind is spinning."
        "The future is happening now and it happening fast. You will need to grasp it or watch it spin off without you..."
        "..."
        
    elif player.family == "Daggermaw": 
        scene expression arena.name with fade
        show marrack with dissolve
        M "Wake up maggots! It is your seccond day as Daggermaws but alas you won't have me breathing down your neck today."
        M "No. Today you will have to head over to the Bloodrunner's sacred grove thing to learn some mumbo jumbo."
        M "Temesh says you are to get a rounded training so head over there and put up a good face for the Daggermaws."
        M "Jump to it!"
        hide marrack
        
        call visitingTheBloodrunners
        
        scene expression arena.name with fade
        show marrack with dissolve
        M "Its light, you shouldn't still be asleep!"
        M "This time you are being sent packing to see what that Coppertail guy wants to show you."
        M "Try not to laugh."
        hide marrack
        
        call visitingTheCoppertails
        
        scene expression arena.name with fade
        show marrack with dissolve
        M "It is a fine morning to be a Daggermaw."
        M "Which is why you are being sent to the Gildclaws."
        M "Temesh is wise and cunning so respect her. Even is she does want to show you some damned mind games and nonsense."
        M "Well soon have you back here learning proper Daggermaw skills but for now, go to it."
        hide marrack
        
        call visitingTheGildclaws
        
        scene expression arena.name with fade
        show marrack with dissolve
        M "Did you all like your little holiday with the other families?"
        M "Good, because now the real work begins!"
        M "Because you are no loger welps you have a choice in what you study now."
        M "But it is not going to be easy, no way at all!" 
        M "Ha ha ha!"
        M "Good luck in your future careers maggots. I know some of you are really going to need it."
        
        scene black with fade
        "As you wander back to your bed you look around you and see the others, some with looks of aprehension, some with looks of determination."
        "You are unsure what you should feel, but the future will happen regardless and you had better make the most of it."
        "..."
        
    elif player.family == "Bloodrunner": 
        scene expression grove.name with fade
        show shana with dissolve
        S "Greetings my young charges."
        S "The stars have deamed this an optimal time for learning and as such you will acompany Clarance and his Coppertails."
        S "While I cannot fully approve of the Coppertail's approach to many things, they see natures offerings as something to be exploited and manipulated, they never the less offer great insights into our world."
        hide shana
        
        call visitingTheCoppertails
        
        scene expression grove.name with fade
        show shana with dissolve
        S "It is another fine morning, blessed by the suns warm embrase."
        S "Today you will be seeing our great leader Temesh and listen to her teachings with her Gildclaws."
        S "Learn them well young ones as they are the reason we no longer have to fight bloody tooth and claw for our existence."
        hide shana
        
        call visitingTheGildclaws
        
        scene expression grove.name with fade
        show shana with dissolve
        S "Favourable moon phases shine tollerance upon us this day and this is well."
        S "For today you must visit Marrack's arena."
        S "She is abbrasive, yes. But wise in the unfortunate ways of war."
        S "While we can thank Temesh for our peaceful lives today, we must thank Marrack for a good prospect of having lives tomorrow."
        S "Peace, alas is fleeting and she can tell you how to make it through times when it doesn not spread its wings for us."
        hide shana
        
        call visitingTheDaggermaws
        
        scene expression grove.name with fade
        show shana with dissolve
        S "My young ones, welcome back once more."
        S "You time with the other families was of edication was it not?"
        S "Your training is now in your hands."
        S "Take what you have learned so far, listen to your heart and help it guide you in the choices you make to form your future."
        S "I will of course be available to offer any guidance I can to you however. "
        S "Now, go and rest, be ready for what the world will bring to you tomorrow and the time after that."
        
        scene black with fade
        "You join the others as they wander back to their beds."
        "Your mind buzzes with ideas and thoughts of the future. You hope that you will be able to make the right choices."
        "..."
        
    elif player.family == "Gildclaw":
        scene expression tent.name with fade
        show temesh with dissolve
        T "My young accolites. This will be the first of three introductory sessions to the other families."
        T "I have chosen for you to pay a visit to the Coppertails to start with. Clarance is wise if... different."
        T "He will guide you in the teachings that I cannot. I bid you farewell until tomorrow."
        hide temesh
        
        call visitingTheCoppertails
        
        scene expression tent.name with fade
        show temesh with dissolve
        T "Ah, it is a pleasant morning once again."
        T "A perfect time to spend in the woods with Shana."
        T "Please proceed to the glade where she and the other Bloodrunners will be waiting."
        hide temesh
        
        call visitingTheBloodrunners
        
        scene expression tent.name with fade
        show temesh with dissolve
        T "Alas, I must inflict upon you the trial of spending time with Marrack."
        T "She is not the easiest to get along with but ease of company is not the first things to be looking for in a warrior."
        T "Aquest to her demands and you will likely lern a lot."
        hide temesh
        
        call visitingTheDaggermaws
        
        scene expression tent.name with fade
        show temesh with dissolve
        T "Welcome back."
        T "You have all begun a journey that will take you through the rest of your lives."
        T "Although for practical purposes this leg of the journy will last a year."
        T "Take advantage of all the families, learn your stregths and your weakenesses."
        T "Learn what you passion is and then hone in on it with ruthlessness."
        T "Your future will be shaped by the things you do duing this year, so make them good things."
        T "I will bid you all a good night and fair passage to your own destiny."
        
        scene black with fade
        "As you turn away you watch the faces of the others. It seems that you are not the only one who feels uncertain."
        "The furture looks bright but you are going to have to do your very best to make sure it remains so."
        "..."

    "ENDING"
    return

label visitingTheCoppertails: 
    scene expression forge.name with fade
    
    show clarance with dissolve
    C "Ah, welcome. Welcome back everyone."
    C "It is your first week as Coppertails and I am glad that we still have everyone"
    C "And I can see that we have more than those faces from yesterday."
    C "Please everyone, extend a warm welcome to the [player.family]s that have joined us for a session today."
    C "They have joined us todat to learn a little of the skills we Coppertsils are good at"
    C "I think we should turn to the work benches and do a little build."
    C "First though, I want everyone to find a partner. We will split Coppertails with [player.family]s."
    
    # Encounter your rival
    if crt_rival.family == "Coppertail":
        hide clarance with dissolve
        show expression crt_rival.imageName
        c "Why do we have to share our time with the damn [player.family]s?"
        c "They are totally worthless!"
        hide expression rival.imageName
        
        show clarance
        C "Calm yourself young [crt_rival.name]. It is good to see that you have a fiery loyalty to your family aready but that was a little rude."
        hide clarance
        
        show expression crt_rival.imageName
        c "Yeah but... "
        c "grrr... "
        c "ok..."
        hide expression rival.imageName
        
    # Encounter your ally
    if crt_ally.family == "Coppertail": 
        hide clarance with dissolve
        show expression crt_ally.imageName
        e "Hey, fancy meeting you here!"
        e "How are you finding life in the [player.family] family?"
        P "Yeah. Its good. Although my first experience was being woken up too early and talked at for far too long."
        e "More or less the same thing with me."
        hide expression crt_ally.imageName        
        show clarance
        C "Its great that you two are on such good terms but we really have to be getting on."
        hide clarance
        
        show expression crt_ally.imageName
        e "I'm sorry sir"
        hide expression crt_ally.imageName
        show clarance
    
    C "So today we are going to have a look at fletching. This is a basic skill that you should all learn."
    C "We will be making a simple wooden crossbow bolt. Nearly all of you will end up with a crossbow at some point and having the skill to make your own ammunition would be an incredibly useful skill to have."
    C "There are a few blanks in front of you... "
    C "But first! I am always forgetting... First!"
    C "Turn to your partner and greet them. Its always good to mix up amongst the families."
    hide clarance with dissolve 
    
    "Feeling somewhat off ballence you turn to your partner at the work bench"
    
    show expression crt_mechanic.imageName with dissolve
    m "Hey there!"
    $crt_mechanic.showName()
    m "I'm [crt_mechanic.name]. Who are you then?"
    P "I'm, err... I'm [player.name]."
    m "Sorry about Clarance. He can be a little... sudden. "
    P "..."
    m "So! You are a [player.family]? How is that?"
    P "It's ok I guess..."
    P "What is it like being a Coppertail?"
    m "Oh it is the best! We have so many cool things that we work on."
    m "There's the agriculture project with the Bloodrunners, the new forge thats being built and the improved blunderbus- "
    P "Wait, havn't you been in the family for only a few days?"
    m "Yeah... "
    m "But I learned a lot!"
    $crt_mechanic.met = True
    hide expression crt_mechanic.imageName
    
    show clarance
    C "Ok then everyone, settle down, settle down. Lets get on with this. "
    C "First, pick up the blank..."
    
    scene black
    "..."
    "... ..."
    scene expression forge.name with fade
    
    show clarance
    C "Well that was more, or less successful. I think we all learned... something."
    C "There is certainly promise amongst everyone here. Keep up that practice and you will all master the skill."
    $player.changeSkillBonus("engineering", 1)
    C "So I think that concludes this session. I hope you all found it useful. I'll see the Coppertails bright and early tomorrow and the [player.family]s next week. "
    hide clarance
    
    "You pick up the bolt you have made and... "
    menu: 
        "Turn to [crt_mechanic.name]...": 
            $playerCompanion = crt_mechanic
            show expression crt_mechanic.imageName
            P "Do you want to do anything after this?"
            m "Sure! Did you have anything in mind?"
        "Hurry off.": 
            pass
    
    # Go to hang out activity cycle. 
    call activityCycle

    return
    
label visitingTheDaggermaws: 
    scene expression arena.name with fade
    # Welcome group to the second day. 
    show marrack with vpunch
    M "Raawr!"
    M "Welcome back maggots to another day at boot camp!"
    M "This time though we have some additional maggots. These whimps are from the [player.family]s."
    M "We are going to be showing them a thing or two so they don't come last in a fight with a sqirrel."
    M "Ha ha ha ha!"
    M "So, you all have a knife don't you?"
    M "Good"
    M "But you don't know how to use it properly I'll bet."
    $crt_fighter.showName()
    M "[crt_fighter.name]!"
    hide marrack
    
    show expression crt_fighter.imageName
    f "Yeah?"
    hide expression crt_fighter.imageName
    
    show marrack
    M "Come here."
    M "And you."
    P "Me?"
    M "Yes, come up here both of you."
    M "Get your knives out."
    M "..."
    M "... Ok, who can tell me what [player.name] did wrong?"
    hide marrack
    
    show expression crt_fighter.imageName
    f "Yeah I know. They didn't have it ready."
    P "I didn't what-"
    show expression crt_fighter.imageName with hpunch
    "[crt_fighter.name] knocks the knife from your hand."
    f "You got a weak grip there!"
    f "Ha ha ha!"
    hide expression crt_fighter.imageName
    
    show marrack
    M "Ha ha ha!"
    M "[crt_fighter.name] is right. You need to be ready with your knife. Now one who wants to cause you harm is going to wait for you to get ready."
    M "Or give you a warning."
    show marrack with vpunch
    "Marrack turns and sweeps [crt_fighter.name] to the floor."
    hide marrack
    
    show expression crt_fighter.imageName
    f "Ow!"
    f "Hey that wasn't fair. I wasn't-"
    hide expression crt_fighter.imageName
    
    show marrack
    M "Ready?"
    M "Exactly."
    M "Now pair up. I want each of you to try and catch the other off guard."
    M "If any of you get blood on my nice arena floor you will be licking it up."
    M "Have at it!"
    
    scene black with fade
    "..."
    "... ..."
    
    scene expression arena.name with fade
    show marrack
    M "I think we can definately stop now."
    M "Stop I said!"
    M "Good."
    M "I saw some good moves there. Others need to work out what the hell their hands are for."
    M "I think this has been a good introduction for the little [player.family]s too. I will see you next week."
    M "The rest of you, I'll see you tomorrow at dawn where we will try some archery drills."
    M "Dismissed!"
    hide marrack with dissolve
    
    $crt_fighter.met = True

    "You see [crt_fighter.name] marching away. Do you..."
    menu:
        "Run up to join him.":
            show expression crt_fighter.imageName
            P "Hey there. That was pretty intense."
            f "Yeah, it was a bit. You arn't too bad you know. Maybe you should ask Marrack if you can be a [crt_fighter.family]."
            P "I don't think she would let me!"
            P "So, do you want to do something now?"
            f "Like what?"
            $playerCompanion = crt_fighter
        "Leave him alone": 
            pass
    
    # Go to hang out activity cycle. 
    call activityCycle
    return
    
label visitingTheGildclaws: 
    scene expression tent.name with fade
    
    # Welcome group to the second day. 
    show temesh with dissolve
    T "Ah another good morning my young accolites."
    T "Today we are joined by the young ones from the [player.family]s."
    T "Please extend them a warm Gildclaws welcome."
    T "They have joined us to learn some of the more neuanced skills needed to make a valuable contribution to our clan."
    T "Today we will be looking more at posture and pose, as well as manners."
    T "Yes, even a rough and ready Daggermaw needs to know a little of tact and delicacy or they will found themselves in a bad way indeed."
    
    if crt_rival.family == "Gildclaws":
        hide temesh
        
        show rival
        c "Even so, I doubt [player.name] has enough class to know how to shake hands!"
        c "They have always been a rough around the edges and it shows now that they have joined the [player.family]s!"
        hide rival
        
        show temesh
        T "[crt_rival.name]! That is certainly not the kind of attitude I want to see comming from a Gildclaw."
        T "Appologiese to [player.name] and I will talk to you afterwards."
        hide temesh
        
        show rival
        c "But-"
        hide rival
        
        show temesh
        T "No. None of that."
        hide temesh
        
        show rival
        r "Ugh, fine."
        r "I am sorry for speaking out of turn."
        hide rival
        
        show temesh
        T "Thank you."
        
    T "So as you can see from the tables set out here we are going to be taking tea."
    T "Yes, it seems trivial but in a formal setting it is a complex activity with many subtleties."
    T "Now, everyone take a seat. Yes two per table."
    T "..."
    T "Yes, I think it would be preferable for the Gildclaws and [player.family]s to mix."
    T "I want one of each at the tables."
    T "Yes, thats better."
    T "Lets begin by introducing ourselves..."
    hide temesh
    
    show expression crt_trader.imageName
    t "Err, good morning to you."
    $crt_trader.showName()
    t "I'm [crt_trader.name]. Nice to meet you... "
    t "..."
    P "Well, I'm [player.name]. It is good to mee you too. I think."
    t "..."
    P "..."
    t "... what do we do now?"
    hide expression crt_trader.imageName
    
    show temesh
    T "Well I hope we are all nicely aquanted with each other now."
    T "So the next part is actully pouring the tea."
    T "First you have to heat the cups by pouring in a little hot water."
    T "Then after you have done that..."
    
    scene black with fade
    "..."
    "... ..."
    
    scene expression tent.name with fade
    
    show temesh with dissolve
    T "Well that was certainly an enlightening experience."
    T "Though I must say that some of you have certainly some work to do."
    T "And we need to buy more teapots too now. But some of those needed replacing anyway"
    T "Anyway."
    T "I will see the Gildclaws tomorrow. As for the [player.family]s. I will bid you adure until next week."
    hide temesh
    
    "[crt_trader.name] rises slowly from the chair, whiping te from himself as he does so."
    
    $crt_trader.met = True

    menu: 
        "Help him.": 
            P "Do you need a hand there?"
            
            show expression crt_trader.imageName
            t "Oh, no. I should be ok I think."
            t "Thank you though."
            P "Hey, after this do you want to hang out for a bit?"
            t "Uhh, sure. What did you have in mind?"
            $playerCompanion = crt_trader
            
        "Leave him.": 
            pass
    
    call activityCycle
    return
    
label visitingTheBloodrunners: 
    # Welcome group to the second day. 
    scene expression grove.name with fade
    
    show shana with dissolve
    S "Welcome back to the grove my young ones. Today we are joined by some of the [player.family]s."
    S "We will be learning a little about herbs this morning."
    S "This is basic medicine work that everyone should know and should be able to use no matter what family or career they join."
    S "If you just divide into pairs I will hand out herb bags for you to examine."
    hide shana with dissolve
    
    "Everyone begins to mvoe about, finding a working partner"
    
    show expression crt_hunter.imageName with dissolve
    h "You. You'll do."
    P "Me?"
    $crt_hunter.showName()
    h "Yeah, come along. I'm [crt_hunter.name]. Lets get this over with."
    hide expression crt_hunter.imageName
    
    if crt_rival.family == "Bloodclaw": 
        "You notice a familier face as he knocks shoulders with you"
        
        show expression crt_rival.imageName
        c "Whatch where you are going butthead!"
        c "I don't want to catch some [player.family] stupidity from you."
        P "You can't catch stupidity. Thats..."
        P "... stupid."
        c "Oh yeah! Why don't you make something of it then."
        hide expression crt_rival.imageName
        
        show expression crt_hunter.imageName
        h "Hey, hold it [rival.name]!"
        h "Stop picking on the stupid little [player.family]."
        P "Hey, I'm not-"
        h "Shut up, come with me, you are my partner."
        hide expression crt_hunter.imageName
        
        show expression crt_rival.imageName
        c "You can't just-"
        hide expression crt_rival.imageName
        
        show expression crt_hunter.imageName
        h "Shut up [crt_rival.name]. I can and I have." 
        h "Now frack off."
        hide expression crt_hunter.imageName
        
        show shana
        S "I think language like that brings disharmony to the glade."
        
    if crt_ally.family == "Bloodrunner": 
        show expression crt_ally.imageName
        e "Hey there! Welcome to the Bloodrunner grove."
        e "How is life with the [player.family]s?"
        P "Its ok I think. Still trying to find my feet."
        P "How about you?"
        e "I'm doing great! I'm a [crt_ally.career]! Lots of things to learn."
        hide expression crt_ally.imageName
        
        show expression crt_hunter.imageName
        h "Come on pip-squeek. We have some learning to do."
        P "See you later [crt_ally.name]."
        hide expression crt_hunter.imageName
        
    show shana
    S "Ok, has everyone found a partner? Good."
    S "Now then, when I give you a bag I want you to empty it out on the ground in front of you."
    S "You and your partner must then spend some time trying to identify them."
    hide shana
    
    "You spend some time musing over the herbs and roots in front of you"
    
    P "Have you seen many of these before?"
    
    show expression crt_hunter.imageName
    h "Of course. Now, if I could just try and remember the names."
    h "Maybe if I taste one... "
    
    scene black with fade
    "..."
    "... ..."
    
    scene expression grove.name with fade
    show shana with dissolve
    S "Well that was an... interesting session."
    hide shana
    
    show expression crt_hunter.imageName
    h "*wheeze*"
    hide expression crt_hunter.imageName
    
    show shana
    S "Are you sure you are ok now?"
    hide shana
    
    show expression crt_hunter.imageName
    h "*nods*"
    h "I'm fine now. Just a bit of a shock."
    hide expression crt_hunter.imageName
    
    show shana
    S "Well if you are sure."
    S "So, we will bring our session to a close now."
    S "By next week however I want an example of all the herbs today to be brought to me from each of you."
    S "For the Bloodrunners, I'll see you again tomorrow. The [player.family]s, I'll see you next week."
    hide shana
    
    "You stand and prepare to leave. You look over at [crt_hunter.name]"
    
    $crt_hunter.met = True

    menu:
        "Ask if she is ok.": 
            show expression crt_hunter.imageName
            P "Are you ok?"
            h "I am fine, like I said."
            P "Well then, do you want to go and do something for the afternoon?"
            h "Like what?"
            $playerCompanion = crt_hunter
        "Leave her to it": 
            pass

    call activityCycle
    return
    