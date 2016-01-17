#-------------------------------------------------------------------------------
# The events that occure within the Riverwood game
#-------------------------------------------------------------------------------
init: 
    python:
        # Stop the menu from appearing
        game.gameLoop.suppressMenu = True
        
        # Chapter 1: Intro and character creation
        game.gameLoop.addEvent(Event("null", "morning", 1, True, lambda: True), 0)      # Skip the morning
        game.gameLoop.addEvent(Event("chapter1", "afternoon", 1, True, lambda: True), 0)

        # Chapter 2: First day in the chose family
        game.gameLoop.addEvent(Event("chapter2", "morning", 1, True, lambda: True), 0)
        game.gameLoop.addEvent(Event("null", "afternoon", 1, True, lambda: True), 0)      # Skip the afternoon

# Null label to skip some time
label null: