#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

screen chapter(title, subtitle = ""):
    
    window:
        #vbox xalign 0.5 yalign 0.5:
        frame at:
            text title xalign 0.5 yalign 0.2
            text subtitle xalign 0.5 yalign 0.3
            textbutton "Continue" xalign 0.5 yalign 0.4 action Return(True)