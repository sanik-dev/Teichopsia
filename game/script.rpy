# Initialize the name variable
default mc_name = "Kayo"

# Todo: Load character assets and audio you dummy :3
label start:
    # Setup
    # Define the character
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

    return