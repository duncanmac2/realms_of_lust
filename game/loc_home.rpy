label lbl_home_bathroom:
    scene loc_home_bathroom1

    if v_day == 1:
        jump lbl_day1_home_bathroom

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
                    scene loc_home_bathroom2
                    show vid_lisa_bathroom_incident at truecenter
                    "My head is in the clouds, thinking about why she didn't woke me up today. I'm so distracted that I find the answer the worst way possible."
                    "blala"

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
                    "t"
        "Play rock":
            me "Ha, I win."
            mia "But..."
            "She is making her sad puppy face. I'm not going to fall for it. But wait a second, I woke up late so Lisa must have already finished her shower."
            me "Mia, Lisa is in the bathroom."
            mia "Shit, you are right, I'm going there now."
            "She runs of to Lisa's room before I can say a word. But why didn't Lisa woke me up today, she usually does. Could it be that she is also running late? Better take a shower before Mia comes back if that's the case, she will probably try to convince me with that face again. And succeed."

            menu:
                "Take a shower in a hurry":
                    "t"