init python:
    # Background always black
    config.layers.insert(0, 'background')

    # Name function
    def func_name_input(str):
        store.your_name = str

    # Time function
    def func_readable_time(time):
        readable_time = divmod(time, 60)
        return str(readable_time[0]).zfill(2) + ":" + str(readable_time[1]).zfill(2)

    # Check time period
    def func_check_time(time, tb_time):
        res = ""

        for t in tb_time:
            tb_period = t.split("-")
            if (int(time) < int(tb_period[1]) and int(time) >= int(tb_period[0])):
                return tb_time[t]

        return res

    # Days
    tb_day = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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

    # Tables time period
    tb_time = {"college_yard": {}, "home_backyard": {}, "home_bathroom": {}, "home_kitchen": {}, "home_living_room": {}, "home_pool": {}, "home_room_dakota": {}, "home_room_emily": {}, "home_room_mc": {}}
    tb_time["college_yard"] = {
        "480-510": "dakota,emily",
        "510-1050": "adriana,dakota,emily"
    }
    tb_time["home_backyard"] = {
        "1050-1095": "adriana,dakota,emily"
    }
    tb_time["home_bathroom"] = {
        "420-450": "emily",
        "450-480": "dakota",
        "480-510": "adriana",
        "1170-1200": "emily",
        "1320-1350": "adriana",
        "1350-1380": "dakota"
    }
    tb_time["home_kitchen"] = {
        "420-450": "adriana,dakota",
        "450-480": "adriana,emily",
        "1125-1140": "adriana",
        "1140-1170": "adriana,dakota,emily"
    }
    tb_time["home_living_room"] = {
        "1170-1200": "adriana,dakota",
        "1200-1350": "adriana,dakota,emily",
        "1350-1380": "emily"
    }
    tb_time["home_pool"] = {
        "1095-1125": "adriana,dakota,emily",
        "1120-1140": "dakota,emily"
    }
    tb_time["home_room_dakota"] = {
        "0-420": "dakota",
        "1380-1440": "dakota"
    }
    tb_time["home_room_emily"] = {
        "0-420": "emily",
        "1380-1440": "emily"
    }
    tb_time["home_room_mc"] = {
        "0-420": "adriana",
        "1350-1440": "adriana"
    }

    ### IMAGES
    ## Adriana ##
    # Others
    for i in range(1,3):
        renpy.image("img_adriana_portrait_" + str(i).zfill(2), "images/people/adriana.chechik/adriana_portrait_" + str(i).zfill(2) + ".jpg")

    for i in range(1,2):
        renpy.image("img_adriana_lesbian_" + str(i).zfill(2), "images/people/adriana.chechik/adriana_lesbian_" + str(i).zfill(2) + ".jpg")

    for i in range(1,2):
        renpy.image("img_adriana_slut_" + str(i).zfill(2), "images/people/adriana.chechik/adriana_slut_" + str(i).zfill(2) + ".jpg")

    # Bathroom
    for i in range(1,7):
        renpy.image("img_adriana_bathroom_s01_" + str(i).zfill(2), "images/people/adriana.chechik/adriana_bathroom_s01_" + str(i).zfill(2) + ".jpg")

    # Living Room
    for i in range(1,5):
        renpy.image("img_adriana_livingroom_s01_" + str(i).zfill(2), "images/people/adriana.chechik/adriana_livingroom_s01_" + str(i).zfill(2) + ".jpg")

    ## Dakota ##
    # Others
    for i in range(1,2):
        renpy.image("img_dakota_portrait_" + str(i).zfill(2), "images/people/dakota.skye/dakota_portrait_" + str(i).zfill(2) + ".jpg")

    # Backyard
    # [SweetSinner.com] Dakota Skye - Solo & Softcore Set for Student Bodies 3 - Scene 4
    for i in range(1,22):
        renpy.image("img_dakota_backyard_s01_" + str(i).zfill(2), "images/people/dakota.skye/dakota_backyard_s01_" + str(i).zfill(2) + ".jpg")

    # Bathroom
    renpy.image("img_dakota_bathroom_s01_pee_03", "images/people/dakota.skye/dakota_bathroom_s01_pee_03.jpg")

    # Living Room
    for i in range(1,4):
        renpy.image("img_dakota_livingroom_s01_" + str(i).zfill(2), "images/people/dakota.skye/dakota_livingroom_s01_" + str(i).zfill(2) + ".jpg")

    ## Emily ##
    # Others
    for i in range(1,2):
        renpy.image("img_emily_portrait_" + str(i).zfill(2), "images/people/emily.willis/emily_portrait_" + str(i).zfill(2) + ".jpg")

    # Bathroom
    for i in range(1,3):
        renpy.image("img_emily_bathroom_s01_" + str(i).zfill(2), "images/people/emily.willis/emily_bathroom_s01_" + str(i).zfill(2) + ".jpg")

    for i in range(4,9):
        renpy.image("img_emily_bathroom_s02_" + str(i).zfill(2), "images/people/emily.willis/emily_bathroom_s02_" + str(i).zfill(2) + ".jpg")

    # Kitchen
    # [AmKingdom] 2018.07.03 - Upskirts and Panties
    # [AmKingdom] 2018.06.20 - Coeds
    for i in range(1,22):
        renpy.image("img_emily_kitchen_s01_" + str(i).zfill(2), "images/people/emily.willis/emily_kitchen_s01_" + str(i).zfill(2) + ".jpg")

    ## NPC OTHERS ##
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

    ## INTRO
    renpy.image("img_intro_01", "images/events/intro_01.jpg")
    renpy.image("img_intro_02", "images/events/intro_02.png")
    renpy.image("img_intro_03", "images/events/intro_03.jpg")

