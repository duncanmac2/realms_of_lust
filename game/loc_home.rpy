#### LOCATIONS ####
label lbl_home_backyard:
    scene loc_home_backyard
    jump lbl_home_backyard_events

label lbl_home_bathroom:
    scene loc_home_bathroom
    jump lbl_home_bathroom_events

label lbl_home_kitchen:
    scene loc_home_kitchen
    jump lbl_home_kitchen_events

label lbl_home_living_room:
    $ v_localisation = "home_living_room"

    call main_show
    scene loc_home_living_room

    if f_intro:
        jump lbl_home_livingroom_adriana_s01_01
    else:
        call screen scr_navigation

label lbl_home_pool:
    scene loc_home_pool
    jump lbl_home_pool_events

label lbl_home_room_dakota:
    scene loc_home_room_dakota
    jump lbl_home_room_dakota_events

label lbl_home_room_emily:
    scene loc_home_room_emily
    jump lbl_home_room_emily_events

label lbl_home_room_mc:
    scene loc_home_room_mc

    if f_intro:
        jump lbl_home_bathroom_adriana_s01_01
    elif tb_stats["lust"]["adriana"] == 100 and v_time == 420:
        jump lbl_adriana_lust
    else:
        jump lbl_home_room_mc_events

#### EVENTS ####
### ROOM MC ###
label lbl_home_room_mc_events:
    jump lbl_home_living_room

### BACKYARD ###
label lbl_home_backyard_events:
    $ attendee = func_check_time(v_time, tb_time["home_backyard"])
    if attendee.find("dakota") != -1 and not tb_events["home_backyard"]["dakota"]:
        jump lbl_home_backyard_dakota_s01
    else:
        "Nobody here right now."
        jump lbl_home_living_room

## Dakota S01 ##
label lbl_home_backyard_dakota_s01:
    scene img_dakota_backyard_s01_01 with d3
    "Dakota is here resting after school."

    menu:
        "You're watching her.":
            scene img_dakota_backyard_s01_02 with d1
            "She pretends to be prissy."
            scene img_dakota_backyard_s01_03 with d1
            "Only to tease you."
            scene img_dakota_backyard_s01_04 with d1
            "With her petite ass."
            scene img_dakota_backyard_s01_05 with d1
            "And her tight pussy."
            scene img_dakota_backyard_s01_06 with d1
            "And her small tits."
            scene img_dakota_backyard_s01_07 with d1
            "And her tight asshole..."
            scene img_dakota_backyard_s01_08 with d1
            dakota "Enjoying the show daddy?"
            me "Can't get enough of it sweetie."

            call time_change(5)

        "Approach her and touch her tight.":
            scene img_dakota_backyard_s01_09 with d3
            dakota "Daddy?"
            scene img_dakota_backyard_s01_10 with d3
            me "Yes sweetie?"
            dakota "Can I see your muscles?"
            me "Only if you show me your tits."
            scene img_dakota_backyard_s01_11 with d3
            dakota "Who'd like to see my small boobs?"
            scene img_dakota_backyard_s01_12 with d3
            me "Your daddy of course. Give me a kiss."
            scene img_dakota_backyard_s01_13 with d3
            dakota "*Moan*"
            scene img_dakota_backyard_s01_14 with d3
            dakota "*Slurp*"
            scene img_dakota_backyard_s01_15 with d3
            dakota "Ahhh daddy."
            scene img_dakota_backyard_s01_16 with d3
            dakota "Mmmmh."
            scene img_dakota_backyard_s01_17 with d3
            dakota "Do you like them?"
            scene img_dakota_backyard_s01_18 with d3
            me "They are so pretty you know."
            scene img_dakota_backyard_s01_19 with d3
            dakota "Thamkm."
            scene img_dakota_backyard_s01_20 with d3
            dakota "Bad daddy! Just because you just paid me a compliment doesn't mean you should try to go down *giggle*."
            scene img_dakota_backyard_s01_21 with d3
            me "I love you so much sweetie, I might not be able to control myself."
            dakota "Me too daddy."

            call time_change(10)

    $ tb_events["home_backyard"]["dakota"] = True

    menu:
        "{color=#858585}-- ??? --{/color}" if tb_stats["lvl"]["dakota"] == 0:
            call lbl_not_yet
            jump lbl_home_living_room

        "Join her." if tb_stats["lvl"]["dakota"] > 0:
            "action"
            jump lbl_home_living_room

        "Back inside.":
            jump lbl_home_living_room

### BATHROOM ###
label lbl_home_bathroom_events:
    $ attendee = func_check_time(v_time, tb_time["home_bathroom"])

    if attendee.find("dakota") != -1 and not tb_events["home_bathroom"]["dakota"]:
        if f_pee:
            jump lbl_home_bathroom_dakota_s01
        else:
            jump lbl_home_living_room
    elif attendee.find("emily") != -1 and not tb_events["home_bathroom"]["emily"]:
        jump lbl_home_bathroom_emily_s02_01
    else:
        "Nobody here right now."
        jump lbl_home_living_room

