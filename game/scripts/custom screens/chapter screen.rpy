#-------------------------------------------------------------------------------
# The chapter change screen
#-------------------------------------------------------------------------------
screen chapter(title, subtitle = ""):
    #on "show" action Show("chapterText", chText="hello")
    on "show" action[Show("chapterTitle", chText=title), Show("subTitle", chText=subtitle)]
    #window:
        #Show("chapterText")
        #vbox xfill True yfill True at slideTransform:
            #text title xalign 0.5 yalign 0.2
            #text subtitle xalign 0.5 yalign 0.3
            #textbutton "Continue" xalign 0.5 yalign 0.4 action Return(True)
            
screen chapterTitle(chText): 
    text chText at slideTransform

screen subTitle(chText): 
    text chText at slideTransform

transform slideTransform:
    yalign 0.1
    
    on show:
        parallel:
            #alpha 0
            easein 0.5 alpha 1.0
        parallel:
            #xalign 0.4 yalign 0.2
            easein 0.5 xalign 0.5
    on hide:
        parallel:
            easeout 0.5 alpha 0
        parallel:
            easeout 0.5 xalign 0.0