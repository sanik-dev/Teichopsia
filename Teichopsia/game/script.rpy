# Initialize the name variable
default mc_name = "Kayo"

# Todo: Load character assets and audio you dummy :3
label start:
    # Setup
    # Define the character
    $ Kayo = Character(mc_name, color="#c8ffc8")
    # scene bg_dark_expanse  # Todo: Load a background image named "bg_dark_expanse"
    # with fade             # Fade-in effect for the background

    # Description and internal thoughts
    "A loud bang jolts me suddenly, heart rate ringing in my ears as a hot rush of pain seared behind my eyes."
    "A dark expanse was all around, whether my eyes were even open or not was up for debate."
    "The air smelled oddly stale, rust permeating throughout the confined space."
    "Tightness of the throat, body aching from disuse."
    
    # Kayo speaks
    Kayo "… Wh… Where…?"
    
    # More internal thoughts and actions
    "My tongue feels like sandpaper, barely a croak coming from my dehydrated throat."
    "Apprehensively, investigating this box was all I could do, everywhere my body hadn’t been was pleasantly cold, clearly not affected by the lingering body heat."
    "It felt nice to rest my head against the assumed metal, if the smell was anything to go by."
    "I weakly made contact with the box’s walls, feeling the surrounding for any way to escape."
    "Aaand absolutely nothing. But, a futile effort is an effort nonetheless."
    "It felt like it’d been hours, but perception of time is a bit fuzzy when there’s no clock, I don’t even have a phone."

    return