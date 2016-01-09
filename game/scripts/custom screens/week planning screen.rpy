#-------------------------------------------------------------------------------
# A screen used to pick activities and lessons for the week
#-------------------------------------------------------------------------------
init:
    $activityTarget = ""
    
screen weekPlan():
    window:
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            text "Today's activities"
            side "l r" xalign 0.5 yalign 0.5:
                frame xalign 0.5:
                    vbox:
                        label _("Choose your afternoon activity:")
                        textbutton "Go exploring" action SetVariable("activityTarget", "explore")
                        #textbutton "Practice skills" action SetVariable("activityTarget", "practice")
                        textbutton "Socialise with clan" action SetVariable("activityTarget", "socialise")
                        textbutton "Hang out with someone" action SetVariable("activityTarget", "hangOut")
                        
                frame xalign 0.5:
                    vbox:
                        label _("Who with?:")
                        for character in game.dateableCharacters: 
                            if character.met == True: 
                                if character.met == True: 
                                    textbutton character.trueName + " " + character.family action SetVariable("playerCompanion", character)
                        
            side "l r":
                hbox:
                    textbutton "Skills" action[Hide("activity"), Show("skills")]
                    textbutton "Relationships" action [Hide("activity"), Show("relationships")]

                if activityTarget != "" and playerCompanion != "":
                    textbutton "Head out" action Jump(activityTarget)
