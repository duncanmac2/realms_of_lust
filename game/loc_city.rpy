#### LOCATIONS ####
label lbl_city_map:
    call main_show
    scene loc_city_map_back
    show loc_city_map at truecenter

    $ v_time += 5

    call time_check
    call screen scr_main_map

label lbl_city_beach:
    scene loc_city_beach

    if v_day == 2:
        jump lbl_city_beach_day2
    elif v_day == 3:
        jump lbl_city_beach_day3

label lbl_city_hospital:
    scene loc_city_hospital

    if v_day == 3:
        jump lbl_city_hospital_day3

### 1ST STREET ###
label lbl_city_street_1st:
    $ v_localisation = "city_first_street"

    call main_show
    scene loc_city_street_1st

    if v_day == 1:
        jump lbl_city_home_marcus_day1a
    elif v_day == 2 and v_time == 0:
        jump lbl_city_home_marcy_day2a
    elif v_day == 2 and v_time > 0:
        jump lbl_city_street_1st_day2
    elif v_day == 3 and v_time == 0:
        jump lbl_city_street_1st_day3
    elif v_day == 4 and v_time == 0:
        jump lbl_city_street_1st_day4
    else:
        call screen scr_navigation

## 1ST STREET - MARCY HOME ##
label lbl_city_home_marcy:
    $ v_localisation = "marcy_home"

    call main_show
    scene loc_city_home_marcy

    if v_day == 1:
        jump lbl_city_home_marcus_day1b
    elif v_day == 2:
        jump lbl_city_home_marcy_day2b
    elif v_day == 3:
        jump lbl_city_home_marcy_day3
    elif v_day == 4:
        jump lbl_city_home_marcy_day4

label lbl_city_home_marcy_bathroom:
    scene loc_city_home_marcy_bathroom

    if v_day == 2:
        jump lbl_city_home_marcy_bathroom_day2
    elif v_day == 3:
        jump lbl_city_home_marcy_bathroom_day3

label lbl_city_home_marcy_pool:
    scene loc_city_home_marcy_pool

    if v_day == 3:
        jump lbl_city_home_marcy_pool_day3

label lbl_city_home_marcy_room:
    scene loc_city_home_marcy_room

    if v_day == 2:
        jump lbl_city_home_marcy_room_day2
    elif v_day == 3:
        jump lbl_city_home_marcy_room_day3

label lbl_city_home_marcy_room_sarah:
    scene loc_city_home_marcy_room_sarah

    if v_day == 3:
        jump lbl_city_home_marcy_room_sarah_day3

## 1ST STREET - PRYIA HOME ##
label lbl_city_home_priya:
    scene loc_city_home_priya

    if v_day == 3:
        jump lbl_city_home_pryia_day3

### 2ND STREET ###
label lbl_city_street_2nd:
    $ v_localisation = "city_second_street"

    call main_show
    scene loc_city_street_2nd
    call screen scr_navigation

## 2ND STREET - CHURCH ##
label lbl_city_church:
    scene loc_city_church

    if v_day == 2:
        jump lbl_city_church_day2
    elif v_day == 3:
        jump lbl_city_church_day3

## 2ND STREET - LILY HOME ##
label lbl_city_home_lily:
    scene loc_city_home_lily

    if v_day == 2:
        jump lbl_city_home_lily_day2
    elif v_day == 3:
        jump lbl_city_home_lily_day3

##  2ND STREET - PGP CORPORATION ##
label lbl_city_pgp_corporation:
    scene loc_city_pgp_corporation

    if v_day == 3:
        jump lbl_city_pgp_corporation_day3

### 3TH STREET ###
label lbl_city_street_3th:
    $ v_localisation = "city_third_street"

    call main_show
    scene loc_city_street_3th
    call screen scr_navigation

### 3TH STREET - GYM ###
label lbl_city_gym:
    scene loc_city_gym

    if v_day == 3:
        jump lbl_city_gym_day3

### 3TH STREET - MALL ###
label lbl_city_mall:
    $ v_localisation = "city_mall"

    call main_show
    scene loc_city_mall

    if v_day == 1:
        jump lbl_city_mall_day1
    elif v_day == 2:
        jump lbl_city_mall_day2
    elif v_day == 3:
        jump lbl_city_mall_day3

label lbl_city_mall_coffee:
    scene loc_city_mall_coffee

    if v_day == 4:
        jump lbl_city_mall_coffee_day4

### 3TH STREET - PARK ###
label lbl_city_park:
    scene loc_city_park

    if v_day == 3:
        jump lbl_city_park_day3

#### EVENTS ####
### MARCY HOME ###
## MARCY HOME - DAY 1 ##
label lbl_city_home_marcus_day1a:
    "We leave the house a few minutes later than usual, but still within a safe margin, the college is close enough that we can go on foot so we can take on the scenery while on the way."
    "My best friend Marcus lives on the house across the street, we usually go together the three of us so we have to go by his house to pick him up."
    show npc_portrait_sarah_01
    "We ring the bell, but it's his mother that greets us."
    "Her name is Sarah Williams, she used to be our nany back in the day. I had a crush on her back then, and can you blame me look at her even now she is beautiful."
    sarah "Hello guys, a bit late aren't you?"
    me "Sorry Sarah, our alarms just didn't go off today."
    sarah "It's ok, Marcus is coming down in a second, he was also late today, he is in the bathroom right now, say he wasn't feeling well."
    me "He is not coming then?"
    sarah "He is, he said it was just a stomach ache, but he was going to \"take care of it\"."
    "Take care of it... that is our code for he is masturbating, shit was he spying on our neighbors again?"
    me "Ok we will wait a bit, I think we can make it if we run."
    hide npc_portrait_sarah_01
    show npc_portrait_marcus at top with d3
    marcus "No need dude I'm right here, sorry for the wait I had to... take care of something..."
    "Definitely masturbating, he knows that I know, that's why he won't shake my hand. God damn it Marcus."
    hide npc_portrait_marcus with d3
    me "Let's go then."
    marcus "Ok bye Mom."
    me "Bye Sarah."
    sarah "Goodbye."

    menu:
        "Go to college":
            jump lbl_college_yard

label lbl_city_home_marcus_day1b:
    if f_day1_lisa_bathroom_incident:
        marcus "Hi mom, [me] came to visit."
        show npc_portrait_sarah_02 with d3
        sarah "Hello boys, how was your day?"
        marcus "Great, I found some great treasure in the campus, but that's a secret between [me] and I, so sorry Mom can't tell you."
        sarah "It's not drugs is it, I swear to god Marcus P. Willians if you are doing drugs you are finding a new place to live."
        marcus "What? No it's not drugs mom, it's something completely legal."
        "I somehow doubt it."
        marcus "Anyway, we are going to some games, are you going to the market today mom?"
        sarah "Yes, do you want me to bring you the usual?"
        marcus "Yes, the new edition is out today."
        sarah "I don't know why I buy those for you."
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sarah buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        marcus "Let's go play some g..."
        hide npc_portrait_sarah_02 with d3
        "*Ring* *ring*"
        "It's my phone, Lisa is calling."
        lisa "{i}[me], were are you? Doesn't matter, come back home right now! You own me an explanation for what happend this morning.{/i}"
        me "Lisa, I will be right there."
        lisa "{i}You have 20 minutes.{/i}"
        "She hung up."
        marcus "Looks like you are in trouble my friend, we will do this some other time."
        me "Sorry man, we will talk later."

        menu:
            "Run home":
                jump lbl_home_living_room

    else:
        marcus "Hi mom, [me] came to visit."
        show npc_portrait_sarah_02 with d3
        sarah "Hello boys, how was your day?"
        marcus "Great, I found some great treasure in the campus, but that's a secret between [me] and I, so sorry Mom can't tell you."
        sarah "It's not drugs is it, I swear to god Marcus P. Willians if you are doing drugs you are finding a new place to live."
        marcus "What? No it's not drugs mom, it's something completely legal."
        "No it isn't."
        marcus "Anyway, we are going to some games, are you going to the market today mom?"
        sarah "Yes, do you want me to bring you the usual?"
        marcus "Yes, the new edition is out today."
        sarah "I don't know why I buy those for you."
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sarah buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        marcus "Let's go play some g..."
        hide npc_portrait_sarah_02 with d3
        "*Ring* *ring*"
        "It's my phone, Lisa is calling."
        lisa "{i}[me], is Mia with you? She isn't aswering her phone.{/i}"
        me "Lisa, no she is with Veronica I think. Do you have her number?"
        lisa "{i}Yes, I will call her right now, she is in so much trouble...{/i}"
        "Poor Mia."
        "After the call Marcus and I spend some hour play some of his old games."
        me "It's getting late man, I will..."
        show npc_portrait_maria_01 with d1
        "Just as I start to stand to go home something catches my eyes."
        hide npc_portrait_maria_01 with d1
        show npc_portrait_maria_02 with d1
        marcus "Ohhh, [me] we are so lucky, she rarely changes in her room. Let's enjoy this gift from the pervert god."
        hide npc_portrait_maria_02 with d1
        show npc_portrait_maria_03 with d1
        me "She is very hot, that's cheerleader for you, but it's time for me to go, see you tomorrow Marcus."
        "He's in a trance, better leave, he has business to attend to."

        $ v_time = 1140

        menu:
            "Go home":
                jump lbl_home_room_mc

## MARCY HOME - DAY 2 ##
label lbl_city_home_marcy_day2a:
    show npc_portrait_mia_11
    mia "Bro are you ok, you have been acting strange today."
    me "I'm fine Mia."
    mia "Are you sure? You are acting weird, you looked like you never seen me in my undies before, hell you already saw me naked, but you were giving me this strange looks."
    me "Sorry sis, it's just... I don't know."
    hide npc_portrait_mia_11
    show npc_portrait_mia_12 at top
    mia "Maybe you should go see the nurse, I'm sure Marcy will go tell you teacher that you are not feeling well."
    me "I don't know... wait who is Marcy?"
    hide npc_portrait_mia_12
    show npc_portrait_mia_11
    mia "What do you mean who is Marcy? She is your best friend, our neighbour, ring any bells?"
    "That can't be... there must be some mistake, it wasn't a dream, couldn't have been, I don't know any Marcy. But she never said this would happen... Nina, it was all real!"
    mia "[me]?"
    me "Oh sorry sis, I'm fine, let's go."

    menu:
        "Marcy's house":
            jump lbl_city_home_marcy