## Adriana S01 ##
label lbl_home_bathroom_adriana_s01_01:
    "The sun is shining through the window."
    me "What time is it? Shit it's late, the alarm didn't go off. Being late on your first day..."
    me "I have to take a shower, better hurry."
    scene img_adriana_bathroom_s01_01 with d3
    adriana "Love, you're gonna be late."
    scene img_adriana_bathroom_s01_02 with d1
    me "I know, I know, I was just about to take a shower."
    scene img_adriana_bathroom_s01_03 with d1
    adriana "You don't have to hide it, you know, it's not like I know it intimately."
    me "Yes, but..."
    scene img_adriana_bathroom_s01_04 with d1
    adriana "No but, now because of you I want to fuck. Would you rather satisfy your wife or not be late?"
    menu:
        "It's my first day!":
            jump lbl_college_yard

        "They can wait for me for a little.":
            scene img_black
            show vid_adriana_bathroom_s01_hj with d1
            adriana "Good answer."
            me "You're the best honey."
            adriana "Oh I know. And guess who is the best to suck your delicious dick?"
            hide vid_adriana_bathroom_s01_hj with d1
            show vid_adriana_bathroom_s01_bj_01 with d3
            me "Hmm, you as always."
            window hide
            pause

            jump lbl_home_bathroom_adriana_s01_02

label lbl_home_bathroom_adriana_s01_02:
    menu:
        "Lick my balls my slutty whore.":
            show vid_adriana_bathroom_s01_bj_02 with d1
            me "That's my girl, lick my balls."
            pause
            hide vid_adriana_bathroom_s01_bj_02 with d1
            jump lbl_home_bathroom_adriana_s01_02

        "Faster my lovely bitch.":
            show vid_adriana_bathroom_s01_bj_03 with d1
            me "Hmmm yes like that."
            pause
            hide vid_adriana_bathroom_s01_bj_03 with d1
            jump lbl_home_bathroom_adriana_s01_02

        "I want to fuck your perverted face.":
            show vid_adriana_bathroom_s01_bj_04 with d1
            me "Take the dick you love so much in your filthy mouth."
            pause
            hide vid_adriana_bathroom_s01_bj_04 with d1
            jump lbl_home_bathroom_adriana_s01_02

        "Let's fuck.":
            hide vid_adriana_bathroom_s01_bj_01 with d1
            jump lbl_home_bathroom_adriana_s01_03