## NAMES & PORTRAITS
# Player
default your_name = ""
define me = DynamicCharacter("your_name", color = clr_dark_red)

# NPC
define adriana = Character("Adriana", color = clr_gray)
define dakota = Character("Dakota", color = clr_gold)
define emily = Character("Emily", color = clr_gray)
define dad_mom = Character("[me] & Adriana", color = clr_dark_red)

define alison = Character("Alison", color = clr_sand)
define emma = Character("Emma", color = clr_auburn)
define hitomi = Character("Hitomi", color = clr_ginger)
define kiara = Character("Kiara", color = clr_brown_dark)
define marcy = Character("Marcy", color = clr_chestnut_brown)
define mia = Character("Mia", color = clr_palegold)

# NPC OTHERS
define unknown = Character("???", color = clr_dark_gray)

## EFFECTS
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
image loc_home_backyard = "images/location/loc_home_backyard.jpg"
image loc_home_bathroom = "images/location/loc_home_bathroom.jpg"
image loc_home_kitchen = "images/location/loc_home_kitchen.jpg"
image loc_home_living_room = "images/location/loc_home_living_room.jpg"
image loc_home_pool = "images/location/loc_home_pool.jpg"
image loc_home_room_mc = "images/location/loc_home_room_mc.jpg"
image loc_home_room_dakota = "images/location/loc_home_room_emily.jpg"
image loc_home_room_emily = "images/location/loc_home_room_emily.jpg"

