#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------

screen skills():
    window:
        text "Player skills"
        vbox xalign 0.5 yalign 0.5 xfill True yfill True:
            side "l r" xalign 0.5 yalign 0.5:
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label "Attributes"
                        hbox:
                            vbox:
                                text "Strenth"
                                text "Dexterity"
                                text "Charisma"
                                text "Inteligence"
                            vbox:
                                text str(player.attr["str"])
                                text str(player.attr["dex"])
                                text str(player.attr["cha"])
                                text str(player.attr["int"])
                frame xalign 0.5 xmaximum 300:
                    vbox:
                        label "Skills"
                        hbox:
                            vbox: 
                                text "Archery (Dex)"
                                text "Close combat (Str)"
                                text "Shield usage (Str)"
                                text "Dodge (Dex)"
                                text "Silent movement (Dex)"
                                text "Exploring (Int)"
                                text "Tracking (Dex)"
                                text "Medicine (Int)"
                                text "Engineering (Int)"
                                text "Investigation (Int)"
                                text "Construction (Int)"
                                text "Firearms (Dex)"
                                text "Diplomacy (Cha)"
                                text "Negotiation (Cha)"
                                text "Presentation (Cha)"
                                text "Performance (Dex)"
                            vbox:
                                text str(player.skillBonus["archery"])
                                text str(player.skillBonus["hand weapon"])
                                text str(player.skillBonus["shield"])
                                text str(player.skillBonus["dodge"])
                                text str(player.skillBonus["silent movement"])
                                text str(player.skillBonus["exploring"])
                                text str(player.skillBonus["tracking"])
                                text str(player.skillBonus["medicine"])
                                text str(player.skillBonus["engineering"])
                                text str(player.skillBonus["investigation"])
                                text str(player.skillBonus["construction"])
                                text str(player.skillBonus["firearms"])
                                text str(player.skillBonus["diplomacy"])
                                text str(player.skillBonus["negotiation"])
                                text str(player.skillBonus["presentation"])
                                text str(player.skillBonus["performance"])
                        
            hbox:
                textbutton "Relationships" action [Hide("skills"), Show("relationships")]
                textbutton "Activities" action [Hide("skills"), Show("activity")]
