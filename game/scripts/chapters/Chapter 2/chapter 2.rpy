#-------------------------------------------------------------------------------
# The index for the second chapter
#-------------------------------------------------------------------------------

label chapter2:

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

    # What to do after the introduction
    if playerCompanion:
        call activityList
    elif:
        # Instroduce the first datable
        if player.family != "Coppertail"]:
            call mechanicIntroduction
