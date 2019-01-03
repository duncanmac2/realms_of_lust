## FUNCTIONS
# Main
label main_show(show_all=0):
    $ v_time_readable = func_readable_time(v_time)

    if show_all == 0:
        hide screen scr_navigation

    return

label time_change:
    $ v_time += 30

    if v_time >= 1140:
        "It's getting late, let's go home."
        jump lbl_home_living_room

    if v_localisation == "city_first_street":
        jump lbl_city_street_1st
    elif v_localisation == "city_second_street":
        jump lbl_city_street_2nd
    elif v_localisation == "city_third_street":
        jump lbl_city_street_3th
    elif v_localisation == "college_yard":
        jump lbl_college_yard

## SCREENS
# Input name
screen scr_name_input:
    input id "input" style "input_text" default your_name changed func_name_input xalign 0.5 yalign 0.5 length 10 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    imagebutton:
        idle "images/interface/b_yes_idle.png" hover "images/interface/b_yes_hover.png" xalign 0.45 yalign 0.65 action [SetVariable("f_name_prompt", False), Jump("lbl_name_input")]
    imagebutton:
        idle "images/interface/b_no_idle.png" hover "images/interface/b_no_hover.png" xalign 0.55 yalign 0.65 action MainMenu(confirm = False)

# Warning
screen scr_warning:
    imagebutton xpos 0.25 ypos 0.8:
        idle ("images/interface/b_continue.png")
        hover ("images/interface/b_continue_hover.png")
        action Jump("game_start")

    imagebutton xpos 0.5 ypos 0.8:
        idle ("images/interface/b_exit.png")
        hover ("images/interface/b_exit_hover.png")
        action Jump("close_renpy")

# Map
screen scr_main_map:
    # MC Room
    button:
        xpos 1180
        ypos 540
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "My room" color clr_black size 16 xpos -20 ypos 48
        action Jump("lbl_home_room_mc")

    # Beach
    button:
        xpos 941 # 947
        ypos 586 # 592
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "Beach" color clr_black size 16 xpos -10 ypos 48
        action Jump("lbl_city_beach")

    # College
    button:
        xpos 808 # 814
        ypos 338 # 344
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "College" color clr_black size 16 xpos -16 ypos 48
        action Jump("lbl_college_yard")

    # First street
    button:
        xpos 892 # 898
        ypos 464 # 470
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "1st street" color clr_black size 16 xpos -30 ypos 48
        action Jump("lbl_city_street_1st")

    # Second street
    button:
        xpos 972 # 978
        ypos 339 # 345
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "2nd street" color clr_black size 16 xpos -30 ypos 48
        action Jump("lbl_city_street_2nd")

    # Third street
    button:
        xpos 774 # 780
        ypos 463 # 469
        focus_mask "images/interface/icon_gps_mask.png"
        add "images/interface/icon_gps.png"
        text "3th street" color clr_black size 16 xpos -30 ypos 48
        action Jump("lbl_city_street_3th")

