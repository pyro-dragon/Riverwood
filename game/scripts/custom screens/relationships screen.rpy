#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

screen relationships():
    window:
        text "Relationship progress"
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            side "tl l bl tr r br" xalign 0.5 yalign 0.5:
                for character in game.dateableCharacters: 
                    if character.met == True: 
                        frame xalign 0.5 xmaximum 300:
                            vbox:
                                label character.trueName + " " + character.family
                                hbox:
                                    add character.thumbnail
                                    vbox:
                                        text "Career: " + character.nick
                                        bar value character.rp range 100
                                        text character.getRpStatement()
                
                        
            hbox:
                textbutton "Skills" action[Hide("relationships"), Show("skills")]
                textbutton "Activities" action[Hide("relationships"), Show("activity")]