label lbl_home_bathroom_adriana_s01_03:
    show vid_adriana_bathroom_s01_vg_01 with d1
    adriana "Grab my tits love, please."
    me "With pleasure."
    hide vid_adriana_bathroom_s01_vg_01 with d1
    show vid_adriana_bathroom_s01_vg_02 with d1
    adriana "You love my little tits daddy?"
    me "Oh yeah, and don't worry, they're gonna grow up when you're older."
    adriana "I'm sure if you spray them with your cum they'll grow."
    me "Coming in your tight pussy work great too."
    hide vid_adriana_bathroom_s01_vg_02 with d1
    show vid_adriana_bathroom_s01_vg_03 with d1
    adriana "*Moan* yesss you can come all you want in my pussy, daddy."
    me "You're moaning so much you're going to alert our daughters."
    adriana "*Giggle* maybe that's the point."
    me "You perverted filthy whore. I love you so much!"
    hide vid_adriana_bathroom_s01_vg_03 with d1
    show img_adriana_bathroom_s01_05 with vpunch
    dakota "Mommy, I need to shower now or I'm gonna be late for school!"
    adriana "Wait a little, your dad's busy pudding my pussy hard."
    dakota "As always... use your bedroom for fuck sake!"
    me "Alright sweetie, we will."
    hide img_adriana_bathroom_s01_05 with d3
    show vid_adriana_bathroom_s01_vg_04 with d3
    adriana "Our lovely little bitch doesn't know what she missing."
    me "With our help, I'm sure she can learn..."
    adriana "You have no idea how wet it makes me thinking about it!"
    me "You'd like that, wouldn't you, watching your daughters get fucked by my big cock?!"
    hide vid_adriana_bathroom_s01_vg_04 with d1
    show vid_adriana_bathroom_s01_vg_05 with d1
    adriana "Fuck yesss daddy, I can't wait!"
    me "Maybe their kinky mother would like to lick their pussy?"
    adriana "*Moan* more than ever. Licking their daddy's hot sperm dripping out of their fuck holes, hmmm..."
    hide vid_adriana_bathroom_s01_vg_05 with d3
    show vid_emily_bathroom_s01_mas with d3
    emily "{size=-7}*Whisper* Daddy and mommy are such perverts...{/size}"
    adriana "Those filthy thoughts... faster, yesss, I need it faster!"
    hide vid_emily_bathroom_s01_mas with d1
    show vid_adriana_bathroom_s01_vg_06 with d1
    me "At your command, princess."
    adriana "Yesss... *moan* yes!"
    me "You like that don't you, fucking slut?"
    adriana "*Moan* yes daddy, I like it so much!"
    me "Didn't you hear a noise?"
    hide vid_adriana_bathroom_s01_vg_06 with d1
    show img_emily_bathroom_s01_01 with vpunch
    emily "Shit!"
    adriana "{size=-7}*Whisper* I think we have a little spy...{/size}"
    adriana "Time for a little game."
    hide img_emily_bathroom_s01_01 with d1
    show img_emily_bathroom_s01_02
    emily "{size=-7}*Whisper* What?{/size}"
    adriana "Please daddy, lick my pussy please."
    hide img_emily_bathroom_s01_02 with d1
    show vid_adriana_bathroom_s01_cun with d1
    me "Only because you've been a good girl."
    adriana "And my ass too! Too bad we don't have the time for a good ass fucking."
    me "We'll have plenty of time when you get back from school."
    adriana "Speaking of school, hurry up and make me come, I gotta go."
    hide vid_adriana_bathroom_s01_cun with d1
    show vid_adriana_bathroom_s01_vg_07 with d1
    adriana "You're the best dick in town daddy, I want a daughter from you!"
    me "I've told you a thousand times already sweetheart, daddy can't get you pregnant."
    adriana "We can always try it, fill my pussy with your hot cum pleassse."
    me "Daddy can't resist your wishes..."
    hide vid_adriana_bathroom_s01_vg_07 with d1
    show img_emily_bathroom_s01_01 with d1
    emily "{size=-7}*Whisper* Are they really talking about getting me pregnant? Naah must be their \"little\" game.{/size}"
    hide img_emily_bathroom_s01_01 with d1
    show vid_adriana_bathroom_s01_vg_08 with d1
    me "Almost here sweetheart!"
    adriana "Make me a baby daddy, make me a baby!"
    hide vid_adriana_bathroom_s01_vg_08 with d1
    show img_white
    pause .1
    with hpunch
    hide img_white
    pause .2
    show img_white
    pause .2
    hide img_white
    pause .2
    with hpunch
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_bathroom_s01_cum.webm")
    show img_adriana_bathroom_s01_06 with d1
    adriana "Oh no, it's all slipping away. I guess the baby won't be for this time."
    me "That's a shame. And now time for school sweetheart!"
    adriana "Yes daddy... Can't wait till evening."
    me "You're telling me!"
    hide img_adriana_bathroom_s01_06 with d1
    show img_emily_bathroom_s01_02 with d1
    emily "{size=-7}*Whisper* Time to go too. I was hoping it would last longer, now I need my girlfriend to make me come.{/size}"
    hide img_emily_bathroom_s01_02 with d5

    jump lbl_college_yard

## Dakota S01 ##
label lbl_home_bathroom_dakota_s01:
    scene img_black
    show vid_dakota_bathroom_s01_pee_01 with d5
    me "What are you..."
    dakota "I'm just peeing in the bathtub, daddy. Don't pretend you don't like it."
    me "Hehe, I will not."
    window hide
    pause
    hide vid_dakota_bathroom_s01_pee_01 with d3
    $ renpy.movie_cutscene("images/people/dakota.skye/dakota_bathroom_s01_pee_02.webm")
    show img_dakota_bathroom_s01_pee_03
    dakota "Oh, how come you're still here?"

    $ tb_events["home_bathroom"]["dakota"] = True

    menu:
        "{color=#858585}-- ??? --{/color}" if tb_stats["lvl"]["dakota"] == 0:
            call lbl_not_yet
            jump lbl_home_living_room

        "Join her." if tb_stats["lvl"]["dakota"] > 0:
            "action"
            jump lbl_home_living_room

        "Go outside.":
            jump lbl_home_living_room

## Emily S02 ##
label lbl_home_bathroom_emily_s02_01:
    scene img_black
    show vid_emily_bathroom_s02_01 with d3
    window hide
    pause
    "Emily is taking a shower."

    $ tb_events["home_bathroom"]["emily"] = True

    menu:
        "Interrupt her directly." if tb_stats["lvl"]["emily"] > 0:
            hide vid_emily_bathroom_s02_01 with d3
            jump lbl_home_bathroom_emily_s02_02

        "Keep watching silently.":
            hide vid_emily_bathroom_s02_01 with d3
            show vid_emily_bathroom_s02_02 with d3
            pause
            hide vid_emily_bathroom_s02_02 with d3
            show vid_emily_bathroom_s02_mas with d3
            pause

            menu:
                "{color=#858585}-- ??? --{/color}" if tb_stats["lvl"]["emily"] == 0:
                    hide vid_emily_bathroom_s02_mas with d3
                    call lbl_not_yet
                    jump lbl_home_living_room

                "Interrupt her." if tb_stats["lvl"]["emily"] > 0:
                    hide vid_emily_bathroom_s02_mas with d3
                    $ renpy.movie_cutscene("images/people/emily.willis/emily_bathroom_s02_03.webm")
                    show img_emily_bathroom_s02_04 with d1
                    me "Sweetie?"
                    hide img_emily_bathroom_s02_04 with d1

                    jump lbl_home_bathroom_emily_s02_02

                "Leave her.":
                    jump lbl_home_living_room

        "Leave her.":
            $ tb_events["home_bathroom"]["emily"] = False
            jump lbl_home_living_room