label lbl_city_home_marcy_day2b:
    if v_time == 720:
        show npc_portrait_sarah_03 with d1
        "Sarah is here, and still using the same shirt..."
        sarah "Oh hello [me], Marcy is not here right now but please come in."
        "I enter the house and make myself comfortable."
        sarah "Do you want some tea or a water?"
        me "No thanks I just wanted to ask a question. Do you know anyone named Marcus?"
        sarah "Marcus? Sorry I don't know anyone by that name, why?"
        me "Oh nothing just, asking."
        sarah "You know if Marcy was a boy I would have called him Marcus, hahaha."
        me "You don't say...."
        "We talk for a few minutes, but it's clear she is oblivious to what's happened."
        me "Thanks for the tea Sarah, I'll go home now, so..."
        sarah "Wait, Marcy will be home soon, just sit and have some more tea. I have to take a shower, but she should be here soon."

        menu:
            "Okay":
                jump lbl_city_home_marcy_bathroom

    else:
        "I have been here hundreds of times, but now I feel like I don't know this place at all, something isn't right, is Marcus really... Only one way to find out."
        show npc_portrait_sarah_03 with d3
        "Sarah answers the doorbell soon."
        "Shit I can almost see her nipples, I always had the hots for Sarah but now isn't the time for looking at her huge and beautiful... no focus."
        me "Hi Sarah, is Marc...y ready?"
        sarah "Oh good morning guys, I will call her, she is just changing."
        hide npc_portrait_sarah_03 with d1
        show npc_portrait_marcy_01 with d1
        "After a few minutes of waiting my worst fears become real."
        marcy "Hey [me]."
        me "I-I... hey... Marcy!?"
        marcy "Yes, that's my name. Are you ok?"
        me "Why does everyone keep asking me that it's fine, ok!"
        marcy "Okaayyy... We should go then."
        me "Yes, sure goodbye Sarah."
        sarah "Bye guys, and don't forget to visit."
        hide npc_portrait_marcy_01 with d3
        "Mia and Marcu...y keep looking at me like I'm crazy. Whatever is going on I have to keep calm, worrying them will not help me, let me try to keep my cool..."

        menu:
            "College":
                jump lbl_college_yard

## MARCY HOME - DAY 3 ##
label lbl_city_home_marcy_day3:
    if v_time == 0:
        "Mia rings the doorbell, Sarah comes to the door soon after."
        show npc_portrait_sarah_04 with d3
        sarah "Good morning guys, how are you."
        me "We are good Sarah thanks for asking, is Marcy ready?"
        sarah "I will call her just a second."
        hide npc_portrait_sarah_04 with d1
        mia "That's a nice lingerie don't you think bro, I wish I had something so stylish."
        me "You like it? Maybe you will get a nice gift sometime this week then."
        mia "Thanks bro you are the best."
        show npc_portrait_marcy_04 with d1
        marcy "Hey, if you are giving gifts give me one too."
        me "I only give gifts to people who are ready on time, unless you are going to college in that outfit I don't think you fit the criteria."
        marcy "Sorry, I spend the night playing games again, come in I will be ready in no time."
        me "Ok, we have the time, but don't take too long."
        marcy "Don't worry I will be right back."
        hide npc_portrait_marcy_04 with d1
        mia "Bro, why didn't you and Marcy ever fucked."
        me "Good question, I guess it never came up on our conversations, and she is my friend, maybe it would be weird after we did."
        "A few minutes later..."
        me "Why is she taking so long? I will go check on her."
        mia "Ok."

        menu:
            "Go to the bathroom":
                jump lbl_city_home_marcy_bathroom
            "Call Marcy":
                jump lbl_city_home_marcy_room

    elif v_time >= 720 and v_time < 780 and tb_event[3]["city_home_marcy"]["sarah"] == 0:
        "Sarah is eating lunch."
        show npc_portrait_sarah_01 with d1
        sarah "[me], what a surprise want to eat with me?"
        me "No thanks Sarah, I was just passing by."
        sarah "Are you sure I have enough food for the both of us."
        me "I'm sure."
        sarah "Then sit down let's talk a little."
        hide npc_portrait_sarah_01 with d3
        "I sit in front of her."
        sarah "I talked to Lisa earlier, I heard Lily is back in town."
        me "She is, she is working at PGP Corp."
        sarah "That's great, it's always good to have family close by. My mother has moved to a house in Canary Street last week, I will be visiting her after I finish my lunch."
        me "Oh, I'm not bothering you then am I?"
        show npc_portrait_sarah_05 with d1
        sarah "Nonsense, you are welcome any time. I don't even know why you still bother knocking on the door, you are like the son I never had, you can come in at any time."
        me "Thanks Sarah, but I'm sure you wouldn't want me to come in the middle of the night like a burglar."
        hide npc_portrait_sarah_05 with d1
        show npc_portrait_sarah_06 with d1
        sarah "Haha, if you want to come and see Marcy in the middle of the night I don't mind, just make sure to wear a condom."
        me "I... I will keep that in mind."
        sarah "It's getting late I'm leaving now, but feel free to stay in Marcy's room if you want, she will be here soon. If you need to leave you know where I keep the spare key, just lock the door."
        hide npc_portrait_sarah_06 with d3
        "She leaves me in the house alone, I better go."

        $ tb_event[3]["city_home_marcy"]["sarah"] = 1
        $ v_time += 10

    elif v_time >= 900 and v_time < 1020 and tb_event[3]["city_home_marcy"]["marcy"] == 0:
        show img_marcy_couch_01 with d3
        "Marcy is on the couch watching some TV."
        me "What are you watching?"
        marcy "Just some show about who can sleep with more woman in a day."
        me "What, serious? Is there a show like that?"
        marcy "Yeah, it's a new one, it's interesting."
        me "Let's watch it together, I want to see how that works."
        hide img_marcy_couch_01 with d1
        show img_marcy_couch_02 with d1
        "After a few minutes Marcy turns to me and asks me a surprising question."
        marcy "How come you never kiss me?"
        me "Wow, that came out of nowhere! I have no idea, maybe because you never asked me to."
        marcy "If I were to ask would you kiss me?"
        me "I would, yes."
        marcy "Then I want a kiss, right now."
        hide img_marcy_couch_02 with d1
        show vid_marcy_kiss at top with d1
        "I don't know what got into her but I have no reason to reject the request."
        hide vid_marcy_kiss with d1
        marcy "That was amazing, we should do it more often."
        me "If you want to, I will admit you are a good kisser."
        show img_marcy_couch_03 with d1
        marcy "Thanks, you are not bad yourself."
        hide img_marcy_couch_03 with d3
        "We continue to watch TV until Marcy falls asleep in the couch. I will let her rest."

        $ tb_event[3]["city_home_marcy"]["marcy"] = 1
        $ v_time += 20

    call main_show
    call screen scr_navigation

## MARCY HOME - DAY 4 ##
label lbl_city_home_marcy_day4:
    show npc_portrait_sarah_07 at top with d1
    sarah "Hey guys, how was your night?"
    hide npc_portrait_sarah_07 with d1
    show npc_portrait_marcy_06 with d1
    marcy "We had a lot of fun mom."
    sarah "I heard, we have thin wall remember."
    me "Crap, we are sorry."
    hide npc_portrait_marcy_06 with d1
    show npc_portrait_sarah_07 at top with d1
    sarah "Don't be sorry honey, I have to admit that I had some fun myself while hearing your moans."
    me "That's... huh... cool."
    sarah "But it would be even better if you could come visit me some nights too."
    me "I...I..."
    hide npc_portrait_sarah_07 with d1
    show npc_portrait_marcy_07 with d1
    marcy "He will mom, later, but we have to leave soon."
    hide npc_portrait_marcy_07 with d1
    "We sit on the table, Marcy sits very close to me and during the entire time we are eating she rubbing me, or herself on me. It's not unpleasant but Sarah is looking jealously at us."
    "And that foot on my leg, it's not Marcy's that's for sure. After we finish I feeling almost like I'm going to faint from too much blood going to my dick. They both look like they are ready to rip my clothes off and kill me from snu snu. Luckily the doorbell rings, it's Mia."
    show npc_portrait_mia_13 with d1
    mia "Good morning Sarah, are the two love birds ready?"
    sarah " Good morning Mia, they are ready."
    me "Hi sis."
    marcy "Hey Mia."
    mia "Morning guys, I hope you didn't have too much fun last night, because we need to leave now."
    marcy "We had an adequate amount of fun right [me]?"
    me "Yes... let's get going, bye Sarah..."

    menu:
        "Go to class":
            jump lbl_college_class

### MARCY BATHROOM ###
## MARCY BATHROOM - DAY 2 ##
label lbl_city_home_marcy_bathroom_day2:
    "I decide to go wait in Marcy's room, I can also see if the place has changed much since... why is the bathroom door open?"
    show img_sarah_shower_01 with d3
    "My curiosity gets the best of me and I take a look."
    hide img_sarah_shower_01 with d1
    window hide
    show img_sarah_shower_02 with d1
    pause
    hide img_sarah_shower_02 with d1
    show img_sarah_shower_03 at top with d1
    pause
    hide img_sarah_shower_03 with d1
    show img_sarah_shower_04 with d1
    "Sara's naked body is amazing, I never got this hard... Ok, change of plans, time to leave. But did she left the door open on purpose?"
    hide img_sarah_shower_04 with d1

    $ v_time = 840

    menu:
        "Out of here":
            jump lbl_city_street_1st

## MARCY BATHROOM - DAY 3 ##
label lbl_city_home_marcy_bathroom_day3:
    if v_time == 0:
        "The bathroom door is open is she in there?"
        show img_sarah_shower_05 with d3
        me "Marcy?"
        hide img_sarah_shower_05 with d1
        show img_sarah_shower_06 with d1
        sarah "No, it's me [me]."
        me "Sorry Sarah, I didn't mean to walk in on you."
        hide img_sarah_shower_06 with d1
        show img_sarah_shower_07 with d1
        sarah "It's ok, I don't mind, in fact I have a question what do you think about them?"
        me "Your breasts?"
        hide img_sarah_shower_07 with d1
        show img_sarah_shower_08 with d1
        sarah "Yes, my breasts, do you like them?"
        me "I think they are really nice."
        sarah "Would you like to touch then?"
        "What a stupid question. Of course I want to touch them."
        me "Yes, yes I would love to."
        sarah "Go ahead them."
        "I to go slow, to savor the moment, the weight, the soft skin, her hard nipples, this is paradise. But then..."
        marcy "[me], where are you? Let's go!"
        me "Shit, I gotta go now Sarah."
        sarah "A shame, if you want to continue this some other time just visit me ok."

        menu:
            "College":
                jump lbl_college_class

    elif v_time >= 1020 and v_time < 1080:
        show img_sarah_shower_08 with d1
        "Sarah is taking a shower. I don't think she saw me yet, not that would matter if she did, so let's just enjoy the show."
        window hide
        pause
        hide img_sarah_shower_08 with d1

    else:
        "The is no one here."

    menu:
        "Go back":
            jump lbl_city_home_marcy

