## FUNCTIONS
# Main
label main_show(show_all=0):
    if show_all == 0:
        scene img_black
        #hide screen scr_map_city
        #hide screen scr_main_info

    elif show_all == "city":
        call main_show
        #show screen scr_map_city
        #if f_change_time:
        #    show screen scr_main_info

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
screen scr_home_room_mc:
    add "images/location/loc_room_mc.jpg"