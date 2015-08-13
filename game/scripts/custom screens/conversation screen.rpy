#-------------------------------------------------------------------------------
# The screen for holding a conversation with your partner- based on Say screen
#-------------------------------------------------------------------------------
screen conversation(partner):
    
    # Display conversation topics
    window: 
        id "topics"
        
        vbox:
            xalign 1
            yalign 0
            for topic in playerCompanion.topics: 
                #text playerCompanion.topics[topic].label
                if playerCompanion.topics[topic].hidden == False:
                    textbutton playerCompanion.topics[topic].title action [SetVariable("conversationTopic", playerCompanion.topics[topic]), Jump("conversationWrapper")]
    
