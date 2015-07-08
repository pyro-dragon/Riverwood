label coppertailIntroduction:

    scene black with fade

    "*hack* *cough* *hack*"

    show Clarence with dissolve
    C "*Clears his throat*"
    C "Good morning you young ‘uns."
    C "Rise and shine, we have to get you all introduced and things"
    C "Follow me"
    C "... "
    C "But don’t touch anything unless I say so."
    hide Clarence with dissolve

    "You rub your bleary eyes and follow after the old gnoll."
    "The other [player.family]s trail after you."
    "Clarence leads you at a remarkable speed for such an old gnoll."
    "He takes you through the den grounds and towards a large, rickerty structure built up against the cliff side."
    "He pushes the door open and beckons everyone inside."

    scene expression forge.name with fade
    show Clarence with dissolve
    C "Welcome to the [player.family]’s forge!"
    C "This is the greatest concentration of gnollish ingenuity this side of the Hebridian mountains."
    C "Some of you have been privileged to have been inside it and seen some of the work that goes on inside here."
    C "For the rest though, this will be a truly magical experience"
    C "Except perhaps not magical-"
    C "thats not something we deal with here."
    C "Here we deal with hard science, technology, craftsmanship, and, well more than a bit of luck."
    C "Well now…"
    "Clarence looks around at everyone in the room."
    C "… lets get you inducted. "
    C "Most of you know some of what we do but not everything. Or much of our history."
    C "The Coppertails were formally branched off from the Daggermaws about seven years ago."
    C "Before that there was an unofficial collective of Daggermaws who had ‘inorganic specialisations’. "
    C "That is metallurgy, mineralogy, construction and engineering, the four key areas that fall under our domain."
    C "Temesh felt that my history made me the appropriate leader for the family."
    C "A male in charge is strange, I know but I have been apprenticed in clock making and later trained in firearms construction."
    C "While I lack any formal training in some of our other areas I have worked with Temesh and the Guildclaws to establish correspondence with numerous guilds in the big cities and we have amassed a sizable library of subject matter free for the use of anyone."
    C "What else is there?"
    C "Hmm…"
    hide Clarence with dissolve

    show expression crt_mechanic.image with dissolve
    m "Umm, what about the research programmes?"
    hide expression crt_mechanic.image

    show Clarence
    C "What about them?"
    hide Clarence

    show expression crt_mechanic.image
    m "Arn’t they important to mention for an induction?"
    hide expression crt_mechanic.image

    show Clarence
    C "Oh yes!"
    C "I should tell you about our research projects!"
    C "We have two major ones  in progress and you my very well be assigned to one or other to help out and learn how we conduct research."
    C "We are working with the Daggermaws on a weapons programme."
    C "Production of a multi-purpose ranged combat weapon. We are taking the latest in black powder technology and trying to put it in a weapon durable and reliable enough for the use of the average Daggermaw."
    C "So far, alas the Daggermaws are proving to have durability requirements much higher than our manufacturing capabilities."
    C "I am trying my best to convince them not to use it as a club but it is tough going."
    C "Our second major project is with the Bloodrunners."
    C "We are researching a form of localised foraging methods."
    C "Farming and agriculture essentially. But don’t tell the Bloodrunners that."
    C "They hold their hunting and foraging close to their hearts."
    C "We are just trying to bring that much closer to home."

    "Clarance slaps his hands together and looks around the room."

    C "Well that is enough yammering from me. I am sure you all want to get stuck into something practical!"
    C "I think, as a starter it should be a good idea to see how you go with some simple metalwork."
    $crt_mechanic.showName();
    C "[crt_mechanic.name] here has done you all a favour and fetched the blades from two of our windmills up on the Overreach"
    C "Everyone take a blade and set yourself up on a workbench."
    hide Clarence

    "You move to a bench near the front. The metal blade you are given is all bent out of shape."
    P "Hmm, what tool should I use?"

    $goodTool = False
    menu: 
        "Screwdriver":
            pass
        "Spanner":
            pass
        "Hammer":
            $player.changeSkillBonus("mechanics", 1)
            $goodTool = True
        "Saw":
            pass

    "You work on the blade for some time."

    if goodTool == True:
        pass
    else:
        "It doesn’t work out very well at all."
        show expression crt_mechanic.image
        m "You don’t seem to be doing very well there."
        m "Do you want some help?"

        menu: 
            "Yeah. I have kind of messed it up havn’t I?":
                $player.changeSkillBonus("social", 1)
                m "Well first problem here is that you’ve got the wrong tool!"
                m "For this you need a hammer and then you start banging away."

            "No! Its fine, everythings fine.":
                pass
        hide expression crt_mechanic.image

    "You start hammering away at the metal."
    "It quickly turns out that it is beyond your untrained hands to repair. "

    show expression crt_mechanic.image
    m "That’s just not working out is it?"
    "She pics up the metal and examines it."
    m "I think this can be repaired but not by a beginner like you. No offense ment."
    m "Excuse me Clarence, can I use one of the smaller forgers? This one seems bent right out."
    hide expression crt_mechanic.image

    show Clarence
    C "Hmm, yes. That one does seem particulally deformed."
    C "It looks like a bird flew into it."
    C "You may fire up forge number three and take your little friend over too. Perhaps you could show him something."
    hide Clarence

    show expression crt_mechanic.image
    m "Thank you sir. "
    m "Come along then, err…"
    P "[player.name]."
    m "Oh yes, of course. Come along [player.name]."
    hide expression crt_mechanic.image

    "You follow [crt_mechanic.name] to the back where numerouse stone and metal behimoths."

    show expression crt_mechanic.image
    m "So have you ever used a forge before?"

    $forgeLie = False
    menu: 
        "Yes I have! Let me show you!":
            $forgeLie = True

        "Not really, not at all":
            pass

    if goodTool == False and forgeLie == True:
        m "I don’t belive you! Just look at what you were doing before."
        call mechanicForgeDemo
    elif goodTool == True and forgeLie == True:
        $crt_mechanic.addRP(1)
        m "Lets see you do this then!"
        call playerForgeDemo

    call closeCoppertailsFirstLesson

    return

