#-------------------------------------------------------------------------------
# The events that occure within the Riverwood game
#-------------------------------------------------------------------------------
# Event structure: label, timeslot, expireryDate, override, conditions
#-------------------------------------------------------------------------------
init 0: 
    python:
        # Stop the menu from appearing
        game.gameLoop.suppressMenu = True
        
        # Chapter 1: Intro and character creation
        game.gameLoop.addEvent(Event("nullEvent", "morning", 2, True, lambda: True), 0)      # Skip the morning
        game.gameLoop.addEvent(Event("chapter1", "afternoon", 2, True, lambda: True), 0)

        # Chapter 2: First day in the chose family
        game.gameLoop.addEvent(Event("chapter2", "morning", 3, True, lambda: True), 1)
        #game.gameLoop.addEvent(Event("mechanicIntroduction", "afternoon", 2, True, lambda: True), 1)    # Oportunity to see the mechanic girl
        
        # End of week assesment by family head
        game.gameLoop.addEvent(Event("endOfWeekAssesment", "morning", 2, True, lambda: True), 4)      # Skip the morning

        # Ally comes to speak to you after the week is over
        game.gameLoop.addEvent(Event("endOfFirstWeek", "evening", 4, True, lambda: True), 4)
        
        # Rival comes to taunt you after the week is over
        game.gameLoop.addEvent(Event("endOfFirstWeekTaunt", "evening", 4, True, lambda: True), 4)

        ## Ship the first weekend menu
        game.gameLoop.addEvent(Event("suppressMenu", "morning", 4, True, lambda: True), 4)
        
        # Family leader explains that you get the weekend off
        game.gameLoop.addEvent(Event("firstWeekend", "morning", 5, False, lambda: True), 5)

# Null label to skip some time
label nullEvent:
    return

# Event to suppress the next activity choice screen
label suppressMenu: 
    "Suppressing the menu"
    $game.gameLoop.suppressMenu = True