# City
image loc_city_map = "images/location/loc_city_map.jpg"
image loc_city_map_back = "images/location/loc_city_map_back.jpg"
image loc_city_church = "images/location/loc_city_church.jpg"
image loc_city_gym = "images/location/loc_city_gym.jpg"
image loc_city_home_lily = "images/location/loc_city_home_lily.jpg"
image loc_city_home_marcy = "images/location/loc_city_home_marcy.jpg"
image loc_city_home_marcy_bathroom = "images/location/loc_city_home_marcy_bathroom.jpg"
image loc_city_home_marcy_pool = "images/location/loc_city_home_marcy_pool.jpg"
image loc_city_home_marcy_room = "images/location/loc_city_home_marcy_room.jpg"
image loc_city_home_marcy_room_sarah = "images/location/loc_city_home_marcy_room_sarah.jpg"
image loc_city_home_priya = "images/location/loc_city_home_priya.jpg"
image loc_city_hospital = "images/location/loc_city_hospital.jpg"
image loc_city_mall = "images/location/loc_city_mall.jpg"
image loc_city_mall_break = "images/location/loc_city_mall_break.jpg"
image loc_city_mall_coffee = "images/location/loc_city_mall_coffee.jpg"
image loc_city_mall_store = "images/location/loc_city_mall_store.jpg"
image loc_city_park = "images/location/loc_city_park.jpg"
image loc_city_pgp_corporation = "images/location/loc_city_pgp_corporation.jpg"
image loc_city_pgp_corporation_office_lily = "images/location/loc_city_pgp_corporation_office_lily.jpg"
image loc_city_street_1st = "images/location/loc_city_street_1st.jpg"
image loc_city_street_2nd = "images/location/loc_city_street_2nd.jpg"
image loc_city_street_3th = "images/location/loc_city_street_3th.jpg"

# College
image loc_college_class = "images/location/loc_college_class.jpg"
image loc_college_corridor = "images/location/loc_college_corridor.jpg"
image loc_college_garden = "images/location/loc_college_garden.jpg"
image loc_college_gym = "images/location/loc_college_gym.jpg"
image loc_college_locker_room = "images/location/loc_college_locker_room.jpg"
image loc_college_nurse = "images/location/loc_college_nurse.jpg"
image loc_college_office_ellie = "images/location/loc_college_office_ellie.jpg"
image loc_college_shower_men = "images/location/loc_college_shower_men.jpg"
image loc_college_teacher_office = "images/location/loc_college_teacher_office.jpg"
image loc_college_yard = "images/location/loc_college_yard.jpg"

## OBJECTS
image obj_pills = "images/objects/pills.jpg"
image obj_sarah_playboy_collection = "images/objects/sarah_playboy_collection.jpg"

### VIDEOS - NPC
## Adriana ##
# Bathroom S01
# [RK Prime] Adriana Chechik - Study Break
image vid_adriana_bathroom_s01_cun = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_cun.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_hj = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_hj.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_bj_01 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_bj_01.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_bj_02 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_bj_02.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_bj_03 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_bj_03.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_bj_04 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_bj_04.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_01 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_01.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_02 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_02.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_03 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_03.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_04 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_04.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_05 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_05.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_06 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_06.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_07 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_07.webm", size=(1920,1080))
image vid_adriana_bathroom_s01_vg_08 = Movie(play="images/people/adriana.chechik/adriana_bathroom_s01_vg_08.webm", size=(1920,1080))

# Living Room S01
# [EvilAngel] Adriana Chechik - Alien Ass Party 4 - Scene 2
image vid_adriana_livingroom_s01_bj_01 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_bj_01.webm")
image vid_adriana_livingroom_s01_bj_02 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_bj_02.webm")
image vid_adriana_livingroom_s01_bj_03 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_bj_03.webm")
image vid_adriana_livingroom_s01_bj_04 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_bj_04.webm")
image vid_adriana_livingroom_s01_vg_01 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_vg_01.webm")
image vid_adriana_livingroom_s01_vg_02 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_vg_02.webm")
image vid_adriana_livingroom_s01_vg_03 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_vg_03.webm")
image vid_adriana_livingroom_s01_an_01 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_an_01.webm")
image vid_adriana_livingroom_s01_an_02 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_an_02.webm")
image vid_adriana_livingroom_s01_an_03 = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_an_03.webm")
image vid_adriana_livingroom_s01_pus = Movie(play="images/people/adriana.chechik/adriana_livingroom_s01_pus.webm")

## Dakota ##
# Bathroom S01
# [InTheCrack] Dakota Skye - Skye Piss Down
image vid_dakota_bathroom_s01_pee_01 = Movie(play="images/people/dakota.skye/dakota_bathroom_s01_pee_01.webm")