### MARCY POOL ###
## MARCY POOL - DAY 3 ##
label lbl_city_home_marcy_pool_day3:
    if v_time >= 840 and v_time < 900 and tb_event[3]["city_home_marcy_pool"]["marcy"] == 0:
        show img_marcy_pool_01 at top with d3
        me "Hey Marcy, swimming?"
        marcy "Yeah!"
        me "Why naked? Don't you have a bikini?"
        marcy "I do but I like the freedom, you should try it sometime."
        me "Maybe later, I will leave you to it."
        hide img_marcy_pool_01 at top with d1
        show img_marcy_pool_02 at top with d1
        marcy "Bye..."
        hide img_marcy_pool_02 with d1

        $ tb_event[3]["city_home_marcy_pool"]["marcy"] = 1
        $ v_time += 5

    else:
        "This is Marcy's pool, we had lots of fun here in the past. I hope we can have even more fun in the future... a different kind of fun."

    menu:
        "Go back":
            jump lbl_city_home_marcy

### MARCY ROOM ###
## MARCY ROOM - DAY 2 ##
label lbl_city_home_marcy_room_day2:
    "I decide to go see Marcy, maybe she has some insight on this changes."
    me "Hey Marcy."
    show npc_portrait_marcy_03
    marcy "Hey [me]."
    me "How did things go on the locker?"
    marcy "After you left, the janitor came in and I had to bail, just like yesterday, didn't even have time to co..."
    me "Whoa, too much information, let's change subject."
    marcy "Do you want to play some games?"
    me "Sure, what do you have there."
    marcy "I found this new game yesterday called \"A Spell for All\" it's amazing."
    me "Never heard of it, let's give it a try."
    hide npc_portrait_marcy_03 with d3
    "After a few minutes."
    me "Is this porn game?"
    marcy "Well yes isn't it cool?"
    me "Kind of, it's just I had a different idea of what we were going to play."
    marcy "We have been playing fighting games for how many years now? Let's try something different for a change."
    show vid_marcy_masturbate at top with d1
    me "Ok, just a few more minutes and... what are you doing?"
    marcy "What do you think?"
    me "Not with me in here you are not!"
    marcy "Why, it's not like you have never seen me naked. This is just the next step on our friendship..."
    "Shit, there it comes again... that overwhelming lust, I just can't take my eyes off her now."
    marcy "You are bigger than I remember..."
    "She points at another bulge in my pants. Shit not again."
    me "Yes, this is..."
    hide vid_marcy_masturbate with d1
    show vid_marcy_boobs_bounce_01 at top with d1
    marcy "Can I see it? I mean as friend... Here is something in return."
    "That is enough to snap me out of the trance."
    me "Bye Marcy!"
    hide vid_marcy_boobs_bounce_01
    marcy "What wait, I sorry..."

    menu:
        "Go home":
            jump lbl_home_living_room

## MARCY ROOM - DAY 3 ##
label lbl_city_home_marcy_room_day3:
    if v_time == 0:
        "The door to the bathroom is open, maybe I... no, no time let's call her."
        me "Marcy?"
        show img_marcy_undress_01 with d1
        marcy "Hey [me], decided to spy on me did you?"
        me "No I came to see why you are taking so long to just change clothes."
        marcy "Oh is because I was looking for something, sorry, I'll find it later."
        hide img_marcy_undress_01 with d1
        show img_marcy_undress_02 with d1
        "She starts striping in front of me, she has a really nice body."
        marcy "So what do you think?"
        me "About?"
        hide img_marcy_undress_02 with d1
        show vid_marcy_boobs_02 at top with d1
        marcy "My tits, are they too big?"
        me "Of course not, I think they are perfect."
        hide vid_marcy_boobs_02 with d1
        show img_marcy_undress_03 at top with d1
        marcy "Aww, thanks, I think it's in the family, mom is big, aunt Ny is big, even grandma Diana is huge. Speaking of which, do you really think it would be awkward if we had sex?"
        me "You heard that huh. I don't know, maybe, what do you think."
        hide img_marcy_undress_03 with d1
        show img_marcy_undress_04 at top with d1
        marcy "Who knows, I think it would be ok, but if you are not sure I understand."
        me "You know that almost sounded like a normal person."
        hide img_marcy_undress_04 with d1
        show img_marcy_undress_05 at top with d1
        marcy "Then I have to tell you, if you want to do something else like getting a blowjob all you need is ask, hahaha..."
        me "Now that's more like you."
        marcy "But serious, if you ever change your mind, call me, you know I'm always ready..."
        me "But you are a virgin too..."
        hide img_marcy_undress_05 with d3
        marcy "That's why I'm always ready. It will happen any day now... I hope. Ok, I'm done let's go."

        menu:
            "College":
                jump lbl_college_class

    elif v_time >= 780 and v_time < 840 and tb_event[3]["city_home_marcy_room"]["marcy"] == 0:
        show img_marcy_nude_01 at top with d3
        me "Hey Marcy, what are you doing?"
        marcy "Playing some games, wanna join me?"
        me "Sure, do I have to follow the dress code however?"
        marcy "Dresscode? Oh, you mean get naked? Your choice, [me], but if you don't don't blame me if you get distracted and lose. If you do get naked we will both be equally distracted don't you think."
        me "That's a fair point. Let me get out of these."
        hide img_marcy_nude_01 with d1
        show img_mc_body_01 at top with d1
        marcy "Shit, I was wrong, I'm at a disadvantage now."
        hide img_mc_body_01 with d1
        me "Let's start, give me the controler."
        "We spend the next few minutes playing, she is right, she can barely stop looking at me... At the end of our match I stand up and I notice that my dick is dangling close to Marcy's face."
        "She is almost like in a trance looking at it when an idea comes to my mind, I start to get closer to her. Her breath is becoming louder and uneven, until she can no longer hold it."
        show vid_marcy_blowjob_01 at top with d1
        "She is sucking like a crazy woman, no technique, no nothing, just pure lust she was holding back for so long."
        hide vid_marcy_blowjob_01 with d1
        show vid_marcy_blowjob_02 at top with d1
        me "Marcy, I'm cumming..."
        hide vid_marcy_blowjob_02 with d1
        show vid_marcy_facial at top with d1
        "After she tastes my cum for a few seconds, she comes back to it."
        hide vid_marcy_facial with d1
        marcy "[me] that's the greatest day in my life! I never thought it was going to happen. Thank you, thank you!"
        "She is very happy about sucking my cock, guess I should expect nothing different from her. An extremely sexual person in an increasingly sexual world, but repressed."
        me "Glad I could help."
        marcy "Can we fuck now?"
        me "Wow, calm down Marcy, let's decide about that later, besides I need time to rest."
        marcy "Oh, you are right, sorry. I'm going to touch myself now then..."
        "She is still a bit strange, I will let her cool down, I will see her later."

        $ tb_event[3]["city_home_marcy_room"]["marcy"] = 1
        $ v_time += 10

    elif v_time >= 1140:
        "I let Lisa know that I will spend the night at Marcy, she acknowledges what I said and I go out. I knock on the door and Marcy let me in."
        marcy "So what brings you here? Maybe you came to fuck me? Hahaha."
        me "Actually, yes."
        marcy "What? You want to... wow, it's happening, it's finally happening! what do I do now? [me] what do we do now?"
        "She is panicking, I always knew she was all bravado .. I will have to take the lead... I WILL HAVE TO TAKE THE LEAD! Ohhh shit what do I do? Calm down! All those years watching porn will not have been in vain."
        "Over the next few minutes we proceed to make awkward advances and decisions, but in the end things workout."
        window hide
        show vid_marcy_boobs_03 at top with d1
        pause
        hide vid_marcy_boobs_03 with d1
        show vid_marcy_sex_01 at top with d1
        pause
        hide vid_marcy_sex_01 with d1
        show vid_marcy_sex_02 at top with d1
        pause
        hide vid_marcy_sex_02 with d1

        menu:
            "Wake up":
                pass

        me "Where... what? Oh right I'm in Marcy's room, that just happened..."
        show img_marcy_nude_02 with d1
        marcy "Hey, sleep well?"
        me "I did, you?"
        marcy "Like an angel! I don't know why we waited so long, we should have done that sooner. Now that we are rested, you want to go at it again?"
        me "I would love to, but we have to be in class in an hour."
        marcy "Let's just no go today."
        me "Won't we get into trouble with Ellie?"
        hide img_marcy_nude_02 with d1
        show npc_portrait_marcy_05 with d1
        marcy "Of couse not, she doesn't care if we go to class or not, if we can pass the finals we are good to go."
        "Interesting development. But still I want to see how things are progressing."
        me "Sorry Marcy, we will do it another time I have things to do on campus today."
        marcy "Awwww. But you will have breakfast with us right?"
        me "Ok, your mother would be upset if I left without at least say hi."
        marcy "Let's head down, but don't forget to put some clothes on, mom is a bit frustrated, she has not had a good fuck in some time. If you just come out with that swinging she will jump you on the spot."
        me "Yes, we don't want that... do we?"
        hide npc_portrait_marcy_05 with d1
        show npc_portrait_marcy_06 with d1
        marcy "Are you asking me if I would be okay if you had sex with my mother?"
        me "Maybe..."
        marcy "Well she is very lonely, maybe it would do her some good..."
        hide npc_portrait_marcy_06 with d1
        "*Knock* *knock*"
        show npc_portrait_sarah_07 at top with d1
        sarah "Guys, breakfast is ready, come down."
        marcy "We will discuss this later, I'm hungry and since you want to go to class we have to hurry."
        hide npc_portrait_sarah_07 with d1

        $ tb_event[3]["city_home_marcy_room"]["marcy_sex"] == 1
        $ v_day = 4
        $ v_time = 0

        menu:
            "Go down for breakfast":
                jump lbl_city_home_marcy

    else:
        "Marcy is not here now."

    menu:
        "Go back":
            jump lbl_city_home_marcy

