#-------------------------------------------------------------------------------
# The events that occure within the Riverwood game
#-------------------------------------------------------------------------------
init 0: 
    python:
        # Stop the menu from appearing
        #game.gameLoop.suppressMenu = True
        
        # Chapter 1: Intro and character creation
        #game.gameLoop.addEvent(Event("null", "morning", 2, True, lambda: True), 0)      # Skip the morning
        #game.gameLoop.addEvent(Event("chapter1", "afternoon", 2, True, lambda: True), 0)

        # Chapter 2: First day in the chose family
        #game.gameLoop.addEvent(Event("chapter2", "morning", 3, True, lambda: True), 1)
        #game.gameLoop.addEvent(Event("mechanicIntroduction", "afternoon", 2, True, lambda: True), 1)    # Oportunity to see the mechanic girl
        
        # Ally comes to speak to you after the week is over
        game.gameLoop.addEvent(Event("endOfFirstWeek", "evening", 4, True, lambda: True), 4)

# Null label to skip some time
label null:
    return

label testEvent1:
    "test 1"
    return
    
label testEvent2:
    "test 2"
    return
    
label testEvent3:
    "test 3"
    return
    
label testEvent4:
    "test 4"
    return
    