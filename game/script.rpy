# Initializing variables
default mc_name = "Kayo"
default window_active = False
default c_vent = 0
default c_knees = 0
default c_door = 0
default c_broom = 0
default c_books = 0
default books_picked_up = 0
default c_notes = 0
default touched_door = False

# Todo: Load character assets and audio
label start:
    #------------------------------Prologue------------------------------#
    call prologue
    jump locker
#------------------------------Locker Escape Scene------------------------------# 

# call locker_escape

# Decision Trees
# call door_decision
# call broom_decision
# call vent_decision
# call knees_decision
# call books_decision
# call notes_decision
