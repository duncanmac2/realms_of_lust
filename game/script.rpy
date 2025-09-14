init python:
    # Background always black
    config.layers.insert(0, 'background')

    # Name function
    def func_name_input(str):
        store.your_name = str

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
    clr_brown_dark = "#331a00"

    ### IMAGES
    #############
    ## Intro
    for i in range(1,3):
        renpy.image("img_intro_" + str(i).zfill(2), "images/intro_" + str(i).zfill(2) + ".webp")

    ## Scenes ##
    for i in range(1,20):
        renpy.image("s001_" + str(i).zfill(3), "images/s001_" + str(i).zfill(3) + ".webp")

    for i in range(1,13):
        renpy.image("s002_" + str(i).zfill(3), "images/s002_" + str(i).zfill(3) + ".webp")

    ## BEACH
    renpy.image("img_beach_nude_01", "images/people/beach/beach_nude_01.jpg")
    renpy.image("img_beach_nude_02", "images/people/beach/beach_nude_02.jpg")
    renpy.image("img_beach_topless", "images/people/beach/beach_topless.jpg")

    ## CHURCH
    renpy.image("npc_portrait_nun_01", "images/people/church/portrait_nun_01.jpg")
    renpy.image("npc_portrait_nun_02", "images/people/church/portrait_nun_02.jpg")

    ## PARK
    for i in range(1,4):
        renpy.image("img_park_exhibition_" + str(i).zfill(2), "images/people/park/park_exhibition_" + str(i).zfill(2) + ".jpg")

## NAMES & PORTRAITS
# Player
default your_name = ""
define me = DynamicCharacter("your_name", color = clr_dark_red)

# NPC
define isha = Character("Isha", color = clr_gold)
define molly = Character("Molly", color = clr_ginger)
define letty = Character("Letty", color = clr_light_orange)

define mom_me = Character("Mom & [me]", color = clr_dark_red)

# NPC OTHERS
define unknown = Character("???", color = clr_dark_gray)

## EFFECTS
define d1 = Dissolve(0.2)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d5 = Dissolve(0.5)
define d8 = Dissolve(0.8)
define sr3 = CropMove(0.3, "slideright")

## INTERFACE
image img_black = Solid(clr_black)
image img_white = Solid(clr_white)
image img_warning = "images/interface/warning.png"

## START
label splashscreen:
    scene img_warning
    call screen scr_warning

label start:
    # Flags
    $ f_name_prompt = True
    $ f_pee = True

    # Variables
    $ v_day = 1

    # Start
    hide screen main_menu
    scene black onlayer background

    jump lbl_intro

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
        jump lbl_s001b

label lbl_intro:
    scene img_intro_01 with d3
    "During World War 3, the world population experienced a significant decline, especially the male population decimated by years of conflict."
    scene img_intro_02 with d3
    "Lilith's legions swept across Europe, ruthless and unstoppable. It seems that fighting continues to rage far beyond the borders."
    "She imposed a merciless matriarchal reign, and men are sent to war as soon as possible."
    "But women do not necessarily have a more enviable fate. The chosen ones are turned, the rejected ones converted, and the less fortunate ones reduced to slavery."

    jump lbl_s001a