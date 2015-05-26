#-------------------------------------------------------------------------------
# This is where all the characters are defined.
#-------------------------------------------------------------------------------

# Put these skills somewhere
#---------------------------
# Archery (Dex)
# Close combat (Str)
# Shield usage (Str)
# Dodge (Dex)

# Silent movement (Dex)
# Exploring (Int)
# Tracking (Dex)
# Medicine (Int)

# Engineering (Int)
# Investigation (Int)
# Construction (Int)
# Firearms (Dex)

# Diplomacy (Cha)
# Negotiation (Cha)
# Presentation (Cha)
# Performance (Dex)

# Put these attributes somewhere
#-------------------------------
# Strength
# Dexterity
# Charisma
# Inteligence

init: 
    python: 
        #---------------------------#
        # The character preferences #
        #---------------------------#
        class CharacterPreference:
            # Constructor
            def __init__(self, name, love, reaction):
                self.name = name
                self.love = love
                self.reaction = reaction
        
        #--------------------------#
        # The game character class #
        #--------------------------#
        class GameCharacter: 
            # Skill links - What skills depend on what attributes
            skillIndex = {
                "archery" : "dex", 
                "hand weapon" : "str", 
                "shield" : "str", 
                "dodge" : "dex", 
                "silent movement" : "dex", 
                "exploring" : "int", 
                "tracking" : "dex", 
                "medicine" : "int", 
                "engineering" : "int", 
                "investigation" : "int", 
                "construction" : "int", 
                "firearms" : "dex", 
                "diplomacy" : "cha", 
                "negotiation" : "cha", 
                "presentation" : "cha", 
                "performance" : "dex"
            }
            
            # Constructor
            def __init__(self, name, family, career, renpyCharacter, imageName, met, hideName, thumbnail):
                self.family = family            # The character family
                self.career = career            # The character career
                self.c = renpyCharacter         # The renpy character representation
                self.image = imageName          # The chracter image given by file name
                self.met = met                  # If the character has been met or not
                self.preferences = {}           # A list of character preferences
                self.rp = 35                    # Relationship points
                self.thumbnail = "characters/thumbnails/" + thumbnail
                
                # If the character name needs to be obscured
                self.trueName = name
                if(hideName):
                    self.name = "?????"
                else: 
                    self.name = name

                # Set attributes
                self.attr = {
                    "str" : 5,
                    "dex" : 5, 
                    "cha" : 5, 
                    "int" : 5
                }
                
                # Set skill bonuses
                self.skillBonus = {
                    "archery" : 0, 
                    "hand weapon" : 0, 
                    "shield" : 0, 
                    "dodge" : 0, 
                    "silent movement" : 0, 
                    "exploring" : 0, 
                    "tracking" : 0, 
                    "medicine" : 0, 
                    "engineering" : 0, 
                    "investigation" : 0, 
                    "construction" : 0, 
                    "firearms" : 0, 
                    "diplomacy" : 0, 
                    "negotiation" : 0, 
                    "presentation" : 0, 
                    "performance" : 0
                }
                
            def getCareer(self):
                return self.career
                    
            # Reveal the character name
            def showName(self):
                self.name = self.trueName
   
            # Return the total skill result
            # Skill bonus + attribute
            def getSkillTotal(self, skill): 
                return self.skillBonus[skill] + self.attr[self.skillIndex[skill]]
            
            # Add to the skill bonus
            def changeSkillBonus(self, skill, change): 
                if self.skillBonus.has_key(skill): 
                    self.skillBonus[skill] += change
                    renpy.show_screen("skillShowBox", skill, change)
                    
            # Add to the attributes
            def changeAttr(self, attr, change):
                if self.attr.has_key(attr):
                    self.attr[attr] += change
                    renpy.show_screen("skillShowBox", attr, change)
                    
            # Test against a skill
            def skillTest(self, skill, goal, bonus = 0):
                total = bonus + self.getSkillTotal(skill)       # Get the total to check the skill against
                roll = renpy.random.randint(1, 20)              # Roll the dice
                
                # Test against the dice
                result = False
                if(roll < total):
                    result = True         # Pass!
                
                    renpy.show_screen("challenegeShowBox", skill, result)

            # Add a preference
            def addPreference(self, preference):
                self.preferences.update({preference.name : preference})
                
            # Check to see if the preference is loved
            def loves(self, preference): 
                if self.preferences.has_key(preference):
                    return self.preferences[preference].love
                else:
                    return False
                    
            # Check to see if the preference is hated
            def hates(self, preference): 
                if self.preferences.has_key(preference):
                    return not self.preferences[preference].love
                else:
                    return False

            # Add relationship points
            def addRp(self, points): 
                self.rp += points
                renpy.show_screen("skillShowBox", self.name + " relationship", points)

            def getRpStatement(self):
                if(self.rp <= 0):               # Zero or less
                    return "Sworn Enemy"
                elif (self.rp <= 10): 
                    return "Hated"
                elif (self.rp <= 20): 
                    return "Annoyed"
                elif (self.rp <= 30): 
                    return "Tolerated"
                elif (self.rp <= 40): 
                    return "Acquaintance"
                elif (self.rp <= 50): 
                    return "Friend"
                elif (self.rp <= 60): 
                    return "Good Friend"
                elif (self.rp <= 70): 
                    return "Trusted Friend"
                elif (self.rp <= 80): 
                    return "Best Friend"
                elif (self.rp <= 90): 
                    return "Crush"
                elif (self.rp > 90):            # 90% or more
                    return "Lover"