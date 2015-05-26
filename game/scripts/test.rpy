label test:
    
    
    $callCount = 0
    
    call testB
    
    "Final call count: [callCount]"
    
    
    scene black with fade
    "Story time"
    
    return
    
label testA:
    "This is testA"
    call testB
    
    return
    
label testB:
    
    $callCount += 1
    
    menu: 
        "Call count: [callCount]":
            call testB
        "pass": 
            pass
    
    $callCount -= 1
    
    return
            
label tryAgain:
    "Try again"
    call testB
    
    return