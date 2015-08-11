#-------------------------------------------------------------------------------
# The screen for holding a conversation with your partner- based on Say screen
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
        
        #conversationTopics = [{"title": "starting", "label": "starting"}, {"title": "finishing", "label": "finishing"}]
        conversationTopic = ""

screen conversation(partner):
    
    # Display conversation topics
    window: 
        id "topics"
        
        vbox:
            xalign 1
            yalign 0
            for topic in playerCompanion.topics: 
                #text playerCompanion.topics[topic].label
                textbutton playerCompanion.topics[topic].title action [SetVariable("conversationTopic", playerCompanion.topics[topic].label), Jump("conversationWrapper")]
    
label conversationWrapper():
    call expression conversationTopic
    call screen conversation(playerCompanion)
    
label starting:
    "This conversation is starting"
    return
    
label finishing:
    "This conversation is finishing"
    return