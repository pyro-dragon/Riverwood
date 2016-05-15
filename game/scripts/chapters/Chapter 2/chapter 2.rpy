#-------------------------------------------------------------------------------
# The index for the second chapter
#-------------------------------------------------------------------------------

label chapter2:
    
    call chapter("Chapter 2", "Meet your family")

    # Push time onwards
    $game.advanceTime()

    scene black
    "You wake slowly, your head spinning."
    "Last night seems so long ago now."
    "The familier sounds of the dawn birds filter through to your ears as you rub your eyes."
    "Everything will be different now. With apprehension and excitement you look forward to the new day and your new life."

    # Family introductions
    if player.family == "Bloodrunner":
        call bloodrunnerIntroduction

    elif player.family == "Coppertail":
        call coppertailIntroduction

    elif player.family == "Daggermaw":
        call daggermawIntroduction

    elif player.family == "Gildclaw":
        call gildclawIntroduction

    # Go send the player off to do something with whoever they met at the introduction
    if playerCompanion != None:
        call activityCycle
    return