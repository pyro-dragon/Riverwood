#-------------------------------------------------------------------------------
# The chapter change screen
#-------------------------------------------------------------------------------
label chapter(title, subtitle):
    scene black
    show expression Text("%s" % title) as ch at slideTransform(0.2, 0.2, 0.6, 0.8)
    show expression Text("%s" % subtitle) as sub at slideTransform(0.8, 0.3, 0.4, 0.2, 0.5)

    pause 3.0

    hide ch
    hide sub
    pause 0.5

    return

transform slideTransform(xstart = 0.4, ystart = 0.5, xdrift = 0.0, xend = 0.0, delaytime = 0.0):
    yalign 0.1
    
    on show:
        xalign xstart yalign ystart alpha 0
        delaytime
        easein 0.5 xalign 0.5 alpha 1.0
        easein 2.5 xalign xdrift
    on hide:
        easeout 0.5 xalign xend alpha 0