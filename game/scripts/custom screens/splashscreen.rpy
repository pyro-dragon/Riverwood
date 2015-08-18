#-------------------------------------------------------------------------------
# The splash screen. Something that shows up before the main menu
#-------------------------------------------------------------------------------

label splashscreen:
    scene black
    with Pause(1)

    show text "Large Scale Industries Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return