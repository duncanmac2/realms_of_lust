#### LOCATIONS ####
label lbl_home_bathroom:
    scene loc_home_bathroom1
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
    else:
        jump lbl_home_room_mc_events

#### EVENTS ####
### ROOM MC ###
label lbl_home_room_mc_events:
    jump lbl_home_living_room

### BATHROOM ###
label lbl_home_bathroom_events:
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
    hide img_emily_bathroom_s01_02 with d3

    jump lbl_college_yard

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

    $ v_time = 1090
    $ f_intro = False
    jump lbl_home_living_room