label lbl_home_bathroom_emily_s02_02:
    show img_emily_bathroom_s02_05 with d1
    emily "Daddy! Want to join me?"
    me "Of course..."
    hide img_emily_bathroom_s02_05 with d3
    show vid_emily_bathroom_s02_k with d3
    emily "You never miss a chance to play with one of your girls *giggle*."
    me "Never!"
    hide vid_emily_bathroom_s02_k with d2
    show vid_emily_bathroom_s02_fg with d2
    me "And most of all, I have to make sure my girls are clean."
    pause
    hide vid_emily_bathroom_s02_fg with d2
    show vid_emily_bathroom_s02_hj with d2
    emily "If it's like that, I'll make sure my daddy's clean too!"
    me "I have a better tool at my disposal for this job."
    hide vid_emily_bathroom_s02_hj with d2
    show vid_emily_bathroom_s02_bj_01 with d2
    me "Like that sweetie, clean your father dick with your mouth."
    hide vid_emily_bathroom_s02_bj_01 with d2
    show img_emily_bathroom_s02_06 with d2
    me "Now that we're all clean, daddy can take care of your pussy."
    hide img_emily_bathroom_s02_06 with d3
    show vid_emily_bathroom_s02_cun with d3
    emily "Yesss dadddyy *moan*{w=3.0} eat my neat pussy."

    $ tmp_count = 0
    jump lbl_home_bathroom_emily_s02_03


label lbl_home_bathroom_emily_s02_03:
    menu:
        "{color=#858585}-- ??? --{/color}" if tb_stats["lvl"]["emily"] == 1:
            call lbl_not_yet
            jump lbl_home_bathroom_emily_s02_03

        "I think my cock's not shiny enough.":
            show vid_emily_bathroom_s02_bj_02 with d3
            me "Makes it shine my little whore."
            hide vid_emily_bathroom_s02_bj_02 with d3

            $ tmp_count += 1
            jump lbl_home_bathroom_emily_s02_03

        "Not shiny {b}enough{/b}!" if tmp_count >= 1:
            show vid_emily_bathroom_s02_bj_03 with d3
            me "You'll have to excuse me, you suck too well to pass it up."
            emily "*Moan*"
            hide vid_emily_bathroom_s02_bj_03 with d3

            $ tmp_count += 1
            jump lbl_home_bathroom_emily_s02_03

        "I gonna have to clean your pussy more thoroughly." if tb_stats["lvl"]["emily"] > 1:
            show vid_emily_bathroom_s02_vg_01 with d3
            me "You like it deep don't you slut?"
            emily "Yesss daddy *moan*{w=0.5} deep and hard."
            me "Just like your whore mother."
            emily "Just like mommy!"
            hide vid_emily_bathroom_s02_vg_01 with d3

            $ tmp_count += 1
            jump lbl_home_bathroom_emily_s02_03

        "I'll sweep your baby hole." if tb_stats["lvl"]["emily"] > 1:
            show vid_emily_bathroom_s02_vg_02 with d3
            me "Do my big tool feels good?"
            emily "Ahhh *moan* aah...{w=0.5} best tool in the world."
            pause
            hide vid_emily_bathroom_s02_vg_02 with d3

            $ tmp_count += 1
            jump lbl_home_bathroom_emily_s02_03

        "I'm gonna make you come, sweetie." if tb_stats["lvl"]["emily"] > 1:
            show vid_emily_bathroom_s02_vg_03 with d3
            emily "Yesss daddy *moan* yesss!"
            hide vid_emily_bathroom_s02_vg_03 with d3

            $ tmp_count += 1
            jump lbl_home_bathroom_emily_s02_03

        "Now for the finishing touch." if tmp_count >= 2:
            hide vid_emily_bathroom_s02_cun
            $ renpy.movie_cutscene("images/people/emily.willis/emily_bathroom_s02_cum_01.webm")
            show img_emily_bathroom_s02_07 with d1
            me "Swallow it all my whore princess."
            hide img_emily_bathroom_s02_07 with d1
            $ renpy.movie_cutscene("images/people/emily.willis/emily_bathroom_s02_cum_02.webm")
            show img_emily_bathroom_s02_08 with d1
            me "Good girl!"
            emily "For you always, daddy."

            jump lbl_home_living_room

