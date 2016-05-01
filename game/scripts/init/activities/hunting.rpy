#-------------------------------------------------------------------------------
# The activity mapper for the hunting activity
#-------------------------------------------------------------------------------

init: 
    $huntingLessonCount = 0

# Entry point for the hunting activity
label hunting:
    
    if huntingLessonCount == 0: 
        call hunting1
        return
        
    scene black with fade
    $player.changeSkillBonus("hunting", 1)
    "..."
    "... ..."

            
return
    
# The intro to the hunting activity
label hunting1:
    $game.setLocation(glade)
    
    show Shana with dissolve
    
    S "Greetings my younglings."
    S "Welcome to the Silent Glade."
    S "It is a little way from the Den site and I do appologise my dears."
    S "But it is from here that we can really begin to connect with the world around us."
    
    
    if player.family == "Coppertail": 
        S "I understand that some of you may have felt the anemosity between our families."
        S "I want you to understand that the Bloodrunners are an open and tollerant family and we will be willing to teach anyone who wishes to learn our ways."
        S "We can teach you how to carry out your careers while minimising your impact on our land."
        S "We can show you the patterns of nature and how you may harvest its bounty for your own work."
        S "And for those of a more practical nature, we can offer our marksmanship range."

    elif player.family == "Daggermaw": 
        S "You may know us more for our supporting role in combat, for archery is an important role for us."
        S "But there is so much more than marksmanship."
        S "Some of you may wish to learn the art of medicine to treat fallen warriors."
        S "There may be others that will be inclined towards reading the world around you, from the alarm calls of birds to the art of disgusing your scent."

    elif player.family == "Gildclaw": 
        S "For most of you, your lived will be spend in dark tents, the river docking and even the town of Riverwood itself."
        S "It is for this reason that I hope you will wish to spend some time with us in the great outdoors learning some real and practical skills."
        S "We offer combat training with bows for those who may wish to learn some self defence skills."
        S "But we can also offer more spiritual training to help you relax and center yourselves during tough negotiations."

    S "Todays lesson will not be onerous though."
    S "I wish to give you a simple introduction to the skills that were once essential for every young gnoll..."
    
    $huntingLessonCount += 1
    
    return
    