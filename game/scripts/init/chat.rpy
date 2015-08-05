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
        
        # Headshot class for a supply of headshots to use
        class Headshot:
             def __init__(self, image, type, male):
                self.image = image
                self.type = type
                self.male = male
                
        # Names
        class Name:
            def __init__(self, name, family, male):
                self.name = name
                self.family = family
                self.male = male
                
        class ConversationManager:
            
            # Constructor
            def __init__(self):
                self.segments = []
                self.segCount = 0
                self.participants = {}
                self.headshots = []
                self.headshotCount = 0
                self.names = []
                self.nameCount = 0
                
                self.AddHeadshot(Headshot("headshots/angry1", "angry", True))
                self.AddHeadshot(Headshot("headshots/angry2", "angry", True))
                self.AddHeadshot(Headshot("headshots/angry3", "angry", False))
                self.AddHeadshot(Headshot("headshots/angry4", "angry", True))
                self.AddHeadshot(Headshot("headshots/angry5", "angry", True))
                
                self.AddHeadshot(Headshot("headshots/bragger1", "bragger", False))
                self.AddHeadshot(Headshot("headshots/bragger2", "bragger", True))
                self.AddHeadshot(Headshot("headshots/bragger3", "bragger", True))
                self.AddHeadshot(Headshot("headshots/bragger4", "bragger", False))
                self.AddHeadshot(Headshot("headshots/bragger5", "bragger", False))
                self.AddHeadshot(Headshot("headshots/bragger6", "bragger", False))
                self.AddHeadshot(Headshot("headshots/bragger7", "bragger", False))
                
                self.AddHeadshot(Headshot("headshots/enthusiastic1", "enthusiastic", True))
                self.AddHeadshot(Headshot("headshots/enthusiastic2", "enthusiastic", True))
                self.AddHeadshot(Headshot("headshots/enthusiastic3", "enthusiastic", False))
                self.AddHeadshot(Headshot("headshots/enthusiastic4", "enthusiastic", False))
                self.AddHeadshot(Headshot("headshots/enthusiastic5", "enthusiastic", True))
                
                self.AddHeadshot(Headshot("headshots/happy1", "happy", False))
                
                self.AddHeadshot(Headshot("headshots/skeptic1", "skeptic", True))
                self.AddHeadshot(Headshot("headshots/skeptic2", "skeptic", False))
                self.AddHeadshot(Headshot("headshots/skeptic3", "skeptic", True))
                self.AddHeadshot(Headshot("headshots/skeptic4", "skeptic", False))
                self.AddHeadshot(Headshot("headshots/skeptic5", "skeptic", False))
                self.AddHeadshot(Headshot("headshots/skeptic6", "skeptic", False))
                self.AddHeadshot(Headshot("headshots/skeptic7", "skeptic", True))
                self.AddHeadshot(Headshot("headshots/skeptic8", "skeptic", False))
                
                self.AddHeadshot(Headshot("headshots/upset1", "upset", True))
                self.AddHeadshot(Headshot("headshots/upset2", "upset", True))
                self.AddHeadshot(Headshot("headshots/upset3", "upset", True))
                self.AddHeadshot(Headshot("headshots/upset4", "upset", False))
                self.AddHeadshot(Headshot("headshots/upset5", "upset", False))
                self.AddHeadshot(Headshot("headshots/upset6", "upset", True))
                self.AddHeadshot(Headshot("headshots/upset7", "upset", True))
                self.AddHeadshot(Headshot("headshots/upset8", "upset", False))
                
                self.AddName(Name("Nightwind", "Bloodrunner", True))
                self.AddName(Name("Featherstorm", "Bloodrunner", True))
                self.AddName(Name("Moonrise", "Bloodrunner", True))
                self.AddName(Name("Summer", "Bloodrunner", False))
                self.AddName(Name("Rain", "Bloodrunner", False))
                self.AddName(Name("Flow", "Bloodrunner", False))
                
                self.AddName(Name("Cogward", "Coppertail", True))
                self.AddName(Name("Marcus", "Coppertail", True))
                self.AddName(Name("Edward", "Coppertail", True))
                self.AddName(Name("Wendy", "Coppertail", False))
                self.AddName(Name("Ermintrude", "Coppertail", False))
                self.AddName(Name("Casey", "Coppertail", False))
                
                self.AddName(Name("Hammer", "Daggermaw", True))
                self.AddName(Name("Slam", "Daggermaw", True))
                self.AddName(Name("Pusher", "Daggermaw", True))
                self.AddName(Name("Slicer", "Daggermaw", False))
                self.AddName(Name("Fracture", "Daggermaw", False))
                self.AddName(Name("Scar", "Daggermaw", False))
                
                self.AddName(Name("Meridian", "Gildclaw", True))
                self.AddName(Name("Ledger", "Gildclaw", True))
                self.AddName(Name("Grant", "Gildclaw", True))
                self.AddName(Name("Saphire", "Gildclaw", False))
                self.AddName(Name("Jade", "Gildclaw", False))
                self.AddName(Name("Ruby", "Gildclaw", False))
                
            def AddHeadshot(self, headshot):
                self.headshots.append(headshot)
                self.headshotCount += 1
                
            def AddName(self, name):
                self.names.append(name)
                self.nameCount += 1
                
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
                tmpPart = GameCharacter(name.name, "none", "none", Character("{image=pic.image}name.name", kind=nvl, window_background=Solid(colour)), pic.image, True, False, "")
                #tmpPart = {"name": name.name, "family": name.family, "thumbnail": pic.image, "male": name.male, "colour": colour}
                
                self.participants[type] = tmpPart
                
                return tmpPart
        
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
        python:
            for part in testcon["participants"]:
                if playerCompanion.family == "Bloodrunner" and part == "Skeptic": 
                    playerCompanion.c.kind = nvl
                    peopleMap.update({part: playerCompanion})
                elif playerCompanion.family == "Coppertail" and part == "enthusiastic": 
                    playerCompanion.c.kind = nvl
                    peopleMap.update({part: playerCompanion})
                elif playerCompanion.family == "Daggermaw" and part == "bragger": 
                    playerCompanion.c.kind = nvl
                    peopleMap.update({part: playerCompanion})
                elif playerCompanion.family == "Gildclaw" and part == "upset":
                    playerCompanion.c.kind = nvl
                    peopleMap.update({part: playerCompanion})
                else: 
                    peopleMap.update({part: conman.getParticipant(part)})
            
            # Create a map of all participant types. 
            # Check the player companion and slot them into a place in the map. 
            # Fill out the rest of the map with randomly chosen extras.
            # Pass the map to each conversation segment to pick out whoever they want to use. 
        
        # Call the conversation segment label
        call expression testcon["conversation"][0].label pass(participants=peopleMap)
        # Pop the segment from the conversation
        $testcon["conversation"].pop(0)
        # Reduce the count
        $testcon["length"] -= 1
        $tmpp = testcon["length"]
        "Length now: [tmpp]"
    return
        
label testchat1(participants): 
    "testchat1"
    participants["enthusiastic"].name "enthusiastic"
    participants["skeptic"].name "skeptic"
    "over"
    return
    
label testchat2(participants): 
    "testchat2"
    participants["upset"].name "upset"
    participants["skeptic"].name "skeptic"
    "over"
    return
    
label testchat3(participants): 
    "testchat3"
    participants["enthusiastic"].name "enthusiastic"
    participants["skeptic"].name "skeptic"
    participants["bragger"].name "bragger"
    "over"
    return
    
label testchat4(participants): 
    "testchat4"
    participants["bragger"].name "bragger"
    participants["skeptic"].name "skeptic"
    "over"
    return
    
label testchat5(participants): 
    "testchat5"
    participants["enthusiastic"].name "enthusiastic"
    participants["upset"].name "upset"
    "over"
    return
    