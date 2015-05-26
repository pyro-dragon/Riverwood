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
    a "[crt_ally.trueName]"
    $crt_ally.showName()
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
    r "[crt_rival.trueName]!"
    $crt_rival.showName()
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
    
    return