### SARAH ROOM ###
## SARAH ROOM - DAY 3 ##
label lbl_city_home_marcy_room_sarah_day3:
    if v_time >= 900 and v_time < 960 and tb_event[3]["city_home_marcy_room_sarah"]["sarah"] == 0:
        "Sarah is changing clothes to go to the gym it seems."
        show img_sarah_gym_01 at top with d3
        sarah "Hey [me], are you looking for Marcy?"
        me "No, I was just admiring how well you keep your body in shape."
        sarah "Thank you, it's not easy, I can tell you that."
        me "I can imagine."
        hide img_sarah_gym_01 at top with d1
        show obj_sarah_playboy_collection at top with d1
        "A collection of rare adult DVDs is on a side of the room. Ever since her husband died they has been on the attic, but it looks like she brought it back here."
        hide obj_sarah_playboy_collection with d1
        sarah "Incredible isn't it? Clayton always loved collecting those. I was always jealous of this girls in the cover so when he died I hid them away, but you know, I can see the beauty of it now."
        me "Marcy must love to come here to borrow some of them from time to time."
        show img_sarah_gym_02 with d1
        sarah "Oh she does belive me, but it's her right, it belongs to her too. But now I have to leave [me], you can stay if you want, it's not like I have anything to hide here."
        me "No, I'm also leaving, I have some things to do. I will see you later Sarah."
        sarah "Later [me]."
        hide img_sarah_gym_02 with d1

        $ tb_event[3]["city_home_marcy_room_sarah"]["sarah"] = 1
        $ v_time += 5

    else:
        "The is no one here."

    menu:
        "Go back":
            jump lbl_city_home_marcy

### MALL ###
## MALL - DAY 1 ##
label lbl_city_mall_day1:
    me "Sorry man, I got other plans."
    marcus "It's cool [me], come see us when you have some time. I have this new game and it's pretty good."
    me "Will do, see you later."
    marcus "See you."
    mia "What are those plans bro?"
    me "Well, I think it's time we go buy some ice cream on that place we used to go always."
    mia "Really, thanks bro, I love you."
    me "Love you too sis."
    "After we enter she mall it's a short way to the \"Snow White\", weird name for a ice cream shop if you ask me but their stuff is divine. Wait were is it?"
    mia "Bro, I think the store closed."
    show loc_city_mall_store at top
    me "It can't be, maybe we came the wrong way here let's ask in here?"
    hide loc_city_mall_store with d1
    show npc_portrait_karen_01 with d1
    karen "Hello, welcome to the... [me]!?"
    mia "Karen, you work here?"
    karen "Hey Mia, yeah I started last month when the store opened, the owner is an old friend."
    "She looks embarrassed, she is not even looking at me. Strange, is it because of me?"
    hide npc_portrait_karen_01 with d1
    show npc_portrait_mia_06 at top with d1
    mia "Bro and I where looking for our favorite ice cream shop, it's been some time since we came here so maybe we made a wrong turn somewhere..."
    karen "What's the name of the place?"
    mia "Snow White."
    hide npc_portrait_mia_06 with d1
    show npc_portrait_karen_02 with d1
    karen "Shit, sorry Mia, the shop used to be here, but they moved to the other side of the town."
    mia "No way, what do we do now?"
    me "I guess there is nothing we can do, let's just go home we will look for it some other day."
    mia "Awww... fine, bye Karen it was nice to see you."
    hide npc_portrait_karen_02 with d1
    show npc_portrait_karen_03 with d1
    karen "Bye... I-it was nice seeing you [me]."
    me "Likewise, Karen."
    hide npc_portrait_karen_03 with d1
    "Mia breaks the silence after we leave the store."
    show npc_portrait_mia_06 at top with d1
    mia "She is totally into you, you know."
    me "You think?"
    mia "I know, but she is too shy to tell you, she is a nice girl why don't you ask her out."
    me "I will think about it, let's go home?"
    mia "Let's!"
    hide npc_portrait_mia_06 with d1

    menu:
        "Go home":
            jump lbl_home_living_room

## MALL - DAY 2 ##
label lbl_city_mall_day2:
    "I should probably look for Karen."
    show npc_portrait_karen_04 at top with d3
    me "Hey Karen."
    karen "[me] is that you you came to buy something?"
    me "Actually I came to see you, want to go to the cafe?"
    karen "That is sweet of you but I can't leave the store now."
    me "But it's empty."
    karen "I know and it's probably going to stay empty for the rest of the day, but the manager won't let me set a foot outside of the shop. However, if we stayed in the back were the employee, and by that I mean me, take a break, we could probably talk a bit."
    me "Great."
    hide npc_portrait_karen_04 with d5
    show img_karen_couch_01 with d5
    karen "You know [me], I'm glad you came to visit... did Veronica told you what I said about you?"
    me "Yeah she did."
    hide img_karen_couch_01 with d1
    show img_karen_couch_02 with d1
    "She leans closer."
    karen "That's good, then you know why I brought you here."
    me "Yes..."
    hide img_karen_couch_02 with d1
    show img_karen_kiss at top with d1
    "This is amazing, this might be the best moment of this day. I'm kissing a hot girl and don't have to feel guilty about it. But it doesn't last long."
    hide img_karen_kiss
    show npc_portrait_hitomi_01
    hitomi "Karen, why are you here and who is this?"
    karen "Oh Ms. Tanaka this is a friend..."
    hitomi "Look I'm not against some down time, with \"friends\", but you should be working now, so get to it or do you want to find a new job?"
    me "I'm sorry it was my idea and..."
    karen "No [me] it's fine, we will talk later."
    "She goes to the front of the store leaving me with her boss."
    me "Ms. Tanaka is it? I'm really sorry..."
    hide npc_portrait_hitomi_01 with d1
    show npc_portrait_hitomi_02 with d1
    hitomi "You know, I don't mind if you visit her but do it during her break from now on, ok. And maybe you could stay after her break ends to get to know someone else."
    me "Sure...?"
    hitomi "Now get moving."
    hide npc_portrait_hitomi_02 with d1

    $ f_day2_mall_karen = True

    menu:
        "Go home":
            jump lbl_home_living_room

## MALL - DAY 3 ##
label lbl_city_mall_day3:
    if v_time < 780:
        "The antique store is closed for lunch."

    elif v_time >= 780 and v_time < 900 and tb_event[3]["city_mall"]["karen"] == 0:
        "Karen is here now, maybe I should talk to her."
        show npc_portrait_karen_05 with d1
        me "Hello Karen."
        karen "[me]? What are you doing here?"
        me "I saw you here and thought I'd say hi."
        karen "That's nice of you, working in an antique store can be very boring, Hitomi... I mean Miss Tanaka is in her office most of the time."
        me "Why are you working here if you don't like it then?"
        karen "It's complicated, I just need the money."
        "She doesn't look like she wants to talk about this. Time to change the subject."
        me "Did you know what happened in the college today? Veronica got a days suspension."
        hide npc_portrait_karen_05 with d1
        show npc_portrait_karen_06 at top with d1
        karen "What for?"
        me "She was caught, having sex with someone on a classroom."
        karen "Really, she never changes does she? I would never even dream of doing something like that."
        me "Not even with the right person?"
        "I smile seductively."
        karen "Well... maybe with the right person..."
        hide npc_portrait_karen_06 with d1
        show img_karen_kiss at top with d1
        "She returns my smile, and start to get closer and closer."
        hide img_karen_kiss
        show npc_portrait_hitomi_03 with vpunch
        hitomi "Karen have you... You young people, haha, I would just leave now, but you still have to work Karen."
        karen "Hito... Miss Tanaka, sorry we..."

        if f_day2_mall_karen:
            hitomi "No need to explain Karen, you are young and full of energy, but do try to keep this activities to the break time. And you, [me]."
            me "Yes miss?"
        else:
            hitomi "No need to explain Karen, you are young and full of energy, but do try to keep this activities to the break time. And you, what's your name?"
            me "I'm [me] miss."

        hitomi "Call me Hitomi, her break is between 3 and 4 PM, you can come here to \"talk\" to her then, but before you leave, I need some muscle here in my office can you help me?"
        me "Uhh, sure."
        hitomi "And Karen, to work my darling, we have clients entering the store."
        hide npc_portrait_hitomi_03 with d1
        "Karen goes to talk to the clients, while I enter Hitomi's office."
        hitomi "Here can you put this box on the top shelf?"
        me "No problem."
        "The box is not heavy at all, but the shelf is so high up that after pushing it to the back, I accidently lose my balance and fall on top of Hitomi, with hands and face on those enormous boobs of hers. They are soft and warm and... wait is she ok?"
        me "Shit, Hitomi are you ok?"
        hitomi "I'm fine, but most important is that a metal pipe in your pants?"
        me "That's..."
        hitomi "Oh... I guess you liked the place where you landed then? I can't blame you."
        "We both stand up."
        show npc_portrait_hitomi_04 with d1
        hitomi "It looks like the box is were where I asked you to put it and we have no broken bones, I call that a well done job."
        me "You are welcome."
        hitomi "Before you go care to tell me something [me]. Did you liked to fondle my breasts?"
        me "It was an accident, but I can't say it was unpleasant."
        hitomi "Give me your hand then."
        hide npc_portrait_hitomi_04 with d1
        show vid_hitomi_boobs at top with d1
        me "She grabs my hand, removes her shirt and puts it in her massive juggs."
        hide vid_hitomi_boobs with d1
        hitomi "Something for you to remember from me. If you are in the mall when Karen is working I would be happy to entertain you while you wait. Now go on, I have to finish a report."
        me "Sure, later Hitomi."

        $ tb_event[3]["city_mall"]["karen"] = 1
        $ v_time += 10

    elif v_time >= 780 and v_time < 900 and tb_event[3]["city_mall"]["karen"] == 1:
        "I will come back later."

    elif v_time >= 900 and v_time < 960 and tb_event[3]["city_mall"]["karen"] == 0:
        "Karen is here. Looks like she works at the antique shop, let's talk to her."
        show npc_portrait_karen_05 with d3
        me "Hey Karen."
        "[me], what are you doing here?"
        me "I was walking around when I saw you, I wanted to tak to you."
        karen "That's so sweet, I'm on my break now, come with me we can talk in the break room."
        hide npc_portrait_karen_05 with d1

        menu:
            "Lead the way":
                pass

        scene loc_city_mall_break
        show img_karen_couch_01 with d1
        karen "So [me], how are things lately?"
        me "They are good, so why do you work here? You need money or something like that?"
        karen "Kind of, it's..."
        "She looks a bit sad."
        me "Hey did you know Veronica got a day of suspension after being caught fucking a dude in a class?"
        karen "Really? Hahaha, she never changes does she. I would never dream of doing that in public."
        me "What if it was the right person?"
        "I give her my best seductive look."
        karen "If it was the right person, maybe..."
        hide img_karen_couch_01 with d1
        show img_karen_couch_02 with d1
        "She comes closer and closer."
        hide img_karen_couch_02 with d1
        show vid_karen_boobs at top with d1
        "We stand there kissing for a good time, but she finally finds some courage and starts to massage my cock from outside of my pants. To not be left behind I put my hand inside her top and feel her boobs."
        hide vid_karen_boobs with d1
        karen "[me]... w-we can't go too far, my boss will not be happy... but I can't just let you leave empty handed."

        "She takes to her knees and opens my pants."
        show img_karen_blowjob_02 with d1
        "She starts slow at first but them picks up the pace, her mouth is so warm it's like I'm going to melt."
        hide img_karen_blowjob_02 with d1
        show vid_karen_blowjob_03 at top with d1
        me "Karen... I'm..."
        karen "Do it, let me taste you cum."
        hide vid_karen_blowjob_03 with hpunch
        "She looks like she is in a bliss, and stays that way for a few seconds, but then she stands up."
        karen "Do you think you will come here again?"
        me "I will, nothing would stop me."
        karen "Then I will have an even better surprise for you next time. But I have to work now, I will see you later."
        me "Later Karen."

        $ tb_event[3]["city_mall"]["karen"] = 2
        $ v_time += 15

    elif v_time >= 900 and v_time < 960 and tb_event[3]["city_mall"]["karen"] == 1:
        "Karen is on her break now, let's go visit her."
        show npc_portrait_karen_05 with d3
        "Hello Karen."
        "[me] you came back, if you want to pick up from where we left off come with me."
        hide npc_portrait_karen_05 with d1

        menu:
            "Lead the way":
                pass

        scene loc_city_mall_break
        "Once we are inside she wastes no time, she give me a passionate kiss."
        show vid_karen_boobs at top with d1
        "We stand there kissing for a good time, but she finally finds some courage and starts to massage my cock from outside of my pants. To not be left behind I put my hand inside her top and feel her boobs."
        karen "[me]..."
        hide vid_karen_boobs with d1
        "She is moaning, she then takes the next step, and takes my cock out and starts massaging it while I take her boobs out as well."
        show vid_karen_blowjob_01 at top with d1
        "We can't contain our lust, maybe it's time to lose my V card... No, I will make this decision with a cool head... but it's so hard when she is giving me a blowjob like this..."
        me "Karen... I..."
        hide vid_karen_blowjob_01 with d1
        show vid_karen_cuni at top with d1
        "That's when an idea comes to mind, I grab her and at the same time start licking her pussy."
        window hide
        hide vid_karen_cuni with d1
        show vid_karen_69 at top with d1
        pause
        hide vid_karen_69 with d1
        "After a little while we reach our climaxes together."
        "She looks like she is in a bliss, and stays that way for a few seconds, but then she stands up."
        karen "Do you think you will come here again?"
        me "I will, nothing would stop me."
        karen "Then I will have an even better surprise for you next time. But I have to work now. I will see you later."
        me "Later Karen."

        $ tb_event[3]["city_mall"]["karen"] = 2
        $ v_time += 15

    else:
        "It say here the store is closed because of an emergency. Guess I will come back tomorrow."

    menu:
        "Back to Third Street":
            jump lbl_city_street_3th

