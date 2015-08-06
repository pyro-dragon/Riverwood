#-------------------------------------------------------------------------------
# This is the management module for the chat system
#-------------------------------------------------------------------------------

init 1: 
    python: 
        
        ##
        # The chat manager
        class ChatManager:
            
            ##
            # Constructor
             def __init__(self):
                 
                 # Create the resource manager
                self.chatRecMan = ChatResourceManager
                self.participants = []          # An array of Roles that contains arrays of Participants
                
            ##
            # Create a conversation
            # @param length (int) The amount of chat segments to use
            # Return a map containing the "conversation" array, the "participants" array and the conversation "length"
            def generateConversation(self, length = 3):
                
                # The array of segments
                chatSegments = []
                
                # Fill out these segments
                for i in range(length):
                    # Generate a random index
                    index = renpy.random.randint(0, self.segCount-1)
                    # Append the segment to the fragment array
                    conversationFragments.append(self.segments[index])
                    # Pop the segment from the list
                    self.segments.pop(index)
                    # Decrease the count
                    self.segCount -= 1
                    
                # Get all the participants
                participants = []
                for i in conversationFragments: 
                    for j in i.participants:
                        participants.append(j)
                # Convert to a set (to eliminate duplicates)
                participants = set(participants)
                
                return {"conversation":conversationFragments, "participants": participants, "length": length}
               
            # Generate a conversation particiapnt (or supply a ready made one)
            def getParticipant(self, type): 
                # Check to see if the participant already exists
                if type in self.participants: 
                    return self.participants[type]
                else:
                    return self.generateParticipant(type)
            
            # Generate a participant
            def generateParticipant(self, type):
                # Pick a headshot
                pic = {}
                while True: 
                    pic = self.headshots[renpy.random.randint(0, self.headshotCount-1)]
                    if pic.type == type: 
                        break
                
                # Pick a name
                name = {}
                while True:
                    name = self.names[renpy.random.randint(0, self.nameCount-1)]
                    if name.male == pic.male:
                        break
                    
                # Pick a colour
                colour = game.generateColour()
                
                #                       name,    family, career, renpyCharacter,                                                 imageName,             met, hideName, thumbnail
                tmpPart = GameCharacter(name.name, "none", "none", Character("{image=" + pic.image + "}" + name.name, kind=nvl, window_background=Solid(colour), window_xfill=True), pic.image, True, False, "")
                #tmpPart = {"name": name.name, "family": name.family, "thumbnail": pic.image, "male": name.male, "colour": colour}
                
                self.participants[type] = tmpPart
                
                return tmpPart