### KITCHEN ###
label lbl_home_kitchen_events:
    $ attendee = func_check_time(v_time, tb_time["home_kitchen"])

    if attendee.find("emily") != -1 and not tb_events["home_kitchen"]["emily"] and v_time < 480:
        jump lbl_home_kitchen_emily_s01
    elif attendee.find("adriana") != -1 and not tb_events["home_kitchen"]["adriana"] and v_time >= 1140:
        jump lbl_home_kitchen_adriana_s01
    else:
        if v_time >= 420 and v_time < 480:
            "You're having breakfast with your family."
            $ v_time = 480
            jump lbl_home_living_room
        elif v_time >= 1125 and v_time < 1140:
            "Adriana is making dinner."
            menu:
                "Help her.":
                    "You prepare the meal with your wife, who is very grateful."
                    $ v_time = 1140
                    jump lbl_home_kitchen_events
                "Leave.":
                    jump lbl_home_living_room
        elif v_time >= 1140 and v_time < 1170:
            "You're having dinner with your family."
            $ v_time = 1170
            jump lbl_home_living_room
        else:
            "Nobody here right now."
            jump lbl_home_living_room

## Adriana S01 ##
label lbl_home_kitchen_adriana_s01:
    scene img_adriana_kitchen_s01_02 with d3
    me "Love?"
    adriana "Yes?"
    me "You seem \"distracted\"."
    scene img_black
    show vid_adriana_kitchen_s01_01
    adriana "Not at all, what makes you think that?"
    dakota "More like \"in heat\"."
    emily "*Giggle*"
    me "Girls..."
    adriana "Come and join me quickly!"
    dakota "I know one who's gonna get her pussy destroyed."
    emily "*Giggle*"
    me "Two minutes, I finish your delicious meal and I'm all yours."
    hide vid_adriana_kitchen_s01_01 with d3
    show vid_adriana_kitchen_s01_mas with d3
    adriana "Two minutes, they're long his two minutes."
    window hide
    pause
    adriana "Finally?"
    hide vid_adriana_kitchen_s01_mas with d3
    show img_adriana_kitchen_s01_03 with d3
    adriana "Well?"
    hide img_adriana_kitchen_s01_03 with d3
    show img_adriana_kitchen_s01_04 with d3
    me "I'm coming, I'm coming."
    hide img_adriana_kitchen_s01_04 with d1
    show img_adriana_kitchen_s01_05 with d1
    adriana "I'm done waiting."
    hide img_adriana_kitchen_s01_05 with d1
    show vid_adriana_kitchen_s01_fg with d1
    me "You really a bitch in heat."
    adriana "{b}Your{/b} bitch in heat."
    me "I know something else that's in heat."
    hide vid_adriana_kitchen_s01_fg with d3
    show vid_adriana_kitchen_s01_bj with d3
    me "You fuckingw whore, behaving like that in front of your daughters!"
    adriana "Mmmm!"
    me "What a perfect example of parental education. Come here so I can give you your reward."
    hide vid_adriana_kitchen_s01_bj with d3
    show vid_adriana_kitchen_s01_cun with d3
    adriana "I try...{w=0.5} aahhh..."
    adriana "...to be a role model for them *moan*."
    hide vid_adriana_kitchen_s01_cun with d3
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_kitchen_s01_in.webm")
    show img_adriana_kitchen_s01_06 with d1
    me "And you know how we reward good mothers like you?"
    hide img_adriana_kitchen_s01_06 with d3
    show vid_adriana_kitchen_s01_vg_01 with d3
    adriana "With a big cock!"
    me "Too bad they're not here to see how well I reward their mother."
    hide vid_adriana_kitchen_s01_vg_01 with d3
    show vid_adriana_kitchen_s01_vg_02 with d3
    adriana "Fuck, fucckk...{w=2.0} {b}fuck{/b}!"
    me "Daddy want to sit down, come impale yourself on my dick."
    hide vid_adriana_kitchen_s01_vg_02 with d3
    show vid_adriana_kitchen_s01_vg_03 with d3
    me "Oh, look, finally Dakota couldn't resist."
    adriana "It's too much, I'm going to..."
    hide vid_adriana_kitchen_s01_vg_03 with d1
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_kitchen_s01_cum_01.webm")
    show img_adriana_kitchen_s01_07 with d1
    adriana "Look at mommy sweetie, look how a whore she is!"
    hide img_adriana_kitchen_s01_07 with d1
    show vid_dakota_bathroom_s01_mas with d1
    dakota "A whore, my mother is whore *moan*."
    adriana "Don't talk to me like that or I..."
    hide vid_dakota_bathroom_s01_mas with d1
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_kitchen_s01_cum_02.webm")
    show img_adriana_kitchen_s01_08 with d3
    adriana "{b}Fuck!{/b} No anal for you tonight, keep pudding my pussy hard!"
    hide img_adriana_kitchen_s01_08 with d1
    $ renpy.movie_cutscene("images/people/dakota.skye/dakota_kitchen_s01_cum.webm")
    show img_adriana_kitchen_s01_09 with d1
    dakota "*Pant* *pant*"
    adriana "Good little whore. Now my pussy [me]!"
    hide img_adriana_kitchen_s01_09 with d1
    show vid_adriana_kitchen_s01_vg_04 with d1
    adriana "Baby you're so good to your mommy tonight."
    me "Hehe it's a son's duty to make his mother scream with pleasure."
    adriana "*Moan*"
    me "Fuck! Come here quick!"
    hide vid_adriana_kitchen_s01_vg_04 with d1
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_kitchen_s01_cum_03.webm")
    show img_adriana_kitchen_s01_10 with d1
    me "Good mommy."
    hide img_adriana_kitchen_s01_10 with d1
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_kitchen_s01_cum_04.webm")
    show img_adriana_kitchen_s01_11 with d1
    adriana "And it's a mother's duty to lick her son's hot sperm."
    hide img_adriana_kitchen_s01_11 with d5

    $ v_time = 1185
    $ tb_events["home_kitchen"]["adriana"] = True

    jump lbl_home_living_room