### COFFEE ###
## COFFEE - DAY 4 ##
label lbl_city_mall_coffee_day4:
    show npc_portrait_lily_07 with d3
    "We take a seat outside and order some food and coffee."
    me "So aunt did you go see grandma at the hospital?"
    hide npc_portrait_lily_07 with d1
    show npc_portrait_lily_08 with d1
    lily "I did..."
    "She does not look all that trilled."
    me "What do you think about her?"
    lily "She looks decades younger and can't shut up about wanting to have sex with a hot dude. And that was yesterday... It's weird, mom was always uptight and now she is like that."
    me "I thought you would like it."
    hide npc_portrait_lily_08 with d1
    show npc_portrait_lily_10 with d1
    lily "So did I, but after being there it felt... I don't know. If Helen was alive how would you fell."
    me "If mom was alive? Good question, grandma was weird for me too, but my mother... I don't know auntie, but I've been thinking about it and have come to the conclusion that we should accept this world we have brought up as it is even if sometimes things get strange for us."
    me "We are the only one that remember the old one after all. I mean grandma would be in a bed for the rest of her life if everything stayed the same, but now she gets to live a new life. Even if she will probably want to fuck both off us soon..."
    lily "I... I think you are right. Well I already fucked my nephew, we are both doomed either way, hahaha."
    hide npc_portrait_lily_10 with d1
    "After a few more minutes of banter, we get into aunt Lily's car and she drops me off at the campus."

    menu:
        "Go to class":
            jump lbl_college_class

### LILY HOME ###
## LILY HOME - DAY 2 ##
label lbl_city_home_lily_day2:
    "That's her house, hope she is home."
    "I ring the doorbell."
    lily "One second!"
    show npc_portrait_lily_02 with d1
    lily "[me]!"
    "She hugs me and holds me tight... too tight."
    me "Aunt Lily I can't breathe."
    lily "Oh sorry, it's just, I haven't seen you in years, you never send pictures I didn't realise you had grown so much."
    me "Thanks, but can we talk inside, it's important?"
    lily "Come in let me make you some tea or coffee."
    me "Just water is fine."
    hide npc_portrait_lily_02 with d3
    show img_lily_couch at top with d3
    "She smiles at me and we head inside the house."
    lily "So, what did you want to talk about?"
    me "Do you know something about our family history, something about having the blood of a god or demon or..."
    hide img_lily_couch
    show npc_portrait_lily_03 at top
    "Her expression changes instantly from happy to nervous."
    lily "Why do you ask? Did something happened?"
    me "So you know something!"
    lily "I-I... There is a legend, told by my grandmother, about the time when a god would come back to this world and ascend his descendants. Some people took it serious, but my mother always thought it was bullshit, so your father and I stopped talking about it..."
    me "Well, what if it was true?"
    hide npc_portrait_lily_03
    show npc_portrait_lily_04 at top
    lily "[me], those are just fairy tales."
    "She was always terrible at lying."
    me "Really, well then I guess it was just a dream."
    lily "WHAT DREAM?"
    me "Well you see I had a dream were a woman named Nina offered me a way to change this world and I accepted."
    hide npc_portrait_lily_04
    show npc_portrait_lily_05 at top
    lily "You did! Awesome, it finally happened, this horrible world will finally be gone. Life has sucked for so long but now we can finally be happy."
    me "So... something you want to tell me dear aunt."
    hide npc_portrait_lily_05 with d1
    show npc_portrait_lily_06 with d1
    lily "Oh... I... I... Ok look, I always knew we were different, I could fell when people were... ehhh... excited. And men always flocked to me even when I was fat as a pig. And those stories grandma told us. I just knew this day would come."
    me "It did, do you know what kind of world she wants to make? Sex, sex everywhere, today has been the most strange day in the history of strange days aunt. First Lisa entered my room only on her lingerie..."
    lily "Oh! That is strange, for some reason a part of me thinks that's normal for her, and the other part is incredulous."
    me "And then Marcus became Marcy..."
    lily "{b}What{/b}? The name Marcy rings a bell, but I remember your friend Marcus..."
    me "That's good because we are the only ones, and then nurse Megan, forget about that."
    hide npc_portrait_lily_06
    show npc_portrait_lily_03 at top
    lily "I can't believe it, so this is what they were talking about? That's amazing!"
    me "It's what now?"
    lily "[me] this is great, I always had these urges, I wanted to go out and fuck the first cock in front of me..."
    me "Ok, I don't want to listen to this."
    lily "...I always masturbated a lot..."
    me "Why am I still listening."
    lily "...But everyone told me those were bad things so I suppressed then, but now..."
    me "OK, that's {b}enough{/b}. Are you even listening to what you are saying? That's crazy."
    hide npc_portrait_lily_03
    show npc_portrait_lily_05 at top
    lily "Really? So you are not enjoying this at all?"
    me "I..."
    lily "Ha, I know deep inside you have the heart of a pervert. Look I have to leave now, but Lisa invited me for dinner. We can talk about that later okay, just think about it."
    me "I-I will, I will be leaving now then, bye Lily."
    hide npc_portrait_lily_05 with d1
    show vid_lily_kiss_01 at top with d1
    "She kisses me with passion."
    hide vid_lily_kiss_01 with d3
    lily "See? Not bad at all."

    if f_day2_nurse:
        $ v_time = 720

        menu:
            "Back to college":
                jump lbl_college_yard

    else:
        $ v_time = 840

        menu:
            "Go back home":
                jump lbl_city_street_1st

## LILY HOME - DAY 3 ##
label lbl_city_home_lily_day3:
    if v_time < 780 and tb_event[3]["city_home_lily"]["lily"] == 0:
        "I ring the door bell."
        show npc_portrait_lily_02 with d3
        lily "[me], I'm glad you are here."
        me "Thanks Lily, I wanted to see you."
        lily "That's so sweet, but you came at a very bad time, I have to leave for work soon."
        me "I see, I will leave then."
        lily "No, stay, I just about to take a shower, we can talk in the bathroom."
        me "In the bathroom? Sure, why not."
        hide npc_portrait_lily_02 with d3
        "I follow her to the place, that's when it hits me, I never saw her naked, I wonder how does she look like..."
        show img_lily_shower_01 with d1
        "Holy shit... just... just... look at her, hot is not the right word to describe her, she could melt steel with her looks."
        lily "[me], honey, you are drooling."
        me "Oh... sorry, aunt Lily you are amazing."
        hide img_lily_shower_01 with d1
        show img_lily_shower_02 with d1
        lily "Thanks [me], by the way I noticed that you are different, is this..."
        me "Oh, I have no idea how it happened, but I can't complain."
        hide img_lily_shower_02 with d1
        show img_lily_shower_03 with d1
        lily "Nice..."
        hide img_lily_shower_03 with d1
        show img_lily_shower_04 at top with d1
        "We continue talking for some time, while I continue to drool on the floor. After she is done she puts her clothes and comes to talk to me."
        hide img_lily_shower_04 with d1
        lily "Hey [me], come see me in my office when you have the time, for now I need to leave, but my house is your house. I even have a room just for you so if you want to stay and wait for me, make yourself at home."
        me "Thanks Lily, but I think I should go explore the town for a bit."
        lily "I understand, but here, a copy of the keys, you can come in any time, even if I'm out ok."
        me "Ok."
        lily "Give me a kiss now."
        show vid_lily_kiss_01 at top with d1
        me "Bye."
        hide vid_lily_kiss_01 with d1

        $ tb_event[3]["city_home_lily"]["lily"] = 1
        $ v_time += 10

    if v_time >= 1140:
        "I tell Lisa my plans to sleep at my aunt and leave, in a few minutes I'm at her door. It's time."
        me "Hey aunt... GOD!"
        lily "Do you like it? Who am I kidding of course you do. Come on in."
        "She continues to lead me to her room, what happens next is a blur..."
        window hide
        show img_lily_boobs_02 with d1
        pause
        hide img_lily_boobs_02 with d1
        show img_lily_blowjob_01 with d1
        pause
        hide img_lily_blowjob_01 with d1
        show img_lily_sex_01 at top with d1
        pause
        hide img_lily_sex_01 with d1
        show vid_lily_sex_02 at top with d1
        pause
        hide vid_lily_sex_02 with d1
        show vid_lily_sex_03 at top with d1
        pause
        hide vid_lily_sex_03 with d1
        "That... was... awesome!"

        menu:
            "Wake up":
                pass

        show img_lily_nude_01 at top with d3
        "When I wake up I have a beatiful woman naked at my side. That so happens to be my aunt."
        lily "Good morning [me]."
        me "Morning beautiful."
        lily "Haha, beautiful? Thanks [me]."
        me "Did you sleep well?"
        lily "It was the best night I had in years, I even feel different."
        me "How so?"
        lily "I don't know, like I'm connected, to you in some way."
        me "That's weird..."
        hide img_lily_nude_01 with d1
        show img_lily_nude_02 with d1
        lily "Thanks for ruining the mood, haha. Want to eat some breakfast? There is a coffee shop around the corner, they sell some great sandwiches."
        me "Sure,I will get my wallet and."
        lily "Don't be silly, leave it to me."
        me "Okay, thanks Lily."
        hide img_lily_nude_02 with d1
        show npc_portrait_lily_01 with d1
        lily "But hey wanna go out just in underware to see what people will do?"
        me "No."
        lily "Awww..."
        hide npc_portrait_lily_01 with d1

        $ tb_event[3]["city_home_lily"]["lily_sex"] = 1
        $ v_day = 4
        $ v_time = 0

        jump lbl_city_mall_coffee

    else:
        "She is not here, so there is nothing to do here now."

    menu:
        "Back to Second Street":
            jump lbl_city_street_2nd

