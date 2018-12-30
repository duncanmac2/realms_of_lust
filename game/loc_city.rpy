#### LOCATIONS ####
label lbl_city_beach:
    scene loc_city_beach

    if v_day == 2:
        jump lbl_city_beach_day2

label lbl_city_church:
    scene loc_city_church

    if v_day == 2:
        jump lbl_city_church_day2

label lbl_city_home_lily:
    scene loc_city_home_lily

    if v_day == 2:
        jump lbl_city_home_lily_day2

label lbl_city_home_marcy:
    scene loc_city_home_marcy

    if v_day == 1:
        jump lbl_city_home_marcus_day1b
    elif v_day == 2:
        jump lbl_city_home_marcy_day2b

label lbl_city_home_marcy_room:
    scene loc_city_home_marcy_room

    if v_day == 2:
        jump lbl_city_home_marcy_room_day2

label lbl_city_mall:
    scene loc_city_mall

    if v_day == 1:
        jump lbl_city_mall_day1
    elif v_day == 2:
        jump lbl_city_mall_day2

label lbl_city_street_1st:
    scene loc_city_street_1st

    if v_day == 1:
        jump lbl_city_home_marcus_day1a
    elif v_day == 2 and v_time == 0:
        jump lbl_city_home_marcy_day2a
    elif v_day == 2 and v_time > 0:
        jump lbl_city_street_1st_day2

#### EVENTS ####
### MARCY HOME ###
## DAY 1 ##
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

## DAY 2 ##
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

### MARCY ROOM ###
## DAY 2 ##
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
            jump lbl_city_street_1st

### MALL ###
## DAY 1 ##
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

## DAY 2 ##
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
            jump lbl_city_street_1st

### LILY HOME ###
## DAY 2 ##
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

### 1ST STREET ###
## DAY 2 ##
label lbl_city_street_1st_day2:
    if v_time == 840:
        "Where should I go?"

        menu:
            "Home":
                jump lbl_home_room_mia
            "Marcy":
                jump lbl_city_home_marcy_room
            "Mall":
                jump lbl_city_mall
            "Visit the church":
                jump lbl_city_church
            "Visit the beach":
                jump lbl_city_beach

### CHURCH ###
## DAY 2 ##
label lbl_city_beach_day2:
    show img_beach_topless with d1
    "Here is the beach, looks like everything is mostly normal here, more topless woman than normal, but nothing very strange."
    hide img_beach_topless with d1
    show img_beach_nude_01 at top with d1
    "Spoke too soon..."
    hide img_beach_nude_01 with d1
    show img_beach_nude_02 at top with d1
    pause
    hide img_beach_nude_02 with d1

    menu:
        "Go home":
            jump lbl_city_street_1st

### CHURCH ###
## DAY 2 ##
label lbl_city_church_day2:
    "This is the local church, maybe they can help me with my crysis..."
    show npc_portrait_nun with d3
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
    hide npc_portrait_nun with d3
    "Let's go home, I think someone owns me anwers, and she should be back in my room later."

    menu:
        "Go home":
            jump lbl_city_street_1st