label playerForgeDemo:
    "You look at the forge."
    "It is big and complicated and you have no idea what to do."
    menu: 
        "Stoke the fire with a poker.": 
            "The fire sparks a little but doesn’t seem much hotter than before."
            m "Thats not really working is it?"
            call mechanicForgeDemo
            return
        "Pull the leaver to the left.": 
            "The bellows start pumping air into the forge through some mysterious mechanical means."
            $crt_mechanic.addRP(1)
            "[crt_mechanic.name] looks impressed."
        "Pull the leaver to the right.": 
            "Water is released from a nozzle abouve and douses the forge fires with an eruption of steam and ash."
            m "Wow, that was spectacular."
            m "We should probably find another forge."
            call mechanicForgeDemo
            return

    m "Ok then smarty pants. What are you going to do next?"

    "You rub your chin."
    menu:
        "Put the twisted metal in the fire":
            "The fire sparks and smolders eventually turning white hot."
            "You watch it."
            m "The fire has pretty much ruined that metal."
            m "You don’t really know what you are doing do you? Good try though."
            m "Lets go get another bit."
            call mechanicForgeDemo
            return
        "Pick up the tongs":
            $crt_mechanic.addRP(1)
            "You use the tongs to hold the metal in the forge fire, watching the heat carefully."
            m "Alrighty then!"
        "Prod the fire": 
            "The fire sparks and you draw your hand back quickly as it burns you."
            P "Ouch!"
            m "Ah well, it was looking good for a while there at least."
            call mechanicForgeDemo
            return
        "\"I really don’t know.\"": 
            m "No worries! We all have our limits."
            call mechanicForgeDemo
            return

    m "So you have the forge going and your metal heated nicely."
    m "What is your next move?"

    menu:
        "Move the now hot metal over to the big power-hammer lurking in the corner.": 
            "You eye up the power-hammer. It is a mass of heavy iron, wheels and belts. "
            "You wander over to the hammer and place it on the surface before searching for the power lever."
            m "No don’t!"
            m "I haven’t even been trained on that yet!"
            m "Lets start again, I am not sure you really know what you are doing."
            call mechanicForgeDemo
            return
        "Dunk the metal in water.": 
            "You remember hearing something about metal ‘remembering’ its shape."
            "Clouds of steam erupt around you."
            m "Wow, thats quite a show!"
            "[crt_mechanic.name] waves the steam away from her"
            m "As exciting as that was I don’t think we should try that again."
            m "Lets start over."
            call mechanicForgeDemo
            return
        "Put the metal on the anvil and select a small hammer.": 
            "You calmly pull the metal from the forge and place in on the anvil."
            "Selecting what seems to be the best hammer for the job you proceed to beat out the widmill blade."
            "After a few more session in the forge and anvil you beat it out flat and quench it and turn it over to [crt_mechanic.name] for inspection."
            $crt_mechanic.addRP(3)
            m "Very well done! I am impressed!"
            m "You certainly do know your way around a forge."
            m "One problem though- "
            m "Its the wrong shape. I windmill blade needs a slight angle and this is just flat."
            "[crt_mechanic.name] pats you on the back."
            m "Still, no worries. I can get this into shape in a jiffy. Good job!"
        
    hide expression crt_mechanic.image with dissolve
    
    return

