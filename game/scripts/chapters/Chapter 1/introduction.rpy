#-------------------------------------------------------------------------------
# The game starts here. The player gets introduced to the families and chooses a
# name and family. The player is also introduced to their ally and rival.
#-------------------------------------------------------------------------------

#-----------------------------
# Introduce the families.
#-----------------------------
label introduction:
    
    # Pass time along into evening.
    $game.advanceTime()
    
    scene expression camp.getBackgroundImage() with fade
    
    "The celebrations had been been going on from the early evening."
    "You, among others have been marking the passing into adulthood. The fire roars and voices rise in song about it."
    "{i}Every few years the gnolls of the Riverwood clan gather all those who have come of age and formally welcome them to the clan as adults.{/i}"
    "{i}It is a time of joy, where the daily struggle for survival is forgotten for a precious few hours.{/i}" 
    "{i}The former cubs can enjoy one last night of fun before they must pick up their duties and responsibilities as full adults.{/i}"

    show expression crt_ally.image with dissolve
    a "Oh, hey there!"
    a "Are you enjoying the party?"

    menu:
        "Yeah! Its going really well thanks.": 
            a "Thats great! Have you tried any of the fish? Its sooooo good!"
            a "*hick*"
        "Its ok I guess.": 
            a "Aww don’t be so glum. Cheer up! We might not get another night like this."

    a "Listen, I gotta go see Temesh. She needs some help with something or something."

    "You laugh. [crt_ally.name] has been your best friend for as long as you can remember. You hope your friendship can withstand the pressures  that adulthood will place on the two of you."
    "You also wander what her name will be after tonight. The tradition of the clan is that new adults can pick their own name."
    "You open your mouth to respond but she had already wandered away."
    hide expression crt_ally.image with dissolve

    show expression crt_rival.image with dissolve
    r "Hey butthead! I bet you get picked last. I bet no one wants you in their family!"

    menu:
        "Shut up [crt_rival.name]! I’d rather be without a family than join yours.":
            r "Wow, what a comeback. That was like you- weak!"
            
        "*Ignore him*":
            r "Ooooo, taking the high-ground are we? You’re pathetic!"

    r "Well I don’t really care about you anymore. My future is golden."
    r "I know exactly what family I am joining and I’ll be going straight to the top! You mark my words."

    "You hate [crt_rival.name] and [crt_rival.name] hates you. It seems like that is the way things have always been."
    "You hope that the responsibilities of adulthood mellow him out somewhat…"
    "… but you hope to the Seven Hells that [crt_rival.name] is not in your family."
    "He does make a good point though. You have to choose a family to join tonight and you have been unable to decide."
    "This will affect your whole future and that is a worrying prospect…"

    r "Ugh, I don’t have the time to hang out with loser trash like you."
    r "I’m outta here."
    hide expression crt_rival.image with dissolve

    "Temesh, the clan leader walks to the middle of the gathering and calls for silence. She waits until all eyes are upon her."

    show Temesh with dissolve
    T "Tonight is an auspicious night. For a night like this comes but once every few years."
    T "Tonight is the night where we welcome the next generation into our families."
    T "It is with new blood that we refresh our families. It is with new blood that we bring new ideas and new ways of doing things."
    T "And in exchange we, of the old blood must pass on our skills and our learning before we pass from this world."
    T "In order to take your first steps into this new phase of your lives you will have to make some crucial decisions."
    T "You must choose a family and you must choose a name."
    T "Your family with take you the rest of the way through your life. Although you are now considered adults, you nevertheless have a long journey ahead of you to learn the skills that will make you an effective member of the clan." 
    T "Your family will teach you these skills and give you a career and role within the clan."
    T "I am sure many of you have already decided which family to join, but some of you I know have yet to decide your future."
    T "Each family head will now come forward and tell you something about their families. "
    hide Temesh with dissolve

    "Temesh takes a step back, letting a gentle-eyed gnoll female take the centre."
        
    show Shana with dissolve
    S "Good evening dears. I am Shana of the Bloodrunner family."
    S "We, the Bloodrunners are the hunters and gatherers of the clan. We are also its medics and holders of natural lore."
    S "We treasure those who consider themselves cunning and keen hunters, but also those of a quiet and more contemplative nature."
    S "The Bloodrunners seek to learn more about the ways of nature and our place within it. We will teach you the skills to fulfil some of the most important roles within the clan. For without food and medicine we would crumble."
    S "If this is the path you wish to follow then the Bloodrunners will welcome you with open arms."
    hide Shana with dissolve

    "Shana smiles and nods and then steps back letting a scraggly, wizened gnoll male take the floor. His fur is dull but his eyes are bright."

    show Clarence with dissolve
    C "Thank you, Shana."
    C "I'm Clarence Coppertail; head honcho of the Coppertail family. "
    C "We are for those young'ns with an enquiring mind. You want to know how a crossbow works? What makes steel  armour better than iron? We can tell you and much more!" 
    C "The Coppertails want those who are inquisitive, quick of mind and aren't afraid to ask 'why?' long after everyone has lost patients in them."
    C "We can teach you how to work metal, how to construct things and how to really look at things." 
    C "Our engineers and researchers are forging ahead with pushing the boundaries of nature and conventional thinking."
    C "If these are the things that really get you excited then I urge you to join our family."
    hide Clarence with dissolve

    "Clarence gives the next gnoll a salute before exchanging places with her."

    show Marrack with dissolve
    M "Pfft. I’m Marrack Daggermaw of the Daggermaw family. If you want to mess about with flowers or bits of wire then the Bloodrunners and Coppertails are your family."
    M "But if you want to be a true gnoll then the Daggermaws are the only family for you!"
    M "We want only the toughest, strongest and most nimble in our ranks."
    M "Its a tough life but we will train you hard; Teach you the ways of the blade and the bow."
    M "Our family fill the most important role in the clan- keeping everyone safe."
    M "We keep the Orc tribes at bay, protect registered trade caravans and continually scout our lands making sure that we are the first to know of any impending threats."
    M "If you think you are tough enough for our family we will welcome you into the fold."
    hide Marrack with dissolve

    "With a thump on her chest and a roar, Marrack stepped aside to allow Temesh back to take the centre once again."
        
    show Temesh with dissolve
    T "As you know, I am Temesh Gildclaw; the clan matriarch and also head of the Gildclaw family."
    T "While Marrack might be the iron fist of the clan; we, the Gildclaws are the velvet glove. We negotiate, trade and discuss." 
    T "We are responsible for the political and mercantile force of the clan in the wider world."
    T "It is the Gildclaws that discuss border disputes. It is the Gildclaws who conducte trade missions. And it is the Gildclaws who keep the clan strong and protected through agreements and contracts."
    T "If you are looking for the finer things in life and wish to get to know the powers that really run things then the Gildclaw family should be your family of choice."

    "Temesh looks around at everyone present. "
        
    T "Now, we shall begin. I will call you up once at a time and ask you each for your choice of family and name."

    "Temesh points to someone to your left and urges them forward …"
    hide Temesh with dissolve

    scene black with fade
    "..."
    "... ..."

    scene expression camp.getBackgroundImage() with fade
    show Temesh with dissolve
    "Temesh looks directly at you and summons you forward."
    "You take a nervous look around and step forward, aware of many eyes upon you."
    hide Temesh with dissolve

    show expression crt_ally.image with dissolve
    a "Good luck!"
    hide expression crt_ally.image with dissolve
        
    show Temesh with dissolve
    T "You are one of those that have yet to show alignment with any family as yet."
    
    return