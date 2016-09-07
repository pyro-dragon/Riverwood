#-------------------------------------------------------------------------------
# The end of week assesment by the family heads
#-------------------------------------------------------------------------------

label endOfWeekAssesment:
    if player.family == "Bloodrunner": 
        call bloodrunnersEndOfWeek1
    elif player.family == "Coppertail": 
        call coppertailsEndOfWeek1
    elif player.family == "Daggermaw": 
        call daggermawEndOfWeek1
    elif player.family == "Gildclaw": 
        call gildclawEndOfWeek1
    else:
        $renpy.say("DEBUG", "Error: No valid family selected.")

    return

label bloodrunnersEndOfWeek1: 
    
    $game.setLocation(glade)
    
    show Shana with dissolve

    S "Well here we are my young blossoms. The end of your first week of training."
    S "I hope you have all had an enlightening experiance and learned a lot so far."
    S "Next week it will be down to you to decide your destiny."
    S "You may choose to train with any of the other families at for least three days a week."
    S "The remaining two days will be spend training with the Bloodrunners."
    S "Now then, it is a fine, Spring day that we have been blessed with and I see no reason not to finish early and let you all enjoy it."
    S "But before I do I must make a request for any volenteers to help perform important Bloodrunner duties this weekend."
    
    menu:
        "Volenteer":
            P "I'd like to volenteer please."
            S "Ah, thank you very much [player.name]."
            S "Now, is there anyone else?"
            S "..."
            S "Anyone?"
            hide Shana with dissolve
            
            show expression crt_hunter.image with dissolve
            h "Ugh, I guess I had better volenteer then."
            hide expression crt_hunter.image with dissolve
            
            show Shana with dissolve
            S "Bless you [crt_hunter.name]!"
    
        "Stay silent":
            S "..."
            S "Anyone?"
            S "I would have hoped you would all be eager to demonstrate your family loyalties."
            S "But, alas, the draw of the weekend is strong. "
            S "In that case I will choose."
            S "[crt_hunter.name]"
            hide Shana
            
            show expression crt_hunter.image
            h "Me??"
            hide expression crt_hunter.image
            
            show Shana 
            S "And, [player.name]."
            
    S "Please meet me here at the Glade at first light tomorrow."
    S "Thank you again, your loyalty to your family will be noted."
    hide Shana
    
    show expression crt_hunter.image
    h "Whatever."
    hide expression crt_hunter.image
    
    show Shana
    S "Now you all may go, see you all next week."
    hide Shana with dissolve
        
    return

label coppertailsEndOfWeek1: 

    $game.setLocation(forge)
    
    show Clarence with dissolve
    C "Hello, hello there everyone."
    C "What an exciting week it must have been for you all!"
    C "Learning lots of new stuff I hope. Getting your minds all sparked up and overflowing with ideas and inspiration and all sorts I have no doubt."
    C "Now I expecf you are all feeling somewhat mentally fatigued after all of that, so instead of foisting upon you another lesson I will let you go early today"
    C "But before I do that I must make an eentsy-weentsy little request from you all."
    C "I am looking for volenteers tohelp me with some seriouse Coppertail family business tomorrow."
    hide Clarence
    
    show expression crt_mechanic.image with hpunch
    m "I'll do it!"
    hide expression crt_mechanic.image
    
    show Clarence with dissolve
    C "Err, yes, thank you [crt_mechanic.name]. I suspected that you might."
    C "I'm going to need more than one though, anyone else?"
    
    menu:
        "Volunteer":
            P "I'd like to volanteer please."
            C "Ah [player.name], that is excelent, most excelent."
        "Stay silent":
            C "Your collective want of enthusiasm does not do you credit, nore will it bode well fot your future career inside the Coppertails."
            C "Lets see here..."
            C "..."
            C "You, yes you, [player.name]."
    
    C "Congratulations on your appointment as my second volunteer."
    C "The rest of you may now do what you wish."
    hide Clarence
    
    show expression crt_mechanic.image
    m "What is it that you need us for, sir?"
    hide expression crt_mechanic.image
    
    show Clarence
    C "Ah, well. You will find out when you get there. "
    C "Mostly I have forgotten why, but I do remember that I need some help tomorrow."
    C "Come by the Forge tomorrow morning and we shall all find out together."
    C "Now then, I have work to do. "
    C "I think."
    hide Clarence with dissolve
    
    show expression crt_mechanic.image
    m "I think we should probably head off now."
    hide expression crt_mechanic.image with dissolve
    
    return
    
