#-------------------------------------------------------------------------------
# The screen for holding a conversation with your partner- based on Say screen
#-------------------------------------------------------------------------------
init: 
    python:
        conversationTopics = [{"title": "starting", "label": "starting"}, {"title": "finishing", "label": "finishing"}]

screen conversation(partner):
    modal True
    
    # Display conversation topics
    window: 
        id "topics"
        
        vbox:
            xalign 1
            yalign 0
            for topic in conversationTopics: 
                textbutton topic["title"] action Show(say(partner.name, topic["label"]))

screen speak(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    # Use the quick menu.
    use quick_menu
    
label starting:
    "This conversation is starting"
    
label finishing:
    "This conversation is finishing"