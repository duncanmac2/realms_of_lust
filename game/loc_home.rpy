## LOCATIONS
label lbl_home_bathroom:
    scene loc_home_bathroom1

    if v_day == 1:
        jump lbl_home_bathroom_day1

label lbl_home_kitchen:
    scene loc_home_kitchen

    if v_day == 1:
        jump lbl_home_kitchen_day1

label lbl_home_living_room:
    scene loc_home_living_room

    if v_day == 1:
        jump lbl_home_living_room_day1

label lbl_home_room_mc:
    scene loc_home_room_mc

    if v_day == 1:
        jump lbl_home_room_mc_day1

## EVENTS
label lbl_home_room_mc_day1:
    if v_time == 1140:
        "Entering my room my computer is on."
        "There is a e-mail notification, let's see what it is about."
        "{i}\"Would you like to change your whole life?\"{/i}"
        "I hate spam, next."
        "\"Hello [me],"
        "It's aunt Lily here, how are you? I have great news I got a job on the PGP Corporation, right there in Libidine town, so I'm moving back there tomorrow."
        "I already got a house and everything, it's on Second Street 458, you absolutely must come visit me tomorrow, no excuses. Also tell Lisa and Mia aunt Lily is back in town."
        "Love you.\""
        "Lily is back in town? That's great, she is dad's younger sister, after grandma got sick she came to live with mom and dad she was way younger than my father so she could not live alone I think she was just 10 when Grandma Kat was sent to the hospital."
        "She is still there by the way, she had a mysterious disease that has kept her there I go visit her sometimes but she is rarely lucid."
        "After the accident she also came to live with Lisa and Mia, but after two years she decided to travel around the world to find herself."
        "She always kept in contact but I sometimes forget to send her news. She is also aunt Lily to Mia since she is my step sister, they are very close. But enough exposition let's... wait I got a new message."
        show npc_portrait_lily_01 with d1
        "PS: we haven't seen eachother in a long time here is a picture to see how I've changed. Not so chubby anymore."
        "Whoa, she really has changed she used to be... well chubby is very generous. She is actualy pretty hot now... what no she is my aunt can't think of her this way."
        "Time to eat some dinner."

        menu:
            "Go eating":
                jump lbl_home_kitchen

    elif v_time == 1200:
        show loc_home_room_mc_bed at top
        "I feel extremely tired all of a sudden. As soon as my head hits the pillow everything goes dark. That is until..."
        nina "Wake uuup..."
        me "What?"
        nina "Wake uupp..."
        hide loc_home_room_mc_bed
        show npc_portrait_nina_01 with d3
        "When I open my eyes a beautiful woman is at the side of my bed, what is she doing in my room..."
        me "Who are you? What are you doing in my room??"
        nina "Calm down [me], let me explain everything to you... My name is Nina, Queen of the Realm of Lust, and I have come with an offer."
        me "What? What kind of offer?"
        hide npc_portrait_nina_01 with d3
        show npc_portrait_nina_02 with d3
        nina "You see every four-hundred years our world align and lust can be free in this world for a day... that's today. But unlike my predecessors I want more, and I have the perfect opportunity to reach these goals. And you are the key."
        me "Me?"
        nina "Yes you my friend, your family is special, long ago my great grandfather impregnated a human, that was your ancestor, the blood of gods run in your veins."
        nina "It's been diluted however but there is still some power there, so if you join me we together can bring this earth in a state of paradise. What say you friend?"
        me "I say this is the strangest dream I've ever had. I mean god, lust... this is weirder than that time I ate those strange brownies. But wait a second if this story is true doesn't that make us cousins or something."
        nina "I think so, but 30 generations removed I think... but that is not important what matter is that you can finally have a better life than the one you have now, in this new world you will be like royalty, you would be second only to me. So what say you... cousin?"
        hide npc_portrait_nina_02 with d3
        show npc_portrait_nina_03 at top with d3
        "It's the strangest dream I've ever had, but why not, it would be a shame if I woke up without banging someone, in my dreams... this sounds so pathetic."
        me "I accept."
        nina "Cool... I mean you have chosen wisely now hold still."
        "She jumps me and plants a kiss in my lips. I can feel the power rushing through me but I feel tired at the same time."
        nina "Before you pass out, know that the corruption of this world will take time, but thanks to you I can came help you so if you need me just..."

        $ v_time = 0
        $ v_day = 2

        menu:
            "Pass out":
                jump lbl_home_room_mc

    else:
        "The sun is shining through the window."
        me "It's already morning already? Why is it so bright?"
        "What time is it? Shit, it's late, very, very late. The alarm didn't go off. I'll be late if I don't hurry, Mr. Smith doesn't take kindly to people who are late for his classes."
        "Shit, I have to take a shower, better hurry."

        jump lbl_home_bathroom

