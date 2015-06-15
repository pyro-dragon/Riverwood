#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
init:
    $lessonTarget = ""
    $activityTarget = ""
    
screen activity():
    window:
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            text "Today's activities"
            side "l r" xalign 0.5 yalign 0.5:
                frame xalign 0.5:
                    vbox:
                        label _("Choose who to learn with:")
                        $lessonTarget = ""
                        textbutton ("Bloodrunners") action SetVariable("lessonTarget", "bloodrunnerLesson")
                        textbutton ("Coppertails") action SetVariable("lessonTarget", "coppertailLesson")
                        textbutton ("Daggermaws") action SetVariable("lessonTarget", "daggermawLesson")
                        textbutton ("Gildclaws") action SetVariable("lessonTarget", "gildclawLesson")
                        
                frame xalign 0.5:
                    vbox:
                        label _("Choose your afternoon activity:")
                        textbutton "Go exploring" action SetVariable("activityTarget", "explore")
                        textbutton "Practice skills" action SetVariable("activityTarget", "practice")
                        textbutton "Socialise with clan" action SetVariable("activityTarget", "socialise")
                        textbutton "Hang out with someone" action SetVariable("activityTarget", "hangOut")
                        
            side "l r":
                hbox:
                    textbutton "Skills" action[Hide("activity"), Show("skills")]
                    textbutton "Relationships" action [Hide("activity"), Show("relationships")]

                textbutton "Head out" action Jump("mainActivityCycle")