label daggermawEndOfWeek1: 

    $game.setLocation(arena)
    
    show Marrack with dissolve
    M "So, my young warriors return."
    M "I expect this was a punishing week for you. "
    M "So many new things..."
    M "So much to take in..."
    M "So much to considder..."
    show Marrack with vpunch
    
    M "Well such it up!"
    M "You are Daggermaw warriors!"
    M "When life gets tough, you get tougher!"
    M "Take a bite right out of life, spit it back in its face. "
    M "Now, I'd love to sen you lot off for a 20 mile run around the Devil Woods to shake out any frustrations-"
    M "-but it seems all the other families are letting their new recruits have today off. "
    M "I do not see why we need to be so soft..."
    M "... but Temesh says I need to stop terrifying the recruits so much."
    M "I told her, I said we arn't training a bunch of bean counters or mushroom pickers here. This is the defence of the clan we are talking about here. Our very existance-"
    hide Marrack
    
    show expression crt_fighter.image
    f "So we can go then?"
    f "That's great because I have some-"
    hide expression crt_fighter.image
    
    show Marrack with hpunch
    M "I'M STILL TALKING!!"
    M "YOU DON'T INTERRUPT WHILE I'M TALKING!"
    M "EVER!"
    hide Marrack
    
    show expression crt_fighter.image
    f "Sor-"
    hide expression crt_fighter.image
    
    show Marrack with vpunch
    M "YOU'RE STILL DOING IT!!"
    M "Right, for that, you lose your weekend rights."
    M "You will report back here at first light tomorrow."
    M "I have some things that I need doing."
    M "That reminds me, I need someone else too."
    M "..."
    M "Well step up, someone."
    M "Where is your sense of duty?"
    
    menu: 
        "Volanteer":
            P "I'll step up"
            M "Good. At least someone around here has some disapline."
        "Stay silent":
            M "Anyone?"
            M "You are going to have to do better than that if you want to call yourselves Daggermaws."
            M "Lets see..."
            M "You."
            P "Me?"
            M "Yes, you."
        
    M "You will also meet here tomorrow at first light."
    M "Lets see just how strong you are."
    M "But for now, you are all dismissed!"
    hide Marrack with dissolve
    
    return
    
label gildclawEndOfWeek1: 
    
    $game.setLocation(tent)
    
    show Temesh with dissolve
    T "A very good morning to you my acolytes."
    T "I trust the week has been engaging and not too onerouse."
    T "It is important that you have now gained an overview abotu what each family is like and what training they have to offer you."
    T "While I would be very flattered that you might want to spend all your time learning from me, it would be worth your time learning from the others."
    T "Up to three times a week you may choose to learn with one of the other families. "
    T "Now then, I have encouraged all the other family leaders to give everyone today off."
    T "It has been a tough week and I think you need time to reflect on all you have leared thus far."
    T "And our family will not be an exception. I wish you all to head away and spend some time thinking and talkning about all you have leared. "
    T "However, before I do I wish to call upon a couple of you for some work I require assistance with tomorrow."
    
    menu:
        "Volanteer": 
            P "I wish to put my name foreard and volenteer."
            T "Ah, that is most excelent!"
        "Stay silent": 
            "..."
            T "Oh, I am a little disapointed by the lack of enthusiasm here."
            T "It doesn't say much about the new generation of Gildclaws, I must say."
            T "Let me see here..."
            T "..."
            T "You, I think you shall be willing to help me tomorrow."
            P "Me?"
            P "But-"
            
    T "Thank you very much, truely."
    T "Well now, I need one more person to help out."
    hide Temesh
    
    show expression crt_trader.image
    t "P-please ma'am, I-I would like t-to help out."
    hide expression crt_trader.image
    
    show Temesh
    T "Thank you [crt_trader.name], that would be very good of you."
    T "I think that should be enough for now."
    T "I shall see you tow tomorrow morning. The rest of you, I will see you first thing Monday morning, bright and early."
    
    return