### PRYIA HOME ###
## PRYIA HOME - DAY 3 ##
label lbl_city_home_pryia_day3:
    if v_time >= 720 and v_time < 960:
        "She is not here right now, must be working."

    elif v_time >= 960 and v_time < 1080 and tb_event[3]["city_home_priya"]["priya"] == 0:
        "I decide to see what our other neighbour Priya is doing. I used to spy on her sunbathing. Once I even caught her topless, I'm pretty sure she knew that I was looking but she didn't seem to care. I think it excited her even."
        show img_priya_pool_01 with d1
        "I sneak to my old pepping spot, and it looks like she is busy."
        window hide
        hide img_priya_pool_01
        show img_priya_pool_02 with d1
        pause
        hide img_priya_pool_02 with d1
        show img_priya_pool_03 with d1
        pause
        hide img_priya_pool_03 with d1
        show img_priya_pool_04 with d1
        "Did she just wink at me? Well now I really know she likes to be watched."
        hide img_priya_pool_04 with d1

        $ tb_event[3]["city_home_priya"]["priya"] = 1
        $ v_time += 10

    else:
        "She must be out right now."

    menu:
        "Back to First Street":
            jump lbl_city_street_1st

### 1ST STREET ###
## 1ST STREET - DAY 2 ##
label lbl_city_street_1st_day2:
    if v_time == 720:
        "Lisa should be having lunch right now maybe I should go talk to her, but Sarah told me to visit maybe I should ask her about Marcus, see if she remember him at all."
        menu:
            "Home":
                jump lbl_home_living_room
            "Sarah":
                jump lbl_city_home_marcy

    elif v_time == 840:
        "Where should I go?"

        menu:
            "Home":
                $ v_time = 900
                jump lbl_home_room_mia
            "Marcy":
                jump lbl_city_home_marcy_room
            "Mall":
                jump lbl_city_mall
            "Visit the church":
                jump lbl_city_church
            "Visit the beach":
                jump lbl_city_beach

## 1ST STREET - DAY 3 ##
label lbl_city_street_1st_day3:
    "On out way to Marcy Mia decides to ask me something."
    show npc_portrait_mia_15 with d1
    mia "So bro, what do you think of lesbians."
    "After picking my jaw from the floor I answer."
    me "Why are you asking me this? Are you...?"
    mia "What no, it's just... Veronica talked to me about teaching me some tricks on the bed and she said we could have some fun while doing it... But is that weird?"
    "Wow, that would be great to see, but what if Veronica takes her virginity before me? Should I take the risk?"

    menu:
        "Yes":
            me "I think it's a good idea sis, Veronica is, how should I put this..."
            mia "Experienced."
            me "Yes, that's the word."
            mia "If you think so bro, I will go to her house later today I think, want me to send you pictures?"
            me "You would do that?"
            mia "Maybe, you have been a good brother, so maybe you deserve it..."
            hide npc_portrait_mia_15 with d1
            "I can't wait to see it now."

        "No":
            me "Mia, I don't know, I don't have nothing against some fun between girls, but if you want some tips, maybe I can help you instead..."
            mia "Wow, wait a minute bro, are you jealous?"
            me "What, me, no, I just..."
            mia "That's so cute! I will tell V to wait on those leasons for now okay."
            me "Thanks Mia."
            hide npc_portrait_mia_15 with d1
            "Mia's first time is mine Veronica, maybe mine is also hers... we will see."

    menu:
        "Marcy's house":
            jump lbl_city_home_marcy

## 1ST STREET - DAY 4 ##
label lbl_city_street_1st_day4:
    "We leave the house and pick Marcy as usual."
    marcy "So... why are you both so happy?"
    me "Mia and I just came to an understanding."
    marcy "Meaning..."
    me "We got closer as people, and as a man and a woman."
    show npc_portrait_marcy_03 with d1
    marcy "YOU GUYS FUCKED EACH OTHER???"
    hide npc_portrait_marcy_03 with d1
    show npc_portrait_mia_16 with d1
    mia "Marcy, shut up we don't want the whole street to know."
    hide npc_portrait_mia_16 with d1
    marcy "SO YOU DID???"
    me "Yes now just stop screaming."
    marcy "You guys...I can't believe it. Does Lisa know?"
    mia "No, and we want to keep it that way."
    marcy "Oh, I got it, it's like those novel you read, secret and forbidden love between brother and sister."
    mia "In a way, yes. But we are not related by blood. Not that it would matter to mom. She would not be happy at all. Even though she apparently also wants his body."
    marcy "She does? Wow, you are getting yourself quite the harem dude, when will it be my turn? Will you add my mother too? Gotta catch them all!"
    "We all laugh at that joke. If only she knew the truth."

    menu:
        "Go to class":
            jump lbl_college_class

### BEACH ###
## BEACH - DAY 2 ##
label lbl_city_beach_day2:
    show img_beach_topless with d1
    "Here is the beach, looks like everything is mostly normal here, more topless woman than normal, but nothing very strange."
    hide img_beach_topless with d1
    show img_beach_nude_01 at top with d1
    "Spoke too soon..."
    hide img_beach_nude_01 with d1
    window hide
    show img_beach_nude_02 at top with d1
    pause
    hide img_beach_nude_02 with d1

    menu:
        "Go home":
            jump lbl_home_living_room

## BEACH - DAY 3 ##
label lbl_city_beach_day3:
    if v_time < 780:
        show vid_beach_boobs_01 at top with d3
        "Nice view."
        hide vid_beach_boobs_01 with d1
        window hide
        show vid_beach_boobs_02 at top with d1
        pause
        hide vid_beach_boobs_02 with d1
        show vid_beach_boobs_03 at top with d1
        pause
        hide vid_beach_boobs_03 with d3
        "After a few minutes I leave."

    elif v_time >= 780 and v_time < 960 and tb_event[3]["city_beach"]["nyomi"] == 0:
        "I came to the beach to relax, but soon I saw a face I knew..."
        show img_nyomi_beach_01 with d3
        "This Nyomi, Sarah's sister and Marcy's aunt, she helped Sarah take care of Mia and I sometimes when Sarah was too busy. I haven't seen her in almost a year... she is as sexy as I remember."
        hide img_nyomi_beach_01 with d1
        show img_nyomi_beach_02 at top with d1
        nyomi "[me]? Is that you?"
        me "It is, how are Nyomi?"
        nyomi "I'm great, is been so long, you are even more handsome, girls must be falling for you all over the place."
        me "Hahaha..."
        nyomi "Sit down let's talk, get confortable, most people don't wear any clothes to this beach, so if you want take those shorts off."
        hide img_nyomi_beach_02 with d1
        show img_mc_body_01 at top with d1
        "Why not? It will be a new experience."
        hide img_mc_body_01 with d1
        show img_nyomi_beach_03 with d1
        nyomi "Oh my you have grown, in all the right places..."
        me "Uhhh, thanks..."
        "We spend a few minutes catching up, talking about all that has happened in our lives."
        nyomi "I need to go now, but you should come to my house, if you can bring my niece with you, she never visits anymore."
        me "Sure Nyomi."
        hide img_nyomi_beach_03 with d3

        $ tb_event[3]["city_beach"]["nyomi"] = 1

    elif v_time >= 780 and v_time < 960 and tb_event[3]["city_beach"]["nyomi"] == 1:
        show img_nyomi_beach_01 with d3
        "Nyomi is here but it's best to leave her alone."
        hide img_nyomi_beach_01 with d3

    elif v_time >= 960 and tb_event[3]["college_gym"]["bonnie"] == 0 and f_day1_lisa_bathroom_incident:
        show img_bonnie_beach with d3
        "That is Bonnie, the crazy girl that entered the man's bathroom while I was taking a shower."
        hide img_bonnie_beach with d3

    elif v_time >= 960 and tb_event[3]["college_gym"]["bonnie"] == 1 and f_day1_lisa_bathroom_incident:
        "Bonnie is here, let's talk to her."
        me "Hey Bonnie."
        show img_bonnie_beach with d1
        bonnie "Hiii..."
        "We talk for a few minutes, it was a nice chat."
        hide img_bonnie_beach with d1

    elif v_time >= 960 and tb_event[3]["college_gym"]["bonnie"] == 0 and not f_day1_lisa_bathroom_incident:
        "I don't know anyone here, except maybe..."
        show img_bonnie_beach with d1
        "No never seen her before."
        hide img_bonnie_beach with d1

    elif v_time >= 960 and tb_event[3]["college_gym"]["bonnie"] == 1 and not f_day1_lisa_bathroom_incident:
        show img_bonnie_beach with d3
        "That strange girl is here, let's talk to her."
        "After a few minutes I leave."
        hide img_bonnie_beach with d3

    $ v_time += 5

    menu:
        "Leave":
            jump lbl_city_map