# Living Room S01
# [InTheCrack] Dakota Skye - Give Fur the Finger
image vid_dakota_livingroom_s01_fg_01 = Movie(play="images/people/dakota.skye/dakota_livingroom_s01_fg_01.webm")
image vid_dakota_livingroom_s01_fg_02 = Movie(play="images/people/dakota.skye/dakota_livingroom_s01_fg_02.webm")

## Emily ##
# Bathroom S01
# [TeensLikeItBig] Emily Willis - Practice Makes A Perfect Slut
image vid_emily_bathroom_s01_mas = Movie(play="images/people/emily.willis/emily_bathroom_s01_mas.webm")

# Bathroom S02
# [CherryPimps] 2018.10.18 - Emily Willis - Shower Time Cums so Quick
image vid_emily_bathroom_s02_01 = Movie(play="images/people/emily.willis/emily_bathroom_s02_01.webm")
image vid_emily_bathroom_s02_02 = Movie(play="images/people/emily.willis/emily_bathroom_s02_02.webm")
image vid_emily_bathroom_s02_k = Movie(play="images/people/emily.willis/emily_bathroom_s02_k.webm")
image vid_emily_bathroom_s02_bj_01 = Movie(play="images/people/emily.willis/emily_bathroom_s02_bj_01.webm")
image vid_emily_bathroom_s02_bj_02 = Movie(play="images/people/emily.willis/emily_bathroom_s02_bj_02.webm")
image vid_emily_bathroom_s02_bj_03 = Movie(play="images/people/emily.willis/emily_bathroom_s02_bj_03.webm")
image vid_emily_bathroom_s02_cun = Movie(play="images/people/emily.willis/emily_bathroom_s02_cun.webm")
image vid_emily_bathroom_s02_fg = Movie(play="images/people/emily.willis/emily_bathroom_s02_fg.webm")
image vid_emily_bathroom_s02_hj = Movie(play="images/people/emily.willis/emily_bathroom_s02_hj.webm")
image vid_emily_bathroom_s02_mas = Movie(play="images/people/emily.willis/emily_bathroom_s02_mas.webm")
image vid_emily_bathroom_s02_vg_01 = Movie(play="images/people/emily.willis/emily_bathroom_s02_vg_01.webm")
image vid_emily_bathroom_s02_vg_02 = Movie(play="images/people/emily.willis/emily_bathroom_s02_vg_02.webm")
image vid_emily_bathroom_s02_vg_03 = Movie(play="images/people/emily.willis/emily_bathroom_s02_vg_03.webm")

## VIDEOS - LOCATION
# Beach
image vid_beach_boobs_01 = Movie(play="images/people/beach/beach_boobs_01.webm", size=(1000,742))
image vid_beach_boobs_02 = Movie(play="images/people/beach/beach_boobs_02.webm", size=(584,440))
image vid_beach_boobs_03 = Movie(play="images/people/beach/beach_boobs_03.webm", size=(800,660))

# Church
image vid_church_nun_blowjob = Movie(play="images/people/church/nun_blowjob.webm", size=(840,416))

# College
image vid_college_masturbate = Movie(play="images/events/college_masturbate.webm")
image vid_college_run = Movie(play="images/events/college_run.webm")
image vid_college_shower_01 = Movie(play="images/events/college_shower_01.webm", size=(620,612))
image vid_college_shower_02 = Movie(play="images/events/college_shower_02.webm", size=(598,736))
image vid_college_shower_03 = Movie(play="images/events/college_shower_03.webm", size=(1000,468))
image vid_college_shower_04 = Movie(play="images/events/college_shower_04.webm")
image vid_college_shower_05 = Movie(play="images/events/college_shower_05.webm", size=(750,741))
image vid_college_spanking = Movie(play="images/events/college_spanking.webm", size=(534,800))

# Gym
image vid_gym_01 = Movie(play="images/people/gym/gym_01.webm", size=(998,556))
image vid_gym_02 = Movie(play="images/people/gym/gym_02.webm", size=(600,592))
image vid_gym_03 = Movie(play="images/people/gym/gym_03.webm", size=(720,406))

