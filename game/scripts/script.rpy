#-------------------------------------------------------------------------------
# This is the primary script. The game stages are controlled from here
#-------------------------------------------------------------------------------

# The game starts here.
label start:

    # Test
    call test
    return
    
    # Do the introduction
    #call chapter("Chapter 1", "Initiation")
    #call chapter1
    
    # Do the meeting stage
    #call chapter("Chapter 2", "Meet your family")
    #call chapter2
    
    # Start the main cycle
    #call chapter("Chapter 3", "On your own")
    
    ">>>> END OF DEMO <<<<"
    
    #call chapter3

    # End of game
    return
