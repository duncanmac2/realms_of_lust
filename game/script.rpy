init python:
    # Background always black
    config.layers.insert(0, 'background')

    # Name function
    def func_name_input(str):
        store.your_name = str

    s_interface_total_width = 1920
    s_interface_total_height = 1080

    # Colors
    clr_black = "#000"
    clr_red = "#f00"
    clr_green = "#33cc33"
    clr_light_orange = "#ff9933"
    clr_white = "#fff"
    clr_gray = "#848484"
    clr_dark_gray = "#666666"
    clr_very_dark_gray = "#404040"
    clr_chestnut_brown = "#605252"
    clr_pink = "#ff1ac6"
    clr_auburn = "#b30600"
    clr_dark_red = "#8b0000"
    clr_very_dark_red = "#4d0000"
    clr_ginger = "#c76223"
    clr_light_ginger = "#dd8c3c"
    clr_dark_ginger = "#633800"
    clr_dark_yellow = "#bf9900"
    clr_gold = "#ffd700"
    clr_sand = "#ffcc66"
    clr_palegold = "#eee8aa"
    clr_blueviolet = "#8a2be2"

    ### IMAGES
    ## MC


    ## NPC
    # Lisa
    for i in range(1,5):
        renpy.image("npc_portrait_lisa_" + str(i).zfill(2), "images/people/brandi_love/lisa_portrait_" + str(i).zfill(2) + ".jpg")

    # Lisa
    for i in range(1,5):
        renpy.image("npc_portrait_mia_" + str(i).zfill(2), "images/people/mia_malkova/mia_portrait_" + str(i).zfill(2) + ".jpg")

## NAMES & PORTRAITS
# Player
default your_name = ""
define me = DynamicCharacter("your_name", image = "portrait_mc", color = clr_dark_red)
image side portrait_mc = "images/portrait/portrait_mc1.jpg"

# NPC
define mia = Character("Mia", image = "portrait_mia", color = clr_palegold)
define lisa = Character("Lisa", color = clr_gold)

image side portrait_mia = "images/portrait/portrait_mia.jpg"

## INTERFACE
image img_black = Solid(clr_black)
image img_white = Solid(clr_white)
image img_warning = "images/interface/warning.png"

## LOCATIONS
image loc_home_bathroom1 = "images/location/loc_home_bathroom1.jpg"
image loc_home_bathroom2 = "images/location/loc_home_bathroom2.jpg"
image loc_home_room_mc = "images/location/loc_home_room_mc.jpg"

## VIDEOS
image vid_lisa_bathroom_incident = Movie(play="images/people/brandi_love/lisa_bathroom_incident.webm",size=(590,590))

## START
label splashscreen:
    scene img_warning
    call screen scr_warning

label start:
    # Flags
    $ f_name_prompt = True
    $ f_bypass = False

    # Variables
    $ v_day = 1

    # Start
    hide screen main_menu
    scene black onlayer background
    jump lbl_bypass

    "Do you have play previous version and want to jump directly to new content?"
    menu:
        "Jump to new content":
            $ f_bypass = True
            jump lbl_censorship
        "Start from the beginning":
            jump lbl_name_input

label game_start:
    show screen main_menu
    return

label close_renpy:
    $ renpy.quit()
    return

label lbl_name_input:
    scene expression "images/interface/bg_input_name.png"

    if your_name == "" or f_name_prompt == True:
        call screen scr_name_input
    else:
        if f_bypass:
            jump lbl_bypass
        else:
            jump lbl_intro

label lbl_intro:
    scene npc_portrait_lisa_01
    "You are [me], a 21-year old college student living with Lisa and her daughter, she is an old friend of your family who offered a place for you to stay when your parents suffered a tragic accident when you were only six."
    "She has raised you ever since, and even so she has been almost your mother during this time it never felt right to call her \"mom\", she understands of course."
    scene npc_portrait_mia_01
    "Her daughter is not the same, however, ever since you moved in she has called you brother and insisted that you call her \"sis\", she was always very close to you, ever since you saved her from a ferocious chihuahua. You were five at the time and she was almost four."
    "Unfortunately they are the only woman you are close to, since you always was a bit of a loner during childhood, and that turned you into an extremely shy individual."
    "Being friend with the most perverted guy in school didn't help either, but this year you have made up your mind that you would lose this V card, one way or the other, and this is where our story begins."

    jump lbl_home_room_mc

label lbl_bypass:
    $ your_name = "John"

    jump lbl_intro