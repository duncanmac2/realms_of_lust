## LOCATIONS
label lbl_home_bathroom:
    scene loc_home_bathroom1

    if v_day == 1:
        jump lbl_day1_home_bathroom

label lbl_home_kitchen:
    scene loc_home_kitchen

    if v_day == 1 and f_day1_lisa_bathroom_incident:
        jump lbl_day1_home_kitchen1
    elif v_day == 1 and not f_day1_lisa_bathroom_incident:
        jump lbl_day1_home_kitchen2

label lbl_home_room_mc:
    scene loc_home_room_mc

    if v_day == 1:
        jump lbl_day1_home_room_mc

label lbl_day1_home_room_mc:
    "The sun is shining through the window."
    me "It's already morning already? Why is it so bright?"
    "What time is it? Shit, it's late, very, very late. The alarm didn't go off. I'll be late if I don't hurry, Mr. Smith doesn't take kindly to people who are late for his classes."
    "Shit, I have to take a shower, better hurry."

    jump lbl_home_bathroom

## EVENTS
label lbl_day1_home_bathroom:
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
                    $ f_day1_lisa_bathroom_incident = True
                    scene loc_home_bathroom2
                    show vid_lisa_bathroom_incident at truecenter
                    "My head is in the clouds, thinking about why she didn't woke me up today. I'm so distracted that I find the answer the worst way possible."
                    lisa "MAX! DON'T YOU KNOW HOW TO KNOCK?"
                    me "SHIT, sorry, I thought you were already finished..."
                    "Why is she here now? But whoa... she is in great shape foor her age... What the fuck am I thinking?"
                    me "I'm..."
                    lisa "GET OUT!!!"
                    "I close the door before doing any more damage by getting hard down there. I'm in soo much trouble as is, I think I will no be getting that money I asked yesterday. God damn it."

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

label lbl_day1_home_kitchen1:
    me "Well... I will be late, smelly, broke and probably grounded for the rest of the week. But I will not be hungry. There is always a bright side (I feel dead inside)."
    show npc_portrait_mia_02 at top
    "After a few minutes pondering if I should eat all of Mia's food for sending me to my figurative demise, she comes down the stair."
    mia "Sooooo... I-I'm sorryyyyy ???"
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

label lbl_day1_home_kitchen2:
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