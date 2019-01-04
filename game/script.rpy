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
    renpy.image("img_mc_body_01", "images/people/MC/mc_body_01.jpg")
    renpy.image("img_mc_body_02", "images/people/MC/mc_body_02.jpg")
    renpy.image("img_mc_bulge", "images/people/MC/mc_bulge.jpg")
    renpy.image("img_mc_dick", "images/people/MC/mc_dick.jpg")
    renpy.image("img_mc_sleep", "images/people/MC/mc_sleep.jpg")

    ## NPC
    # Bonnie
    renpy.image("img_bonnie_ass", "images/people/kennedy_leigh/bonnie_ass.jpg")
    renpy.image("img_bonnie_beach", "images/people/kennedy_leigh/bonnie_beach.jpg")
    renpy.image("img_bonnie_handjob_01", "images/people/kennedy_leigh/bonnie_handjob_01.jpg")
    renpy.image("img_bonnie_undress", "images/people/kennedy_leigh/bonnie_undress.jpg")

    for i in range(1,8):
        renpy.image("img_bonnie_shower_" + str(i).zfill(2), "images/people/kennedy_leigh/bonnie_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,2):
        renpy.image("npc_portrait_bonnie_" + str(i).zfill(2), "images/people/kennedy_leigh/bonnie_portrait_" + str(i).zfill(2) + ".jpg")

    # Dakota
    for i in range(1,2):
        renpy.image("npc_portrait_dakota_" + str(i).zfill(2), "images/people/dakota/dakota_portrait_" + str(i).zfill(2) + ".jpg")

    # Ellie
    renpy.image("img_ellie_spread", "images/people/julia_ann/ellie_spread.jpg")

    for i in range(1,2):
        renpy.image("img_ellie_dakota_" + str(i).zfill(2), "images/people/julia_ann/ellie_dakota_" + str(i).zfill(2) + ".jpg")

    for i in range(1,5):
        renpy.image("img_ellie_undress_" + str(i).zfill(2), "images/people/julia_ann/ellie_undress_" + str(i).zfill(2) + ".jpg")

    for i in range(1,4):
        renpy.image("npc_portrait_ellie_" + str(i).zfill(2), "images/people/julia_ann/ellie_portrait_" + str(i).zfill(2) + ".jpg")

    # Emma
    for i in range(1,4):
        renpy.image("img_emma_hospital_" + str(i).zfill(2), "images/people/sophie_dee/emma_hospital_" + str(i).zfill(2) + ".jpg")

    # Hitomi
    for i in range(1,7):
        renpy.image("npc_portrait_hitomi_" + str(i).zfill(2), "images/people/hitomi_tanaka/hitomi_portrait_" + str(i).zfill(2) + ".jpg")

    # Karen
    renpy.image("img_karen_blowjob_02", "images/people/jayden_jaymes/karen_blowjob_02.jpg")
    renpy.image("img_karen_kiss", "images/people/jayden_jaymes/karen_kiss.jpg")

    for i in range(1,3):
        renpy.image("img_karen_couch_" + str(i).zfill(2), "images/people/jayden_jaymes/karen_couch_" + str(i).zfill(2) + ".jpg")

    for i in range(1,10):
        renpy.image("npc_portrait_karen_" + str(i).zfill(2), "images/people/jayden_jaymes/karen_portrait_" + str(i).zfill(2) + ".jpg")

    # Lisa
    renpy.image("img_lisa_gym_01", "images/people/brandi_love/lisa_gym_01.jpg")
    renpy.image("img_lisa_kiss_01", "images/people/brandi_love/lisa_kiss_01.jpg")
    renpy.image("img_lisa_pool_01", "images/people/brandi_love/lisa_pool_01.jpg")

    for i in range(1,6):
        renpy.image("img_lisa_shower_" + str(i).zfill(2), "images/people/brandi_love/lisa_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,8):
        renpy.image("npc_portrait_lisa_" + str(i).zfill(2), "images/people/brandi_love/lisa_portrait_" + str(i).zfill(2) + ".jpg")

    # Lily
    renpy.image("img_lily_blowjob_01", "images/people/lilith_lust/lily_blowjob_01.jpg")
    renpy.image("img_lily_couch", "images/people/lilith_lust/lily_couch.jpg")
    renpy.image("img_lily_sex_01", "images/people/lilith_lust/lily_sex_01.jpg")

    for i in range(1,3):
        renpy.image("img_lily_nude_" + str(i).zfill(2), "images/people/lilith_lust/lily_nude_" + str(i).zfill(2) + ".jpg")

    for i in range(1,3):
        renpy.image("img_lily_boobs_" + str(i).zfill(2), "images/people/lilith_lust/lily_boobs_" + str(i).zfill(2) + ".jpg")

    for i in range(1,6):
        renpy.image("img_lily_shower_" + str(i).zfill(2), "images/people/lilith_lust/lily_portrait_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,13):
        renpy.image("npc_portrait_lily_" + str(i).zfill(2), "images/people/lilith_lust/lily_portrait_" + str(i).zfill(2) + ".jpg")

    # Marcy
    renpy.image("img_marcy_boobs_01", "images/people/brittney_white/marcy_boobs_01.jpg")

    for i in range(1,4):
        renpy.image("img_marcy_couch_" + str(i).zfill(2), "images/people/brittney_white/marcy_couch_" + str(i).zfill(2) + ".jpg")

    for i in range(1,3):
        renpy.image("img_marcy_nude_" + str(i).zfill(2), "images/people/brittney_white/marcy_nude_" + str(i).zfill(2) + ".jpg")

    for i in range(1,3):
        renpy.image("img_marcy_pool_" + str(i).zfill(2), "images/people/brittney_white/marcy_pool_" + str(i).zfill(2) + ".jpg")

    for i in range(1,6):
        renpy.image("img_marcy_undress_" + str(i).zfill(2), "images/people/brittney_white/marcy_undress_" + str(i).zfill(2) + ".jpg")

    for i in range(1,8):
        renpy.image("npc_portrait_marcy_" + str(i).zfill(2), "images/people/brittney_white/marcy_portrait_" + str(i).zfill(2) + ".jpg")

    # Maria
    for i in range(1,4):
        renpy.image("npc_portrait_maria_" + str(i).zfill(2), "images/people/ariana_marie/maria_portrait_" + str(i).zfill(2) + ".jpg")

    # Megan
    renpy.image("img_megan_boobs_02", "images/people/nikki_benz/megan_boobs_02.jpg")
    renpy.image("img_megan_handjob", "images/people/nikki_benz/megan_handjob.jpg")
    renpy.image("img_megan_taste", "images/people/nikki_benz/megan_taste.jpg")

    for i in range(1,5):
        renpy.image("npc_portrait_megan_" + str(i).zfill(2), "images/people/nikki_benz/megan_portrait_" + str(i).zfill(2) + ".jpg")

    # Mia
    renpy.image("img_mia_bikini", "images/people/mia_malkova/mia_bikini.jpg")
    renpy.image("img_mia_book", "images/people/mia_malkova/mia_book.jpg")
    renpy.image("img_mia_handjob", "images/people/mia_malkova/mia_handjob.jpg")
    renpy.image("img_mia_kiss_01", "images/people/mia_malkova/mia_kiss_01.jpg")
    renpy.image("img_mia_kiss_lisa", "images/people/mia_malkova/mia_kiss_lisa.jpg")
    renpy.image("img_mia_nude", "images/people/mia_malkova/mia_nude.jpg")
    renpy.image("img_mia_pussy", "images/people/mia_malkova/mia_pussy.jpg")

    for i in range(1,3):
        renpy.image("img_mia_ass_" + str(i).zfill(2), "images/people/mia_malkova/mia_ass_" + str(i).zfill(2) + ".jpg")

    for i in range(1,4):
        renpy.image("img_mia_shower_" + str(i).zfill(2), "images/people/mia_malkova/mia_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,18):
        renpy.image("npc_portrait_mia_" + str(i).zfill(2), "images/people/mia_malkova/mia_portrait_" + str(i).zfill(2) + ".jpg")

    # Nina
    for i in range(1,8):
        renpy.image("npc_portrait_nina_" + str(i).zfill(2), "images/people/alexis_texas/nina_portrait_" + str(i).zfill(2) + ".jpg")

    # Nyomi
    for i in range(1,4):
        renpy.image("img_nyomi_beach_" + str(i).zfill(2), "images/people/nyomi_bank/nyomi_beach_" + str(i).zfill(2) + ".jpg")

    # Pryia
    for i in range(1,5):
        renpy.image("img_priya_pool_" + str(i).zfill(2), "images/people/priya_rai/priya_pool_" + str(i).zfill(2) + ".jpg")

    # Rikki
    for i in range(1,2):
        renpy.image("npc_portrait_rikki_" + str(i).zfill(2), "images/people/rikki_six/rikki_portrait_" + str(i).zfill(2) + ".jpg")

    # Sarah
    renpy.image("img_sarah_facial", "images/people/diamond_jackson/sarah_facial.jpg")
    renpy.image("img_sarah_nude", "images/people/diamond_jackson/sarah_nude.jpg")

    for i in range(1,3):
        renpy.image("img_sarah_gym_" + str(i).zfill(2), "images/people/diamond_jackson/sarah_gym_" + str(i).zfill(2) + ".jpg")

    for i in range(1,9):
        renpy.image("img_sarah_shower_" + str(i).zfill(2), "images/people/diamond_jackson/sarah_shower_" + str(i).zfill(2) + ".jpg")

    for i in range(1,8):
        renpy.image("npc_portrait_sarah_" + str(i).zfill(2), "images/people/diamond_jackson/sarah_portrait_" + str(i).zfill(2) + ".jpg")

    # Veronica
    renpy.image("img_veronica_bikini", "images/people/angela_white/veronica_bikini.jpg")

    for i in range(2,5):
        renpy.image("img_veronica_gym_" + str(i).zfill(2), "images/people/angela_white/veronica_gym_" + str(i).zfill(2) + ".jpg")

    for i in range(1,3):
        renpy.image("npc_portrait_veronica_" + str(i).zfill(2), "images/people/angela_white/veronica_portrait_" + str(i).zfill(2) + ".jpg")

    ## NPC OTHERS
    renpy.image("npc_portrait_jason_01", "images/people/others/portrait_jason_01.jpg")
    renpy.image("npc_portrait_jason_02", "images/people/others/portrait_jason_02.jpg")
    renpy.image("npc_portrait_grandma", "images/people/others/portrait_grandma.jpg")
    renpy.image("npc_portrait_marcus", "images/people/others/portrait_marcus.jpg")
    renpy.image("npc_portrait_mr_smith_01", "images/people/others/portrait_mr_smith_01.jpg")
    renpy.image("npc_portrait_mr_smith_02", "images/people/others/portrait_mr_smith_02.jpg")

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
default mc_portrait = "old"
image side portrait_mc = ConditionSwitch("mc_portrait == 'old'", "images/portrait/portrait_mc1.jpg", "mc_portrait == 'new'", "images/portrait/portrait_mc2.jpg")
define me = DynamicCharacter("your_name", image="portrait_mc", color = clr_dark_red)

# NPC
define bonnie = Character("Bonnie", image = "portrait_bonnie", color = clr_sand)
define dakota = Character("Dakota", image = "portrait_dakota", color = clr_gold)
define ellie = Character("Ellie", image = "portrait_ellie", color = clr_gold)
define emma = Character("Emma", image = "portrait_emma", color = clr_auburn)
define hitomi = Character("Hitomi", image = "portrait_hitomi", color = clr_ginger)
define jane = Character("Jane", image = "portrait_jane", color = clr_gray)
define karen = Character("Karen", image = "portrait_karen", color = clr_gray)
define lily = Character("Lily", image = "portrait_lily", color = clr_auburn)
define lisa = Character("Lisa", image = "portrait_lisa", color = clr_gold)
define marcy = Character("Marcy", image = "portrait_marcy", color = clr_chestnut_brown)
define megan = Character("Megan", image = "portrait_megan", color = clr_sand)
define mia = Character("Mia", image = "portrait_mia", color = clr_palegold)
define nina = Character("Nina", image = "portrait_nina", color = clr_sand)
define nyomi = Character("Nyomi", image = "portrait_nyomi", color = clr_chestnut_brown)
define priya = Character("Priya", image = "portrait_priya", color = clr_gray)
define rikki = Character("Rikki", image = "portrait_rikki", color = clr_palegold)
define sarah = Character("Sarah", image = "portrait_sarah", color = clr_chestnut_brown)
define veronica = Character("Veronica", image = "portrait_veronica", color = clr_gray)

image side portrait_bonnie = "images/portrait/portrait_bonnie.jpg"
image side portrait_dakota = "images/portrait/portrait_dakota.jpg"
image side portrait_ellie = "images/portrait/portrait_ellie.jpg"
image side portrait_emma = "images/portrait/portrait_emma.jpg"
image side portrait_hitomi = "images/portrait/portrait_hitomi.jpg"
image side portrait_jane = "images/portrait/portrait_jane.jpg"
image side portrait_karen = "images/portrait/portrait_karen.jpg"
image side portrait_lily = "images/portrait/portrait_lily.jpg"
image side portrait_lisa = "images/portrait/portrait_lisa.jpg"
image side portrait_marcy = "images/portrait/portrait_marcy.jpg"
image side portrait_megan = "images/portrait/portrait_megan.jpg"
image side portrait_mia = "images/portrait/portrait_mia.jpg"
image side portrait_nina = "images/portrait/portrait_nina.jpg"
image side portrait_nyomi = "images/portrait/portrait_nyomi.jpg"
image side portrait_priya = "images/portrait/portrait_priya.jpg"
image side portrait_rikki = "images/portrait/portrait_rikki.jpg"
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
image loc_home_bathroom1 = "images/location/loc_home_bathroom1.jpg"
image loc_home_bathroom2 = "images/location/loc_home_bathroom2.jpg"
image loc_home_kitchen = "images/location/loc_home_kitchen.jpg"
image loc_home_living_room = "images/location/loc_home_living_room.jpg"
image loc_home_pool = "images/location/loc_home_pool.jpg"
image loc_home_room_lisa_bed = "images/location/loc_home_room_lisa_bed.jpg"
image loc_home_room_mc = "images/location/loc_home_room_mc.jpg"
image loc_home_room_mc_bed = "images/location/loc_home_room_mc_bed.jpg"
image loc_home_room_mia = "images/location/loc_home_room_mia.jpg"

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

## VIDEOS - NPC
# MC
image vid_mc_erection = Movie(play="images/people/MC/MC_erection.webm")

# Bonnie
image vid_bonnie_blowjob_01 = Movie(play="images/people/kennedy_leigh/bonnie_blowjob_01.webm", size=(800,426))
image vid_bonnie_blowjob_02 = Movie(play="images/people/kennedy_leigh/bonnie_blowjob_02.webm", size=(960,540))
image vid_bonnie_handjob_02 = Movie(play="images/people/kennedy_leigh/bonnie_handjob_02.webm", size=(900,506))

# Ellie
image vid_ellie_cuni = Movie(play="images/people/julia_ann/ellie_cuni.webm", size=(800,450))

# Hitomi
image vid_hitomi_boobs = Movie(play="images/people/hitomi_tanaka/hitomi_boobs.webm")

# Karen
image vid_karen_69 = Movie(play="images/people/jayden_jaymes/karen_69.webm")
image vid_karen_blowjob_01 = Movie(play="images/people/jayden_jaymes/karen_blowjob_01.webm", size=(1000,560))
image vid_karen_blowjob_03 = Movie(play="images/people/jayden_jaymes/karen_blowjob_03.webm", size=(866,406))
image vid_karen_boobs = Movie(play="images/people/jayden_jaymes/karen_boobs.webm", size=(1000,562))
image vid_karen_cuni = Movie(play="images/people/jayden_jaymes/karen_cuni.webm", size=(1080,480))

# Lily
image vid_lily_kiss_01 = Movie(play="images/people/lilith_lust/lily_kiss_01.webm", size=(960,544))
image vid_lily_kiss_02 = Movie(play="images/people/lilith_lust/lily_kiss_02.webm", size=(1000,460))
image vid_lily_sex_02 = Movie(play="images/people/lilith_lust/lily_sex_02.webm", size=(1000,576))
image vid_lily_sex_03 = Movie(play="images/people/lilith_lust/lily_sex_03.webm", size=(1000,502))

# Lisa
image vid_lisa_bathroom_incident = Movie(play="images/people/brandi_love/lisa_bathroom_incident.webm", size=(590,590))
image vid_lisa_gym_02 = Movie(play="images/people/brandi_love/lisa_gym_02.webm", size=(1080,606))
image vid_lisa_handjob_cum = Movie(play="images/people/brandi_love/lisa_handjob_cum.webm", size=(816,460))
image vid_lisa_kiss_02 = Movie(play="images/people/brandi_love/lisa_kiss_02.webm", size=(1000,540))
image vid_lisa_kiss_03 = Movie(play="images/people/brandi_love/lisa_kiss_03.webm", size=(800,778))
image vid_lisa_show_boobs = Movie(play="images/people/brandi_love/lisa_boobs_01.webm")
image vid_lisa_room_masturbate = Movie(play="images/people/brandi_love/lisa_masturbation.webm")
image vid_lisa_undress = Movie(play="images/people/brandi_love/lisa_undress.webm", size=(450,652))

# Marcy
image vid_marcy_blowjob_01 = Movie(play="images/people/brittney_white/marcy_blowjob_01.webm", size=(920,800))
image vid_marcy_blowjob_02 = Movie(play="images/people/brittney_white/marcy_blowjob_02.webm", size=(738,744))
image vid_marcy_boobs_02 = Movie(play="images/people/brittney_white/marcy_boobs_02.webm", size=(630,716))
image vid_marcy_boobs_03 = Movie(play="images/people/brittney_white/marcy_boobs_03.webm", size=(1000,562))
image vid_marcy_boobs_bounce_01 = Movie(play="images/people/brittney_white/marcy_boobs_bounce_01.webm", size=(552,780))
image vid_marcy_boobs_bounce_02 = Movie(play="images/people/brittney_white/marcy_boobs_bounce_02.webm", size=(552,780))
image vid_marcy_facial = Movie(play="images/people/brittney_white/marcy_facial.webm", size=(1000,600))
image vid_marcy_kiss = Movie(play="images/people/brittney_white/marcy_kiss.webm", size=(1000,560))
image vid_marcy_masturbate = Movie(play="images/people/brittney_white/marcy_masturbate.webm", size=(704,512))
image vid_marcy_sex_01 = Movie(play="images/people/brittney_white/marcy_sex_01.webm", size=(365,800))
image vid_marcy_sex_02 = Movie(play="images/people/brittney_white/marcy_sex_02.webm")

# Megan
image vid_megan_blowjob = Movie(play="images/people/nikki_benz/megan_blowjob.webm", size=(750,844))
image vid_megan_boobs_01 = Movie(play="images/people/nikki_benz/megan_boobs_01.webm", size=(800,450))
image vid_megan_lesbian = Movie(play="images/people/nikki_benz/megan_lesbian.webm", size=(1000,450))

# Mia
image vid_mia_ass_03 = Movie(play="images/people/mia_malkova/mia_ass_03.webm", size=(437,791))
image vid_mia_ass_04 = Movie(play="images/people/mia_malkova/mia_ass_04.webm", size=(800,680))
image vid_mia_finger = Movie(play="images/people/mia_malkova/mia_finger.webm", size=(764,610))
image vid_mia_handjob_cum = Movie(play="images/people/mia_malkova/mia_handjob_cum.webm", size=(800,418))
image vid_mia_masturbate = Movie(play="images/people/mia_malkova/mia_masturbate.webm", size=(1000,496))

# Rikki
image vid_rikki_blowjob_01 = Movie(play="images/people/rikki_six/rikki_blowjob_01.webm", size=(650,833))

# Sarah
image vid_sarah_titjob = Movie(play="images/people/diamond_jackson/sarah_titjob.webm", size=(720,540))

# Veronica
image vid_veronica_blowjob = Movie(play="images/people/angela_white/veronica_blowjob.webm", size=(960,540))
image vid_veronica_gym_01 = Movie(play="images/people/angela_white/veronica_gym_01.webm", size=(735,721))

## VIDEOS - LOCATION
# Beach
image vid_beach_boobs_01 = Movie(play="images/people/beach/beach_boobs_01.webm", size=(1000,742))
image vid_beach_boobs_02 = Movie(play="images/people/beach/beach_boobs_02.webm", size=(584,440))
image vid_beach_boobs_03 = Movie(play="images/people/beach/beach_boobs_03.webm", size=(800,660))

# Church
image vid_church_nun_blowjob = Movie(play="images/people/church/nun_blowjob.webm", size=(840,416))

# College
image vid_college_run = Movie(play="images/events/college_run.webm")
image vid_college_shower_01 = Movie(play="images/events/college_shower_01.webm", size=(620,612))
image vid_college_shower_02 = Movie(play="images/events/college_shower_02.webm", size=(598,736))
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
    ## EVENTS
    # Normal
    $ tb_event = {3: {}, 4: {}}

    $ tb_event[3] = {
        "city_beach": {},
        "city_gym": {},
        "city_home_lily": {},
        "city_home_marcy": {},
        "city_home_marcy_pool": {},
        "city_home_marcy_room": {},
        "city_home_marcy_room_sarah": {},
        "city_home_priya": {},
        "city_mall": {},
        "city_park": {},
        "city_pgp_corporation": {},
        "college_garden": {},
        "college_gym": {},
        "college_office_ellie": {},
        "home_kitchen": {},
        "home_living_room": {},
        "home_room_mc": {},
        "home_room_mia": {}
    }

    $ tb_event[3]["city_beach"] = { "nyomi": 0 }
    $ tb_event[3]["city_gym"] = { "lisa": 0, "sarah": 0, "veronica": 0 }
    $ tb_event[3]["city_home_lily"] = { "lily": 0, "lily_sex": 0 }
    $ tb_event[3]["city_home_marcy"] = { "marcy": 0 , "sarah": 0}
    $ tb_event[3]["city_home_marcy_pool"] = { "marcy": 0 }
    $ tb_event[3]["city_home_marcy_room"] = { "marcy": 0 }
    $ tb_event[3]["city_home_marcy_room_sarah"] = { "sarah": 0 }
    $ tb_event[3]["city_home_priya"] = { "priya": 0 }
    $ tb_event[3]["city_mall"] = { "karen": 0 }
    $ tb_event[3]["city_park"] = { "marcy": 0 }
    $ tb_event[3]["city_pgp_corporation"] = { "lily": 0 }
    $ tb_event[3]["college_garden"] = { "veronica": 0 }
    $ tb_event[3]["college_gym"] = { "bonnie": 0 }
    $ tb_event[3]["college_office_ellie"] = { "aphrodisiac": 0 }
    $ tb_event[3]["home_kitchen"] = { "mia": 0 }
    $ tb_event[3]["home_living_room"] = { "lisa_hj": 0 }
    $ tb_event[3]["home_room_mc"] = { "mia_sex": 0 }
    $ tb_event[3]["home_room_mia"] = { "mia_finger": 0 }

    # Repeatable
    $ tb_repeatable = {3: {}, 4: {}}

    $ tb_repeatable[3] = {
        "college_nurse": {}
    }

    $ tb_repeatable[3]["college_nurse"] = { "bj": 0, "hj": 0 }


    # Flags
    $ f_bypass = False
    $ f_name_prompt = True
    $ f_day1_lisa_bathroom_incident = False
    $ f_day2_mall_karen = False
    $ f_day2_nurse = False
    $ f_day2_shower = False
    $ f_day3_shower = False
    $ f_day3_spy = False
    $ f_day4_jane_friend = False

    # Variables
    $ v_day = 1
    $ v_time = 0
    $ v_time_readable = ""
    $ v_localisation = ""

    # Start
    hide screen main_menu
    scene black onlayer background

    "Do you have play previous version and want to jump directly to new content?"
    menu:
        "Jump to new content":
            $ f_bypass = False
            #jump lbl_name_input
            jump lbl_bypass
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
    $ mc_portrait = "new"
    $ v_day = 3
    $ v_time = 720

    $ f_day1_lisa_bathroom_incident = True
    $ f_day2_mall_karen = True
    $ f_day2_nurse = True
    $ f_day2_shower = True
    $ f_day3_shower = True
    $ f_day3_spy = False

    jump lbl_city_map