## Emily S01 ##
label lbl_home_kitchen_emily_s01:
    $ rand = renpy.random.randint(1,2)
    if rand == 1:
        scene img_emily_kitchen_s01_01 with d3
        emily "You don't look so good, daddy."
        me "You know I'm not a morning person sweetie, and besides, I have to get to work..."
        emily "College is fun! But don't worry, I've got something to cheer you up."
        scene img_emily_kitchen_s01_02 with d3
        me "Oh, just what I needed."
        scene img_emily_kitchen_s01_03 with d3
        emily "Do you like my pussy, daddy?"
        me "How a father couldn't like her daughter's pussy?"
        emily "*Giggle* true."
        scene img_emily_kitchen_s01_04 with d3
        emily "And my small tits?"
        me "I love everything about you, sweetheart."
        scene img_emily_kitchen_s01_05 with d3
        emily "I love everything about you too, daddy."
        if tb_stats["lvl"]["emily"] > 0:
            emily "Especially your big fat dick *moan*."
        scene img_emily_kitchen_s01_06 with d3
        me "You know I have to stop myself very hard from taking my dick out and sticking it in your cunt."
        scene img_emily_kitchen_s01_07 with d3
        emily "You mean in that cunt *giggle*?"
        scene img_emily_kitchen_s01_08 with d3
        emily "Or maybe in my tight asshole?"
        scene img_emily_kitchen_s01_09 with d3
        emily "I like to tease you like this."
        scene img_emily_kitchen_s01_10 with d3
        emily "Mmmmmh."
        scene img_emily_kitchen_s01_11 with d3
        me "You're killing me, sweetie."

    else:
        scene img_emily_kitchen_s01_12 with d3
        emily "Daddy, I put on a little show for you before you go to work."
        scene img_emily_kitchen_s01_13 with d3
        emily "First my small tits."
        scene img_emily_kitchen_s01_14 with d3
        emily "I love groping them."
        scene img_emily_kitchen_s01_15 with d3
        emily "Hard *moan*."
        scene img_emily_kitchen_s01_16 with d3
        emily "I put those panties especially for you daddy."
        scene img_emily_kitchen_s01_17 with d3
        emily "*Moan* I love doing that."
        scene img_emily_kitchen_s01_18 with d3
        emily "It feels so good when you look at me with that longing look in your eye."
        scene img_emily_kitchen_s01_19 with d3
        emily "I know exactly what you're thinking..."
        scene img_emily_kitchen_s01_20 with d3
        emily "Maybe there..."
        scene img_emily_kitchen_s01_21 with d3
        emily "Or maybe in both *giggle*."

    $ tb_events["home_kitchen"]["emily"] = True

    menu:
        "{color=#858585}-- ??? --{/color}" if tb_stats["lvl"]["emily"] == 0:
            call lbl_not_yet
            jump lbl_home_living_room

        "Join her." if tb_stats["lvl"]["emily"] > 0:
            "action"
            jump lbl_home_living_room

        "Go outside.":
            jump lbl_home_living_room

    jump lbl_home_living_room

