#-------------------------------------------------------------------------------
# The splash screen. Something that shows up before the main menu
#-------------------------------------------------------------------------------

screen releaseNotes(displayNotes):
    # Read me box
    frame:
        xalign 0.5
        yalign 0.5
        xminimum 0.7
        xmaximum 0.7
        yminimum 0.7
        ymaximum 0.8
        
        frame: 
            background "#FFFFFF"
            xalign 0.5
            yalign 0.0
            xmaximum  1.0
            ymaximum  1.0
            has viewport
            draggable True
            mousewheel True
            scrollbars "vertical"
            
            text displayNotes color "#000000" size 12 font "cour.ttf" 
            
        textbutton "Close" action Return(0) yalign 1.1 xalign 1.0

label splashscreen:
    
    # Read the display notes
    $notes = game.getFileData("change notes.txt", "flat")
    $versionNum = game.getFileData("version.txt", "flat")
    
    scene black
    call screen releaseNotes(notes)

    with Pause(1)

    show text "Large Scale Industries Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return