# Home
image vid_pc_game = Movie(play="images/events/pc_game.webm", size=(996,818))
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
    $ f_bypass = False
    $ f_intro = True
    $ f_name_prompt = True
    $ f_pee = True

    # Variables
    $ v_day = 1
    $ v_time = 480
    $ v_time_readable = ""
    $ v_localisation = ""

    # Lust
    $ tb_stats = {"lust": {}, "lvl": {}}
    $ tb_stats["lust"] = {
        "mc": 0,
        "adriana": 0,
        "dakota": 0,
        "emily": 0,
        "school": 0
    }
    $ tb_stats["lvl"] = {
        "dakota": 0,
        "emily": 0,
        "school": 0
    }

    # Events
    $ tb_events = {"college_yard": {}, "home_backyard": {}, "home_bathroom": {}, "home_kitchen": {}, "home_living_room": {}, "home_pool": {}, "home_room_dakota": {}, "home_room_emily": {}, "home_room_mc": {}}
    $ tb_events["college_yard"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_backyard"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_bathroom"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_kitchen"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_living_room"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_pool"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_room_dakota"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_room_emily"] = { "adriana": False, "dakota": False, "emily": False }
    $ tb_events["home_room_mc"] = { "adriana": False, "dakota": False, "emily": False }

    # Start
    hide screen main_menu
    scene black onlayer background

    #jump lbl_censorship
    jump lbl_bypass

    "Do you have play previous version and want to jump directly to new content?"
    menu:
        "Jump to new content":
            $ f_bypass = False
            #jump lbl_name_input
            jump lbl_bypass
        "Start from the beginning":
            jump lbl_censorship

label game_start:
    show screen main_menu
    return

label close_renpy:
    $ renpy.quit()
    return

label lbl_censorship:
    "The game contains some rather \"extreme\" scenes such as water-sports. Do you want to censor them while knowing that you will inevitably miss a little bit of content?"
    menu:
        "Yes.":
            $ f_pee = False
        "No, I want to see that.":
            $ f_pee = True

    jump lbl_name_input

label lbl_name_input:
    scene expression "images/interface/bg_input_name.png"

    if your_name == "" or f_name_prompt == True:
        call screen scr_name_input
    else:
        if f_bypass:
            jump lbl_bypass
        else:
            jump lbl_intro

label lbl_not_yet:
    "I have to corrupt her further first."
    return

label lbl_intro:
    scene img_intro_01 with d3
    "During World War 3, the world population experienced a significant decline, especially the male population decimated by years of conflict."
    scene img_adriana_portrait_01
    "Your wife Adriana has always loved sex, and during the war she turned to female friends to satisfy her needs."
    scene img_adriana_lesbian_01
    "She never forget to send you videos of her lovemaking and perhaps it was her love and support that gave you the strength to survive."
    scene img_intro_02
    "Your two daughters, conceived before going to war, are now young adults full of life and, above all, of desires."
    scene img_emily_portrait_01
    "Emily, the oldest, has lived without you longer than her sister, and seems more attracted to women. Oddly enough, she's more naive than her sister."
    scene img_dakota_portrait_01
    "Dakota, on the other hand, has always been attracted to men, but only knows one in town, you."
    scene img_adriana_slut_01
    "After the war, morals became loose. They called it \"the true sexual liberation\". Thanks to leaps in science and technology there were less problems and more time for sex."
    scene img_intro_03
    "You and Adriana have taken advantage of this, but since you just became a professor at the local university, the opportunities seem to be widening even more..."
    "You are going to have to satisfy your needs, those of your wife, your daughters and your students. If your wife is not satisfied, she will go elsewhere, and this can be an opportunity to have fun together with her friends."
    "Your daughters' desire will grow if they see you frolicking at home or at university, becoming closer to their daddy."

    jump lbl_home_room_mc

label lbl_bypass:
    $ f_intro = False
    $ f_pee = True
    $ your_name = "John"
    $ v_time = 420

    jump lbl_home_living_room