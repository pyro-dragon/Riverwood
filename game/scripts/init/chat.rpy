#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

# Participant types
# Enthusiastic
# Skeptic
# Upset
# Bragger

init 1: 
    python: 
        class ConversationManager:
            
            # Constructor
            def __init__(self):
                self.segments = []
                self.segCount = 0
                self.participants = {}
                
            # Add a chat segment
            def AddSegment(self, segment):
                self.segments.append(segment)
                self.segCount += 1
                
            # Create a conversation
            # Return a map containing the "conversation" array, the "participants" array and the conversation "length"
            def generateConversation(self, length = 3):
                conversationFragments = []
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
            def generateParticipant(self, type): 
                # Check to see if the participant already exists
                if type in self.participants: 
                    return self.participants[type]
                else
                    # TODO: Generate enough character for conversations
                    # Add to self.participants
        
        class ChatSegment: 
            
            # Constructor
            def __init__(self, name, label, participants):
                self.name = name
                self.label = label
                self.participants = participants
                self.told = False
                
    $conman = ConversationManager()
    $conman.AddSegment(ChatSegment("test1", "testchat1", ["enthusiastic", "skeptic"]))
    $conman.AddSegment(ChatSegment("test2", "testchat2", ["upset", "skeptic"]))
    $conman.AddSegment(ChatSegment("test3", "testchat3", ["enthusiastic", "skeptic", "bragger"]))
    $conman.AddSegment(ChatSegment("test4", "testchat4", ["bragger", "skeptic"]))
    $conman.AddSegment(ChatSegment("test5", "testchat5", ["enthusiastic", "upset"]))
    
label conversation:
    $testcon = conman.generateConversation()
    $tmpp = testcon["length"]
    "Length: [tmpp]"
    $names = testcon["conversation"][0].name + testcon["conversation"][1].name + testcon["conversation"][2].name
    $pants = testcon["participants"]
    "Names: [names]"
    "Pants: [pants]"
    
    # Cycle through all conversation segments
    while testcon["length"] > 0:
        # Asign character to participant
        $peopleMap = {}
        for part in testcon["participants"]:
            if playerComapnion.family == "Bloodrunner" and part = "Skeptic": 
                $peopleMap.update({part, playerCompanion})
            elif playerComapnion.family == "Coppertail" and part = "enthusiastic": 
                $peopleMap.update({part, playerCompanion})
            elif playerComapnion.family == "Daggermaw" and part = "bragger": 
                $peopleMap.update({part, playerCompanion})
            elif playerComapnion.family == "Gildclaw" and part = "upset":
                $peopleMap.update({part, playerCompanion})
            else: 
                $peopleMap.update({part, conman.generateParticipant(part)})
            
            # Create a map of all participant types. 
            # Check the player companion and slot them into a place in the map. 
            # Fill out the rest of the map with randomly chosen extras.
            # Pass the map to each conversation segment to pick out whoever they want to use. 
        
        # Call the conversation segment label
        call expression testcon["conversation"][0].label
        # Pop the segment from the conversation
        $testcon["conversation"].pop(0)
        # Reduce the count
        $testcon["length"] -= 1
        $tmpp = testcon["length"]
        "Length now: [tmpp]"
    return
        
label testchat1(enthusiastic = "e", skeptic = "s"): 
    "testchat1"
    enthusiastic "enthusiastic"
    skeptic "skeptic"
    "over"
    return
    
label testchat2(upset = "u", skeptic = "s"): 
    "testchat2"
    upset "upset"
    skeptic "skeptic"
    "over"
    return
    
label testchat3(enthusiastic = "e", skeptic = "s", bragger = "b"): 
    "testchat3"
    enthusiastic "enthusiastic"
    skeptic "skeptic"
    bragger "bragger"
    "over"
    return
    
label testchat4(bragger = "b", skeptic = "s"): 
    "testchat4"
    bragger "bragger"
    skeptic "skeptic"
    "over"
    return
    
label testchat5(enthusiastic = "e", upset = "u"): 
    "testchat5"
    enthusiastic "enthusiastic"
    upset "upset"
    "over"
    return
    