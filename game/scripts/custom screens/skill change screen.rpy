#-------------------------------------------------------------------------------
# This shows changes to the skills
#-------------------------------------------------------------------------------
screen skillNoteScreen(skill, score):
    modal False
    timer 0.1 action Show("skillShowBox", dissolve, skill, score)
    timer 3.0 action Hide("skillShowBox", dissolve)
    timer 4.0 action [Hide("skillNoteScreen"), Return()]

screen skillShowBox(skill, score):
    modal False
    vbox xalign 0.1 yalign 0.3 xfill True yfill True:
        frame xalign 0.1 yalign 0.3:
            text skill + " " + score
                
    #timer 3.0 action Hide("skillShowBox", transition=slideawaydown)
    