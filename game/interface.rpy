## FUNCTIONS
# Main
label main_show(show_all=0):
    $ v_time_readable = func_readable_time(v_time)

    if show_all == 0:
        hide screen scr_navigation

    return

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

## SCREENS LOCATIONS
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

        text "{b}" + v_time_readable + "{/b}" size 20 xalign 0.5

        imagebutton:
            xpos 8
            ypos 32
            idle "images/interface/icon_map.png"
            #action [Hide("scr_phone"), Show("scr_phone_gallery"), SetVariable("f_photo_new", False)]

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
        ymaximum 323

        if v_localisation == "college_yard":
            imagebutton:
                idle "images/interface/loc_college_nurse.jpg"
                hover "images/interface/loc_college_nurse_hover.jpg"
                action [SetVariable("v_localisation", "college_nurse"), Jump("lbl_college_nurse")]

            imagebutton:
                ypos 62
                idle "images/interface/loc_college_gym.jpg"
                hover "images/interface/loc_college_gym_hover.jpg"
                action [SetVariable("v_localisation", "college_gym")]

            imagebutton:
                ypos 124
                idle "images/interface/loc_college_teacher_office.jpg"
                hover "images/interface/loc_college_teacher_office_hover.jpg"
                action [SetVariable("v_localisation", "college_teacher_office"), Jump("lbl_college_teacher_office")]

            imagebutton:
                ypos 186
                idle "images/interface/loc_college_garden.jpg"
                hover "images/interface/loc_college_garden_hover.jpg"
                action [SetVariable("v_localisation", "college_garden")]

            imagebutton:
                ypos 248
                idle "images/interface/loc_college_locker_room.jpg"
                hover "images/interface/loc_college_locker_room_hover.jpg"
                action [SetVariable("v_localisation", "college_garden")]