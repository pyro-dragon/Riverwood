#-------------------------------------------------------------------------------
# The events that occure within the Riverwood game
#-------------------------------------------------------------------------------
init: 
    python:
        # Intro and character creation
        game.gameLoop.addEvent(Event("chapter1", "morning", 1, True, lambda: True), 0)