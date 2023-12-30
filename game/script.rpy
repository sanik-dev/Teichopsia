# Initializing the name variable
default mc_name = "Kayo"

# Initializing counter for Imagemaps
default window_active = False
default c_vent = 0
default c_knees = 0
default c_door = 0
default c_broom = 0
default c_books = 0
default books_picked_up = 0
default c_notes = 0

# Initialising Switches
default touched_door = False

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
            ground "dark_locker.png" 
            hotspot (731, 0, 491, 210) action Jump("vent") sensitive not window_active
            hotspot (642, 670, 646, 363) action Jump('knees') sensitive not window_active
            hotspot (618, 245, 686, 221) action Jump('door') sensitive not window_active
            hotspot (413, 123, 145, 619) action Jump ('broom') sensitive not window_active
            hotspot (1288, 747, 336, 327) action Jump ('books') sensitive not window_active
            hotspot (32, 12, 382, 799) action Jump ('notes') sensitive not window_active
            
    label locker:
        show screen dark_locker
        $ renpy.pause()
        return
    
    #---------------------Door Decision Tree---------------------#
    label door:
        if c_door == 0:
            # show the dialogue box again
            $ window_active = True
            window show

            "The door is locked, but I can't see a keyhole anywhere."
            "Pushing on it reveals a small gap in the bottom right corner, but it's too dark to see anything through it."

            # door clicked counter
            $ c_door += 1
            # door has been touched check
            $ touched_door = True
            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True)

            jump locker

    #---------------------Broom Decision Tree---------------------#
    label broom:
        if c_broom < 2:
            # show the dialogue box again
            $ window_active = True
            window show

            # broom clicked counter
            $ c_broom += 1

            if touched_door == True:
                "It’s jabbing my leg a bit, I think it’s a broom or something."
                "It’s pressing against the door slightly, maybe I could pry the door open..."
                menu:
                    "Should i try to open it with the broom?"

                    "Yes":
                        "I wedge the length of the broom into the gap and pull with all of my remaining strength."
                        "The door creaks open, and I can see a sliver of light from the outside."
                    "No":
                        "Maybe i'll try something else."
            else:
                "It’s jabbing my leg a bit, I think it’s a broom or something."
                "I'd use it to shove the door open, but I think my legs would do a far better job."

        window hide

        # Delay to avoid double clicks
        $ window_active = False
        $ renpy.pause(0.5, hard=True)

        jump locker

    #---------------------Vent Decision Tree---------------------#
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
    
    #---------------------Knees Decision Tree---------------------#
    label knees:
        if c_knees == 0:
            # show the dialogue box again
            $ window_active = True

            "No wonder my legs hurt so much."
            "That's definitely a bruise... Probably a scrape too. I should disinfect that, huh..."

            # knee clicked counter
            $ c_knees += 1

            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True)
        
            jump locker

    #---------------------Books Decision Tree---------------------#
    label books:
        if c_books < 3:
            # show the dialogue box again
            $ window_active = True
            window show

            # books clicked counter
            $ c_books += 1

            if touched_door == True:
                if c_books == 1:
                    "It's already cramped in here, these books aren't helping at all."
                    "The books all vary in size, maybe one could wedge the door ajar?"
                elif c_books == 2:
                    "I can't read any of these, but I can feel the pages are all stuck together."
                elif c_books == 3:
                    "I can't read any of these, but I can feel the pages are all stuck together."
                    "I think I can make out a few words though, something about a 'chemical spill'?"
            else:
                "It's already cramped in here, these books aren't helping at all."
                "This locker clearly wasn't made to fit someone my size..."

            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True)

            jump locker

    #---------------------Notes Decision Tree---------------------#
    label notes:
        if c_notes < 4:
            # show the dialogue box again
            $ window_active = True
            window show

            # notes clicked counter
            $ c_notes += 1

            if c_notes == 1:
                "This must be a little reminder note, I can’t read it at all."
                "Maybe the writer will come back soon?"

                menu:
                    "What should I do with the note?"

                    "Take it":
                        "I decided to take the note with me."
                        # Add note1 to inventory or note1 = True
                    "Leave it":
                        "Better not mess with fate"

            elif c_notes == 2:
                "There sure are a lot of these, maybe the writer is the forgetful type."

                menu:
                    "What should i do with this note?"

                    "Take it":
                        "I decided to take the note with me."
                        # Add note2 to inventory or note2 = True
                    "Leave it":
                        "Better not mess with fate"

            elif c_notes == 3:
                "This one appears to have more words than the others, not like i can read it anyway"

                menu:
                    "What about this one?"

                    "Take it":
                        "I decided to take the note with me."
                        # Add note3 to inventory or note3 = True
                    "Leave it":
                        "Better not mess with fate"

            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True)

            jump locker

        else:

            jump locker
            window hide

            # Delay to avoid double clicks
            $ window_active = False
            $ renpy.pause(0.5, hard=True) 






    


        