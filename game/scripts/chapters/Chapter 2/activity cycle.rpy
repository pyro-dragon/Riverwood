#-------------------------------------------------------------------------------
# This is the main activity selection and execution cycle. Player chooses their 
# activity for that day. Note: If they do with with someone else they may get a 
# bonus based on the companions skills. They also gain relationship points.
#-------------------------------------------------------------------------------

#-----------------------------
# The root of the activity
# cycle system.
#-----------------------------
label activityCycle:  
    if playerCompanion == "none": 
        P "Hmm, what should I do?"
    else: 
        P "Hmm, what should we do?"
        
    menu: 
        "Explore the surrounding area": 
            call explore
        "Practice [player.career.name] skills": 
            call practice
        #"Hang out with the other young [player.family]s": 
        #    call socialise
        #"Spend time with [playerCompanion.name]" if (playerCompanion != "none"): 
        #    call hangOut
        #"Spend time with someone else" if (peopleKnown > 1):
        #    call seeSomeoneElse
        
    return

#-----------------------------
# Do the exploration catagory.
# The outcomes of this are 
# dependant on the players
# current location and their
# and their partners explore
# skill
#-----------------------------
label explore: 
    # Check if we are at the edge of the territory (there is nothing more to explore from here)
    # Return to activity menu if there is nothing to do
    if len(discoverableAreas) <= 0: 
        #"There is nothing left to explore"
        jump activityCycle
            
    if playerCompanion != "none":
        P "Lets go for a walk. We can explore the surrounding area!"
    else: 
        P "I'll go for a bit of an explore"
    
    if playerCompanion != "none": 
        if playerCompanion.loves("exploring"):
            $playerCompanion.c(playerCompanion.preferences["exploring"].reaction)
            $playerCompanion.addRp(3)
        elif playerCompanion.hates("exploring"):
            $playerCompanion.c(playerCompanion.preferences["exploring"].reaction)
            $playerCompanion.addRp(-3)
            
    # Roll dice and get score
    $score = renpy.random.randint(1, 100) + player.getSkill("exploring")
        
    # Compare score against remaining places to explore
    # Grab a random place
    $place = discoverableAreas[renpy.random.randint(0, len(discoverableAreas) - 1)]
            
    # If there are still unexplored places and the score is higher than the easiest hidden space then reveal a space
    if score > place.discoveryScore:
        # Make place visitable
        $place.discover()
        "You have found the [place.name]!"
            
        # Give big skill reward
        $player.skillBonus["exploring"] += 3
            
        # Gain RP award
        $playerCompanion.addRp(3)
            
        # Remove place from list
        $discoverableAreas.remove(place)
            
        python: 
            # Check if the place has any matching keywords- if so, add even more rp
            for word in place.keyWords: 
                if playerCompanion != "none" and playerCompanion.loves(word): 
                    playerCompanion.c(word + " : " + playerCompanion.preferences[word].reaction)
                    playerCompanion.addRp(1)
                    break
    else:
        "You have failed to find anywhere interesting"
        # Give small skill reward
        $player.skillBonus["exploring"] += 1
            
    return
    
label practice: 
    if playerCompanion != "none":
        "You spend some time practicing your [player.career.name] skills with [playerCompanion.name]."
        
        # Boosts for primary skills
        
        "..."
        # Get randomised skill boost
        $boostScore = renpy.random.randint(3, 6)
        $smallBoost = boostScore/3              # Small boost is 1/3rd of the boost
        $bigBoost = boostScore - smallBoost     # Big boost is the remaining 2/3rds of the boost
        "... ..."
        
        #See who has the highest primary skill
        if player.skillBonus[player.career.primarySkill] > playerCompanion.skillBonus[playerCompanion.career.primarySkill]:
            # Player has the highet primary skill
            $player.skillBonus[player.career.primarySkill] += bigBoost
            $playerCompanion.skillBonus[playerCompanion.career.primarySkill] += smallBoost
            "You get a boost of [bigBoost] to your [player.career.primarySkill] skill!"
        else:
            # Companion has the highest primary skill
            $player.skillBonus[player.career.primarySkill] += smallBoost
            $playerCompanion.skillBonus[playerCompanion.career.primarySkill] += bigBoost
            "You get a boost of [smallBoost] to your [player.career.primarySkill] skill."



        # Boosts for secondary skills

        "..."
        # Get randomised skill boost
        $boostScore = renpy.random.randint(3, 6)
        $smallBoost = boostScore/3              # Small boost is 1/3rd of the boost
        $bigBoost = boostScore - smallBoost     # Big boost is the remaining 2/3rds of the boost
        "... ..."
        
        #See who has the highest secondary skill
        if player.skillBonus[player.career.secondarySkill] > playerCompanion.skillBonus[playerCompanion.career.secondarySkill]:
            # Player has the highet secondary skill
            $player.skillBonus[player.career.secondarySkill] += bigBoost
            $playerCompanion.skillBonus[playerCompanion.career.secondarySkill] += smallBoost
            "You get a Sboost of [bigBoost] to your [player.career.secondarySkill] skill!"
        else:
            # Companion has the highest secondary skill
            $player.skillBonus[player.career.secondarySkill] += smallBoost
            $playerCompanion.skillBonus[playerCompanion.career.secondarySkill] += bigBoost
            "You get a boost of [smallBoost] to your [player.career.secondarySkill] skill."

        # Companion reaction
        python: 
            for word in player.career.keywords: 
                if playerCompanion.loves(word): 
                    playerCompanion.c(playerCompanion.preferences[word].reaction)
                    playerCompanion.addRp(1)
                    break
                elif playerCompanion.hates(word): 
                    playerCompanion.c(playerCompanion.preferences[word].reaction)
                    playerCompanion.addRp(-1)
                    break
        
    else:
        "You spend some time on your own, honing your [player.career.name] skills."
        
        # Gain a reasonable skill bonus
        $boost = renpy.random.randint(1, 2)
        $player.skillBonus[player.career.primarySkill] += boost
        "You get a boost of [boost] to your [player.career.primarySkill] skill."
        $boost = renpy.random.randint(1, 2)
        $player.skillBonus[player.career.secondarySkill] += boost
        "You get a boost of [boost] to your [player.career.secondarySkill] skill."
        
    # Go back to plot
    return
    
label socialise: 
    "Unavailable"
    # Gain a bonus to social skills
    # Chance to learn a rumour or random info about random person.
    # Random chance at meeting a new datable
    
    # Go back to plot
    return
    
label hangOut: 
    "Unavailable"
    # Have a small conversation to learn more about them
    # Make some choices to gain/lose favour.
    
    # Go back to plot
    return
    
label seeSomeoneElse: 
    P "Who should I see?"
    menu: 
        "[ally.name]":
            pass
        "[rival.name]":
            pass
        "[hunter.name]" if hunter.met == True:
            pass
        "[mechanic.name]" if mechanic.met == True:
            pass
        "[fighter.name]" if fighter.met == True:
            pass
        "[trader.name]" if trader.met == True:
            pass
        
    # Menu of all known contacts
    # Lose relationship points for ditching a partner if you currently have one. 
    # Check if character is available
    # Offer activity list