label mechanicForgeDemo:
    m "Let me show you."
    m "First you have to get the forge fires pumped up. If you pull that lever over there it will engage the water bellows."
    menu: 
        "Water bellows? Why do we want to pump water into the fire?": 
            $crt_mechanic.addRP(-1)
            m "No. They are regular air-blowing bellows, they are just driven by water power."
        "Ah, bellows driven by water power yes?": 
            $crt_mechanic.addRP(2)
            m "Thats right! There are turbines located deep in the caves. I can show you them later!"

    m "Anyway, we get the air going and- yes you can see it now."
    "Flames leap from the coals and a wave of heat hits you in the face."
    P "I think my whiskers got singed."
    m "Well step back a bit then silly! This is much hotter than regular fire."
    m "Ok then, go and pick up those tongs."
    m "No, those ones. Yes. Thank you."

    "You watch as [crt_mechanic.name] picks up the mangled prop blade and holds it in the heart of the fire."
    "It glows white hot!"

    m "Pass me the hammer please!"
    if goodTool == False:
        m "Thats the big square thing on the end of the handle."

    "[crt_mechanic.name] takes the now glowing metal and lays it down on the anvil."
    "She takes the hammer and lays a few resounding clangs on it."
    "Sparks fly!"

    m "Now you try."
    "[crt_mechanic.name] hands you the tongs."

    menu: 
        "I’d rather not thank you. I am more of a thinker.":
            call refuseTongs
        "*Take the tongs*":
            call takeTongs

    return
    
label refuseTongs:
    $crt_mechanic.addRP(-3)
    m "Oh, well ok then."

    show black with fade
    "You watch as [crt_mechanic.name] beats out the fin. A look of concentration on her face."
    "She doesn’t acknowledge your presence at all."
    $player.changeSkillBonus("social", -1)

    return

    label takeTongs: 
    "You take the tongs and put the metal back in the fire."
    $crt_mechanic.addRP(2)
    m "Be careful not to burn it. You have to watch the colour change very carefully."

    show black with fade
    "[crt_mechanic.name] guides you through the rest of the repair."
    "The fin doesn’t look amazing when you are through with it but [crt_mechanic.name] seems satisfied."
    $player.changeSkillBonus("mechanicSkill", 1)

    return

label closeCoppertailsFirstLesson: 
    show expression forge.name with fade
    show Clarence with dissolve
    C "Alright guys, these are looking really good now!"
    C "I think the wind mills are certainly going to give us a few more months of service with these repairs."
    C "I’ll let you go now. But I will see you all bright and early tomorrow."
    C "Go and have some fun, you did some great work here today."

    return