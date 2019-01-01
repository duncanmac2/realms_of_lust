#### LOCATIONS ####
label lbl_city_map:
    call main_show
    scene loc_city_map_back
    show loc_city_map at truecenter

    $ v_time += 5

    call screen scr_main_map

label lbl_city_beach:
    scene loc_city_beach

    if v_day == 2:
        jump lbl_city_beach_day2
    elif v_day == 3:
        jump lbl_city_beach_day3

### 1ST STREET ###
label lbl_city_street_1st:
    scene loc_city_street_1st

    if v_day == 1:
        jump lbl_city_home_marcus_day1a
    elif v_day == 2 and v_time == 0:
        jump lbl_city_home_marcy_day2a
    elif v_day == 2 and v_time > 0:
        jump lbl_city_street_1st_day2
    elif v_day == 3:
        jump lbl_city_street_1st_day3

## 1ST STREET - MARCY HOME ##
label lbl_city_home_marcy:
    scene loc_city_home_marcy

    if v_day == 1:
        jump lbl_city_home_marcus_day1b
    elif v_day == 2:
        jump lbl_city_home_marcy_day2b
    elif v_day == 3:
        jump lbl_city_home_marcy_day3

label lbl_city_home_marcy_bathroom:
    scene loc_city_home_marcy_bathroom

    if v_day == 2:
        jump lbl_city_home_marcy_bathroom_day2
    elif v_day == 3:
        jump lbl_city_home_marcy_bathroom_day3

label lbl_city_home_marcy_room:
    scene loc_city_home_marcy_room

    if v_day == 2:
        jump lbl_city_home_marcy_room_day2
    elif v_day == 3:
        jump lbl_city_home_marcy_room_day3

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
    scene loc_city_mall

    if v_day == 1:
        jump lbl_city_mall_day1
    elif v_day == 2:
        jump lbl_city_mall_day2
    elif v_day == 3:
        jump lbl_city_mall_day3

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
    "Her name is Sarah Williams, she used to be our nany back in the day, I had a crush on her back then, and can you blame me look at her even now she is beautiful."
    sarah "Hello guys, a bit late aren't you?"
    me "Sorry Sara, our alarms just didn't go off today."
    sarah "It's ok, Marcus is coming down in a second, he was also late today, he is in the bathroom right now, say he wasn't feeling well."
    me "He is not coming then?"
    sarah "He is, he said it was just a stomach ache, but he was going to \"take care of it\""
    "Take care of it... that is our code for he is masturbating, shit was he spying on our neighbors again?"
    me "Ok we will wait a bit, I think we can make it if we run."
    hide npc_portrait_sarah_01
    show npc_portrait_marcus at top with d3
    marcus "No need dude I'm right here, sorry for the wait I had to... take care of something..."
    "Definitely masturbating, he knows that I know, that's why he won't shake my hand... God damn it Marcus."
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
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sara buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        marcus "Let's go play some g..."
        hide npc_portrait_sarah_02 with d3
        "*Ring* *ring*"
        "It's my phone, Lisa is calling..."
        lisa "{i}[me], were are you? Doens't matter, come back home right now! You own me an explanation for what happend this morning.{/i}"
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
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sara buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        marcus "Let's go play some g..."
        hide npc_portrait_sarah_02 with d3
        "*Ring* *ring*"
        "It's my phone, Lisa is calling..."
        lisa "{i}[me], is Mia with you? She isn't aswering her phone.{/i}"
        me "Lisa, no she is with Veronica I think. Do you have her number?"
        lisa "{i}Yes, I will call her right now, she is in so much trouble...{/i}"
        "Poor Mia."
        "After the call Marcus and I spend some hour play some of his old games."
        me "It's getting late man, I will..."
        show npc_portrait_maria_01 with d3
        "Just as I start to stand to go home something catches my eyes."
        hide npc_portrait_maria_01 with d3
        show npc_portrait_maria_02 with d3
        marcus "Ohhh, [me] we are soo lucky, she rarely changes in her room. Let's enjoy this gift from the pervert god."
        hide npc_portrait_maria_02 with d3
        show npc_portrait_maria_03 with d3
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
        hide npc_portrait_sarah_03
        show npc_portrait_marcy_01 with d3
        "After a few minutes of waiting my worst fears become real."
        marcy "Hey [me]."
        me "I-I... hey... Marcy!?"
        marcy "Yes, that's my name... are you ok?"
        me "Why does everyone keep asking me that it's fine, ok!"
        marcy "Okaayyy... We should go then..."
        me "Yes, sure goodbye Sarah."
        sarah "Bye guys, and don't forget to visit."
        "Mia and Marcu...y keep looking at me like I'm crazy. Whatever is going on I have to keep calm, worrying them will not help me, let me try to keep my cool..."

        menu:
            "College":
                jump lbl_college_yard

