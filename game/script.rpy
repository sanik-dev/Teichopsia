# Initializing the name variable
default mc_name = "Kayo"

# Initializing counter for Imagemaps
default window_active = False
default c_vent = 0


# Todo: Load character assets and audio you dummy :3
label start:

    #------------------------------Prologue------------------------------#

    # Setup
    $ Kayo = Character(mc_name, color="#c8ffc8")
    scene dark # First of bg transition; fade in from black
    with fade

    # Description and internal thoughts
    "An ache creeping over my whole body was the first and only sensation I could feel."
    "There was no sound, no light, nothing at all."

    scene dark_expanse_blur # Second of bg transition; blured haloing
    with fade

    # Kayo speaks
    Kayo "Wh…Where am I?"
    scene dark_expanse # Third of bg transition; fade in from blur
    with dissolve

    # More internal thoughts and actions
    "My voice could barely croak out even those words, like sandpaper against skin."
    "This is just like waking from a six hour nap, head fuzzy, confused, and I really need some water."
    scene dark_locker # Fourth of bg transition; fade into locker
    with dissolve

    "In fact, I have no idea how I got here at all."
    "The last thing I remember is going to class, but even that feels like an eternity ago."
    "Maybe I should find a way out of here first."

    window hide
    jump locker

    #------------------------------Locker Escape Scene------------------------------# 

    # Background and Imagemaps assigned to the locker scene
    screen dark_locker:
        imagemap:
            ground "dark_locker.jpg" 
            hotspot (731, 0, 491, 210) action Jump("vent") sensitive not window_active

    label locker:
        show screen dark_locker
        $ renpy.pause()
        return
    
    label vent:
        # Restrict textbox to imagemap counter limit
        if c_vent < 2:
            # show the dialogue box again
            $ window_active = True
            window show

            # vent clicked counter
            $ c_vent += 1

            if c_vent == 1:
                "There are three long thin holes, but its too dark outside to see anything."
            elif c_vent == 2:
                "I might not be able to see anything, but I can certainly smell a concerning amount of chemicals in the air."
                "If its this strong inside this locker what is it even like outside?"

            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True)

            jump locker