# Navigation
screen scr_navigation:
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        ypos 10
        text v_localisation.replace("_", " ").title() size 50

    frame:
        xpos 10
        ypos 10
        xmaximum 120
        ymaximum 95

        text "{b}" + v_time_readable + "{/b}" size 20 xpos 8 ypos 3

        if v_localisation == "city_first_street" or v_localisation == "city_second_street" or v_localisation == "city_third_street" or v_localisation == "college_yard":
            imagebutton:
                xpos 78
                ypos 4
                idle "images/interface/icon_time_plus.png"
                action Jump("time_change")

        imagebutton:
            xpos 8
            ypos 32
            idle "images/interface/icon_map.png"
            action Jump("lbl_city_map")

        imagebutton:
            xpos 60
            ypos 32
            idle "images/interface/icon_phone.png"
            #action [Hide("scr_phone"), Show("scr_phone_gallery"), SetVariable("f_photo_new", False)]

    frame:
        xpadding 10
        ypadding 10
        xpos 1757
        ypos 10
        xmaximum 153
        ymaximum 385

        # College
        if v_localisation == "college_yard":
            imagebutton:
                idle "images/interface/loc_college_nurse.jpg"
                hover "images/interface/loc_college_nurse_hover.jpg"
                action Jump("lbl_college_nurse")

            imagebutton:
                ypos 62
                idle "images/interface/loc_college_gym.jpg"
                hover "images/interface/loc_college_gym_hover.jpg"
                action Jump("lbl_college_gym")

            imagebutton:
                ypos 124
                idle "images/interface/loc_college_teacher_office.jpg"
                hover "images/interface/loc_college_teacher_office_hover.jpg"
                action Jump("lbl_college_teacher_office")

            imagebutton:
                ypos 186
                idle "images/interface/loc_college_garden.jpg"
                hover "images/interface/loc_college_garden_hover.jpg"
                action Jump("lbl_college_garden")

            imagebutton:
                ypos 248
                idle "images/interface/loc_college_locker_room.jpg"
                hover "images/interface/loc_college_locker_room_hover.jpg"
                action Jump("lbl_college_locker_room")

        # First street
        elif v_localisation == "city_first_street":
            imagebutton:
                idle "images/interface/loc_home_living_room.jpg"
                hover "images/interface/loc_home_living_room_hover.jpg"
                action Jump("lbl_home_living_room")

            imagebutton:
                ypos 62
                idle "images/interface/loc_city_home_marcy.jpg"
                hover "images/interface/loc_city_home_marcy_hover.jpg"
                action Jump("lbl_city_home_marcy")

            imagebutton:
                ypos 124
                idle "images/interface/loc_city_home_priya.jpg"
                hover "images/interface/loc_city_home_priya_hover.jpg"
                action Jump("lbl_city_home_priya")

        # Second street
        elif v_localisation == "city_second_street":
            imagebutton:
                idle "images/interface/loc_city_home_lily.jpg"
                hover "images/interface/loc_city_home_lily_hover.jpg"
                action Jump("lbl_city_home_lily")

            imagebutton:
                ypos 62
                idle "images/interface/loc_city_pgp_corporation.jpg"
                hover "images/interface/loc_city_pgp_corporation_hover.jpg"
                action Jump("lbl_city_pgp_corporation")

            imagebutton:
                ypos 124
                idle "images/interface/loc_city_church.jpg"
                hover "images/interface/loc_city_church_hover.jpg"
                action Jump("lbl_city_church")

        # Third street
        elif v_localisation == "city_third_street":
            imagebutton:
                idle "images/interface/loc_city_gym.jpg"
                hover "images/interface/loc_city_gym_hover.jpg"
                action Jump("lbl_city_gym")

            imagebutton:
                ypos 62
                idle "images/interface/loc_city_mall.jpg"
                hover "images/interface/loc_city_mall_hover.jpg"
                action Jump("lbl_city_mall")

            imagebutton:
                ypos 124
                idle "images/interface/loc_city_park.jpg"
                hover "images/interface/loc_city_park_hover.jpg"
                action Jump("lbl_city_park")

        # Home
        elif v_localisation == "home_living_room":
            imagebutton:
                idle "images/interface/loc_home_room_mc.jpg"
                hover "images/interface/loc_home_room_mc_hover.jpg"
                action Jump("lbl_home_room_mc")

            imagebutton:
                ypos 62
                idle "images/interface/loc_home_room_mia.jpg"
                hover "images/interface/loc_home_room_mia_hover.jpg"
                action Jump("lbl_home_room_mia")

            imagebutton:
                ypos 124
                idle "images/interface/loc_home_room_lisa.jpg"
                hover "images/interface/loc_home_room_lisa_hover.jpg"
                action Jump("lbl_home_room_lisa")

            imagebutton:
                ypos 186
                idle "images/interface/loc_home_kitchen.jpg"
                hover "images/interface/loc_home_kitchen_hover.jpg"
                action Jump("lbl_home_kitchen")

            imagebutton:
                ypos 248
                idle "images/interface/loc_home_pool.jpg"
                hover "images/interface/loc_home_pool_hover.jpg"
                action Jump("lbl_home_pool")

            imagebutton:
                ypos 310
                idle "images/interface/loc_city_street_1st.jpg"
                hover "images/interface/loc_city_street_1st_hover.jpg"
                action Jump("lbl_city_street_1st")