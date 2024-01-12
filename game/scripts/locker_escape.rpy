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
        $ window_active = True
        window show

        "The door is locked, but I can't see a keyhole anywhere."
        "Pushing on it reveals a small gap in the bottom right corner, but it's too dark to see anything through it."

        $ c_door += 1
        $ touched_door = True
        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)

        jump locker
    else:
        jump locker
#---------------------Broom Decision Tree---------------------#
label broom:
    if c_broom < 2:
        $ window_active = True
        window show

        $ c_broom += 1

        "It’s jabbing my leg a bit, I think it’s a broom or something."

        if touched_door:
            "It’s pressing against the door slightly, maybe I could pry the door open..."
            menu:
                "Should I try to open it with the broom?"

                "Yes":
                    "I wedge the length of the broom into the gap and pull with all of my remaining strength."
                    "The door creaks open, and I can see a sliver of light from the outside."
                "No":
                    "Maybe I'll try something else."
        else:
            "I'd use it to shove the door open, but I think my legs would do a far better job."

        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)

    jump locker
#---------------------Vent Decision Tree---------------------#
label vent:
    if c_vent < 2:
        $ c_vent += 1

        $ window_active = True
        window show

        if c_vent == 1:
            "There are three long thin holes, but it's too dark outside to see anything."
        elif c_vent == 2:
            "I might not be able to see anything, but I can certainly smell a concerning amount of chemicals in the air."
            "If it's this strong inside this locker, what is it even like outside?"

        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)

    jump locker
#---------------------Knees Decision Tree---------------------#
label knees:
    "No wonder my legs hurt so much."
    "That's definitely a bruise... Probably a scrape too. I should disinfect that, huh..."

    $ c_knees += 1

    $ renpy.pause(0.5, hard=True)

    jump locker
#---------------------Books Decision Tree---------------------#
label books:
    if c_books < 3:
        $ c_books += 1

        $ window_active = True
        window show

        "It's already cramped in here, these books aren't helping at all."

        if touched_door:
            if c_books == 1:
                "The books all vary in size, maybe one could wedge the door ajar?"
            elif c_books == 2:
                "I can't read any of these, but I can feel the pages are all stuck together."
            else:
                "I can't read any of these, but I can feel the pages are all stuck together."
                "I think I can make out a few words though, something about a 'chemical spill'?"
        else:
            "This locker clearly wasn't made to fit someone my size..."

        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)

        jump locker
#---------------------Notes Decision Tree---------------------#
label notes:
    if c_notes < 4:
        $ c_notes += 1

        $ window_active = True
        window show

        if c_notes == 1:
            "This must be a little reminder note, I can’t read it at all."
            "Maybe the writer will come back soon?"
        elif c_notes == 2:
            "There sure are a lot of these, maybe the writer is the forgetful type."
        else:
            "This one appears to have more words than the others, not like I can read it anyway."

        menu:
            "What should I do with this note?"

            "Take it":
                "I decided to take the note with me."
            "Leave it":
                "Better not mess with fate"

        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)

        jump locker
    else:
        jump locker
        window hide

        $ window_active = False
        $ renpy.pause(0.5, hard=True)