### CHURCH ###
## CHURCH - DAY 2 ##
label lbl_city_church_day2:
    "This is the local church, maybe they can help me with my crysis..."
    show npc_portrait_nun_01 with d1
    nun "Hello, young man, can I help you?"
    me "Hello sister, can I speak with the priest?"
    nun "Sorry he isn't here right now, but maybe I can help?"
    me "Maybe, have you noticed something wrong with our city today?"
    nun "What do you mean exactly?"
    me "People seem a bit too open to desire today, it's like someone turned on the lusty buttom on everyone, my sister almost french kissed me in front of my friend today."
    me "My... someone who is like a mother to me entered my room half naked today and didn't think much of the erection I got..."
    "She is uncomfortable, maybe I should hold back on the details..."
    nun "Mister, why do you think that's strange? I mean people shouldn't be making love on the streets but the holy book teaches us that this passion is a gift and should not be ashamed to express our love physically."
    me "It does?"
    nun "Yes, the goddess teaches us that..."
    "Goddess? What is going on here, now that she mentioned it, the figures on the wall are mostly feminine."
    nun "...and that's why you should always wash your hands after touching the doornobs."
    me "Oh, right thanks sister, I should go now, but thanks for the advice."
    hide npc_portrait_nun_01 with d1
    "Let's go home, I think someone owns me anwers, and she should be back in my room later."

    menu:
        "Go home":
            jump lbl_home_living_room

## CHURCH - DAY 3 ##
label lbl_city_church_day3:
    if v_time < 840:
        "The place is empty, but I can hear Kyle's voice coming from a room."
        kyle "And remember, there is nothing wrong with being gay, that's what my greatest friend thought me."
        if f_day1_lisa_bathroom_incident:
            "Veronica was right!"
        else:
            "He is gay?"

    elif v_time >= 840 and v_time < 1020:
        show npc_portrait_nun_02 at top with d3
        "There are a few nuns here, their habits are not quite how I remember them."
        hide npc_portrait_nun_02 with d3

    elif v_time >= 1020 and v_time < 1080:
        "There is a line of nuns leading to somewhere in the back. This warants some investigation."
        show vid_church_nun_blowjob at top with d3
        "After some sneaking around I finally understand what is going on."
        "Sisters, receive my holy seed as the goddess demands."
        nun "Yes father."
        "Interesting demands Nina."
        hide vid_church_nun_blowjob with d3

    elif v_time >= 1080:
        "The church is closed for now, I will come back later."

    $ v_time += 5

    menu:
        "Back to Second Street":
            jump lbl_city_street_2nd

### PGP CORPORATION ###
## PGP CORPORATION - DAY 3 ##
label lbl_city_pgp_corporation_day3:
    if v_time < 780:
        "This is where Lily works? Nice, no wonder she can afford such a huge house. What is that sound?"
        show vid_rikki_blowjob_01 at top with d1
        "Better leave them alone."
        hide vid_rikki_blowjob_01 with d1

    elif v_time >= 780 and tb_event[3]["city_pgp_corporation"]["lily"] == 0:
        show npc_portrait_rikki_01 with d1
        me "Hi, I'm [me], can I see Lilith? She is new here."
        rikki "Oh, so you are the famous [me]? She talks about you all the time, you are as handsome as she says, go on in third door on the right."
        me "Thanks."
        hide npc_portrait_rikki_01 with d1
        "Third door she said... right here then."
        "*Knock* *knock*"
        lily "Come in."
        me "Hi auntie."
        show npc_portrait_lily_11 with d1
        lily "[me]! Came to visit little old me?"
        me "I did, I wanted to tell you about everything Nina told me so far..."
        "After a few minutes of explaining later."
        lily "Wow, seriously, cool, I noticed my libido is taking a lot of effort to control as of late."
        me "I know right! I have a bonner everywhere I go, it's worse than an overdose of the blue pill."
        lily "I can see that."
        me "And I can hear that buzzing sound coming from under your desk..."
        lily "Guilty, but since you are here how about we help each other."
        me "What kind of help? Like a handjob?"
        hide npc_portrait_lily_11 with d1
        show npc_portrait_lily_12 with d1
        lily "No dummie, I want you to pull that cock out and fuck me."
        me "Whoa, whoa, calm down Lily, I have been taking advantage of the situations that arise but I haven't taken that step yet."
        lily "Oh, I get it, waiting for the right girl to fuck are we?"
        me "I don't know, maybe, or maybe it's like when you are in a candy store and you don't know what you want to pick."
        hide npc_portrait_lily_12 with d1
        show npc_portrait_lily_11 with d1
        lily "How about this, come stay the night in my home today if you are ready, I don't think Mia or Lisa are ready for that either. So if you want to keep it in the family, you come or blue balls for a day or two, it's your call."
        me "Ok I will think about it."
        lily "Do you want to talk about something else?"
        me "No, I think it's time for me to go, bye aunt Lily."
        hide npc_portrait_lily_11 with d1
        show img_lily_boobs_01 with d1
        lily "Bye, [me] but before you leave here is some motivation."
        me "Great Scott!"
        hide img_lily_boobs_01 with d3
        "After I leave, moans start coming from the office."

        $ tb_event[3]["city_pgp_corporation"]["lily"] = 1
        $ v_time += 5

    elif v_time >= 780 and tb_event[3]["city_pgp_corporation"]["lily"] == 1:
        show loc_city_pgp_corporation_office_lily at top with d1
        "She is probably busy now, it's best not to disturb her."
        hide loc_city_pgp_corporation_office_lily at top with d1

    $ v_time += 5

    menu:
        "Back to Second Street":
            jump lbl_city_street_2nd

### GYM ###
## GYM - DAY 3 ##
label lbl_city_gym_day3:
    if v_time < 840:
        "The gym is closed for lunch right now."

    elif v_time >= 840 and v_time < 960 and tb_event[3]["city_gym"]["veronica"] == 0:
        show vid_veronica_gym_01 at top with d1
        "This is the gym that is closest to my house, it's decent, my membership is still valid, but I haven't come here to train in a long time. I see a friendly face, Veronica."
        hide vid_veronica_gym_01 with d1
        show img_veronica_gym_02 with d1
        veronica "[me], I haven't seen you here before, are you a new member?"
        me "Not exactly, I bought a 2 years membership along time ago, come in once and never again."
        veronica "Whoa, then how do you keep those guns?"
        me "Guns? Oh, you mean how do I keep in shape? Would you believe me if I said magic?"
        veronica "Haha, very funny, are you thinking of begin coming in now?"
        me "Well I did pay for the membership, even if it expires in a couple of month, I should get some use out of it."
        veronica "That's cool, I think Marcy's mom and Lisa also come here."
        me "They do. It was Lisa who convinced me to buy that membership."
        hide img_veronica_gym_02 with d1
        show img_veronica_gym_03 with d1
        veronica "Do you want some help, whatever you have been doing to keep in shape, you could always use the help when dealing with this equipment."
        me "Sure, why not."
        "I start to work out, and Veronica stays by my side giving me tips."
        me "Hey Veronica, can I ask you a personal question?"
        hide img_veronica_gym_03 with d1
        show img_veronica_gym_02 with d1
        veronica "Go ahead."
        me "You have a reputation... people call you a..."
        veronica "Slut? Yes that's what happens when you go around sleeping with every dick available, and some woman too, but I'm happy with my choices, I guess even I would call myself a slut at this point. Why?"
        me "Well, you like to flirt with almost every male around but you never even suggested doing something sexual with me. Why?"
        veronica "Look at the time, it's time for me to talk with someone... You should go take a shower!"
        hide img_veronica_gym_02 with hpunch
        "And in a flash she disappears from my sight, I think she was embarrassed..."

        menu:
            "Shower":
                scene loc_college_shower_men
                pass

        show img_veronica_gym_04 with d1
        "I start to enjoy a great shower when Veronica bursts in the room."

        if tb_event[3]["college_garden"]["veronica"] == 1:
            veronica "Look, about what I said, yes I would like for you to fuck me, in fact I think about it all the time. The reason I sleep around so much is because I can't have the one guy I have been fantasising for years and..."
        else:
            veronica "Look, about what you asked, you are my best friend's brother, and I know Mia likes you a lot. So it would not be fair to take away from her the chance for the both of you to lose you virginity together."
            veronica "No matter how much I want to fuck you, and trust me I have been fantasizing about you even before I knew what the word sex meant and..."

        hide img_veronica_gym_04 with d1
        "She pauses for a second and realises what she just said, she then try to run away but I grab her by the waist."
        me "Before you go, I need to say some things myself. I get that you don't want to lose a friend but I'm not exclusive property of my sister, and I can have sex with whoever I choose. Mia know this, maybe she want to wait for me, but it's my decision to make if I will wait for her."
        veronica "But [me] I..."
        me "Just as it is your decision to have sex with me or no, but that does not mean we can't do some other stuff together."
        "She stopped strugling so I let her go."
        me "So what do you think?"
        veronica "I don't know, I still think I will wait for Mia to find the will to do it with you first, but..."
        me "But..."
        veronica "I wanted to taste you for a long time and after that hug, I don't think I can wait any longer."
        show vid_veronica_blowjob at top with d1
        "She drops on her kneed and grabs my cock."
        me "Ver... that's.... ahh..."
        hide vid_veronica_blowjob with hpunch
        me "I'm cumming..."
        veronica "So, will you tell her what just happenned?"
        me "If you want to keep it a secret, I will keep my mouth shut, but in my opinion you should tell her."
        veronica "I think you are right. You can finish your shower, we will see each other some other time."
        me "Bye V."
        veronica "Only Mia is suposed to call me that... but I will make on exception for you."

        $ tb_event[3]["city_gym"]["veronica"] = 1
        $ v_time += 15

        menu:
            "Back to the gym":
                jump lbl_city_gym

    elif v_time >= 960 and v_time < 1020 and tb_event[3]["city_gym"]["sarah"] == 0:
        show img_sarah_gym_01 at top with d1
        "Looks like Sarah is keeping in shape."
        sarah "Hey [me], do you still have that membership you bought a couple years ago."
        me "Yep, still valid for two months."
        sarah "I still don't know how you got so... muscular without regular visits, hahaha."
        me "Yeah, good genetics I think..."
        sarah "Yeah those pesky genetics, I got these thanks to my mother you know."
        "She points at her boobs."
        sarah "All men should thank her for them, me on the other hand have to keep exercising regulary to avoid back pain. I have thought about having a surgery to..."
        hide img_sarah_gym_01
        show img_sarah_gym_02 with vpunch
        me "Noooo!"
        "Shit, that slipped out..."
        sarah "Whoa, I guess you really do like them, hahaha."
        me "Yeah, that's..."
        sarah "Calm down [me], I'm not getting under the knife, that idea was scratched a long time ago, also those back pains have been getting even more rare in the last few days..."
        "Nina you are the best, you really do think of everything."
        sarah "Well, I'm finished, can you help me take my top off there is this stupid zipper in the back please."
        hide img_sarah_gym_02 with d1
        "Her mouth says something innocent, but her eyes say that she intends to do something naughty..."
        me "I would love to."

        menu:
            "Follow her":
                scene loc_college_locker_room
                pass

        sarah "Here we are, unzip it for me, please."
        show img_sarah_nude with d1
        "It's an easy request, done in seconds."
        sarah "Thanks [me], so since you like my puppies so much how about I use them as a way to thank you properly?"
        me "I do like the sound of that."
        sarah "Then pull it, I garantee you will love it."
        window hide
        hide img_sarah_nude with d1
        show vid_sarah_titjob at top with d1
        pause
        hide vid_sarah_titjob with d1
        show img_sarah_facial at top with d1
        me "Sarah that's... I'm cumming."
        hide img_sarah_facial with d3
        me "You were right, I loved it."
        sarah "Glad to hear it, but listen, let's keep this a secret from Marcy...."
        me "Keep it a secret? Why?"
        sarah "It's complicated, just trust me ok."
        me "If you say so."
        sarah "Great, now I have to go home, come by some time."
        me "I will..."
        "That's odd, why can't Marcy know?"

        $ tb_event[3]["city_gym"]["sarah"] = 1
        $ v_time += 15

        menu:
            "Back to the gym":
                jump lbl_city_gym

    elif v_time >= 1020 and v_time < 1080 and tb_event[3]["city_gym"]["lisa"] == 0:
        show img_lisa_gym_01 with d1
        "Lisa is here now, she always try to stay in shape."
        me "Hi Lisa."
        hide img_lisa_gym_01 with d2
        lisa "Sweetie, I'm so glad to see you back here, are you going to start frequenting the place again?"
        me "Maybe, for today I was just exploring the town and ended up here."
        lisa "Well if you decide to start working out here again, maybe we could help each other on our routines."
        me "That's a good idea, do you want some help right now?"
        lisa "In fact yes I do, can you help me do some stretches?"
        me "On it."
        window hide
        show vid_lisa_gym_02 at top with d1
        pause
        hide vid_lisa_gym_02 with d1
        lisa "That was great sweetie, it sure would be nice if you could help me everyday."

        me "Let's do this, if I have the time I will come by to help you."
        lisa "That would be great thanks."
        me "I will be going now."
        lisa "Bye [me], don't be late for dinner."

        $ tb_event[3]["city_gym"]["lisa"] = 1
        $ v_time += 15

    elif v_time >= 1080:
        "No one I know here but the view..."
        show vid_gym_01 at top with d1
        pause
        hide vid_gym_01 with d1
        show vid_gym_02 at top with d1
        pause
        hide vid_gym_02 with d1
        show vid_gym_03 at top with d1
        pause
        hide vid_gym_03 with d1

        $ v_time += 5

    else:
        "There is a lot of people here, no one I know though."

    menu:
        "Back to Third Street":
            jump lbl_city_street_3th

