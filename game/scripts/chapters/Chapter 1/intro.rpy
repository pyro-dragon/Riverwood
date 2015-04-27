#-------------------------------------------------------------------------------
# The game starts here. The player gets introduced to the families and chooses a
# name and family. The player is also introduced to their ally and rival.
#-------------------------------------------------------------------------------

#-----------------------------
# Introduce the families.
#-----------------------------
label introduction:
    scene expression camp.name
    "The celebrations had been loud and wild but now everyone rests. The four family heads call everyone to gather as they begin the naming ceremony. All the young cubs, you among them gather on logs in the front."
    
    $player.changeSkillBonus("dodge", 1)
    
    show ellie with dissolve
    e "This is so exciting!"
    hide ellie with dissolve
    
    "You laugh. Ellie has been a friend for as long as you can remember. Ellie though, as with you yourself will be known by your cub names no longer after tonight."
    "You want to respond but you are too nervous. Before you can work up the courage Charrd nudges you."
    
    show charrd with dissolve
    c "Hey butthead! I bet you get picked last. I bet no one wants you in their family."
    hide charrd with dissolve
    
    "You hate Charrd. Ever since you could walk he would try to beat you, try to be better than you. You ignore him for now but you wonder what family he will be in."
    "The head of the clan speaks up, silencing everyone."
    
    show temesh with dissolve
    T "Greetings friends, family and cubs. Tonight is a very special night and it comes once every four years. Tonight the cubs who are of age receive their names and are received officially into their family's."
    T "A name and a family is very important. Your choice now will affect the life you lead going forth. You may choose a name yourself or ask one of the the family heads to choose one for you. Be warned though, this choice is final and will be what you will be known as for every day that comes after this night."
    T "Many of you have already chosen your family allegiances too. For those that have not and those that wish to change you may do so, but this is also a permanent choice so I will urge you to give great thought about this also."
    T "Each family head will now introduce themselves and tell you a little about them and the ways their family follows to aid you in your choice tonight. "
    hide temesh with dissolve

    "Temesh takes a step back, giving the floor to a slender, sharp-faced gnoll female."
    
    show shana with dissolve
    S "I am Shana Bloodrunner, head of the Bloodrunner family. We are a cunning family, knowledgeable in the ways of nature. We are the food gatherers and medicine makers of the clan. We offer training in herbs, hunting and the cycles of the seasons. We expect our members to be patient, to move silently and to open up their senses to the world around them."
    hide shana with dissolve
    #"She gives a silent nod and then steps back letting a scraggly, wizened gnoll male take the floor. His fur is dull but his eyes are bright."
    "She gives a silent nod and then steps back, letting a scrawny, oddly dressed gnoll male take the floor. Brass and copper instruments hang from his belt."
    

    show clarance with dissolve
    C "Thank you. I'm Clarance Coppertail. Head honcho of the Coppertail family. We are for those young'ns with an inquiring mind. You want to know how a crossbow works? What makes iron armor better than copper? We can tell you and much more! The Coppertails want cubs who are inquisitive, quick of mind and aren't afraid to ask 'why?' long after everyone has lost patients in them."
    hide clarance with dissolve
    "With a nod he stepped back, giving way to a hulking bruit of a gnoll."

    show marrack with dissolve
    M "Raaaaghh!! I am Marrack Daggermaw! We Daggermaws haven't got time for all that nonsense about nature and machines, we just know we are the toughest and best! We defend the clan from all its enemies. If you think you are tough, strong headed and have the dexterity of paw to handle a blade or bow then we want you."
    hide marrack with dissolve
    "With a smart salute and a jangle of chain mail Marrack stepped aside to allow Temesh back."
    
    show temesh with dissolve
    T "And as you know, I am Temesh Gildclaw. While Marrack might be the iron fist, we, the Gildclaws are the velvet glove. We negotiate, trade and discuss. We are looking for cubs who are after the more refined things in life. We want those with a quick mouth and a quick mind behind it. We want level-headed cubs who's first instinct is to words when conflict raises its head."
    "Temesh gave a flourishing bow. On standing again she glared out at the young gnolls gathered in front of her."
    
    T "Now, we shall begin. You there, come forward."
    "Temesh pointed at a small cub sat on the far left, urging them forwards... "
    hide temesh with dissolve
    "..."
    "... ..."
    
    show temesh with dissolve
    T "And now you. Come." 
    "Temesh indicated for you to come forward"
    hide temesh with dissolve
    
    show ellie with dissolve 
    e "Good luck!"
    hide ellie with dissolve
    
    show temesh with dissolve
    T "Now you, you are interesting. From what I have seen of you, you could join any family."
    jump chooseFamily

#-----------------------------
# Choose the family and assign 
# the ally and rival.
#-----------------------------
label chooseFamily:
    T "Which family will you choose?"
    
    menu: 
        "I like the ways of the Bloodrunners. (Nature, Hunters, Medicine)":
            jump bloodrunners
        
        "I have a great interest in joining the Coppertails. (Machines, Metal craft, Investigation)":
            jump coppertails
            
        "The others seem so wimpy, I'll join the Daggermaww. (Fighting, Tactics, Intimidation)":
            jump daggermaws
            
        "It will be an honour to join the Gildclaws. (Diplomacy, Trade, Economics)":
            jump gildclaws

#-----------------------------
# Choose the Bloodrunners.
#-----------------------------
label bloodrunners:
    $player.family = "Bloodrunner"
    $crt_ally.family = "Daggermaw"
    $crt_ally.name = "Scarah"
    $crt_rival.family = "Coppertail"
    $crt_rival.name= "Scorch"
    jump checkFamily
    
