label bloodrunnerIntroduction:

    show Shana with dissolve
    S "Suns blessings my young ones."
    S "This is the first dawn of your new life with your new family." 
    S "I am pleased so many of you chose to walk the path of the [player.family]s."
    S "Please, follow me and I will take you to the sacred grounds of our family."
    hide Shana with dissolve

    "You trail after your fellow [player.family]s, heading out of the den site and into the forest."
    "After what seems like twenty minutes you emerge into an open space. The ground is mossy and the sun shines down brightly."
    
    scene expression glade.name with fade
    show Shana with dissolve
    S "Welcome to the [player.family] glade."
    S "It is where we come to meditate, discuss with our fellow [player.family]s."
    S "Now then, who can tell me what is so special about this spot?"

    menu:
        "Raise your hand":
            call bi_answerQuestion
    
        "Let someone else answer":
            $bi_answerWrong = False
            call bi_wrongNoAnswer
        
    S "This node can also allow those who are specially attuned to read the health of the land."
    S "It can help us predict good hunting seasons and lean times when we should prepare."
    S "So, my young ones. Let me tell you a little about our history."
    S "The Riverwood clan was formed by our leader Temesh and her partner Marrack some twenty-two years ago."
    S "The Gildclaws and the Daggermaws were the first two families to exist within the clan and this was fine for a few years."
    S "This was of course, until Temesh and Marrack decided that the current breakdown was not benefiting all."
    S "I was asked if I would like to form my own family."
    S "She wanted me to take those from the Daggermaws who did not wish to pursue a military career."
    S "While it is true that both we and the Daggermaws have an extensive cross over in skills;"
    S "Weapons, tracking, camouflage, ambushing, trapping."
    S "It is the motivations behind these that make us differ."
    S "We are hunters, trappers, gatherers."
    S "They are soldiers, guards, strategists."
    S "At the time of our founding we were primarily tasked with hunting. But since then we have been teaching other skills."
    S "We have been moving away from the Daggermaws and continue to strive to define our own identity within the Riverwood clan."

    S "I think that is enough history for you."
    S "I am sure you are all eager to get going on something practical."
    S "Lets see how good your observation skills are."
    S "I want you to find a partner and head out into the surrounding area and see if you can find me a sample of the pop cap mushroom."
    S "The do not usually grow at this time of year but around here they feed off of the natural energies and fruit early."
    S "Try closing your eyes and seeing if you can get yourselves in tune with the energies. You will find them so much quicker that way."

    "You close your eyes and take a deep breath, taking in the scent of fresh moss, pollen and the many other natural odours of this green spot."

    scene black with fade
    "You try to imagine your own internal spirit expanding downward into the soil."
    "You visualise it reaching into the vast, glowing network of life that runs under you."
    "You sense someone approach."
    "They kick you."
    P "Ouch!"

    scene expression glade.name with fade
    show expression crt_hunter.image
    h "Are you coming or what?"
    P "Oh, yeah sorry. I was just trying to sense this natural energy Shana was-"
    h "You don’t believe all of that do you?"

    if bi_answerWrong == True:
        P "But you answered the question."
        h "Yeah, I know. I’ve studied under Shana for a while."
        h "I know her way of thinking."
    else:
        P "I, err."
        P "Well I-"

    h "I have a great respect for her."
    h "She used to be quite a skillful hunter when she was younger."
    h "She has gone… strange in later life though."
    h "Some say she has gone mad, and the way she carries on about this ‘natural energy’ and ‘lay line’ dung, I would be inclined to believe it."
    h "Come on. Lets look for this mushroom."
    hide hunter

    #[test players herbs or explore skill to find mushroom- unlikely outcome anyways]
    $findMushroom = False
    
    "…"
    "… …"
    if findMushroom:
        P "Here is one, look!"
        show expression crt_hunter.image
        h "How did you find one so quickly?"
        P "Well, you know. I am just in tune with the natural energies after all!"
        h "Hmph."
        h "Maybe it was just dumb luck."
    else:    # Most likely outcome
        h "I found one!"
        show expression crt_hunter.image
        h "I’ve got one of those mushrooms."
        P "That was pretty quick."
        P "Maybe you are in tune with the natural energies after all!"
        h "Or maybe I just know where to look because of skill, training and experience."
        P "Or that."
    
    h "Come on then, we should get this back to Shana so she can do whatever nonsense she has in mind for it"
    hide expression crt_hunter.image
    
    scene expression glade.name
    show Shana
    S "Oh my, you two have returned with a mushroom! And so quickly too."
    S "[crt_hunter.name] I knew you would be great at this. The forest spirits constantly smile down on you."
    S "I hope you have been sharing some of your favour with your friend."
    
    if crt_hunter:
        h "Well [player.name] found it actually"
        S "Oh my! Then they must be blessed by the forest spirits too"

    S "Please, bring me the mushroom. I have a use for it in a potion Temesh requested I make."
    S "I think you two can head off now that you have brought me this."
    S "I will see you back here tomorrow bright and early!"
    hide Shana
    
    scene black
    "You head back to the den site."
    "As you approach you see [crt_hunter.name] heading away."
    
    menu:
        "Call her over":
            show expression crt_hunter.image
            h "what is it?"
            P "do you want to do something together?"
            h "Ok, what did you have in mind?"
            $playerCompanion == crt_hunter
        "Let her go":
            pass
    return
        
label bi_answerQuestion:
    S "Yes, [player.name]?"
    
    menu:
        "Its a long way from the Coppertails horrible, smoky forge.":
            S "True! But not the significant reason. "
            $bi_answerWrong = True
        
        "The trees look nicer here.":
            S "They are a lot greener here, thats true."
            S "But I’m looking for the reason of why that is"
            $bi_answerWrong = True

        "Its a sight of natural power.":
            S "Thats right!"
            S "Our beautiful glade here is on the site of two crossing lay lines."
            S "Through their power we can summon up the natural energies to help us in our work."
            $bi_answerWrong = False

    if bi_answerWrong:
        call bi_wrongNoAnswer

label bi_wrongNoAnswer:
    hide Shana
    show expression crt_hunter.image with dissolve
    h "I know the answer."
    hide expression crt_hunter.image

    $crt_hunter.showName()
    
    show Shana
    S "Go ahead [crt_hunter.name]."
    hide Shana
    

    show expression crt_hunter.image with dissolve
    h "This is a place of power."
    h "You can draw energy up from the node point of two intersecting lay lines."
    hide expression crt_hunter.image
        
    show Shana
    S "Thats right!"
    S "Did everyone get that?"
    
    return