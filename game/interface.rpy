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
    text v_localisation color clr_dark_red size 100 xalign 0.5 yalign 0.1

    frame:
        xpadding 28
        ypadding 10
        xpos 10
        ypos 10
        xmaximum 120
        ymaximum 95

        python:
            ui.text("{b}" + v_time_readable + "{/b}", size = 20)

        imagebutton:
            xpos -13
            ypos 32
            idle "images/interface/icon_map.png"
            #action [Hide("scr_phone"), Show("scr_phone_gallery"), SetVariable("f_photo_new", False)]

        imagebutton:
            xpos 37
            ypos 32
            idle "images/interface/icon_phone.png"
            #action [Hide("scr_phone"), Show("scr_phone_gallery"), SetVariable("f_photo_new", False)]

        #vbox: