#-------------------------------------------------------------------------------
# Gildclaw lessons
#-------------------------------------------------------------------------------
label firstWeekendGildclaws: 
    scene black
    show Temesh with dissolve
    
    T "Arise my young acolytes. "
    T "The week has been long for you, I am shure."
    T "However it is now a time for rest, reflextion and relaxation."
    T "At the end of every week you have two days to do with as you desire."
    T "It would be wise to spend this time between socialising with your fellow clanmates."
    T "However, if you deel you need to spend some more time on your studies then I will not stop you."
    T "We start trining again as usual after the weekend so please be mindful of this in your choice of activities."
    
    hide Temesh with dissolve
    
    return

label gildclawLesson1:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your first lesson."
    T "Posture"
    "Presentation +1"
    $player.changeSkillBonus("presentation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson2:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your second lesson."
    T "Pursuasion"
    "Diplomacy +1"
    $player.changeSkillBonus("diplomacy", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson3:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your third lesson."
    T "Valuation"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson4:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your fourth lesson."
    T "Economics 1: Coinage and currency"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson5:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your fifth lesson."
    T "Clan history"
    "Exploring +1"
    $player.changeSkillBonus("exploring", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson6:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your sith lesson."
    T "Presentation"
    "Presentation +1"
    $player.changeSkillBonus("presentation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson7:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your seventh lesson."
    T "Aesthetics"
    "Presentation +1"
    $player.changeSkillBonus("presentation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson8:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your eighth lesson."
    T "Economics 2: Supply and demand"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson9:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your ninth lesson."
    T "Local history"
    "Exploring +1"
    $player.changeSkillBonus("exploring", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson10:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your tenth lesson."
    T "Politics 1: Speachcraft/Rhetoric"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson11:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your eleventh lesson."
    T "Manors and manorisms"
    "Presentation +1"
    $player.changeSkillBonus("presentation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson12:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your twelth lesson."
    T "Reading faces"
    "Diplomacy +1"
    $player.changeSkillBonus("diplomacy", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson13:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your thirteenth lesson."
    T "Economics 3: Specilaisations"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson14:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your fourteenth lesson."
    T "Chess"
    "Performance +1"
    $player.changeSkillBonus("performance", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson15:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your fifteenth lesson."
    T "Politics 2: Debate"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson16:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your sixteenth lesson."
    T "Dance"
    "Performance +1"
    $player.changeSkillBonus("performance", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson17:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your seventeenth lesson."
    T "Book keeping"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson18:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your eighteenth lesson."
    T "The peerage"
    "Performance +1"
    $player.changeSkillBonus("performance", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson19:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your ninteenth lesson."
    T "Language"
    "Negotiation +1"
    $player.changeSkillBonus("negotiation", 1)
    hide temesh

    scene black with fade
    return

label gildclawLesson20:
    scene expression tent.name with fade
    show temesh with dissolve
    T "Welcome to your twentith lesson."
    T "Law"
    "Diplomacy +1"
    $player.changeSkillBonus("iplomacy", 1)
    hide temesh

    scene black with fade
    return