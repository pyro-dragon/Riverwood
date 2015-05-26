#-------------------------------------------------------------------------------
# The character creation scene
#-------------------------------------------------------------------------------

#-----------------------------
# Choose the players family
#-----------------------------
label chooseFamily: 

    T "Which family will you choose?"
    
    menu:
        "I in tune with the ways of the Bloodrunners. (Nature, Hunters, Medicine)":
            jump chooseBloodrunners
            
        "I have a great interest in joining the Coppertails. (Industry, Crafting, Science)":
            jump chooseCoppertails
                
        "The Daggermaws seem like the only family tough enough for me! (Fighting, Tactics, Scouting)":
            jump chooseDaggermaws
                
        "It will be an honour to join the Gildclaws. (Diplomacy, Trade, Economics)":
            jump chooseGildclaws
            
    return

#-----------------------------
# Choose the Bloodrunners.
#-----------------------------
label chooseBloodrunners:
    $player.family = "Bloodrunner"
    $crt_ally.family = "Daggermaw"
    $crt_ally.name = "Scarah"
    $crt_rival.family = "Coppertail"
    $crt_rival.name= "Scorch"
    jump checkFamily

#-----------------------------
# Choose the Coppertails.
#-----------------------------
label chooseCoppertails:
    $player.family = "Coppertail"
    $crt_ally.family = "Gildclaw"
    $crt_ally.name = "Deft"
    $crt_rival.family = "Daggermaw"
    $crt_rival.name = "Dirge"
    jump checkFamily
    
#-----------------------------
# Choose the Daggermaws.
#-----------------------------
label chooseDaggermaws:
    $player.family = "Daggermaw"
    $crt_ally.family = "Bloodrunner"
    $crt_ally.name = "Swift"
    $crt_rival.family = "Gildclaw"
    $crt_rival.name = "Silver"
    jump checkFamily
    
#-----------------------------
# Choose the Gildclaws.
#-----------------------------
label chooseGildclaws:
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
    T "Excellent. I am sure you will be an asset to the [player.family]s."
    T "Now, you must take a name for yourself. You can either choose one yourself of have your new family suggest a name. Which would you like?"
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
            "Moon Spirit":
                $player.name = "Moon Spirit"
                jump checkName

            "Sharp Eye":
                $player.name = "Sharp Eye"
                jump checkName

    elif player.family == "Coppertail":
        menu: 
            "Gelda":
                $player.name = "Gelda"
                jump checkName
                
            "Rivet":
                $player.name = "Rivet"
                jump checkName
                
    elif player.family == "Daggermaw":
        menu: 
            "Quick Fang":
                $player.name = "Quick Fang"
                jump checkName
                
            "Ripper":
                $player.name = "Ripper"
                jump checkName
                
    elif player.family == "Gildclaw":
        menu: 
            "Credit":
                $player.name = "Coin"
                jump checkName
                
            "Debit":
                $player.name = "Gilt"
                jump checkName

#-----------------------------
# The outro to the naming 
# ceremony. 
#-----------------------------
label concludeCeremony:
    show Temesh
    T "Very well. [player.name] of the [player.family] family. Welcome."
    T "Take your place with your family."
    hide Temesh

    "You walk calmly over to your new family, your heart pumping fast and your mind buzzing. "
    "Temesh calls the next young gnoll forward."

    show Temesh
    T "Are you ready to pick your family?"
    hide Temesh

    show expression crt_ally.image
    a "Yes. I think I have decided."
    a "I choose the [crt_ally.family] family."

    "For a moment she looked toward you, an apologetic look in her eyes. She turns back to Temesh and nods."
    a "Yes, I choose the [crt_ally.family]s"
    hide expression crt_ally.image

    show Temesh
    T "Very well. And what name will you go by?"
    hide Temesh

    show expression crt_ally.image
    a "[crt_ally.name]"
    hide expression crt_ally.image

    show Temesh
    T "[crt_ally.name], of the [crt_ally.family]s family. Welcome."
    hide Temesh

    show expression crt_rival.image
    r "Damn, I’m being picked last aren't I?"
    hide expression crt_rival.image

    show Temesh
    T "Calm yourself there young one. Come forth."
    T "Which family will you join?"
    hide Temesh

    show expression crt_rival.image
    "[crt_rival.name] glares at you before turning back to Temesh."
    r "I will join the [crt_rival.family]s."
    hide expression crt_rival.image

    show Temesh
    T "And what name will you go by?"
    hide Temesh

    show expression crt_rival.image
    r "[crt_rival.name]!"
    hide expression crt_rival.image

    show Temesh
    T "Then I welcome you [crt_rival.name] of the [crt_rival.family]s."
    hide Temesh

    "You watch as [crt_rival.name] takes up station next to his new family."

    show Temesh
    T "That now concludes the naming ceremony of the Riverwood clan. I would like to welcome you all as fresh young adults. You now have every privilege a full clan member is entitled to, but you also have responsibilities too."
    T "You will do well to listen to those older and wiser than you as they guide you into the future. Take heed of their teachings and you will become a full and productive member of our clan. Making both your families and your clanmates proud of you and of the clan itself."
    T "The rest of the evening is your own. Tomorrow you will wake with new names and a new life."
    T "Goodnight and fair-future to all."
    hide Temesh

    "You take a look over toward- what was it now? Ah yes, [crt_ally.name]."
    "It will take some getting used to."
    "You try to catch her eye but she is already lost in the crowd of her new family."

    scene black with fade
    "..."
    "You turn back toward your new family. You smile and greet faces, young and old and talk until the fires die down into embers."
    "Your new life begins... "