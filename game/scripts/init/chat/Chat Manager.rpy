#-------------------------------------------------------------------------------
# This defines missions which are the individual units of story
#-------------------------------------------------------------------------------

# Participant types
# Enthusiastic
# Skeptic
# Upset
# Bragger

init 2: 
    python: 
        class ChatManager:
            
            # Constructor
            def __init__(self):
                self.recMan = ChatResourceManager()
                self.partMan = ParticipantManager(self.recMan)
                
            # Create a chat
            # Return a map containing the "chat" array, the "participants" array and the conversation "length"
            def generateChat(self, length = 3):
                chatSegments = []
                for i in range(length):
                    # Append the segment to the fragment array
                    chatSegments.append(self.recMan.GetRandomSegment())
                    
                # Get all the roles
                roles = []
                for i in chatSegments: 
                    for j in i.roles:
                        roles.append(j)
                # Convert to a set (to eliminate duplicates)
                roles = set(roles)
                
                return {"chatSegments":chatSegments, "roles": roles}
                
    $chatMan = ChatManager()
    
label chat:
    $game.setLocation(camp)
    
    $testcon = chatMan.generateChat()
    #$tmpp = testcon["length"]
    #"Length: [tmpp]"
    #$names = testcon["chatSegments"][0].label
    #$names = testcon["chatSegments"][0].label + testcon["chatSegments"][1].label + testcon["chatSegments"][2].label
    #$roles = testcon["roles"]
    #"Names: [names]"
    #"Roles: [roles]"
    
    # Cycle through all chat segments
    
    #for segment in testcon["chatSegments"]:
    #while testcon["chatSegments"]:
    python:
            # Asign character to participant
        peopleMap = {}
        for role in testcon["roles"]:
            if playerCompanion.family == "Bloodrunner" and role == "Skeptic" : 
                peopleMap.update({role: chatMan.partMan.getParticipant(role)})
            elif playerCompanion.family == "Coppertail" and role == "enthusiastic":
                peopleMap.update({role: chatMan.partMan.getParticipant(role)})
            elif playerCompanion.family == "Daggermaw" and role == "bragger": 
                peopleMap.update({role: chatMan.partMan.getParticipant(role)})
            elif playerCompanion.family == "Gildclaw" and role == "upset":
                peopleMap.update({role: chatMan.partMan.getParticipant(role)})
            else: 
                peopleMap.update({role: chatMan.partMan.getParticipant(role)})
        
    while testcon["chatSegments"]:
        # Call the conversation segment label
        call expression testcon["chatSegments"][0].label pass(participants=peopleMap)
        # Pop the used segment from the list
        $testcon["chatSegments"].pop(0)
        
    nvl clear
    
    return