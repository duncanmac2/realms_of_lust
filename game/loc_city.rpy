#### LOCATIONS ####
label lbl_city_home_marcus:
    scene loc_city_home_marcus

    if v_day == 1:
        jump lbl_city_home_marcus_day1b
    elif v_day == 2:
        jump lbl_city_home_marcus_day2b

label lbl_city_mall:
    scene loc_city_mall

    if v_day == 1:
        jump lbl_city_mall_day1

label lbl_city_street_1st:
    scene loc_city_street_1st

    if v_day == 1:
        jump lbl_city_home_marcus_day1a
    elif v_day == 2:
        jump lbl_city_home_marcus_day2a

#### EVENTS ####
### MARCUS HOME ###
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

label lbl_city_home_marcus_day2a:
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
            jump lbl_city_home_marcus

label lbl_city_home_marcus_day2b:
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

### MALL ###
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