screen tester():
    modal True
    tag testScreen
    zorder 1
                
    window: 
        text "This is one string"

        add "characters/temesh.png" xalign 1.0 yalign 0.0
        
        bar value Preference("music volume")

        button: 
            text "button"

        fixed:
            text "Fixed area"

        frame: 
            xpadding 10
            ypadding 10
            xalign 0.5
            yalign 0.5
            
            text "This is a frame"

        grid 2 4:
            button: 
                text "coppertails"
            text "morning"

            button: 
                text "gildclaws"
            text "afternoon"

            button: 
                text "daggermaws"
            text "evening"

            button: 
                text "bloodrunners"
            text "night"
            
        hbox:
            text "left"
            text "right"

        text "enter some input": 
            xpos 20 
            ypos 130
        input default "Joseph P. Blow, ESQ.":
            xpos 20 
            ypos 150
            
        key "p" action ShowMenu('preferences')

        label "TestLabel"
        
        null height 30

        mousearea:
            area (0, 0, 1.0, 100)

        side "tl br":
            text "one side"
            text "another side"
            
        textbutton "Wine" action Jump("wine")
        
        #timer 3.0 action Jump("too_slow")
        
        transform:
            textbutton "Wine" action Jump("wine")
        
        vbar value Preference("voice volume")

        side "c b r":
            area (100, 100, 600, 400)

            viewport id "vp":
                draggable True

                add "characters/hunter.jpg"

        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")
        
        