label lbl_home_bathroom_day1:
    "When I'm about to enter the bathroom, I hear a loud scream."
    show npc_portrait_mia_01
    mia "Waitttt..."
    "It's my little \"sister\", Mia"
    mia "Please bro, I need to take a shower now or I will be late for my class."
    me "Same here, why are you getting up just now?"
    mia "My alarm stopped working, please bro a lady should never smell bad, you are a guy, no one is going to care."
    me "Are you crazy, of course they will, specially the girls."
    mia "Pleaseeee..."
    me "Okay, let's play for it, rock, paper, scissors!"
    mia "I... fine."

    menu:
        "Play paper":
            me "Damn it!"
            mia "Yesss, sorry bro, its was your idea, but if you are desperate we could shower together, hihihi."
            "She likes to tease me, but she is not brave enough to actually take a shower with me. But then again, I could use that to my advantage."
            me "Okay let's go!"
            mia "What??? But... but..."
            me "You offered it, I don't mind so..."
            "I start to take of my shirt."
            mia "Ok, I'm sorry I was just teasing, please don't take off your shirt."
            me "What am I supposed to do then?"
            mia "Hey, bro, mom must be finished with her shower by now, I bet she won't mind if you take a shower there."
            me "Good idea sis."
            "I run to Lisa's room as fast as I can. Its weird tough, Lisa usually wakes both of up every morning... huhhh"

            menu:
                "Open the door":
                    scene loc_home_bathroom2
                    show vid_lisa_bathroom_incident at truecenter
                    "My head is in the clouds, thinking about why she didn't woke me up today. I'm so distracted that I find the answer the worst way possible."
                    lisa "MAX! DON'T YOU KNOW HOW TO KNOCK?"
                    me "SHIT, sorry, I thought you were already finished..."
                    "Why is she here now? But whoa... she is in great shape foor her age... What the fuck am I thinking?"
                    me "I'm..."
                    lisa "GET OUT!!!"
                    "I close the door before doing any more damage by getting hard down there. I'm in soo much trouble as is, I think I will no be getting that money I asked yesterday. God damn it."

                    $ f_day1_lisa_bathroom_incident = True

                    jump lbl_home_kitchen

        "Play scissors":
            me "It's a tie."
            mia "Then lets play again bro!"
            me "Better idea, why you don't take a shower on Lisa's bathroom? She is most likely finished by now."
            mia "That's... a really good idea, why didn't I think of that earlier."
            me "Well you are a bit of an airhead."
            mia "Hey!!!"
            me "It's true. Go on now, or we will not make it in time."
            mia "Crap, you are right."
            me "Now lets hurry, still have to go to Marcus's house."

            menu:
                "Take a shower in a hurry":
                    jump lbl_home_kitchen

        "Play rock":
            me "Ha, I win."
            mia "But..."
            "She is making her sad puppy face. I'm not going to fall for it. But wait a second, I woke up late so Lisa must have already finished her shower."
            me "Mia, Lisa is in the bathroom."
            mia "Shit, you are right, I'm going there now."
            "She runs of to Lisa's room before I can say a word. But why didn't Lisa woke me up today, she usually does. Could it be that she is also running late? Better take a shower before Mia comes back if that's the case, she will probably try to convince me with that face again. And succeed."

            menu:
                "Take a shower in a hurry":
                    jump lbl_home_kitchen

