#-------------------------------------------------------------------------------
# This is where the chat components are loaded in. Use XML if needed
#-------------------------------------------------------------------------------

init 1: 
    python: 
        
        ##
        # Headshot class for a supply of headshots to use
        class Headshot:
            
            ##
            # Constructor
            # @param image (string) A path to the headshot image
            # @param male (boolean) If the subject is male or not
            # @param family (string) The family the headshot belongs to
            # @param roles (array)(string) An array of strings that describe the roles thi subject can fill
             def __init__(self, image, male, family, roles):
                self.image = image
                self.male = male
                self.family = family
                self.roles = roles
                
        ##
        # Name class for possible names for chat characters
        class Name:
            
            ##
            # Constructor
            # @param name (string) The name. This is a first name
            # @param family (string) The typ of name. Choose from Bloodrunner, Coppertail, Daggermaw and Gildclaw
            # @param male (boolean) If te name is for a male or not
            def __init__(self, name, family, male):
                self.name = name
                self.family = family
                self.male = male
                
        ##
        # Chat segment class
        class ChatSegment:
            
            ##
            # Constructor
            # @param label (string) The label for the chat segment
            # @param roles (array) And array of strings for the roles that participate in this chat segment
            def __init__(self, label, roles):
                self.label = label
                self.roles = roles
                
        ##
        # The chat resouce manager
        class ChatResourceManager:
            
            ##
            # Constructor
            # Add all the resources. Read from XML in future
            def __init__(self):
                self.headshots = []
                self.names = []
                self.chatSegments = []          # Standard chat segments
                self.priorityChatSegments = []  # Special segments that should be discussed first
                
                self.AddHeadshot(Headshot("characters/headshots/angry1.png", True, "Bloodrunner", ["angry"]))
                self.AddHeadshot(Headshot("characters/headshots/angry2.png", True, "Coppertail", ["angry"]))
                self.AddHeadshot(Headshot("characters/headshots/angry3.png", False, "Daggermaw", ["angry"]))
                self.AddHeadshot(Headshot("characters/headshots/angry4.png", True, "Gildclaw", ["angry"]))
                self.AddHeadshot(Headshot("characters/headshots/angry5.png", True, "Bloodrunner", ["angry"]))
                
                self.AddHeadshot(Headshot("characters/headshots/bragger1.png", False, "Bloodrunner", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger2.png", True, "Coppertail", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger3.png", True, "Daggermaw", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger4.png", False, "Gildclaw", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger5.png", False, "Bloodrunner", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger6.png", False, "Coppertail", ["bragger"]))
                self.AddHeadshot(Headshot("characters/headshots/bragger7.png", False, "Daggermaw", ["bragger"]))
                
                self.AddHeadshot(Headshot("characters/headshots/enthusiastic1.png", True, "Bloodrunner", ["enthusiastic"]))
                self.AddHeadshot(Headshot("characters/headshots/enthusiastic2.png", True, "Coppertail", ["enthusiastic"]))
                self.AddHeadshot(Headshot("characters/headshots/enthusiastic3.png", False, "Daggermaw", ["enthusiastic"]))
                self.AddHeadshot(Headshot("characters/headshots/enthusiastic4.png", False, "Gildclaw", ["enthusiastic"]))
                self.AddHeadshot(Headshot("characters/headshots/enthusiastic5.png", True, "Bloodrunner", ["enthusiastic"]))
                
                self.AddHeadshot(Headshot("characters/headshots/happy1.png",False, "Bloodrunner", ["happy"]))
                
                self.AddHeadshot(Headshot("characters/headshots/skeptic1.png", True, "Bloodrunner", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic2.png", False, "Coppertail", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic3.png", True, "Daggermaw", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic4.png", False, "Gildclaw", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic5.png", False, "Bloodrunner", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic6.png", False, "Coppertail", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic7.png", True, "Daggermaw", ["skeptic"]))
                self.AddHeadshot(Headshot("characters/headshots/skeptic8.png", False, "Gildclaw", ["skeptic"]))
                
                self.AddHeadshot(Headshot("characters/headshots/upset1.png", True, "Bloodrunner", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset2.png", True, "Coppertail", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset3.png", True, "Daggermaw", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset4.png", False, "Gildclaw", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset5.png", False, "Bloodrunner", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset6.png", True, "Coppertail", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset7.png", True, "Daggermaw", ["upset"]))
                self.AddHeadshot(Headshot("characters/headshots/upset8.png", False, "Gildclaw", ["upset"]))
                
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
                
                self.AddSegment(ChatSegment("testchat1", ["enthusiastic", "skeptic"]))
                self.AddSegment(ChatSegment("testchat2", ["upset", "skeptic"]))
                self.AddSegment(ChatSegment("testchat3", ["enthusiastic", "skeptic", "bragger"]))
                self.AddSegment(ChatSegment("testchat4", ["bragger", "skeptic"]))
                self.AddSegment(ChatSegment("testchat5", ["enthusiastic", "upset"]))
                
            ##
            # Add a headshot to the resource manager
            # @param headshot (object) The headshot object to add
            def AddHeadshot(self, headshot):
                self.headshots.append(headshot)
                
            ##
            # Get a random headshot
            # @param male (boolean) If the headshot should be male or not
            # @param role (string) A role that the headshot can play
            # @param family (string) The headshot family
            def GetRandomHeadshot(self, male=None, role=None, family=None):
                
                # Create a temporary array
                tmpArr = self.headshots
                
                # Check if we have the gender filter
                if male:
                    # Cycle through the temp array and remove those that don't match
                    for i in tmpArr:
                        if i.male != male:
                            tmpArr.pop(i)
                            
                # Check if we have the role filter
                if role != None:
                    # Cycle through the temp array
                    for i in tmpArr:
                        
                        # Cycle through the headshot roles
                        for j in i.roles:
                            matched = False
                            # Compare and check for matches
                            if j == role:
                                matched = True
                        
                        # Check if there was any matches
                        if matched == False:
                            # No matches, get rid of this headshot
                            tmpArr.remove(i)
                        
                # Check if we have a family filter
                if family != None: 
                    # Cycle through the temp array and remove those that don't match
                    for i in tmpArr: 
                        if i.family != family:
                            tmpArr.remove(i)
                         
                # Check if there are any names
                if not tmpArr: 
                        
                    # There are no names left. 
                    return None
                else: 
                    # Get a random chat name
                    return tmpArr[renpy.random.randint(0, len(tmpArr) -1)]
                
            ##
            # Add a name to the resource manager
            # @param name (object) The name object to add
            def AddName(self, name):
                self.names.append(name)
                
            ##
            # Get a random name
            # @param male (boolean) Filter the selection by gender
            # @param family (string) Filter the selection by family
            def GetRandomName(self, male=None, family=None):
                
                # Create a temporary array
                tmpArr = self.names
                
                # Check if we have the gender filter
                if male != None:
                    #return "male"
                    # Cycle through the temp array and remove those that don't match
                    for i in tmpArr:
                        if i.male != male:
                            tmpArr.remove(i)
                        
                # Check if we have a family filter
                if family != None: 
                    return "family"
                    # Cycle through the temp array and remove those that don't match
                    for i in tmpArr: 
                        if i.family != family:
                            tmpArr.remove(i)
                         
                # Check if there are any names
                if not tmpArr: 
                        
                    # There are no names left. 
                    return None
                        
                else: 
                    # Get a random chat name
                    return tmpArr[renpy.random.randint(0, len(tmpArr) -1)]
                
            ##
            # Add a chat segment
            # @param segment (object) The chat object to add
            # @param priority (boolean) Defauly = False If the chat segment needs to be added to the priority queue or not
            def AddSegment(self, segment, priority = False):
                if priority == True: 
                    self.priorityChatSegments.append(segment)
                else: 
                    self.chatSegments.append(segment)
                    
            ##
            # Get a random chat segment
            def GetRandomSegment(self): 
                
                # Check if there is anything in the priority list
                if not self.priorityChatSegments:
                    
                    # List is empty. Check if there is any in the regulat list
                    if not self.chatSegments: 
                        
                        # There are no segments left. 
                        return None
                        
                    else: 
                        # Get a random chat segment
                        return self.chatSegments[renpy.random.randint(0, len(self.chatSegments) - 1)]
                        
                else:
                    # Get the top priotity chat segment
                    return self.priorityChatSegments[0]