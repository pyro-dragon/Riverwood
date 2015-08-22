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
                self.used = False
                
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
                self.used = False
                
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
                self.used = False
                
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
                
                self.getFileData()
                
                self.AddSegment(ChatSegment("testchat1", ["enthusiastic", "skeptic"]))
                self.AddSegment(ChatSegment("testchat2", ["upset", "skeptic"]))
                self.AddSegment(ChatSegment("testchat3", ["enthusiastic", "skeptic", "bragger"]))
                self.AddSegment(ChatSegment("testchat4", ["bragger", "skeptic"]))
                self.AddSegment(ChatSegment("testchat5", ["enthusiastic", "upset"]))
                self.AddSegment(ChatSegment("testchat6", ["enthusiastic", "upset"]))
                
            ##
            # Get the file data and fill out the storage arrays
            def getFileData(self): 
                self.getNameData()
                self.getHeadshotData()
                
            ##
            # Get name data from files and return it as an array
            def getNameData(self):
                names = game.getFolderData("resources/names")
                
                for name in names:
                    self.AddName(Name(name["name"], name["family"], True if name["sex"] == "male" else False))
            
            ##
            # Get headshot data from files and return it
            def getHeadshotData(self): 
                headshots = game.getFolderData("resources/headshots")

                for headshot in headshots:
                    #say(None, "Name: " + headshot["image"] + "\nSex: " + headshot["sex"] + "\nFamily: " + headshot["family"])
                    #self.AddHeadshot(Headshot("characters/headshots/" + headshot["image"], headshot["sex"] == "male" else False, headshot["family"], headshot["roles"]))
                    self.AddHeadshot(Headshot("characters/headshots/" + headshot["image"], True if headshot["sex"] == "male" else False, headshot["family"], headshot["roles"]))
                
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
                tmpArr = filter(lambda item: item.used == False , self.headshots)
                
                # Check if we have the gender filter
                if male != None:
                    # Filter by gender
                    tmpArr = filter(lambda item: item.male == male , tmpArr)
                        
                # Check if we have a family filter
                if family != None: 
                    # Filter by family
                    tmpArr = filter(lambda item: item.family == family , tmpArr)
                            
                # Check if we have the role filter
                if role != None:
                    # Filter by role (filter each role list and only add headshots where at least one role matches
                    tmpArr = filter(lambda item: len(filter(lambda itemRole: itemRole == role , item.roles)) > 0 , tmpArr)
                
                # Check if there are any headshots
                if not tmpArr: 
                        
                    # There are no names left. 
                    return None
                else: 
                    # Get a random chat name
                    tmpHeadshot = tmpArr[renpy.random.randint(0, len(tmpArr) -1)]
                    
                    # Mark it as used
                    self.headshots[self.headshots.index(tmpHeadshot)].used = True
                    
                    # Return the name object
                    return tmpHeadshot
                
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
                tmpArr = filter(lambda item: item.used == False , self.names)
                
                # Check if we have the gender filter
                if male != None:
                    # Filter by gender
                    tmpArr = filter(lambda item: item.male == male , tmpArr)
                        
                # Check if we have a family filter
                if family != None: 
                    # Filter by family
                    tmpArr = filter(lambda item: item.family == family , tmpArr)
                         
                # Check if there are any names
                if not tmpArr: 
                        
                    # There are no names left. 
                    renpy.say(None, "No names matched!")
                    return None
                        
                else: 
                    # Get a random chat name
                    tmpName = tmpArr[renpy.random.randint(0, len(tmpArr) -1)]
                    
                    # Mark it as used
                    self.names[self.names.index(tmpName)].used = True
                    
                    return tmpName
                
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
                        tmpArr = filter(lambda item: item.used == False , self.chatSegments)
                        
                        tmpSeg = tmpArr[renpy.random.randint(0, len(tmpArr) - 1)]
                    
                        # Mark it as used
                        self.chatSegments[self.chatSegments.index(tmpSeg)].used = True
                        
                        # Return the segment
                        return tmpSeg
                else:
                    # Get the top priotity chat segment
                    tmpSeg = self.priorityChatSegments[0]
                    
                    # Remove the segment
                    self.priorityChatSegments.pop[0]
                    
                    # Return the segment
                    return tmpSeg