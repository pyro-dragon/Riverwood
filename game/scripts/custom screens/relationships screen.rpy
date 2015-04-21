#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

screen relationships():
    window:
        text "Relationship progress"
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            side "tl l bl tr r br" xalign 0.5 yalign 0.5:
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_mechanic.trueName + " " + crt_mechanic.family
                        hbox:
                            add crt_mechanic.thumbnail
                            vbox:
                                text "Career: " + crt_mechanic.career.name
                                bar value crt_mechanic.rp range 100
                                text crt_mechanic.getRpStatement()
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_trader.trueName + " " + crt_trader.family
                        hbox:
                            add crt_trader.thumbnail
                            vbox:
                                text"Career: " + crt_trader.career.name
                                bar value crt_trader.rp range 100
                                text crt_trader.getRpStatement()
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_ally.trueName + " " + crt_ally.family
                        hbox:
                            add crt_ally.thumbnail
                            vbox:
                                text "Career: " + crt_ally.career
                                bar value crt_ally.rp range 100
                                text crt_ally.getRpStatement()
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_fighter.trueName + " " + crt_fighter.family
                        hbox:
                            add crt_fighter.thumbnail
                            vbox:
                                text "Career: " + crt_fighter.career.name
                                bar value crt_fighter.rp range 100
                                text crt_fighter.getRpStatement()
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_hunter.trueName + " " + crt_hunter.family
                        hbox:
                            add crt_hunter.thumbnail
                            vbox:
                                text "Career: " + crt_hunter.career.name
                                bar value crt_hunter.rp range 100
                                text crt_hunter.getRpStatement()
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label crt_rival.trueName + " " + crt_rival.family
                        hbox:
                            add crt_rival.thumbnail
                            vbox:
                                text "Career: " + crt_rival.career
                                bar value crt_rival.rp range 100
                                text crt_rival.getRpStatement()
                        
            hbox:
                textbutton "Skills" action[Hide("relationships"), Show("skills")]
                textbutton "Activities" action[Hide("relationships"), Show("activity")]