### LIVING ROOM ###
## Adriana S01 ##
label lbl_home_livingroom_adriana_s01_01:
    "After a hard day of work."
    adriana "Close your eyes daddy, your youngest daughter has a surprise for you."
    scene img_black with d1
    me "Ok."
    me "{i}(Dakota has a surprise for me? Or maybe...){/i}"
    adriana "I just came home from school and you promised to shove it deep in my ass. Extend your arms now."
    me "{i}(I didn't promise anything, but hey!{w=0.5} Are those her boobs?){/i}"
    adriana "Right on target, you can open your eyes."
    show img_adriana_livingroom_s01_01 with d3
    me "I can see you didn't even take the time to take off your school uniform."
    adriana "Do you like it daddy?"
    hide img_adriana_livingroom_s01_01 with d1
    show vid_adriana_livingroom_s01_pus with d1
    me "More than you can imagine."
    adriana "That not my asshole daddy. Do you want to start slow, or do you want to go straight to the main course?"

    menu:
        "I just want to fuck your ass baby.":
            hide vid_adriana_livingroom_s01_pus with d3
            jump lbl_home_livingroom_adriana_s01_03

        "We have all the time in the world.":
            hide vid_adriana_livingroom_s01_pus with d3
            show vid_adriana_livingroom_s01_bj_01 with d3
            jump lbl_home_livingroom_adriana_s01_02

label lbl_home_livingroom_adriana_s01_02:
    menu:
        "Daddy gonna fuck your face like you like it.":
            show vid_adriana_livingroom_s01_bj_02 with d1
            me "I'm gonna wash your mouth with my dick."
            pause
            hide vid_adriana_livingroom_s01_bj_02 with d1
            jump lbl_home_livingroom_adriana_s01_02

        "Take it deep slut.":
            show vid_adriana_livingroom_s01_bj_03 with d1
            me "That's your punishment for talking dirty at school."
            pause
            hide vid_adriana_livingroom_s01_bj_03 with d1
            jump lbl_home_livingroom_adriana_s01_02

        "More face fucking.":
            show vid_adriana_livingroom_s01_bj_04 with d1
            me "Daddy never gets tired of it.{w=0.5} And you too bitch!"
            pause
            hide vid_adriana_livingroom_s01_bj_04 with d1
            jump lbl_home_livingroom_adriana_s01_02

        "Impale yourself on my dick.":
            show vid_adriana_livingroom_s01_vg_01 with d1
            me "You like it don't you?"
            adriana "Yes *moan*{w=0.5} yesss !"
            pause
            hide vid_adriana_livingroom_s01_vg_01 with d1
            jump lbl_home_livingroom_adriana_s01_02

        "Let me see your ass when I fuck your pussy.":
            show vid_adriana_livingroom_s01_vg_02 with d1
            me ""
            pause
            hide vid_adriana_livingroom_s01_vg_02 with d1
            jump lbl_home_livingroom_adriana_s01_02

        "Up in your ass now.":
            hide vid_adriana_livingroom_s01_bj_01 with d3
            jump lbl_home_livingroom_adriana_s01_03

label lbl_home_livingroom_adriana_s01_03:
    show vid_adriana_livingroom_s01_an_01 with d3
    adriana "Yes please daddy *moan*{w=0.8} destroy my ass with your big cock!"
    me "Did you do well at school?"
    adriana "No, daddy, so punish me with your dick."
    hide vid_adriana_livingroom_s01_an_01 with d1
    $ renpy.movie_cutscene("images/people/dakota.skye/dakota_livingroom_s01_str_01.webm")
    show img_dakota_livingroom_s01_01 with d1
    me "Oh, I have a feeling we have a little spy again."
    dakota "You're making so much noise, the whole neighborhood must hear you. So I might as well get involved."
    me "{i}(Huhu, good, good. How far is she going to go?){/i}"
    dakota "And don't mind me, I'm only going to touch myself watching two rutting animals."
    me "{i}(Not far...){/i}"
    adriana "Don't worry, sweetie, you can watch mommy get her ass rammed all you want."
    hide img_dakota_livingroom_s01_01 with d1
    $ renpy.movie_cutscene("images/people/dakota.skye/dakota_livingroom_s01_str_02.webm")
    show img_black with d3
    hide img_black
    show img_dakota_livingroom_s01_02 with d3
    dakota "Do you like my pussy?"
    dad_mom "Of course sweetie."
    hide img_dakota_livingroom_s01_02 with d3
    show vid_dakota_livingroom_s01_fg_01 with d3
    dakota "I'll start then, you can go on."
    hide vid_dakota_livingroom_s01_fg_01 with d2
    show vid_adriana_livingroom_s01_an_02 with d2
    me "With pleasure."
    adriana "My fucking god daddy!"
    dakota "You two are unbelievable. My girlfriends never want to believe there's nothing better than a good dick."
    adriana "Oh yeah honey *moan*{w=0.5} you couldn't be more right. Especially your father's."
    me "Have you tried any others bitch?"
    adriana "Don't be silly, now take that dildo and shove it in my ass."
    hide vid_adriana_livingroom_s01_an_02 with d1
    show vid_adriana_livingroom_s01_vg_03 with d1
    dakota "{size=-7}*Whisper* yes daddy your big thing in my little asshole."
    adriana "Fuck, two dicks at the same time *moan*{w=0.5} nothing beats it."
    dakota "{size=-7}*Whisper* must be so good..."
    me "Time to switch."
    hide vid_adriana_livingroom_s01_vg_03 with d1
    show vid_adriana_livingroom_s01_an_03 with d1
    adriana "*Moan* even better this way."
    me "You can't live without my dick in your ass, don't you slut?"
    adriana "I can't *moan*{w=0.5} I can't daddy."
    dakota "Mommy, you're such a whore!"
    adriana "Yesss mommy is a filthy whore!"
    hide vid_adriana_livingroom_s01_an_03 with d1
    show vid_dakota_livingroom_s01_fg_02 with d1
    dakota "Watching you two...{w=0.5} sooo good!"
    me "Daddy is almost here sweetie."
    adriana "In my mouth, I want it in my mouth!"
    hide vid_dakota_livingroom_s01_fg_02
    show img_white
    pause .1
    with hpunch
    hide img_white
    pause .2
    show img_white
    pause .2
    hide img_white
    pause .2
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_livingroom_s01_cum_01.webm")
    show img_adriana_livingroom_s01_02 with d3
    me "Take that slut!"
    dakota "*moan* yesss take that mommy you whore!"
    me "And swallows everything like a good daddy's girl."
    hide img_adriana_livingroom_s01_02 with d3
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_livingroom_s01_cum_02.webm")
    show img_adriana_livingroom_s01_03 with d3
    adriana "Yum, delicious as always daddy."
    me "I spoil you too much love."
    adriana "*Giggle*"
    hide img_adriana_livingroom_s01_03 with d1
    show img_adriana_livingroom_s01_04 with d1
    adriana "I know one who enjoyed the show."
    dakota "Yeaaah maybe."
    hide img_adriana_livingroom_s01_04 with d1
    show img_dakota_livingroom_s01_03 with d1
    dakota "Anyway, see you later the old."
    me "The old? Tssss..."
    hide img_dakota_livingroom_s01_03 with d5

    $ v_time = 1090
    $ f_intro = False
    jump lbl_home_living_room