## MARCY HOME - DAY 3 ##
label lbl_city_home_marcy_day3:
    "Mia rings the doorbell, Sarah comes to the door soon after."
    show npc_portrait_sarah_04 with d3
    sarah "Good morning guys, how are you."
    me "We are good Sarah thanks for asking, is Marcy ready?"
    sarah "I will call her just a second."
    hide npc_portrait_sarah_04 with d3
    mia "That's a nice lingerie don't you think bro, I wish I had something so stylish."
    me "You like it? Maybe you will get a nice gift sometime this week then."
    mia "Thanks bro you are the best."
    show npc_portrait_marcy_04
    marcy "Hey, if you are giving gifts give me one too."
    me "I only give gifts to people who are ready on time, unless you are going to college in that outfit I don't think you fit the criteria."
    marcy "Sorry, I spend the night playing games again, come in I will be ready in no time."
    me "Ok, we have the time, but don't take too long."
    marcy "Don't worry I will be right back."
    hide npc_portrait_marcy_04 with d3
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
    "The bathroom door is open is she in there?"
    show img_sarah_shower_05 with d3
    "Marcy?"
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
    "Shit, there its comes again... that overwhelming lust, I just can't take my eyes off her now."
    marcy "You are bigger than I remember..."
    "She points at another bulge in my pants... shit not again."
    me "Yes, this is..."
    hide vid_marcy_masturbate with d1
    show vid_marcy_boobs_bounce at top with d1
    marcy "Can I see it? I mean as friend... Here is something in return."
    "That is enough to snap me out of the trance."
    me "Bye Marcy!"
    hide vid_marcy_boobs_bounce
    marcy "What wait, I sorry..."

    menu:
        "Go home":
            jump lbl_home_living_room

## MARCY ROOM - DAY 3 ##
label lbl_city_home_marcy_room_day3:
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

### MALL ###
## MALL - DAY 1 ##
label lbl_city_mall_day1:
    me "Sorry man, I have some others plans."
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
    me "It can't be, maybe we came the wrong way here lets ask in here?"
    hide loc_city_mall_store with d3
    show npc_portrait_karen_01 with d3
    karen "Hello, welcome to the... [me]!?"
    mia "Karen, you work here?"
    karen "Hey Mia, yeah I started last month when the store opened, the owner is an old friend."
    "She looks embarrassed, she is not even looking at me... strange, is it because of me?"
    hide npc_portrait_karen_01 with d3
    show npc_portrait_mia_06 at top with d3
    mia "Bro and I where looking for our favorite ice cream shop, it's been some time since we came here so maybe we made a wrong turn somewhere..."
    karen "What's the name of the place?"
    mia "Snow White."
    hide npc_portrait_mia_06 with d3
    show npc_portrait_karen_02 with d3
    karen "Shit, sorry Mia, the shop used to be here, but they moved to the other side of the town."
    mia "No way, what do we do now?"
    me "I guess there is nothing we can do, let's just go home we will look for it some other day."
    mia "Awww... fine, bye Karen it was nice to see you."
    hide npc_portrait_karen_02 with d3
    show npc_portrait_karen_03 with d3
    karen "Bye... I-it was nice seeing you [me]."
    me "Likewise, Karen."
    hide npc_portrait_karen_03 with d3
    "Mia breaks the silence after we leave the store."
    show npc_portrait_mia_06 at top with d1
    mia "She is totally into you, you know."
    me "You think?"
    mia "I know, but she is too shy to tell you, she is a nice girl why don't you ask her out."
    me "I will think about it, let's go home?"
    mia "Let's!"

    menu:
        "Go home":
            jump lbl_home_living_room

## MALL - DAY 2 ##
label lbl_city_mall_day2:
    "I should probably look for Karen..."
    show npc_portrait_karen_04 at top with d3
    me "Hey Karen."
    karen "[me] is that you you came to buy something?"
    me "Actually I came to see you, want to go to the cafe?"
    karen "That is sweet of you but I can't leave the store now."
    me "But it's empty."
    karen "I know and it's probably going to stay empty for the rest of the day, but the manager won't let me set a foot outside of the shop. However, if we stayed in the back were the employee, and by that I mean me, take a break, we could probably talk a bit."
    me "Great."
    hide npc_portrait_karen_04 with d5
    show img_karen_couch_01 at top with d5
    karen "You know [me], I'm glad you came to visit... did Veronica told you what I said about you?"
    me "Yeah she did."
    hide img_karen_couch_01 with d1
    show img_karen_couch_02 at top with d1
    "She leans closer."
    karen "That's good, then you know why I brought you here."
    me "Yes..."
    hide img_karen_couch_02 with d1
    show img_karen_kiss at top with d1
    "This is amazing, this might be the best moment of this day, I'm kissing a hot girl and don't have to feel guilty about it. But it doesn't last long."
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

    menu:
        "Go home":
            jump lbl_home_living_room

