label prologue:
    $ Kayo = Character(mc_name, color="#c8ffc8")
    scene dark # First of bg transition; fade in from black
    with fade

    "An ache creeping over my whole body was the first and only sensation I could feel."
    "There was no sound, no light, nothing at all."

    scene dark_expanse_blur # Second of bg transition; blured haloing
    with fade

    Kayo "Wh…Where am I?"
    scene dark_expanse # Third of bg transition; fade in from blur
    with dissolve

    "My voice could barely croak out even those words, like sandpaper against skin."
    "This is just like waking from a six hour nap, head fuzzy, confused, and I really need some water."
    scene dark_locker # Fourth of bg transition; fade into locker
    with dissolve

    "In fact, I have no idea how I got here at all."
    "The last thing I remember is going to class, but even that feels like an eternity ago."
    "Maybe I should find a way out of here first."

    window hide
    return  # End of prologue