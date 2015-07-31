#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

init 1: 
    python: 
        class ConversationManager:
            
            # Constructor
            def __init__(self):
                self.segments = []
                self.segCount = 0
                
            # Add segment
            def AddSegment(self, segment):
                self.segments.append(segment)
                self.segCount += 1
                
            # Create a conversation
            def generateConversation(self, length = 3):
                conversationFragments = []
                for i in range(length):
                    index = renpy.random.randint(0, self.segCount-1)
                    conversationFragments.append(self.segments[index])
                    self.segments.pop(index)
                    
                # Get all the participants
                participants = []
                for i in range(length - 1):
                    for j in conversationFragments[i].participants:
                        participants.append(j)
                participants = set(participants)
                
                return {"conversation":conversationFragments, "participants": participants, "length": length}
        
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
    "Names: [names]"
    while testcon["length"] > 0:
    #for i in range(testcon.conversation.length):
        call expression testcon["conversation"][0].label
        #$testcon["conversation"][0].told = True
        $testcon["conversation"].pop(0)
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
    