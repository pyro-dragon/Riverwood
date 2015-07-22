#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

init 1: 
    python: 
        class ChatSegment: 
            
            # Constructor
            def __init__(self, name, label, participants):
                self.name = name
                self.label = label
                self.participants = participants
                self.told = False