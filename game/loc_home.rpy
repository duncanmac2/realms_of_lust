#### LOCATIONS ####
label lbl_home_bathroom:
    scene loc_home_bathroom1
    jump lbl_home_bathroom_events

label lbl_home_kitchen:
    scene loc_home_kitchen
    jump lbl_home_kitchen_events

label lbl_home_living_room:
    $ v_localisation = "home_living_room"

    call main_show
    scene loc_home_living_room
    jump lbl_home_living_room_events

label lbl_home_pool:
    scene loc_home_pool
    jump lbl_home_pool_events

label lbl_home_room_dakota:
    scene loc_home_room_dakota
    jump lbl_home_room_dakota_events

label lbl_home_room_emily:
    scene loc_home_room_emily
    jump lbl_home_room_emily_events

label lbl_home_room_mc:
    scene loc_home_room_mc
    jump lbl_home_room_mc_events

#### EVENTS ####
### ROOM MC ###
label lbl_home_room_mc_events:
    if f_intro:
        "The sun is shining through the window."
        me "It's already morning already? Why is it so bright?"
        "What time is it? Shit, it's late, very late. The alarm didn't go off. Être en retard dès son premier jour, ."
        "Shit, I have to take a shower, better hurry."

        jump lbl_home_bathroom

### BATHROOM ###
label lbl_home_bathroom_events:
    if f_intro:
        show vid_dakota_anal_01 at top with d1
        pause
        hide vid_dakota_anal_01 with d1