## LOCATIONS
label lbl_city_home_marcus:
    scene loc_city_home_marcus

    if v_day == 1:
        jump lbl_city_home_marcus_day1b

label lbl_city_street_1st:
    scene loc_city_street_1st

    if v_day == 1:
        jump lbl_city_home_marcus_day1a

## EVENTS
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
        "Hi mom, [me] came to visit."
        "Hello boys, how was your day?"
        "Great, I found some great treasure in the campus, but that's a secret between max and I, so sorry Mom cant tell you."
        "Its not drugs is it, I swear to god Marcus P. Willians if you are doing drugs you are finding a new place to live."
        "What? No its not drugs mom, its something completely legal."
        "I somehow doubt it."
        "Anyway, we are going to some games, are you going to the market today mom?"
        "Yes, do you want me to bring you the usual?"
        "Yes, the new edition is out today."
        "I don't know why I buy those for you."
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sara buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        "Lets go play some p..."
        "RING... RING..."
        "It's my phone, Lisa is calling..."
        "Max, were are you? Doens't matter, come back home right now! You own me an explanation for what happend this morning."
        "Lisa, I will be right there."
        "You have 20 minutes."
        "She hung up."
        "Looks like you are in trouble my friend, we will do this some other time."
        "Sorry Man, we will talk later."

        menu:
            "Run home":
                jump lbl_college_yard

    else:
        "Hi mom, [me] came to visit."
        "Hello boys, how was your day?"
        "Great, I found some great treasure in the campus, but that's a secret between max and I, so sorry Mom cant tell you."
        "Its not drugs is it, I swear to god Marcus P. Willians if you are doing drugs you are finding a new place to live."
        "What? No its not drugs mom, its something completely legal."
        "No it isn't."
        "Anyway, we are going to some games, are you going to the market today mom?"
        "Yes, do you want me to bring you the usual?"
        "Yes, the new edition is out today."
        "I don't know why I buy those for you."
        "The usual is their codeword for naughty magazines, Marcus is a collector. Sara buys them for him because his father used to give them to him as a gift every month, so after he passed away she kept the tradition, not that she is happy about it."
        "Lets go play some p..."
        "RING... RING..."
        "Its my phone, Lisa is calling..."
        "Max, is Mia with you?She is not aswering her phone."
        "Lisa, no she is with Veronica I think.Do you have her number?"
        "Yes, I will call her right now, she is in so much truble..."
        "Poor Mia."
        "After the call Marcus and I spend some hour play some of his old games."
        "Its getting late man, I will..."
        "Just as I start to stand to go home something catches my eyes."
        "Ohhh, Max we are soo lucky, she rarely changes in her room.Lets enjoy this gift from the pervert god."
        "She is very hot, that's cheerleader for you, but its time for me to go, see you tomorrow Marcus."
        "He is in a trance, better leave, he has business to attend to."

        menu:
            "Go home":
                jump lbl_college_yard