label lbl_home_kitchen_day1:
    if f_day1_lisa_bathroom_incident and v_time == 0:
        me "Well... I will be late, smelly, broke and probably grounded for the rest of the week. But I will not be hungry. There is always a bright side (I feel dead inside)."
        show npc_portrait_mia_02 at top
        "After a few minutes pondering if I should eat all of Mia's food for sending me to my figurative demise, she comes down the stair."
        mia "Sooooo... I-I'm sorryyyyy???"
        hide npc_portrait_mia_02
        show npc_portrait_mia_03 at top with d3
        me "Sorry doesn't cut it Mia, Lisa will eat me alive when we are back from college, you know how she is she doens't even own a bikini because it shows too much skin... And I saw her naked !!!"
        mia "I didn't know, I thought she was down here and just forgot to wake us. Please forgive me Max, I-I will... talk to Hikari, I know you have a crush on her so I will set you up on a date, how about that?"
        me "That would be great, except last month I tried to ask her out. All she said is she does not go out with losers and perverts. A pervert. ME?"
        mia "Well, you do hang around Markus a lot."
        me "I know. Let's do this then, you will owe me a favor, whatever I ask, whenever I ask. Deal?"
        hide npc_portrait_mia_03
        show npc_portrait_mia_04 at top with d3
        mia "Uhhhh... ok deal!"
        me "Good now let's go, we are already late as it is."

        menu:
            "To Marcus":
                jump lbl_city_street_1st

    elif v_time == 1140:
        show npc_portrait_lisa_02 with d3
        "Time to have dinner with my family, they are already on the table waiting for me."
        me "Hey guys I have great news, aunt Lily is moving into town tomorrow."
        hide npc_portrait_lisa_02 with d3
        show npc_portrait_mia_07 at top with d3
        mia "Really!!! Awesome, then we can go see her right it's been ages since we last saw her."
        lisa "Yes it has, did she find a job here?"
        me "On the PGP Corporation, don't know what she does there tough."
        hide npc_portrait_mia_07 with d3
        show npc_portrait_lisa_01 with d3
        lisa "That's great, I will call her for the barbecue on Sunday, but since you brought the subject of family, I had some good news about grandma Emma."
        lisa "It looks like there was a new development in her treatment, the doctor says she is much better now and she may even be able to talk to us on a more regular basis now."
        me "That's great, it's the best news I've had all year."
        lisa "I will visit her tomorrow, but you will have to wait some time to visit her yourself the doctor says it's better to go one at a time, for now."
        hide npc_portrait_lisa_01 with d3
        "The dinner goes as always after that, I make a bad joke, Mia laughs, Lisa goes on to wash the dishes. I decide to go to my room early today, I feel spleepy for some reason."
        me "I'm going to bed, good night sis."
        mia "Good night bro."
        me "Good night Lisa."
        lisa "Night sweetie."
        "She gives me a kiss on the cheek."

        $ v_time = 1200

        menu:
            "Go to my room":
                jump lbl_home_room_mc

    else:
        "During my shower I heard some screaming, Lisa was probably in the shower when Mia opened the door... she will be pissed. Both of them will actually. Lisa is very shy she hates to show skin, even to Mia."
        show npc_portrait_mia_05 at top
        "When I step in the kitchen Mia is looking upset, she gives me a look that screams \"you own me one\"."
        hide npc_portrait_mia_05
        show npc_portrait_lisa_01 at top with d3
        me "Good morning Lisa."
        lisa "Good morning [me], didn't you set the alarm for the right time today?"
        me "I did, but it didn't go off, strange right?"
        lisa "Yes, now that you mentioned, mine didn't either, neither did Mia's clock and hers is and old mechanical one."
        me "So... the screaming..."
        lisa "It's nothing, Mia just forgot her manner that's all, here a sandwich eat it on the way you have to go now."
        me "Shit you are right."
        lisa "Language! Now go."
        me "Bye Lisa."
        mia "Bye Mom..."

        menu:
            "Leave":
                jump lbl_city_street_1st

label lbl_home_living_room_day1:
        "She is here, and waiting for me, it was a good life..."
        lisa "[me], sit down."
        "That's not a request, it's best to do as the lady says."
        lisa "So, don't you know how to knock? What did you have in your mind to open MY bathroom door when I was showering?"
        me "I'm so sorry, Mia told me that you were done, and I was running late so I didn't think..."
        lisa "Well you should have, you are not a kid anymore. You know you are in trouble right?"
        me "Yes."
        lisa "Good, you will be not be getting any money from me this month, if you want you will be getting a job or taking it from your savings."
        me "I understand."
        lisa "Look I was very angry most of the day, it's a good thing I had the time to cool down or you would be getting a much harsher punishment. Let's just leave it that and forget this ever happened okay. Now go to your room you left your computer on."
        me "I did? Okay I will go."

        $ v_time = 1140

        menu:
            "My room":
                jump lbl_home_room_mc