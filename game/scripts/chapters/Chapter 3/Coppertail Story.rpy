#-------------------------------------------------------------------------------
# Coppertail Missions
#-------------------------------------------------------------------------------
label firstWeekendCoppertails: 
    scene black
    show Clarence with dissolve
    
    C "Wakey wakey youg'uns!"
    C "You have had a jolly busy week I trust."
    C "But it is time for joyousness as the weekend is here!"
    C "You have two days, two full days to do with what you wish!"
    C "So go out there, have some fun, learn some new things about the world and eachother."
    C "But don't get too emphatic, we have another week of training to follow."
    C "Then another weekend, then more training then a weekend and then more training and..."
    C "... Well, you get the idea."
    C "I hope."
    
    hide Clarence with dissolve
    
    return

init 2:
    $playerHasCopper = False
    
    python:
        coppertailMissions = []
        # missionLabel, overrideAfternoon, condition, conditionPassLabel, conditionFailLabel
        coppertailMissions.append(Mission("Clarence announces his plan", False, lambda: True, "clarencePlan"))
        coppertailMissions.append(Mission("Return copper", False, lambda: playerHasCopper, "refineCopper", "noCopper"))
        coppertailMissions.append(Mission("Processing the copper", False, lambda: True))
        
# Mission 0
label clarencePlan:
    C "You need to get me some copper!!"
    return

label refineCopper:
    C "We are going to refine this copper now"
    return
    
label noCopper: 
    C "I am waiting for you to bring me my copper!"
    $playerHasCopper = True
    return

label coppertailLesson1:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your first lesson."
    C "Mathematics 1: Simple arithmetics"
    "Inteligence +1"
    $player.changeAttr("int", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson2:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your second lesson."
    C "Technical drawing"
    "Engineering +1"
    $player.changeSkillBonus("exploring", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson3:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your third lesson."
    C "Weights and measures"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson4:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your fourth lesson."
    C "Workshop safety"
    "Investigation +1"
    $player.changeSkillBonus("investigation", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson5:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your fifth lesson."
    C "Hand tool usage"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson6:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your sith lesson."
    C "Woodwork"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson7:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your seventh lesson."
    C "Joinery"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson8:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your eighth lesson."
    C "Glues and their applications"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson9:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your ninth lesson."
    C "Finishing"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson10:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your tenth lesson."
    C "Mathematics 2: Algebra"
    "Inteligence +1"
    $player.changeAttr("int", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson11:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your eleventh lesson."
    C "Ore surveying"
    "Exploring +1"
    $player.changeSkillBonus("exploring", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson12:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your twelth lesson."
    C "Mining"
    "Strength +1"
    $player.changeAttr("str", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson13:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your thirteenth lesson."
    C "Metallogy"
    "Firearms +1"
    $player.changeSkillBonus("firearms", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson14:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your fourteenth lesson."
    C "Materials"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson15:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your fifteenth lesson."
    C "Mathematics 3: Quatratics"
    "Inteligence +1"
    $player.changeAttr("int", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson16:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your sixteenth lesson."
    C "Riviting"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson17:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your seventeenth lesson."
    C "Welding"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson18:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your eighteenth lesson."
    C "Lathe work"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson19:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your ninteenth lesson."
    C "Basic architecture"
    "Construction +1"
    $player.changeSkillBonus("construction", 1)
    hide clarance

    scene black with fade
    return

label coppertailLesson20:
    scene expression forge.name with fade
    show clarance with dissolve
    C "Welcome to your twentith lesson."
    C "Clockwork"
    "Engineering +1"
    $player.changeSkillBonus("engineering", 1)
    hide clarance

    scene black with fade
    return