### LUST ###
label lbl_adriana_lust:
    scene img_black
    "Adriana stirred all night, obviously disturbed. Maybe you've been neglecting her too much lately?"
    "As soon as she gets up, she calls her best friend Megan."
    show img_adriana_lust_s01_01 with d3
    adriana "Megan?"
    megan "Yes love?"
    adriana "Do you want to come to yoga this morning?"
    megan "Do we have a new code name to \"I want to get laid\"?"
    adriana "Pretty much..."
    megan "I'll be right there!"
    hide img_adriana_lust_s01_01 with d3
    show vid_adriana_lust_s01_yog with d3
    megan "After all, you really wanted to do yoga?"
    adriana "I'm waiting for [me] to get up."
    megan "Oh a threesome, love it!"
    adriana "Not just yet, we have to make him suffer a little first."
    megan "He hasn't been fucking you lately?"
    adriana "{b}Not enough!{/b}"
    megan "I know one who's gonna sleep on the couch tonight *giggle*."
    adriana "Exactly!"
    hide vid_adriana_lust_s01_yog with d5
    show img_adriana_lust_s01_02 with d5
    me "Adriana, Megan? Ready for a bit of exercise?"
    adriana "*Tsk* not with you anyway."
    me "I..."
    megan "Well, I'm sick of yoga, let's fuck!"
    hide img_adriana_lust_s01_02
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_lust_s01_cun_01.webm")
    show vid_adriana_lust_s01_cun_02 with d5
    megan "That's right you little whore, licks my pussy. I've waited far too long."
    me "Mayb..."
    megan "Shut the fuck up! You know how long it's been since your bitch wife licked my pussy?"
    me "{i}(Well, just shut up and enjoy the show, I guess.){/i}"
    hide vid_adriana_lust_s01_cun_02 with d5
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_lust_s01_cun_03.webm")
    show img_adriana_lust_s01_03 with d1
    megan "Drink this already, you little whore. Don't worry, I've got plenty more where that came from."
    adriana "You never disappoint."
    megan "Never."
    hide img_adriana_lust_s01_03 with d1
    show vid_adriana_lust_s01_ks with d1
    adriana "Mmmm..."
    megan "*Moan*"
    me "{i}(They want me dead...){/i}"
    hide vid_adriana_lust_s01_ks with d3
    show vid_adriana_lust_s01_cun_04 with d3
    adriana "Yes, yesss lick me good love."
    hide vid_adriana_lust_s01_cun_04 with d1
    $ renpy.movie_cutscene("images/people/adriana.chechik/adriana_lust_s01_cun_05.webm")
    show img_adriana_lust_s01_04 with d1
    adriana "Fuck, fuck *moan*. I've got some in reserve for you, too."



    jump lbl_home_living_room