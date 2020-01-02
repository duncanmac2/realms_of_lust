#### LOCATIONS ####
label lbl_college_class:
    call main_show
    scene loc_college_class

    if v_day == 1:
        jump lbl_college_class_day1
    elif v_day == 2:
        jump lbl_college_class_day2
    elif v_day == 3 and v_time < 720:
        jump lbl_college_class_day3
    elif v_day == 4:
        jump lbl_college_class_day4

label lbl_college_corridor:
    call main_show
    scene loc_college_corridor

    if v_day == 4:
        jump lbl_college_corridor_day4

label lbl_college_garden:
    call main_show
    scene loc_college_garden

    if v_day == 1:
        jump lbl_college_garden_day1
    elif v_day == 2:
        jump lbl_college_garden_day2
    elif v_day == 3:
        jump lbl_college_garden_day3
    elif v_day == 4:
        jump lbl_college_garden_day4

label lbl_college_gym:
    call main_show
    scene loc_college_gym

    if v_day == 3:
        jump lbl_college_gym_day3

label lbl_college_locker_room:
    call main_show
    scene loc_college_locker_room

    if v_day == 1:
        jump lbl_college_locker_room_day1
    elif v_day == 2:
        jump lbl_college_locker_room_day2
    elif v_day == 3:
        jump lbl_college_locker_room_day3
    elif v_day == 4:
        jump lbl_college_locker_room_day4

label lbl_college_nurse:
    call main_show
    scene loc_college_nurse

    if v_day == 2:
        jump lbl_college_nurse_day2
    elif v_day == 3:
        jump lbl_college_nurse_day3
    elif v_day == 4:
        jump lbl_college_nurse_day4

label lbl_college_office_ellie:
    call main_show
    scene loc_college_office_ellie

    if v_day == 3:
        jump lbl_college_office_ellie_day3
    elif v_day == 4:
        jump lbl_college_office_ellie_day4

label lbl_college_shower_men:
    call main_show
    scene loc_college_shower_men

    if v_day == 1:
        jump lbl_college_shower_men_day1

label lbl_college_teacher_office:
    call main_show
    scene loc_college_teacher_office

    if v_day == 3:
        jump lbl_college_office_ellie
    elif v_day == 4:
        jump lbl_college_office_ellie

label lbl_college_yard:
    $ v_localisation = "college_yard"

    call main_show
    scene loc_college_yard
    jump lbl_college_yard_events

#### EVENTS ####
### SCHOOLYARD ###
label lbl_college_yard_events:
    "The college part will be implemented in the next version."

    $ v_time = 1050
    $ tb_events["home_bathroom"]["adriana"] = False
    $ tb_events["home_bathroom"]["dakota"] = False
    $ tb_events["home_bathroom"]["emily"] = False
    $ tb_events["home_kitchen"]["adriana"] = False
    $ tb_events["home_kitchen"]["dakota"] = False
    $ tb_events["home_kitchen"]["emily"] = False

    jump lbl_home_living_room