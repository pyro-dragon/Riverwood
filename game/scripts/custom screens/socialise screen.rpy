#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""
    
screen activity():
    window:
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            text "Socialising"
            side "l r" xalign 0.5 yalign 0.5:
                frame xalign 0.5:
                    vbox:
                        label _("Choose your afternoon activity:")
                        textbutton "Go exploring" action SetVariable("activityTarget", "explore")
                        textbutton "Practice skills" action SetVariable("activityTarget", "practice")
                        textbutton "Socialise with clan" action SetVariable("activityTarget", "socialise")
                        textbutton "Hang out with someone" action SetVariable("activityTarget", "hangOut")
                        
                frame xalign 0.5:
                    vbox:
                        label _("Who with?:")
                        if crt_trader.met == True: 
                            textbutton crt_trader.trueName + " " + crt_trader.family action SetVariable("playerCompanion", crt_trader)
                        if crt_mechanic.met == True: 
                            textbutton crt_mechanic.trueName + " " + crt_mechanic.family action SetVariable("playerCompanion", crt_mechanic)
                        if crt_hunter.met == True: 
                            textbutton crt_hunter.trueName + " " + crt_hunter.family action SetVariable("playerCompanion", crt_hunter)
                        if crt_fighter.met == True: 
                            textbutton crt_fighter.trueName + " " + crt_fighter.family action SetVariable("playerCompanion", crt_fighter)
                        if crt_ally.met == True: 
                            textbutton crt_ally.trueName + " " + crt_ally.family action SetVariable("playerCompanion", crt_ally)
                        if crt_rival.met == True: 
                            textbutton crt_rival.trueName + " " + crt_rival.family action SetVariable("playerCompanion", crt_rival)
                        
            side "l r":
                hbox:
                    textbutton "Skills" action[Hide("activity"), Show("skills")]
                    textbutton "Relationships" action [Hide("activity"), Show("relationships")]

                if activityTarget != "" and playerCompanion != "":
                    textbutton "Head out" action Jump(activityTarget)
