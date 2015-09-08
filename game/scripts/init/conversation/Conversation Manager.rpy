#-------------------------------------------------------------------------------
# The conversation manager
#-------------------------------------------------------------------------------
init: 
    python:
        ##
        # Class describing a conversation topic
        class Topic:
            
            ##
            # Constructor
            # @param title (string) The title of the topic. It will appear in the conversation menu
            # @param label (string) The label to execute for this topic
            # @param hidden (boolean) (default=True) If the topic should be hidden from the menu or not
            # @param condition (function) A lambda function to reveal the topic when update() is run
            def __init__(self, title, label, hidden=True, condition=False):
                self.title = title
                self.label = label
                self.hidden = hidden
                self.condition = condition
                self.read = False
                
            ##
            # Update the topic by running the lambda and revealing the topic
            def update(self):
                if condition: 
                    self.hidden = False
        
        conversationTopic = ""
        talkTurns = 3      # The amount the player gets to talk before home time

# Conversation entry label
label conversation:
    
    python: 
        
        # Get a list of location names and the locations as tuples
        locationItems = []
        for location in game.locations: 
            if location.discovered == True:
                locationItems.append((location.name, location))
            
        # Apply the tuple this to display a menu and get the result
        result = renpy.display_menu(locationItems)
        
        # Set the current location
        game.currentLocation = result
    
    scene expression game.currentLocation.getBacgroundImage() with fade
    show expression playerCompanion.image with dissolve
    call screen conversation(playerCompanion)

# Pre-process conversations before calling them, then go back to the topic screen
label conversationWrapper():

    # Check if we have talked about this before
    if conversationTopic.read == True: 
        call expression playerCompanion.topics["repeat"].label
        
    # Call the actual topic label
    call expression conversationTopic.label
        
    # Mark it as read
    $conversationTopic.read = True
        
    # Remove a talk turn
    $talkTurns = talkTurns - 1
    
    # Check if we should return to the menu or get away
    if talkTurns > 0:
        # Head back to the conversation screen
        call screen conversation(playerCompanion)
    else:
        call expression playerCompanion.topics["late"].label
        
    return