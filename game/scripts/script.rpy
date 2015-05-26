#-------------------------------------------------------------------------------
# This is the primary script. The game stages are controlled from here
#-------------------------------------------------------------------------------

# The game starts here.
label start:

    # Test
    #call test
    
    # Do the introduction
    call chapter1
    
    # Do the meeting stage
    call meetings
    
    # Start the main cycle
    call chapter3

    # End of game
    return
