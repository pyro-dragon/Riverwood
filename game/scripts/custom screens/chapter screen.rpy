#-------------------------------------------------------------------------------
# The chapter change screen
#-------------------------------------------------------------------------------
screen chapter(title, subtitle = "", jumppoint = ""):
    on "show" action[Show("chapterTitle", chText=title), Show("subTitle", chText=subtitle)]
    
    timer 3.0 action[Hide("chapterTitle"), Hide("subTitle")]
    
    # Close the window
    timer 3.5 action[Hide("chapterTitle"), Jump(jumppoint)]
    #textbutton "Head out" action Jump(jumppoint)
            
screen chapterTitle(chText): 
    text chText at slideTransform(0.2, 0.2)

screen subTitle(chText): 
    text chText at slideTransform(0.8, 0.3)

transform slideTransform(xstart = 0.4, ystart = 0.5):
    yalign 0.1
    
    on show:
        parallel:
            #alpha 0
            easein 0.5 alpha 1.0
        parallel:
            xalign xstart yalign ystart
            easein 0.5 xalign 0.5
    on hide:
        parallel:
            easeout 0.5 alpha 0
        parallel:
            easeout 0.5 xalign xstart