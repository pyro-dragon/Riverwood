#-------------------------------------------------------------------------------
# The events that occure within the Riverwood game
#-------------------------------------------------------------------------------
init 0: 
    python:
        # Stop the menu from appearing
        game.gameLoop.suppressMenu = True
        
        # Chapter 1: Intro and character creation
        game.gameLoop.addEvent(Event("null", "morning", 2, True, lambda: True), 1)      # Skip the morning
        game.gameLoop.addEvent(Event("chapter1", "afternoon", 1, True, lambda: True), 1)

        # Chapter 2: First day in the chose family
        game.gameLoop.addEvent(Event("chapter2", "morning", 3, True, lambda: True), 2)
        game.gameLoop.addEvent(Event("null", "afternoon", 3, True, lambda: True), 2)      # Skip the afternoon

        game.gameLoop.addEvent(Event("testEvent1", "morning", 2, True, lambda: True), 3)
        game.gameLoop.addEvent(Event("testEvent1", "afternoon", 2, True, lambda: True), 3)

        game.gameLoop.addEvent(Event("testEvent2", "morning", 5, True, lambda: True), 4)
        game.gameLoop.addEvent(Event("testEvent2", "afternoon", 5, True, lambda: True), 4)

        game.gameLoop.addEvent(Event("testEvent3", "morning", 3, True, lambda: True), 5)
        game.gameLoop.addEvent(Event("testEvent3", "afternoon", 3, True, lambda: True), 5)

        #game.gameLoop.addEvent(Event("testEvent4", "morning", 4, True, lambda: True), 3)

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
    