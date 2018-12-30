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
    renpy.image("img_mc_body", "images/people/MC/mc_body.jpg")
    renpy.image("img_mc_dick", "images/people/MC/mc_dick.jpg")
    renpy.image("img_mc_sleep", "images/people/MC/mc_sleep.jpg")

    ## NPC
    # Bonnie
    for i in range(1,5):
        renpy.image("img_bonnie_shower_" + str(i).zfill(2), "images/people/kennedy_leigh/bonnie_shower_" + str(i).zfill(2) + ".jpg")

    # Ellie
    for i in range(1,2):
        renpy.image("npc_portrait_ellie_" + str(i).zfill(2), "images/people/julia_ann/ellie_portrait_" + str(i).zfill(2) + ".jpg")

    # Hitomi
    for i in range(1,3):
        renpy.image("npc_portrait_hitomi_" + str(i).zfill(2), "images/people/hitomi/hitomi_portrait_" + str(i).zfill(2) + ".jpg")

    # Karen
    renpy.image("img_karen_kiss", "images/people/jayden_jaymes/karen_kiss.jpg")

    for i in range(1,3):
        renpy.image("img_karen_couch_" + str(i).zfill(2), "images/people/jayden_jaymes/karen_couch_" + str(i).zfill(2) + ".jpg")

    for i in range(1,5):
        renpy.image("npc_portrait_karen_" + str(i).zfill(2), "images/people/jayden_jaymes/karen_portrait_" + str(i).zfill(2) + ".jpg")

    # Lisa
    renpy.image("img_lisa_kiss_01", "images/people/brandi_love/lisa_kiss_01.jpg")

    for i in range(1,6):
        renpy.image("img_lisa_shower_" + str(i).zfill(2), "images/people/brandi_love/lisa_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,8):
        renpy.image("npc_portrait_lisa_" + str(i).zfill(2), "images/people/brandi_love/lisa_portrait_" + str(i).zfill(2) + ".jpg")

    # Lily
    renpy.image("img_lily_couch", "images/people/lilith/lily_couch.jpg")

    for i in range(1,11):
        renpy.image("npc_portrait_lily_" + str(i).zfill(2), "images/people/lilith/lily_portrait_" + str(i).zfill(2) + ".jpg")

    # Marcy
    renpy.image("img_marcy_boobs_01", "images/people/brittney_white/marcy_boobs_01.jpg")

    for i in range(1,6):
        renpy.image("img_marcy_undress_" + str(i).zfill(2), "images/people/brittney_white/marcy_undress_" + str(i).zfill(2) + ".jpg")

    for i in range(1,5):
        renpy.image("npc_portrait_marcy_" + str(i).zfill(2), "images/people/brittney_white/marcy_portrait_" + str(i).zfill(2) + ".jpg")

    # Maria
    for i in range(1,4):
        renpy.image("npc_portrait_maria_" + str(i).zfill(2), "images/people/ariana_marie/maria_portrait_" + str(i).zfill(2) + ".jpg")

    # Megan
    for i in range(1,4):
        renpy.image("npc_portrait_megan_" + str(i).zfill(2), "images/people/nikki_benz/megan_portrait_" + str(i).zfill(2) + ".jpg")

    # Mia
    renpy.image("img_mia_handjob", "images/people/mia_malkova/mia_handjob.jpg")
    renpy.image("img_mia_kiss_01", "images/people/mia_malkova/mia_kiss_01.jpg")

    for i in range(1,3):
        renpy.image("img_mia_ass_" + str(i).zfill(2), "images/people/mia_malkova/mia_ass_" + str(i).zfill(2) + ".jpg")

    for i in range(1,16):
        renpy.image("npc_portrait_mia_" + str(i).zfill(2), "images/people/mia_malkova/mia_portrait_" + str(i).zfill(2) + ".jpg")

    for i in range(1,4):
        renpy.image("img_mia_shower_" + str(i).zfill(2), "images/people/mia_malkova/mia_shower_" + str(i).zfill(2) + ".jpg")

    # Nina
    for i in range(1,8):
        renpy.image("npc_portrait_nina_" + str(i).zfill(2), "images/people/alexis_texas/nina_portrait_" + str(i).zfill(2) + ".jpg")

    # Sarah
    for i in range(1,9):
        renpy.image("img_sarah_shower_" + str(i).zfill(2), "images/people/diamond_jackson/sarah_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,5):
        renpy.image("npc_portrait_sarah_" + str(i).zfill(2), "images/people/diamond_jackson/sarah_portrait_" + str(i).zfill(2) + ".jpg")

    # Veronica
    for i in range(1,3):
        renpy.image("npc_portrait_veronica_" + str(i).zfill(2), "images/people/angela_white/veronica_portrait_" + str(i).zfill(2) + ".jpg")

    ## NPC OTHERS
    renpy.image("npc_portrait_jason_01", "images/people/others/portrait_jason_01.jpg")
    renpy.image("npc_portrait_jason_02", "images/people/others/portrait_jason_02.jpg")
    renpy.image("npc_portrait_marcus", "images/people/others/portrait_marcus.jpg")
    renpy.image("npc_portrait_mr_smith_01", "images/people/others/portrait_mr_smith_01.jpg")
    renpy.image("npc_portrait_mr_smith_02", "images/people/others/portrait_mr_smith_02.jpg")

    ## BEACH
    renpy.image("img_beach_nude_01", "images/people/beach/beach_nude_01.jpg")
    renpy.image("img_beach_nude_02", "images/people/beach/beach_nude_02.jpg")
    renpy.image("img_beach_topless", "images/people/beach/beach_topless.jpg")

    ## CHURCH
    renpy.image("npc_portrait_nun", "images/people/church/portrait_nun.jpg")

## NAMES & PORTRAITS
# Player
default your_name = ""
default mc_portrait = "old"
image side portrait_mc = ConditionSwitch("mc_portrait == 'old'", "images/portrait/portrait_mc1.jpg", "mc_portrait == 'new'", "images/portrait/portrait_mc2.jpg")
define me = DynamicCharacter("your_name", image="portrait_mc", color = clr_dark_red)

# NPC
define bonnie = Character("Bonnie", image = "portrait_bonnie", color = clr_sand)
define ellie = Character("Ellie", image = "portrait_ellie", color = clr_gold)
define hitomi = Character("Hitomi", image = "portrait_hitomi", color = clr_ginger)
define karen = Character("Karen", image = "portrait_karen", color = clr_gray)
define lily = Character("Lily", image = "portrait_lily", color = clr_auburn)
define lisa = Character("Lisa", image = "portrait_lisa", color = clr_gold)
define marcy = Character("Marcy", image = "portrait_marcy", color = clr_chestnut_brown)
define megan = Character("Megan", image = "portrait_megan", color = clr_sand)
define mia = Character("Mia", image = "portrait_mia", color = clr_palegold)
define nina = Character("Nina", image = "portrait_nina", color = clr_sand)
define sarah = Character("Sarah", image = "portrait_sarah", color = clr_chestnut_brown)
define veronica = Character("Veronica", image = "portrait_veronica", color = clr_gray)

image side portrait_bonnie = "images/portrait/portrait_bonnie.jpg"
image side portrait_ellie = "images/portrait/portrait_ellie.jpg"
image side portrait_hitomi = "images/portrait/portrait_hitomi.jpg"
image side portrait_karen = "images/portrait/portrait_karen.jpg"
image side portrait_lily = "images/portrait/portrait_lily.jpg"
image side portrait_lisa = "images/portrait/portrait_lisa.jpg"
image side portrait_marcy = "images/portrait/portrait_marcy.jpg"
image side portrait_megan = "images/portrait/portrait_megan.jpg"
image side portrait_mia = "images/portrait/portrait_mia.jpg"
image side portrait_nina = "images/portrait/portrait_nina.jpg"
image side portrait_sarah = "images/portrait/portrait_sarah.jpg"
image side portrait_veronica = "images/portrait/portrait_veronica.jpg"

# NPC OTHERS
define figgs = Character("Figgs", color = clr_dark_gray)
define jason = Character("Jason", image = "portrait_jason", color = clr_dark_gray)
define kyle = Character("Kyle", image = "portrait_kyle", color = clr_dark_gray)
define marcus = Character("Marcus", image = "portrait_marcus", color = clr_dark_gray)
define mr_smith = Character("Mr Smith", image = "portrait_mr_smith", color = clr_dark_gray)
define nun = Character("Nun", image = "portrait_nun", color = clr_dark_gray)
define unknown = Character("???", color = clr_dark_gray)

image side portrait_kyle = "images/portrait/portrait_kyle.jpg"
image side portrait_jason = "images/portrait/portrait_jason.jpg"
image side portrait_marcus = "images/portrait/portrait_marcus.jpg"
image side portrait_mr_smith = "images/portrait/portrait_mr_smith_01.jpg"
image side portrait_mr_smith younger = "images/portrait/portrait_mr_smith_02.jpg"
image side portrait_nun = "images/portrait/portrait_nun.jpg"

## Effects
define d1 = Dissolve(0.2)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d5 = Dissolve(0.5)
define sr3 = CropMove(0.3, "slideright")

## INTERFACE
image img_black = Solid(clr_black)
image img_white = Solid(clr_white)
image img_warning = "images/interface/warning.png"

## LOCATIONS
# Home
image loc_home_bathroom1 = "images/location/loc_home_bathroom1.jpg"
image loc_home_bathroom2 = "images/location/loc_home_bathroom2.jpg"
image loc_home_kitchen = "images/location/loc_home_kitchen.jpg"
image loc_home_living_room = "images/location/loc_home_living_room.jpg"
image loc_home_room_lisa_bed = "images/location/loc_home_room_lisa_bed.jpg"
image loc_home_room_mc = "images/location/loc_home_room_mc.jpg"
image loc_home_room_mc_bed = "images/location/loc_home_room_mc_bed.jpg"
image loc_home_room_mia = "images/location/loc_home_room_mia.jpg"

# City
image loc_city_home_marcy = "images/location/loc_city_home_marcy.jpg"
image loc_city_home_marcy_bathroom = "images/location/loc_city_home_marcy_bathroom.jpg"
image loc_city_home_marcy_room = "images/location/loc_city_home_marcy_room.jpg"
image loc_city_mall = "images/location/loc_city_mall.jpg"
image loc_city_mall_store = "images/location/loc_city_mall_store.jpg"
image loc_city_street_1st = "images/location/loc_city_street_1st.jpg"

# College
image loc_college_class = "images/location/loc_college_class.jpg"
image loc_college_garden = "images/location/loc_college_garden.jpg"
image loc_college_locker_room = "images/location/loc_college_locker_room.jpg"
image loc_college_nurse = "images/location/loc_college_nurse.jpg"
image loc_college_shower_men = "images/location/loc_college_shower_men.jpg"
image loc_college_yard = "images/location/loc_college_yard.jpg"

## VIDEOS
# MC
image vid_mc_erection = Movie(play="images/people/MC/MC_erection.webm")

# Lily
image vid_lily_kiss_01 = Movie(play="images/people/lilith/lily_kiss_01.webm", size=(960,544))
image vid_lily_kiss_02 = Movie(play="images/people/lilith/lily_kiss_02.webm", size=(1000,460))

# Lisa
image vid_lisa_bathroom_incident = Movie(play="images/people/brandi_love/lisa_bathroom_incident.webm", size=(590,590))
image vid_lisa_handjob_cum = Movie(play="images/people/brandi_love/lisa_handjob_cum.webm", size=(800,418))
image vid_lisa_kiss_02 = Movie(play="images/people/brandi_love/lisa_kiss_02.webm", size=(1000,540))
image vid_lisa_kiss_03 = Movie(play="images/people/brandi_love/lisa_kiss_03.webm", size=(800,778))
image vid_lisa_show_boobs = Movie(play="images/people/brandi_love/lisa_boobs_01.webm")
image vid_lisa_room_masturbate = Movie(play="images/people/brandi_love/lisa_masturbation.webm")

# Marcy
image vid_marcy_boobs_02 = Movie(play="images/people/brittney_white/marcy_boobs_02.webm", size=(630,716))
image vid_marcy_boobs_bounce = Movie(play="images/people/brittney_white/marcy_boobs_bounce.webm", size=(552,780))
image vid_marcy_masturbate = Movie(play="images/people/brittney_white/marcy_masturbate.webm", size=(704,512))

# Mia
image vid_mia_masturbate = Movie(play="images/people/mia_malkova/mia_masturbate.webm", size=(1000,496))

# College
image vid_college_run = Movie(play="images/events/college_run.webm")
image vid_college_shower_01 = Movie(play="images/events/college_shower_01.webm", size=(620,612))
image vid_college_shower_02 = Movie(play="images/events/college_shower_02.webm", size=(598,736))
image vid_college_spanking = Movie(play="images/events/college_spanking.webm", size=(534,800))

# Home
image vid_pc_porn_01 = Movie(play="images/events/pc_porn_01.webm", size=(1000,522))
image vid_pc_porn_02 = Movie(play="images/events/pc_porn_02.webm", size=(1000,514))
image vid_pc_porn_03 = Movie(play="images/events/pc_porn_03.webm", size=(570,848))
image vid_pc_porn_04 = Movie(play="images/events/pc_porn_04.webm", size=(1000,560))

## START
label splashscreen:
    scene img_warning
    call screen scr_warning

label start:
    # Flags
    $ f_name_prompt = True
    $ f_bypass = False
    $ f_day1_lisa_bathroom_incident = False
    $ f_day2_nurse = False
    $ f_day2_shower = False
    $ f_day3_shower = False
    $ f_day3_spy = False

    # Variables
    $ v_day = 1
    $ v_time = 0

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