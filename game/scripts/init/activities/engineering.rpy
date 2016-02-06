#-------------------------------------------------------------------------------
# The activity mapper for the engineering activity
#-------------------------------------------------------------------------------

init: 
    $engineeringLessonCount = 0

# Entry point for the engineering activity
label engineering:
    
        if engineeringCount == 0: 
            call engineering1
            return
            
        scene black with fade
        $player.changeSkillBonus("engineering", 1)
        "..."
        "... ..."

            
return
    
# The intro to the engineering activity
label engineering1:
    $game.setLocation(forge)
    
    show Clarence with dissolve
    
    C "Ah, welcome, welcome!"
    C "It is good to see all you youngsters"
    C "I am Clarance Coppertail and I am the head of the Coppertail family."
    C "As you may know already, we deal with the exciting field of technology and craftwork!"
    
    if player.family == "Bloodrunner": 
        C "Now some of you would be questioning what that has to do with you."
        C "You guys are Bloodrunners arn't you? You are all about understanding nature and making use of what she has to offer."
        C "Almost the polar opposite of us with our machines and tools and experimentation."
        C "In fact you will find we are very similar! We seek to understand nature and use it as best we can."
        C "To find the best metals we need to understand geology. To build strong buildings we need to understand how to grow strong timber."
        C "The Coppertails and Bloodrunners have a long history of working together on all kinds of projects."

    elif player.family == "Daggermaw": 
        C "Now I know a lot of you are groaning at having to spend a few hours down in the workshop with the 'nerds', but I think some of you will really value what we do."
        C "Part of our mandate from Temesh is that we make and experiment with new kinds of weapons to help keep our clan ahead."
        C "My own background is in firearms manufacture in fact."
        C "Studying with us will most certainly involve using some of the most cutting edge weapons at the clans disposal as well as being able to help us design them."
        C "Also we could certainly use some strong arms around the place. We have to move around some pretty weighty things from time to time."

    elif player.family == "Gildclaw": 
        C "Now you guys might feel a little reluctant to get your hands dirty, but Temesh insists everyone gets to sample each family and the training it offeres."
        C "Engineering and science are important subjects to study, especially for the Gildclaws."
        C "You will almost certainly spend most of your days negotiating prices on and trading in materials and products we use here."
        C "Knowlege of mineral extraction and manufacturing techniques may give you an edge in price negotiations that your opposite number may not."

    C "So I think we shall get started on todays lesson."
    C "Its quite simple and will demonstrate some basic principals..."
    
    return
    