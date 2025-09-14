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

# White
screen scr_white:
    zorder 3
    add Solid(clr_white)

## ANIMATIONS
label animations:
# S001
    image ani_s001_01:
        "s001_013"
        0.2
        "s001_014"
        0.2
        repeat

    image ani_s001_02:
        "s001_015"
        0.2
        "s001_016"
        0.2
        repeat

# S002
    image ani_s002_01:
        "s002_003"
        0.8
        "s002_004"
        0.8
        repeat

    image ani_s002_02:
        "s002_005"
        0.4
        "s002_006"
        0.4
        repeat