#-----------------------------
# Choose the Coppertails.
#-----------------------------
label coppertails:
    $player.family = "Coppertail"
    $crt_ally.family = "Gildclaw"
    $crt_ally.name = "Deft"
    $crt_rival.family = "Daggermaw"
    $crt_rival.name = "Dirge"
    jump checkFamily
    
#-----------------------------
# Choose the Daggermaws.
#-----------------------------
label daggermaws:
    $player.family = "Daggermaw"
    $crt_ally.family = "Bloodrunner"
    $crt_ally.name = "Swift"
    $crt_rival.family = "Gildclaw"
    $crt_rival.name = "Silver"
    jump checkFamily
    
#-----------------------------
# Choose the Gildclaws.
#-----------------------------
label gildclaws:
    $player.family = "Gildclaw"
    $crt_ally.family = "Coppertail"
    $crt_ally.name = "Spark"
    $crt_rival.family = "Bloodrunner"
    $crt_rival.name = "Shade"
    jump checkFamily
    
#-----------------------------
# Check that the player is ok
# with their choice of family.
#-----------------------------
label checkFamily:
    "Is that your final choice?"
    
    menu: 
        "Yes, I want to join the [player.family]!":
            jump chooseName
            
        "No, I want to know the choices again.":
            jump chooseFamily
    
#-----------------------------
# Choose how to decide the 
# player name. 
#-----------------------------
label chooseName:
    T "Excellent. I am sure you will be an asset to your chosen family."
    T "Now, you must take a name for yourself. You can either choose one yourself of have your new family head give you a name. Which would you like?"
    
    menu:
        "I'll choose my own name.":
            jump makeName
            
        "I'll let my family pick for me": 
            jump pickName
            
#-----------------------------
# Type out the player name. 
#-----------------------------
label makeName:
    $player.name = renpy.input("Very well, what will your name be?")
    $player.name = player.name.strip()
    jump checkName
    
#-----------------------------
# Check that the player is ok
# with their choice of name. 
#-----------------------------
label checkName:
    T "So you want [player.name] to be your name?"
    
    menu: 
        "Yes! I shall be known as [player.name]!":
            jump concludeCeremony
        
        "No, on second thoughts I want to pick again.":
            jump chooseName
    
#-----------------------------
# Select the name from a list.
#-----------------------------
label pickName:
    "Ok, here is a list of names you can choose"
    if player.family == "Bloodrunner":
        menu: 
            "Leaf-mould":
                $player.name = "Leaf-mould"
                jump checkName
            "Sprint":
                $player.name = "Sprint"
                jump checkName
    elif player.family == "Coppertail":
        menu: 
            "Weld":
                $player.name = "Weld"
                jump checkName
            "Rivet":
                $player.name = "Rivet"
                jump checkName
    elif player.family == "Daggermaw":
        menu: 
            "Crash":
                $player.name = "Crash"
                jump checkName
            "Ducker":
                $player.name = "Ducker"
                jump checkName
    elif player.family == "Gildclaw":
        menu: 
            "Credit":
                $player.name = "Credit"
                jump checkName
            "Debit":
                $player.name = "Debit"
                jump checkName

#-----------------------------
# The outro to the naming 
# ceremony. 
#-----------------------------
label concludeCeremony:
    "Very well. [player.name] of the [player.family] family. Welcome."
    
    "You take your place at the side of your chosen family and watch as the other cubs are called..."
    T "Now you, approach."
    hide temesh with dissolve
    
    show ellie with dissolve
    e "Yes..."
    hide ellie with dissolve
    
    show temesh with dissolve
    T "I know you will suite the [crt_ally.family] well. Will you choose this?"
    hide temesh with dissolve

    show ellie with dissolve
    "For a moment she looked toward you, an apologetic look in her eyes. She turns back to Temesh and nods."
    e "Yes, I choose the [crt_ally.family]s"
    hide ellie with dissolve
    
    show temesh with dissolve
    T "Very well. And what name will you go by?"
    hide temesh with dissolve
    
    show ellie with dissolve
    e "[crt_ally.name]"
    hide ellie with dissolve
    
    show temesh with dissolve
    T "[crt_ally.name], of the [crt_ally.family]s family. Welcome."
    hide temesh with dissolve
    
    show charrd with dissolve
    c "Damn, I am being picked last aren't I?"
    hide charrd with dissolve
    
    show temesh with dissolve
    T "Calm yourself there young cub. Come forth."
    T "You, I think, you will do well in the [crt_rival.family] family. Would you agree?"
    hide temesh with dissolve

    show charrd with dissolve
    c "Damn right I will!"
    hide charrd with dissolve

    show temesh with dissolve
    T "And what name do you want?"
    hide temesh with dissolve

    show charrd with dissolve
    c "[crt_rival.name]"
    hide charrd with dissolve
    
    "You watch as [crt_rival.name] takes up station next to his new family."
    
    show temesh with dissolve
    T "That now concludes the naming ceremony of the Riverwood clan. I would like to welcome you all as fresh young adults. You now have every privilege a full clan member is entitled to, but you also have responsibilities too."
    T "You will do well to listen to those older and wiser than you as they guide you into the future. Take heed of their teachings and you will become a full and productive member of our clan. Making both your families and your clanmates proud of you and of the clan itself."
    T "The rest of the evening is your own but I urge you to get an early night for tomorrow begins your training in whatever skill your family will teach you."
    T "Goodnight and fair-future to all."
    hide temesh with dissolve
    
    "You take another look over toward Ellie-"
    "no..."
    "[crt_ally.name]... It is going to take some getting use to now."
    "You try to catch her eye but she is already lost in the crowd of her new family."
    
    scene black with dissolve
    "..."
    "You turn back toward your new family. You smile and greet faces, young and old and talk until the fires die down into embers."
    "Your new life begins... "
    
#-----------------------------
# End of scene
#-----------------------------
return