## MALL - DAY 3 ##
label lbl_city_mall_day3:
    "bla"

    $ v_time += 5

    menu:
        "Back to Third Street":
            jump lbl_city_street_3th

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
    lily "I-I... There is a legend, told by my grandmother, about the time when a god would come back to this world and ascend his descendants, some people took it serious, but your my mother always thought it was bullshit, so your father and I stoped talking about it..."
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
    lily "You did!!! Awesome, it finally happened, this horrible world will finally be gone, life has sucked for so long but now we can finally be happy."
    me "So... something you want to tell me dear aunt."
    hide npc_portrait_lily_05 with d1
    show npc_portrait_lily_06 with d1
    lily "Oh... I... I... Ok look, I always knew we were different, I could fell when people were... ehhh... excited. And men always flocked to me even when I was fat as a pig. And those stories grandma told us. I just knew this day would come."
    me "It did, do you know what kind of world she wants to make? Sex, sex everywhere, today has been the most strange day in the history of strange days aunt. First Lisa entered my room only on her lingerie..."
    lily "Oh! That is strange, for some reason a part of me thinks that's normal for her, and the other part is incredulous."
    me "And then Marcus became Marcy..."
    lily "WHAT? The name Marcy rings a bell, but I remember your friend Marcus..."
    me "That's good because we are the only ones, and then nurse Megan, forget about that."
    hide npc_portrait_lily_06
    show npc_portrait_lily_03 at top
    lily "I can't believe it, so this is what they were talking about? That's AMAZING!!!"
    me "It's what now???"
    lily "[me] this is great, I always had these urges, I wanted to go out and fuck the first cock in front of me..."
    me "Ok, I don't want to listen to this."
    lily "...I always masturbated a lot..."
    me "Why am I still listening."
    lily "...But everyone told me those were bad things so I suppressed then, but now..."
    me "OK, that's ENOUGH. Are you even listening to what you are saying? That's crazy."
    hide npc_portrait_lily_03
    show npc_portrait_lily_05 at top
    lily "Really? So you are not enjoying this at all?"
    me "I..."
    lily "Ha, I know deep inside you have the hearth of a pervert. Look I have to leave now, but Lisa invited me for dinner, we can talk about that later okay, just think about it."
    me "I-I will, I will be leaving now then, bye Lily."
    hide npc_portrait_lily_05 with d1
    show vid_lily_kiss_01 at top with d1
    "She kisses me with passion."
    hide vid_lily_kiss with d3
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

    else:
        "She is not here, so there is nothing to do here now."

    menu:
        "Back to Second Street":
            jump lbl_city_street_2nd

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
            "I can't wait to see it now."

        "No":
            me "Mia, I don't know, I don't have nothing against some fun between girls, but if you want some tips, maybe I can help you instead..."
            mia "Wow, wait a minute bro, are you jealous?"
            me "What, me, no, I just..."
            mia "That's so cute! I will tell V to wait on those leasons for now okay."
            me "Thanks Mia."
            "Mia's first time is mine Veronica, maybe mine is also hers... we will see."

    menu:
        "Marcy's house":
            jump lbl_city_home_marcy


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
        show vid_city_beach_boobs_01 at top with d3
        "Nice view."
        hide vid_city_beach_boobs_01 with d1
        show vid_city_beach_boobs_02 at top with d1
        pause
        hide vid_city_beach_boobs_02 with d1
        show vid_city_beach_boobs_03 at top with d1
        pause
        hide vid_city_beach_boobs_03 with d3
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
        show img_mc_body at top with d1
        "Why not? It will be a new experience."
        hide img_mc_body with d1
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
    show npc_portrait_nun_01 with d3
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
    hide npc_portrait_nun_01 with d3
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
        show img_lily_boobs with d1
        lily "Bye, [me] but before you leave here is some motivation."
        me "Great Scott!"
        hide img_lily_boobs with d3
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
    "bla"

    $ v_time += 5

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

    menu:
        "Back to Third Street":
            jump lbl_city_street_3th