### PARK ###
## PARK - DAY 3 ##
label lbl_city_park_day3:
    if v_time < 1020:
        "Things here are still mostly normal... with some exceptions."
        window hide
        show img_park_exhibition_01 with d1
        pause
        hide img_park_exhibition_01 with d1
        show img_park_exhibition_02 at top with d1
        pause
        hide img_park_exhibition_02 with d1
        show img_park_exhibition_03 with d1
        pause
        hide img_park_exhibition_03 with d1

        $ v_time += 5

    elif v_time >= 1020 and v_time < 1080 and tb_event[3]["city_park"]["marcy"] == 0:
        "Marcy is here, she looks a litle sad."
        me "Are you ok?"
        marcy "Hey [me], I was just remembering, my dad used to bring me here everyday you remember."
        me "I do, you used to call me and we would come here and run around for hours."
        marcy "Yeah, things were simpler back then."
        me "I remember sometimes we would jump in the water and your dad has to give us his jacket because our clothes were soaked."
        show vid_marcy_boobs_bounce_02 at top with d1
        marcy "We had to go home naked under that \"blanket\" more than once. I miss him."
        hide vid_marcy_boobs_bounce_02 with d1
        me "I know, we are never ready for the dead of the ones we love."
        marcy "[me], can you stay here with for a while."
        me "Of course Marcy."
        "Later..."

        $ tb_event[3]["city_park"]["marcy"] = 1
        $ v_time += 20

    elif v_time >= 1020 and v_time < 1080:
        "There is nothing to do here now."

    else:
        "It's getting late and it's not completely safe to be in the park during the night yet."

    menu:
        "Back to Third Street":
            jump lbl_city_street_3th

### HOSPITAL ###
## HOSPITAL - DAY 3 ##
label lbl_city_hospital_day3:
    "On the way to the hospital I receive another e-mail this one reads:"
    if tb_event[3]["city_pgp_corporation"]["lily"] == 1:
        "{i}Hope you considered my proposal, I will wait for you in my room.\nxoxo Lily{/i}"
    else:
        "{i}Hey [me], I talked to Lisa and she has told me that you are still a virgin. I'd be more than happy to take that away from you. If you want to, come sleep in my house tonight... of course sleep is the last thing we will be doing. xoxo Lily{/i}"

    lisa "We are here [me], put the phone away."
    lisa "Hello, we are here to see Emma."
    unknown "Oh, I'm afraid only one person can go in at a time. "
    lisa "That's ok, [me] you go in, it's the first door on the left."
    show npc_portrait_grandma at top with d1
    "I follow the instructions and start walking to her room, I still remember the last time I saw her."
    hide npc_portrait_grandma with d1
    "I wonder if she's all right."
    show img_emma_hospital_01 at top with d1
    emma "[me]! My, it's been so long..."
    me "G-Grandma!?"
    emma "That's me [me], I missed you so much."
    me "Grandma you look... better."
    emma "I know right. I fell a few decades younger."
    "And looks like it too. Someone owes me some explanations."
    emma "Sit down, we haven't seen eachother in months. How is college?"
    me "It's good."
    emma "Have you rocked the boat of any young ladies?"
    me "Grandma!?"
    hide img_emma_hospital_01 with d1
    show img_emma_hospital_02 at top with d1
    emma "What? when I was your age I couldn't go more than a couple of days without some dick."
    "You know, I thought I would be used to this kind of conversations by now. But this! It's super awkward."
    emma "It's sad that all the nurses and doctors are woman, I haven't had any action in ages..."
    "It just got even more awkward..."
    emma "I still got it you know, if you were not my grandson, I would jump you as soon as you entered this room!"
    "Breath [me], that's how it's going to be from now on, better get used to it."
    emma "So, young man, do you think I'm still attractive enough?"
    me "I... I think so?"
    hide img_emma_hospital_02 with d1
    show img_emma_hospital_03 with d1
    emma "I knew it! Thanks [me], I mean look at my puppies..."
    emma "They still pack some punch don't they?"
    me "Definitely."
    hide img_emma_hospital_03 with d1
    "After that we talk for several more minutes, say our goodbyes and I leave."

    menu:
        "Leave the room":
            pass

    "After I leave the room, I bump into someone I was not expecting, Karen."
    show npc_portrait_karen_07 with d1
    karen "[me], what a surprise, what are you doing here?"
    me "I came to see my grandmother, she has been hospitalized here for a few years. What about you?"
    karen "I..."
    hide npc_portrait_karen_07

    if f_day2_mall_karen or tb_event[3]["city_mall"]["karen"] == 1:
        show npc_portrait_hitomi_05
        hitomi "Karen I spoke to the doctor and... [me], you are here too? Visiting someone?"
        me "My grandmother, yes. Why both of you are here?"
        karen "You see [me], Hitomi is a friend of my late father and she is helping me take care of my sister. She was hospitalized here too."
        me "Was?"
        hide npc_portrait_hitomi_05 with d1
        show npc_portrait_karen_08 with d1
        karen "She was discharged today, she just suddenly got better. I guess miracles do happen."
        hitomi "Indeed."
        karen "We have to go we are dealing with the papers of her release."
        me "I understand, I have to go too, Lisa and Mia are waiting for me. Bye Karen."
        hide npc_portrait_karen_08 with d1
        show img_karen_kiss at top with d1
        "I approach her for a kiss and she reciprocates."
        hide img_karen_kiss with d1
        show npc_portrait_hitomi_06 with d1
        hitomi "Oh young people are so lively."
        hide npc_portrait_hitomi_06 with d1
        show npc_portrait_karen_09 with d1
        karen "Come see me again in the store [me]."
        me "I will."
        hide npc_portrait_karen_09 with d1

    else:
        show npc_portrait_hitomi_05
        hitomi "Karen I spoke to the doctor and... oh hello, are you a friend of Karen?"
        me "Yes, I'm [me]. Nice to meet you miss..."
        hitomi "Please call me Hitomi."
        karen "She is a friend of my late father and she is helping me take care of my sister. She was hospitalized here too. She is also my boss and owner of the store I work in."
        me "Was hospitalized?"
        hide npc_portrait_hitomi_05 with d1
        show npc_portrait_karen_08 with d1
        karen "She was discharged today, she just suddenly got better. I guess miracles do happen."
        hitomi "Indeed."
        hide npc_portrait_karen_08 with d1
        show npc_portrait_hitomi_06 with d1
        hitomi "Karen I will go deal with the papers, why don't you stay here and talk to this lovely young man."
        hide npc_portrait_hitomi_06
        "Before she can say anything Hitomi disappears."
        me "Well, I guess you are stuck with me."
        karen "That's not a bad thing, can I ask you something?"
        me "Go ahead."
        karen "Veronica told me several times that I should ask you on a date, but I don't have the time, because I have to work all day... Could you if you have the time, visit me at the store?"
        me "Of course Karen, whenever you want."
        show npc_portrait_karen_09 with d1
        karen "That's great... shit I need to go, but I will see you later right?"
        me "Count on it."
        hide npc_portrait_karen_09 with d1
        show img_karen_kiss at top with d1
        "In her excited state she gives me a kiss and runs off to the distance."
        hide img_karen_kiss with d1

    menu:
        "Go home":
            jump lbl_home_room_mc