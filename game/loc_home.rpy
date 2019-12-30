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
        me "What time is it? Shit it's late, the alarm didn't go off. Being late on your first day..."
        me "I have to take a shower, better hurry."

        jump lbl_home_bathroom

### BATHROOM ###
label lbl_home_bathroom_events:
    if f_intro:
        scene img_adriana_bathroom_s01_01 with d3
        adriana "Love, you're gonna be late."
        scene img_adriana_bathroom_s01_02 with d1
        me "I know, I know, I was just about to take a shower."
        scene img_adriana_bathroom_s01_03 with d1
        adriana "You don't have to hide it, you know, it's not like I know it intimately."
        me "Yes, but..."
        scene img_adriana_bathroom_s01_04 with d1
        adriana "No but, now because of you I want to fuck. Would you rather satisfy your wife or not be late?"
        menu:
            "It's my first day!":
                jump lbl_college_yard
            "They can wait for me for a little.":
                scene img_black
                show vid_adriana_bathroom_s01_hj with d1
                adriana "Good answer."
                me "You're the best honey."
                adriana "Oh I know. And guess who is the best to suck your delicious dick?"
                hide vid_adriana_bathroom_s01_hj with d1
                show vid_adriana_bathroom_s01_bj_01 with d3
                me "Hmm, you as always."
                window hide
                pause

                jump lbl_home_bathroom_adriana_s01_01

label lbl_home_bathroom_adriana_s01_01:
    menu:
        "Lick my balls my slutty whore.":
            show vid_adriana_bathroom_s01_bj_02 with d1
            pause
            jump lbl_home_bathroom_adriana_s01_01

        "Faster bitch!":
            show vid_adriana_bathroom_s01_bj_03 with d1
            pause
            jump lbl_home_bathroom_adriana_s01_01

        "I want to fuck your perverted face.":
            show vid_adriana_bathroom_s01_bj_04 with d1
            pause
            jump lbl_home_bathroom_adriana_s01_01

        "Let's fuck.":
            jump lbl_home_bathroom_adriana_s01_02

label lbl_home_bathroom_adriana_s01_02:
    #window show