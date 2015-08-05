image X = "characters/headshots/skeptic1.png"
image Y = "characters/headshots/skeptic2.png"
image Z = "characters/headshots/skeptic3.png"

define X = Character('{image=X}Rex', kind=nvl, window_background=Solid("#f00"), window_xfill=True)
define Y = Character('{image=Y}Trish', kind=nvl, window_background=Solid("#0f0"), window_xfill=True)
define Z = Character('{image=Z}Alex', kind=nvl, window_background=Solid("#00f"), window_xfill=True)

label test:
    $crt_mechanic.met = True
    $playerCompanion = crt_mechanic
    call conversation
    "Hi"
    X "You've created a new Ren'Py game."
    Y "You've created a new Ren'Py game."

    X "Once you add a story, pictures, and music, you can release it to the world!"
    Y "Once you add a story, pictures, and music, you can release it to the world!"
    
    X "You've created a new Ren'Py game."
    Y "You've created a new Ren'Py game."

    Z "hey!"

    X "Once you add a story, pictures, and music, you can release it to the world!"
    Y "Once you add a story, pictures, and music, you can release it to the world!"
    
    Z "ho!"
    
    X "You've created a new Ren'Py game."
    Y "You've created a new Ren'Py game."

    X "Once you add a story, pictures, and music, you can release it to the world!"
    Y "Once you add a story, pictures, and music, you can release it to the world!"
    
    X "You've created a new Ren'Py game."
    Y "You've created a new Ren'Py game."

    X "Once you add a story, pictures, and music, you can release it to the world!"
    Y "Once you add a story, pictures, and music, you can release it to the world!"
    return
    
    #call screen chapter(title="Chapter 1", subtitle="The revenge of jetty")
    $crt_trader.met = True
    $crt_mechanic.met = True
    $crt_fighter.met = True
    $crt_hunter.met = True
    $playerCompanion = crt_mechanic
    #call screen activity()
    #call conversation