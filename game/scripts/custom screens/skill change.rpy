#-------------------------------------------------------------------------------
# This shows changes to the skills
#-------------------------------------------------------------------------------
screen skillNote():
    textbutton "click" action Show("skillShow", transition=slideright)

screen skillShow():
    vbox xalign 0.1 yalign 0.7 xfill True yfill True:
            frame xalign 0.1 yalign 0.3:
                text "So, how do you feel."
                
    timer 3.0 action Hide("skillShow", transition=slideleft)
    