#### LOCATIONS ####
label lbl_home_bathroom:
    scene loc_home_bathroom1

    if v_day == 1:
        jump lbl_home_bathroom_day1
    elif v_day == 2:
        jump lbl_home_bathroom_day2
    elif v_day == 3:
        jump lbl_home_bathroom_day3

label lbl_home_kitchen:
    scene loc_home_kitchen

    if v_day == 1:
        jump lbl_home_kitchen_day1
    elif v_day == 2:
        jump lbl_home_kitchen_day2
    elif v_day == 3:
        jump lbl_home_kitchen_day3
    elif v_day == 4:
        jump lbl_home_kitchen_day4

label lbl_home_living_room:
    $ v_localisation = "home_living_room"

    call main_show
    scene loc_home_living_room

    if v_day == 1:
        jump lbl_home_living_room_day1
    elif v_day == 2:
        jump lbl_home_living_room_day2
    elif v_day == 3:
        jump lbl_home_living_room_day3

label lbl_home_pool:
    scene loc_home_pool

    if v_day == 3:
        jump lbl_home_pool_day3

label lbl_home_room_lisa:
    scene loc_home_room_lisa_bed

    if v_day == 2:
        jump lbl_home_room_lisa_day2
    elif v_day == 3:
        jump lbl_home_room_lisa_day3

label lbl_home_room_mc:
    scene loc_home_room_mc

    if v_day == 1:
        jump lbl_home_room_mc_day1
    elif v_day == 2:
        jump lbl_home_room_mc_day2
    elif v_day == 3:
        jump lbl_home_room_mc_day3

label lbl_home_room_mia:
    scene loc_home_room_mia

    if v_day == 2:
        jump lbl_home_room_mia_day2
    elif v_day == 3:
        jump lbl_home_room_mia_day3

#### EVENTS ####
### ROOM MC ###
## ROOM MC - DAY 1 ##
label lbl_home_room_mc_day1:
    if v_time == 1140:
        "Entering my room my computer is on."
        "There is a e-mail notification, let's see what it is about."
        "{i}\"Would you like to change your whole life?\"{/i}"
        "I hate spam, next."
        "{i}Hello [me],{/i}"
        "{i}It's aunt Lily here, how are you? I have great news I got a job on the PGP Corporation, right there in Libidine town, so I'm moving back there tomorrow.{/i}"
        "{i}I already got a house and everything, it's on Second Street 458, you absolutely must come visit me tomorrow, no excuses. Also tell Lisa and Mia aunt Lily is back in town.{/i}"
        "{i}Love you.{/i}"
        "Lily is back in town? That's great, she is dad's younger sister. After grandma got sick she came to live with mom and dad. She was way younger than my father so she could not live alone I think she was just 10 when grandma Kat was sent to the hospital."
        "She is still there by the way, she had a mysterious disease that has kept her there. I go visit her sometimes but she is rarely lucid."
        "After the accident she also came to live with Lisa and Mia, but after two years she decided to travel around the world to find herself."
        "She always kept in contact but I sometimes forget to send her news. She is also aunt Lily to Mia since she is my step sister, they are very close. But enough exposition let's... wait I got a new message."
        show npc_portrait_lily_01 with d1
        "PS: we haven't seen each other in a long time here is a picture to see how I've changed. Not so chubby anymore."
        hide npc_portrait_lily_01 with d1
        "Whoa, she really has changed she used to be... well chubby is very generous. She is actually pretty hot now... what no she is my aunt can't think of her this way."
        show vid_pc_game at top with d1
        "Let's kill some time before dinner."
        hide vid_pc_game with d1
        "Time to eat."

        menu:
            "Go eating":
                jump lbl_home_kitchen

    elif v_time == 1200:
        show loc_home_room_mc_bed at top
        "I feel extremely tired all of a sudden. As soon as my head hits the pillow everything goes dark. That is until..."
        nina "Wake uupp..."
        me "What?"
        nina "Wake uupp..."
        hide loc_home_room_mc_bed
        show npc_portrait_nina_01 with d3
        "When I open my eyes a beautiful woman is at the side of my bed. What is she doing in my room?"
        me "Who are you? What are you doing in my room?"
        nina "Calm down [me], let me explain everything to you. My name is Nina, Queen of the Realm of Lust, and I have come with an offer."
        me "What? What kind of offer?"
        hide npc_portrait_nina_01 with d1
        show npc_portrait_nina_02 with d1
        nina "You see every four-hundred years our world align and lust can be free in this world for a day. That's today. But unlike my predecessors I want more, and I have the perfect opportunity to reach these goals. And you are the key."
        me "Me?"
        nina "Yes you my friend, your family is special. Long ago my great grandfather impregnated a human, that was your ancestor, the blood of gods run in your veins."
        nina "It's been diluted however but there is still some power there, so if you join me we together can bring this earth in a state of paradise. What say you friend?"
        me "I say this is the strangest dream I've ever had. I mean god, lust... this is weirder than that time I ate those strange brownies. But wait a second if this story is true doesn't that make us cousins or something?"
        nina "I think so, but 30 generations removed I think. But that is not important what matter is that you can finally have a better life than the one you have now, in this new world you will be like royalty, you would be second only to me. So what do you say... cousin?"
        hide npc_portrait_nina_02 with d1
        show npc_portrait_nina_03 at top with d1
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

## ROOM MC - DAY 2 ##
label lbl_home_room_mc_day2:
    if v_time == 900:
        "Let me see what is going on in the rest of the world."
        "{i}President makes all beaches open to nudists.{/i}"
        "{i}Porn industry surpasses Hollywood.{/i}"
        "Ok, that's enough, it's not a local phenomena. Shit, I think Lily is here."

        menu:
            "Kitchen":
                jump lbl_home_kitchen

    elif v_time == 1200:
        show loc_home_room_mc_bed at top
        "After a few minutes Lily knocks on my door."
        hide loc_home_room_mc_bed with d1
        show npc_portrait_lily_07 with d1
        lily "Can I come in?"
        me "Yes come in."
        lily "So have you given any thought about our situation?"
        me "I..."
        hide npc_portrait_lily_07
        show npc_portrait_nina_04 with vpunch
        "That's when a cloud of purple smoke comes out of nowhere."
        nina "Hello partn..."
        hide npc_portrait_nina_04
        show npc_portrait_lily_08
        "We all stare at each other for a few seconds before Lily breaks the silence."
        lily "It's you! You are the goddess that he was talking about."
        hide npc_portrait_lily_08 with d1
        show npc_portrait_nina_05 with d1
        nina "And you! I can feel the blood in you, are you Lilith?"
        lily "Just Lily please."
        nina "Well we have a happy family reunion here, [me] why didn't you tell me your aunt was in the city?"
        me "Well for starters, I thought it was all a dream, second what the hell happened with Marcus?"
        hide npc_portrait_nina_05 with d1
        show npc_portrait_nina_06 with d1
        nina "Oh, your friend? Well I thought he would be the best candidate to show you the power we possess. He was not the only one but he is the only man I thought you would notice was changed straight away. Didn't you like it? I think she is pretty hot."
        me "I want to say no, but the words just won't come out, I have been thinking about it and you are right I should enjoy this. My life before sucked, and now I have a chance to be better, why shouldn't I take it? I also suppressed my inner pervert for too long."
        nina "Well said, now Lily, [me] is the heir to the most of the old blood so I chose him as my catalyst, and partner, but that doesn't mean you can't have some fun."
        nina "I will give you a blessing so you don't have to worry about your mind being altered, once the corruption is done, you and [me] will be like gods, but like I said he is in charge here and you will probably also be affected by the corruption."
        hide npc_portrait_nina_06 with d1
        show npc_portrait_lily_09 with d1
        lily "I will?"
        nina "It can't be helped sorry, but it should be nothing major, just an increased sex drive and stamina."
        lily "Well, that is actually kind of cool."
        nina "Good then, I need to go now [me] can fill you in on the detail later, good night and see you soon."
        me "Wait, why are guys turning into chicks? You are not planning for a \"planet of the girls\" type of world are you?"
        nina "Oh that... I just assumed you would like have more women than man in your town, that is unless you are into guys... or NTR..."
        me "NO, NO NTR, UNDERSTAND?"
        hide npc_portrait_lily_09 with d1
        show npc_portrait_nina_07 with d1
        nina "Okay, okay. So expect a lot of the guys you know to acquire some tits as the week goes. But I really have to go now, mom doesn't like... I mean my time is up. My friends, forces beyond my control pull me back to my dimension. Good night."
        hide npc_portrait_nina_07 with d1
        "She leaves the room in cloud of smoke."
        lily "[me], this is great, we are going to have so much fun."
        me "Yes we will, but tomorrow, I need to sleep now."
        show vid_lily_kiss_02 at top with d1
        lily "Let me give you a goodnight's kiss then."
        hide vid_lily_kiss_02 with d1
        me "Whoa that was..."
        lily "Just a taste... goodnight [me]."

        $ v_day = 3
        $ v_time = 0
        $ mc_portrait = "new"

        menu:
            "Sleep":
                jump lbl_home_room_mc

    else:
        show img_mc_sleep at top with d3
        "You wake up for another day."
        hide img_mc_sleep with d3
        me "What time is it... It's morning already? Shit hope I'm not late again. But what a strange dream, and I didn't even get to see some boobs, that's my luck for you. Why I'm naked?"
        "In that moment between me noticing I'm completely nude and before I can put any clothes, Lisa comes through the door and sees me in all my glorious nakedness."
        show npc_portrait_lisa_03 at top with d3
        lisa "[me] are you u... Why are you naked?"
        "A lot of scenarios go through my head, is she going to freak out, faint, beat me to a pulp? But no what happens next no one could predict. She is only mildly embarrassed!"
        lisa "You should put some clothes sweetie."
        hide npc_portrait_lisa_03
        show npc_portrait_lisa_04
        "But before I can recover from the shock I realise that I'm not the only one that's not properly dressed."
        hide npc_portrait_lisa_04 with d3
        show vid_mc_erection at top
        "That is a bit too much for a man to take."
        "I try to hide it before she can see it. To no avail it seems."
        hide vid_mc_erection
        show npc_portrait_lisa_04 with d3
        me "Please, put some clothes Lisa."
        lisa "Did you just get an... erection?"
        "She blushes, but no signs of getting angry."
        lisa "Looks sweetie it's perfectly normal for a man to have those \"reactions\" to a woman's body, I should have put some more clothes. But you have nothing to be ashamed of."
        me "O-Ok... Can I put some clothes now?"
        lisa "Ah sure, sorry."
        hide npc_portrait_lisa_04 with d3
        "Before she leaves I think I saw her trying to take another look at my manhood. Has the world gone crazy? The Lisa I know would never just leave her room before putting clothes."
        "Could that dream... no that's crazy talk, maybe she is drunk for some reason, she acts completely out of character when she drinks. I should take a cold shower. Or maybe I should take care of this bad boy the fun way."

        menu:
            "Shower":
                jump lbl_home_bathroom
            "My PC":
                jump lbl_home_room_mc_day2_pc

label lbl_home_room_mc_day2_pc:
    "I boot the laptop on my desk ready for some action, let's see..."
    show vid_pc_porn_01 at top
    "There."
    hide vid_pc_porn_01 with d1
    window hide
    show vid_pc_porn_02 at top with d1
    pause
    hide vid_pc_porn_02 with d1
    show vid_pc_porn_03 at top with d1
    pause
    hide vid_pc_porn_03 with d1
    show vid_pc_porn_04 at top with d1
    pause
    hide vid_pc_porn_04 with d1
    "I spend a few minutes masturbating looking at my favorite videos but all I can think of is Lisa and her gorgeous body."
    "I climax still thinking about it, now I'm feeling guilty, time to take a cold shower."

    menu:
        "Breakfast":
            jump lbl_home_room_lisa

## ROOM MC - DAY 3 ##
label lbl_home_room_mc_day3:
    if v_time == 0:
        "It's morning, time to wake up to a bright new day... The fuck?"
        "I don't remember having a six-pack or being so tall and handsome? God damn it Nina warn me before you mess with my body. Not that I mind it I look good. But Lisa should be coming here any..."
        show npc_portrait_lisa_04 with d1
        lisa "[me] time to wake up."
        hide npc_portrait_lisa_04 with d1
        show img_mc_body_01 at top with d1
        me "...time now. Morning Lisa. Sorry I just woke up didn't have time to get dressed."
        hide img_mc_body_01 with d1
        show npc_portrait_lisa_04 with d1
        lisa "Come on sweetie, how many times have I seen you naked before. You are not even hard this time, should I feel offended?"
        "You know a few days ago if Lisa ever said that to me I would have freaked out, now it's a normal morning chat."
        lisa "If you keep waking up before I can call you maybe I will stop coming here each morning."
        "Let's push our luck a bit."
        me "No, please, if you don't then I won't have this magnificent view first thing in the morning, it's pretty good for my morale."
        lisa "Well, I'm glad you like it, should I start coming in only my panties then?"
        "She is playing it as a joke but there is a hint of a serious proposal there, maybe..."
        me "That would be a bad idea, your boobs are so incredible I would get a permanent boner..."
        lisa "Ohhh [me], stop joking, I'm sure you prefer some younger girl would show you her breasts..."
        me "What, are you kidding you are not old, you are the hottest mom I know, the very definition of MILF."
        hide npc_portrait_lisa_04 with d1
        show vid_lisa_show_boobs with d1
        lisa "That so kind of you sweetie, since you think so here is a reward."
        hide vid_lisa_show_boobs with d1
        show vid_mc_erection at top with d1
        "One small step for a man..."
        hide vid_mc_erection at top with d1
        show vid_lily_kiss_01 at top with d1
        lisa "Now that's the right reaction, I will let you go to the bathroom now, but before I leave."
        hide vid_lily_kiss_01 at top with d1
        lisa "Now let's go, you don't want to be late again right?"
        me "Ok, I'm going."
        "Time to see what the day has in store for us."

        menu:
            "Go take a shower":
                jump lbl_home_bathroom
            "Go eat something":
                jump lbl_home_kitchen
            "Spy on Lisa":
                jump lbl_home_room_lisa

    elif v_time >= 1140:
        "Ahhh home. What do I do now? Aunt Lily has a good point, maybe it's time to lose my virginity and she is hot... Marcy would probably also be on board... or I could just sleep and leave this for later."

        menu:
            "Go over to Marcy":
                jump lbl_city_home_marcy_room
            "Go to aunt Lily":
                jump lbl_city_home_lily
            "Just sleep":
                pass

        "You know what, it's late and today was already very fun, I will let the sex for a later date."

        menu:
            "Go to sleep":
                pass

        mia "Wake up bro..."
        me "Uhhh... five more minutes..."
        mia "Bro, wake up already!"
        me "Uhh... Mia?"
        show img_mia_nude at top with d1
        mia "Yeah it's me wake up."
        me "Why are you waking me up, were is Lisa?"
        mia "Mom had to leave for a meeting with her publisher, it was an emergency, so she asked me to wake you up. Now let's go."
        me "Okay, okay. No need to push it."
        hide img_mia_nude with d1
        show img_mc_body_02 at top with d1
        mia "Hey, since when do you sleep naked?"
        hide img_mc_body_02 with d1
        me "I don't know, a week maybe. Why?"
        mia "Well it's a bit distracting seeing your manhood in its full glory just like that in the morning."
        me "Yeah, what can I do. It's always like that in the morning. Also..."
        show vid_mia_ass_04 at top with d1
        mia "You are saying this is part my fault?"
        me "Pretty much."
        hide vid_mia_ass_04 with d1
        if tb_event[3]["home_room_mia"]["mia_finger"] == 1:
            mia "Well maybe I can help you like you helped me yesterday in my room. As your sister, it's my duty right?"
        else:
            mia "Well maybe I can help you get rid of it, I'm you sister after all, it's my duty to help you."
        me "Are you sure you just want to help me, that is the reason?"
        mia "W-why else would I do this?"
        me "Maybe you like it, maybe you want to touch it, maybe you want to go even further."
        show npc_portrait_mia_03 with d1
        "She starts looking nervous, she looks like she wants to leave the room, should I let her?"

        $ v_day = 4
        $ v_time = 0

        menu:
            "Grab her":
                hide npc_portrait_mia_03 with d1
                show img_mia_kiss_02 at top with d1
                "I grab her by the arm and she looses her balance and falls on top of me. We are face to face."
                me "We can't keep dancing around this forever Mia, you know you want to go all the way with me, just admit it."
                mia "I... I... we can't, if mom finds out..."
                me "This is not about Lisa, it's about you and me. Now tell me, do you want to have sex with me?"
                mia "I do! I wanted this for so long."
                me "Then, it's time to forget what other people will think and just follow you heart."
                hide img_mia_kiss_02 with d1
                show img_mia_kiss_03 at top with d1
                mia "Bro..."
                window hide
                hide img_mia_kiss_03 with d1
                show vid_mia_handjob_02 at top with d1
                pause
                hide vid_mia_handjob_02 at top with d1
                show vid_mia_sex_01 at top with d1
                pause
                hide vid_mia_sex_01 at top with d1
                show vid_mia_sex_02 at top with d1
                pause
                hide vid_mia_sex_02 at top with d1
                show vid_mia_cum_ass at top with d1
                pause
                hide vid_mia_cum_ass at top with d1
                me "So how was it?"
                mia "Better than I could have ever hoped for. Am I... your first?"
                me "You are but I will be honest with you, aunt Lily wanted me to sleep at her house last night, so you almost weren't."
                mia "Auntie... she... she... but she is..."
                me "Aunt Lily is a certified pervert sis, but that's not a bad thing is it?"
                mia "I guess not. But does this mean you are going to have sex with her some other time?"
                me "Probably, does this bother you?"
                mia "It should, but it does not. You know I think mom also has the hots for you bro, are we a weird family?"
                me "Ha, I think we are average."
                mia "I guess you are right, you have to hear Veronica's family stories sometimes. But that enough chat, we have to leave or we will be late."

                $ tb_event[3]["home_room_mc"]["mia_sex"] = 1

                menu:
                    "Go to college":
                        jump lbl_city_street_1st

            "Let her run away":
                hide npc_portrait_mia_03 with d1
                "Let her go, she will come around to the idea eventually. I will go take a shower, I think Mia is taking hers in Lisa's bathroom."
                "After a refreshing shower I go down the stairs to eat breakfast."

                menu:
                    "Down the stairs":
                        jump lbl_home_kitchen



    else:
        "Nothing to do here."

    menu:
        "Go back":
            jump lbl_home_living_room

### BATHROOM ###
## BATHROOM - DAY 1 ##
label lbl_home_bathroom_day1:
    "When I'm about to enter the bathroom, I hear a loud scream."
    show npc_portrait_mia_01
    mia "Waitttt..."
    "It's my little \"sister\", Mia."
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
            mia "Yesss, sorry bro, it's was your idea, but if you are desperate we could shower together, hihihi."
            "She likes to tease me, but she is not brave enough to actually take a shower with me. But then again, I could use that to my advantage."
            me "Okay let's go!"
            mia "What? But... but..."
            me "You offered it, I don't mind so..."
            "I start to take of my shirt."
            mia "Ok, I'm sorry I was just teasing, please don't take off your shirt."
            me "What am I supposed to do then?"
            mia "Hey, bro, mom must be finished with her shower by now, I bet she won't mind if you take a shower there."
            me "Good idea sis."
            "I run to Lisa's room as fast as I can. It's weird tough, Lisa usually wakes both of up every morning."

            menu:
                "Open the door":
                    pass

            scene loc_home_bathroom2
            show vid_lisa_bathroom_incident at top
            "My head is in the clouds, thinking about why she didn't woke me up today. I'm so distracted that I find the answer the worst way possible."
            lisa "[me]! Don't you know how to knock?"
            me "SHIT, sorry, I thought you were already finished..."
            "Why is she here now? But whoa... she is in great shape foor her age... What the fuck am I thinking?"
            me "I'm..."
            lisa "GET OUT!"
            "I close the door before doing any more damage by getting hard down there. I'm in so much trouble as is, I think I will no be getting that money I asked yesterday. God damn it."

            $ f_day1_lisa_bathroom_incident = True

            jump lbl_home_kitchen

        "Play scissors":
            me "It's a tie."
            mia "Then let's play again bro!"
            me "Better idea, why you don't take a shower on Lisa's bathroom? She is most likely finished by now."
            mia "That's... a really good idea, why didn't I think of that earlier."
            me "Well you are a bit of an airhead."
            mia "Hey!"
            me "It's true. Go on now, or we will not make it in time."
            mia "Crap, you are right."
            me "Now let's hurry, still have to go to Marcus's house."

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

## BATHROOM - DAY 2 ##
label lbl_home_bathroom_day2:
    if v_time == 840:
        "Let's see where is Lisa."
        "I hear someone on her shower, I shouldn't... but I can't stop thinking about it. Fuck! One look, just one look."
        window hide
        show img_lisa_shower_01 with d1
        me "Whoa..."
        hide img_lisa_shower_01 with d1
        show img_lisa_shower_02 at top with d1
        pause
        hide img_lisa_shower_02 with d1
        show img_lisa_shower_03 at top with d1
        pause
        hide img_lisa_shower_03 with d1
        show img_lisa_shower_04 with d1
        pause
        hide img_lisa_shower_04 with d1
        show img_lisa_shower_05 with d1
        "Dammit. I did it again."

        $ v_time = 900

        menu:
            "Time to go":
                jump lbl_home_room_mc

    else:
        mia "WAIT BROOOO!!!"
        show npc_portrait_mia_01 with d3
        me "Oh no."
        me "I'm sorry sis but I'm really in desperate need of a shower."
        mia "Well so am I, so let's play for it!"
        me "Why? We have more than enough time for both of us to take a shower. Just go eat breakfast and come back in a few minutes."
        mia "Please, let me take it first, I dropped cholacolate in my... my... underwear and now it's sticky."
        me "I thought Lisa had told you to stop eating candy before breakfast. Also how did you manage to... you know what, never mind."
        mia "That's why you need to let me shower before she finds out."
        me "Ok, let's do this, the same as yesterday."
        mia "Okay."
        "As I'm about to play scissors I catch a glimpse of her nipple and I forget to open my hand..."
        mia "Yeah. Paper beats rock, I win. But if you are so desperate you could come in and take a shower with me."
        "This again? She is way too shy to bathe together she just likes to keep teasing me, but let's see how far she is willing to go."
        me "I will take you up on that offer."
        mia "Well come in then."
        "She stands at the door holding the door open for me."
        mia "What are you waiting for?"
        "She thinks she can win against me in the bluffing game, not today."

        menu:
            "Go inside":
                hide npc_portrait_mia_01 with d3
                pass

        "We are both inside, she is red as a tomato, but no signs of backing down. Time to take it to the next level."
        me "What are you waiting for? We don't have all morning."
        "I start to take my clothes off, with a smirk on my face she will never..."
        show img_mia_shower_01 at top with d1
        mia "No need to push it."
        "She just started to take her clothes off, and in a moment she is naked in front of me while I have only my underwear."
        mia "I know it's been a while since we took a shower together, but it's all right, we are family after all."
        "It's clear she is trying to convince herself. As for me im trying to hide my massive erection from her... Should I go in or just give up?"
        hide img_mia_shower_01 with d1
        show img_mia_shower_02 with d1
        "Her body is incredible, I always knew she was beautiful but this! Can you get a hard on on top of a hard on?"
        "That's when she see my \"situation\"."
        mia "What is... ooh that's why you were so desperate to come in... it's, it's ok bro. You are a man after all, cold showers are good to keep you awake."
        "I can't believe this is happening, who is this, this is not Mia, the dream! No that's crazy..."
        me "Are you sure you don't want to do this?"
        mia "It's all right, bro. We are family."
        me "Yeah, you already said that."
        "It's obvious she is not as cool with this situation as she makes herself to be. But I don't have the time to just give up now, so I step inside the shower."
        "Mia does the same and soon we are in this awkward situation, back to back, washing ourselves in silence. That is until she bumps into me. The only thing I can think off is that her ass is soft and smooth, if the water wasn't so cold I would be hard again."
        hide img_mia_shower_02 with d1
        show img_mia_shower_03 with d1
        mia "Sorry bro. Are you... you know... less excited?"
        me "I think so, yes."
        mia "Ok, you can turn around then, can you wash my back?"
        hide img_mia_shower_03 with d1
        show img_mia_ass_01 with d1
        "That sight is too much, I can feel my blood flowing to my dick again."
        me "Sorry, I'm done here, need to go see you downstairs."
        mia "But..."
        hide img_mia_ass_01
        "I don't give her time to say anything else, as I put a towel around my waist and run of to put some clothes in my room."
        "Time for breakfast then."

        $ f_day2_shower = True

        menu:
            "Kitchen":
                jump lbl_home_kitchen

## BATHROOM - DAY 3 ##
label lbl_home_bathroom_day3:
    "Ah, a shower in a hot morning, the only way this would be better is if I had some comp..."
    show img_mia_shower_02 with hpunch
    "The door then opens so fast it's like someone really needed to use this room."
    me "Holy shit, Mia! Knock before you enter."
    mia "Sorry I didn't mean to scare you, I just came here for us to take our shower together."
    "By the sounds of it, it's a more common occurrence now, in her mind at least."
    me "Well, you are already naked so come in."
    hide img_mia_shower_02 with d1
    show img_mia_shower_03 with d1
    mia "What about that?"
    hide img_mia_shower_03 with d1
    show img_mc_dick at top with d1
    me "That? What are you talking about... ohhh!"
    hide img_mc_dick with d1
    show img_mia_shower_03 with d1
    me "Can you blame me? You are quite hot, sis."
    mia "Aww... that was almost sweet, but thanks bro, since I'm the cause, maybe I can be the solution?"
    me "Meaning?"
    mia "Let me take care of that monster for you, I-I can use my hands."
    "She is equal parts nervous and eaguer, how can I say no."
    me "Come on in then sis."
    mia "Ok, Veronica showed me how this works."
    me "She did WHAT?"
    hide img_mia_shower_03 with d1
    show img_mia_handjob_01 at top with d1
    mia "Calm down bro, it was on a dildo... let's see."
    "She is inexperienced, if it was not for the fact that she was my sister, and that she is smoking hot, it would take a long time for me to cum. But as things stand..."
    hide img_mia_handjob_01 with d1
    show vid_mia_handjob_cum at top with d1
    mia "Wow, so the is what it feels like... it tastes funny."
    hide vid_lisa_handjob_cum with d1
    me "Mia that was... ok."
    mia "Just ok?"
    me "For a first timer... hahaha."
    mia "Haha, come on bro, wash my back at least now."
    "After we are finished, Mia heads to her room to put some clothes and I go to the kitchen to have some breakfast."

    $ f_day3_shower = True

    menu:
        "Kitchen":
            jump lbl_home_kitchen

### KITCHEN ###
## KITCHEN - DAY 1 ##
label lbl_home_kitchen_day1:
    if f_day1_lisa_bathroom_incident and v_time == 0:
        me "Well... I will be late, smelly, broke and probably grounded for the rest of the week. But I will not be hungry. There is always a bright side (I feel dead inside)."
        show npc_portrait_mia_02 at top with d3
        "After a few minutes pondering if I should eat all of Mia's food for sending me to my figurative demise, she comes down the stair."
        mia "Sooooo... I-I'm sorryyyyy."
        hide npc_portrait_mia_02 with d1
        show npc_portrait_mia_03 with d1
        me "Sorry doesn't cut it Mia, Lisa will eat me alive when we are back from college. You know how she is, she doesn't even own a bikini because it shows too much skin... and I saw her naked!"
        mia "I didn't know, I thought she was down here and just forgot to wake us. Please forgive me [me], I-I will... talk to Hikari, I know you have a crush on her so I will set you up on a date, how about that?"
        me "That would be great, except last month I tried to ask her out. All she said is she does not go out with losers and perverts. A pervert, ME?"
        mia "Well, you do hang around Marcus a lot."
        me "I know. Let's do this then, you will owe me a favor, whatever I ask, whenever I ask. Deal?"
        hide npc_portrait_mia_03 with d1
        show npc_portrait_mia_04 at top with d1
        mia "Uhhhh... ok deal!"
        me "Good now let's go, we are already late as it is."

        menu:
            "To Marcus":
                jump lbl_city_street_1st

    elif v_time == 1140:
        show npc_portrait_lisa_02 with d3
        "Time to have dinner with my family, they are already on the table waiting for me."
        me "Hey guys I have great news, aunt Lily is moving into town tomorrow."
        hide npc_portrait_lisa_02 with d1
        show npc_portrait_mia_07 at top with d1
        mia "Really! Awesome, then we can go see her right it's been ages since we last saw her."
        lisa "Yes it has, did she find a job here?"
        me "On the PGP Corporation, don't know what she does there tough."
        hide npc_portrait_mia_07 with d1
        show npc_portrait_lisa_01 with d1
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

## KITCHEN - DAY 2 ##
label lbl_home_kitchen_day2:
    if f_day2_shower and v_time == 0:
        "What a strange day."
        show npc_portrait_lisa_05 with d3
        "Lisa is here already, properly dressed."
        me "Hey, Lisa can I ask you something? Are you feeling any different?"
        lisa "Where did that come from? I don't think so why?"
        me "You were always shy with nudity an all that, why then you entered my room only on your underwear today?"
        hide npc_portrait_lisa_05 with d1
        show npc_portrait_lisa_06 with d1
        lisa "I think you are exaggerating a bit [me], I don't usually walk around like that, but it's not like you have never seen me in a bikini right, it's almost the same thing. I just forgot to put clothes for some reason."
        "A bikini? Lisa only owns one pieces, she would never wear a bikini, even in our pool. What the fuck."
        hide npc_portrait_lisa_06 with d1
        show npc_portrait_mia_01 with d1
        mia "Morning, bro, mom."
        lisa "Good morning Mia."
        hide npc_portrait_mia_01 with d3
        "The rest of our time goes as usual, but it's clear that something is not right..."
        "After we eat, Mia and I finish getting ready and leave the house."

        menu:
            "To Marcus":
                jump lbl_city_street_1st

    elif v_time == 0:
        "What a strange day."
        show npc_portrait_mia_08 with d1
        "Mia is already here, but what is she wearing?"
        me "Mia, what are you doing go put some clothes."
        hide npc_portrait_mia_08 with d3
        show npc_portrait_mia_09 with d3
        mia "Why, it's still too early to leave."
        me "If Lisa..."
        "That's when I remember what she was wearing when she came to wake me up... I know I asked this before but, what is going on?"
        mia "Bro?"
        me "Never mind, let's just eat."
        hide npc_portrait_mia_09 with d3
        show npc_portrait_mia_10 with d3
        mia "Are you ok?"
        me "I'm fine sis, just a little tired."
        "I try to eat some food, but I feel a bit sick. Also my mind starts to wonder when did Mia became so hot, I never saw her that way before, but now..."
        hide npc_portrait_mia_10
        show npc_portrait_lisa_06
        lisa "Good morning."
        "I almost jump out of the chair."
        me "Oh... Good morning."
        mia "Morning mom."
        hide npc_portrait_lisa_06 with d3
        "The rest of our time goes as usual, but it's clear that something is not right..."
        "After we eat, Mia and I finish getting ready and leave the house."

        menu:
            "To Marcus":
                jump lbl_city_street_1st

    elif v_time == 900:
        show npc_portrait_lily_01
        "I walk down the stair aunt Lily is giving everyone hugs."
        lisa "[me] come say hi to your aunt."
        lily "Yes, I need another hug from my nephew."
        "She wraps her arms around me but this time instead of crushing me it looks like she is trying to make me feel her breasts pressing against me... damn it, it's a success."
        hide npc_portrait_lily_01 with d1
        show npc_portrait_mia_13 with d1
        mia "[me], auntie said you went to see her today, I should be angry you went alone, but now I can have you all to myself then auntie."
        hide npc_portrait_mia_13 with d1
        show npc_portrait_lisa_01 with d1
        lisa "Let's eat guys, before it gets cold."
        hide npc_portrait_lisa_01 with d1
        "We have a very interesting dinner, Lily tell everyone about her trips, people she met. After we are done, Mia drags Lily to her room, and I decide to go to mine."

        $ v_time = 1200

        menu:
            "Go to my room":
                jump lbl_home_room_mc

## KITCHEN - DAY 3 ##
label lbl_home_kitchen_day3:
    if v_time == 0:
        if not f_day3_shower and not f_day3_spy:
            "There is no one here now, they must be taking a shower, why do I feel like I lost an opportunity?"
            "A few minutes later."
            show npc_portrait_mia_14 with d3
            mia "Hey bro, good morning."
            me "Morning Mia. Aren't you going to put pants on?"
            mia "Later, I'm hungry now, give some of that jam."
            hide npc_portrait_mia_14 with d3
            show npc_portrait_lisa_07 with d3
            "After a few minutes Lisa comes down the stair to join us."
            lisa "Good morning guys."
            mia "Good morning."
            lisa "Mia, I have a favor to ask, can you go to the library before you come back home today to get me a book, talk to the librarian tell her it's for me."
            mia "Research for your latest book?"
            "Oh right Lisa is writer, that's why she stays home most of the time, I don't know this never came up before, it's almost like \"someone\" had not decide what Lisa's job was until now."
            lisa "Yes and no, it's research for the next book, after I finish writing the one I'm working on now. I want to delve in the world of erotica, so the librarian, Jessica is holding onto some steamy material for me."
            mia "Cool, what is it the theme of the book?"
            lisa "I don't know for certain yet, maybe something about forbidden love..."
            me "That's a little vague isn't it?"
            lisa "Well, I didn't start working on it it so there is a lot work to be done."
            mia "Yeah, bro give her some time."
            "We talk for a few more minutes, before it's time to go out. We put some proper clothes and get ready to leave."
            hide npc_portrait_lisa_07 with d1

        elif f_day3_shower:
            show npc_portrait_lisa_07 with d1
            lisa "Hey sweetie, come on sit down, is Mia coming down?"
            me "She will be here soon..."
            hide npc_portrait_lisa_07 with d1
            show npc_portrait_mia_14 with d1
            mia "Already here bro."
            "Wow, no wonder she was so fast she put only her top."
            lisa "Sit down kid, the food will get cold."
            "We take our usual places at the table."
            lisa "So how was the shower?"
            me "That's an unusual question, why?"
            lisa "Well since you don't have a hard on right now, I can assume only two things, you jerked off on Mia in the bathroom or Mia jerked you off, which one is it."
            me "Maybe I'm not in the mood."
            lisa "I'm not wearing a top, and Mia has no pants, or panties, unless you became gay in the last few minutes I doubt you would be flacid right now."
            mia "Mom, why are you so interested in what we do in there, are you jealous?"
            hide npc_portrait_mia_14 with d1
            show npc_portrait_lisa_03 at top with d1
            lisa "Well, I-I... look I know you are both virgins, and it's normal for siblings to explore their sexuality together, but I just want to make sure you don't take it too far, okay. I'm too young to be a grandmother."
            mia "MOM! It's not like that, I just used my hands ok, that's all."
            lisa "Well, I guess that's okay, what you can't do is fuck each other, you are still brother and sister after all. Blood related or no."
            me "So... what you are saying is blowjobs are ok?"
            hide npc_portrait_lisa_03 with d1
            show npc_portrait_mia_03 with d1
            mia "You wish bro, that's not going to happen."
            "It's totally going to happen."
            me "Right, but if did happen, would you be angry?"
            lisa "[me], let's change the subject ok."
            "That's not a yes."
            "We talk for a few more minutes before it's time to leave."
            hide npc_portrait_mia_03 with d1

        elif f_day3_spy:
            show npc_portrait_mia_14 with d1
            "Mia is here already, her pants however are not..."
            me "Morning sis."
            mia "Hey, bro are you done spying on my mom?"
            me "I-I... what... no, I was... you see..."
            mia "Haha, relax silly, I'm not mad, it must be torture to live in a house with a beauty like her, walking around half naked all the time, I'm just surprised it took this long for you to do it."
            me "Really? Well thanks Mia for being so cool about it."
            mia "It's fine, maybe the next time call me, it would be... fun."
            hide npc_portrait_mia_14
            show npc_portrait_lisa_03 at top with vpunch
            lisa "What an interesting conversation you are having!"
            "We both freeze in shock as Lisa walks behind me."
            mia "MOM, this is not what it looks like..."
            lisa "Kids sit down, I want to talk with both of you."
            "We do as we are told, even a future god is not immune to motherly wrath... but she does not seem angry."
            lisa "Kids, I just realised something, both of you are still virgins correct?"
            "We nod."
            lisa "That is not common for your age, so I think maybe I have been sheltering both of you too much, and even worse teasing you without realising it."
            lisa "So I think it's time for us to be more open to each other, about how we feel, our desires and wants. I want you both to feel more confident in yourselves and your bodies."
            me "What are you trying to say Lisa?"
            lisa "Ok, [me] I want you to be honest, did you felt sexual desires for Mia or I?"
            me "That's... I... yes..."
            lisa "And you Mia?"
            hide npc_portrait_lisa_03 with d1
            show npc_portrait_mia_03 with d1
            mia "Yes."
            lisa "So did I, and I think those desires are normal, I don't mean we should act on then, completely that is, we are family after all."
            lisa "But from now on if you are felling horny, I think we should help eachother to the best of our ability. No sex however, but I would not be opposed to some other forms of release..."
            me "Are you saying we are free to do things like... blowjobs maybe?"
            lisa "Not in public, but if both parties agree with it then yes."
            hide npc_portrait_mia_03 with d1
            "Everything is going very well, that is the best family talk we have ever had."
            mia "Mom that's... shit bro we have to leave soon."
            lisa "Sorry kids, go put some clother I will make you a sandwhich to eat on the way."
            "A few minutes later..."

        show vid_lisa_kiss_02 at top with d1
        lisa "Have a nice day guys, come here give me a goodbye kiss..."
        hide vid_lisa_kiss_02 with d1
        show vid_lisa_kiss_03 at top with d1
        lisa "You too Mia."
        hide vid_lisa_kiss_03 with d1
        "That's a good way to start your day."

        menu:
            "Outside":
                jump lbl_city_street_1st

    elif v_time >= 1020 and v_time < 1080 and tb_event[3]["home_kitchen"]["mia"] == 0:
        "Mia is here, grabing some snacks to hide in her room again."
        me "What are you doing sis?"
        show npc_portrait_mia_17 with hpunch
        mia "Ahhh... [me]! Don't scare me like that."
        me "Sorry. You are going to hide these in your room again aren't you? Honestly sis, I don't know how you are not overweight."
        hide npc_portrait_mia_17 with d1
        show vid_mia_ass_03 at top with d1
        mia "I do some exercises every day in the evening."
        me "Well, go ahead then, before mom catches you."
        hide vid_mia_ass_03 with d1

        $ tb_event[3]["home_kitchen"]["mia"] = 1
        $ v_time += 5

    elif v_time >= 1080 and v_time < 1140:
        show npc_portrait_lisa_01 with d3
        "Lisa is here preparing dinner, let's not bother her."
        hide npc_portrait_lisa_01 with d3

    elif v_time >= 1140:
        show npc_portrait_mia_06 at top with d3
        "Lisa and Mia are waiting for me in the kitchen, the have a smile on their faces."
        hide npc_portrait_mia_06 with d1
        show npc_portrait_lisa_04 with d1
        lisa "[me], sweetie I have great news for you! I was in the hospital were your grandma is today and guess what? She is fully awake and contious."
        me "Really that's wonderful! When can I visit?"
        lisa "Finish eating your dinner and we are going."
        me "That's awesome."
        hide npc_portrait_lisa_04 with d1
        "I start to gobble down on the food so fast that I almost choke to death. I haven't talked to grandma in months, she got worse in August and... wait a second, is she affected by the corruption too? I don't know what to think about it, she is very old and I am not into that..."
        "I will think about this later, time to go."

        menu:
            "Hospital":
                jump lbl_city_hospital

    else:
        "No one is here now."

    menu:
        "Go back":
            jump lbl_home_living_room

## KITCHEN - DAY 4 ##
label lbl_home_kitchen_day4:
    if v_time == 0:
        me "Mia come on, I am sorry ok. I shouldn't have teased you like that."
        mia "That is not it bro, I have been thinking and, you are right I feel a desire towards you and I can't explain it. Worse I know I'm not the only one. I caught mom more than once touching herself looking at your picture."
        me "That is a little creepy."
        mia "I know right, but that is not the point. Both of us have this desire and we have tried to suppress it for a long time, and I can't anymore."
        me "Are you saying..."
        mia "That whenever you are ready, so am I... as long as we are alone at home. It might be hypocrisy on her part but I'm 100\% sure she would ground us for life if she caught us having sex."
        me "We are alone right now."
        mia "And late for class bro, Marcy is coming to pick us up soon."
        me "Why,we usually go to her."
        mia "She said something about breaking the routine or something."
        "*Knock* *knock*"
        mia "That's is her, are you ready?"
        me "Yes let's go."

        menu:
            "Go to class":
                jump lbl_college_class

### LIVING ROOM ###
## LIVING ROOM - DAY 1 ##
label lbl_home_living_room_day1:
    "She is here, and waiting for me, it was a good life..."
    lisa "[me], sit down."
    "That's not a request, it's best to do as the lady says."
    lisa "So, don't you know how to knock? What did you have in your mind to open {b}my{/b} bathroom door when I was showering?"
    me "I'm so sorry, Mia told me that you were done, and I was running late so I didn't think..."
    lisa "Well you should have, you are not a kid anymore. You know you are in trouble right?"
    me "Yes."
    lisa "Good, you will be not be getting any money from me this month, if you want you will be getting a job or taking it from your savings."
    me "I understand."
    lisa "Look, I was very angry most of the day, it's a good thing I had the time to cool down or you would be getting a much harsher punishment. Let's just leave it that way and forget this ever happened okay? Now go to your room, you left your computer on."
    me "I did? Okay I'm going."

    $ v_time = 1140

    menu:
        "My room":
            jump lbl_home_room_mc

## LIVING ROOM - DAY 2 ##
label lbl_home_living_room_day2:
    if v_time == 720:
        me "Lisa I went to see the nurse and she told me to come home earlier."
        "That's a lie, but it's better than saying that the nurse showed me her tits and asked me to jack off to them."
        lisa "Really? Are you not feeling well?"
        me "No, I'm fine, she said it was just stress, can I have lunch with you?"
        lisa "Sure, sit down I will bring you a plate."
        "We talk for a bit while eating. After lunch I decide to help her wash the dishes."
        lisa "So I've been thinking, have you ever kissed a girls."
        me "Whoooa... where is this coming from?"
        lisa "It's just, I never see you with any girls besides Mia, and no, her kisses do not count. Those are sister kisses."
        "That's one messed up sentence."
        me "Well I can't say I have?"
        lisa "Well I have been thinking, are you scared that you no good at it?"
        me "Well maybe, experience is important to get good at, well everything."
        lisa "My thoughts exactly, so I think you should train with me."
        me "Are you serious? But you are like a mother to me."
        lisa "Oh sweetie, that's really nice of you. But that's even more reason to teach you. So that you can be more confident."
        "What is this? My mind is going numb just thinking about it. What aunt Lily said should I just enjoy it or fight it? Maybe just a kiss is not a bad idea..."
        me "O-Ok... then when do we start?"
        lisa "Right now, if that's what you want to."
        me "Okay then how..."
        lisa "Sit here."
        "She sits close to me and starts telling me what to do."
        lisa "Put your hand on my back lower back... yes just like that, no come close. Look in my eyes a come closer."
        "Her scent is intoxicating, and she is coming closer."
        show img_lisa_kiss_01 at top with d3
        "Her lips are so soft and moist I'm losing myself in the moment."
        "My hands start to move on their on and I find myself caressing her ass. She then stops when she feel my hands lifting her shirt a bit."
        hide img_lisa_kiss_01 with d3
        lisa "Ok, *pant* that's enough for today [me] *pant*, you did good..."
        me "Yes... uhh thanks?"
        lisa "I have to leave now, take care, ok."
        "I decide to spend some time playing games."
        "Where will I go now?"

        $ v_time = 840

        menu:
            "Outside":
                jump lbl_city_street_1st
            "I think Mia is home":
                $ v_time = 900
                jump lbl_home_room_mia

    elif v_time == 840:
        "Lisa and Mia should be home by now, it looks like Lisa is in the bathroom and Mia on her room."
        "Where should I go?"

        menu:
            "See what Lisa is doing":
                jump lbl_home_bathroom
            "Look for Mia":
                jump lbl_home_room_mia
            "Go play a videogame":
                $ v_time = 900
                jump lbl_home_room_mc

## LIVING ROOM - DAY 3 ##
label lbl_home_living_room_day3:
    if v_time >= 840 and v_time < 900 and tb_event[3]["home_living_room"]["lisa_hj"] == 0:
        "Lisa and Mia are talking in the living room."
        me "Hey guys what are you tal..."
        show img_mia_kiss_lisa at top with hpunch
        lisa "Oh sweetie your sister asked me to teach her a few kissing techniques."
        me "I see..."
        mia "Is that... whoa bro, that must have really turned you on! You dick is poking out of you pants."
        me "I can't denied that it was hot... maybe you could teach Mia some handjob techniques next Lisa."
        lisa "I don't see why not, come closer."
        hide img_mia_kiss_lisa with d1
        "She pull my pants down and starts working on my shaft. She is talking with Mia but all I can do is feel her hand on my cock."
        show vid_lisa_handjob_cum at top with d1
        lisa "Wow, that was a lot of cum sweetie, you need to relieve yourself more often. If you need help you can ask me or Mia."
        hide vid_lisa_handjob_cum with d1
        me "I will, I promise."

        $ tb_event[3]["home_living_room"]["lisa_hj"] = 1
        $ v_time += 10

    call main_show
    call screen scr_navigation

### LISA ROOM ###
## LISA ROOM - DAY 2 ##
label lbl_home_room_lisa_day2:
    "I'm on my way to the kitchen when I hear some noises from Lisa's room, the door is not closed so i decide to take a look."
    show vid_lisa_room_masturbate at top with d3
    "Ohhh... [me]..."
    "What the fuck! Is she...? But... Why am I still looking? It's best to leave if she catches me I'm a dead man."
    hide vid_lisa_room_masturbate with d3

    menu:
        "Kitchen":
            jump lbl_home_kitchen

## LISA ROOM - DAY 3 ##
label lbl_home_room_lisa_day3:
    if v_time == 0:
        "That was a great way to start my day, but now what am I supposed to do? I have a boner and it's killing me, maybe Lisa should take responsibility for it..."
        "Her door is half open let's see what she is doing... she is not here? Oh wait she is in her bathroom I can hear the water running."
        if f_day1_lisa_bathroom_incident:
            "If only I had heard that monday I would have avoided a lot of trouble. But I don't think she would mind if I take a peek now."
        else:
            "Let's take a peek, after what happened in my room, I'm sure she would not mind."
        scene loc_home_bathroom2
        show img_lisa_shower_05 with d1
        "Oh, I was not expecting this, maybe she was as excited as me from what happened earlier, maybe she needs some help. But should I risk it? That's a bit far from what we have done so far."
        menu:
            "Do it":
                hide img_lisa_shower_05
                show img_lisa_shower_01 with vpunch
                lisa "AHHHH... damnit [me] you scared me, can't you see I'm taking care of my business here. Wait were you spying on me?"
                me "That... is not important, I thought you maybe want some help."
                "I nod suggestively..."
                hide img_lisa_shower_01 with d1
                show img_lisa_shower_03 at top with d1
                lisa "As happy as I'm that you are willing to help me, I want some time alone, so it's time for you to GET OUT!"
                me "Sorry Lisa, I'm going."
                "Shit I knew that would be a bit too far, guess I will have to wait a few days before we can go further."

            "Don't do it":
                "Now let's get out of here before she sees me."

        $ f_day3_spy = True

        menu:
            "Kitchen":
                jump lbl_home_kitchen

    elif v_time >= 960 and v_time < 1020:
        "Lisa is getting ready for te gym."
        window hide
        show vid_lisa_undress at top with d1
        pause
        hide vid_lisa_undress with d1
        show img_lisa_gym_01 with d1
        "She is hot."
        hide img_lisa_gym_01 with d1

    else:
        "The room is empty."

    menu:
        "Go back":
            jump lbl_home_living_room

### MIA ROOM ###
## MIA ROOM - DAY 2 ##
label lbl_home_room_mia_day2:
    if v_time == 840:
        "I decide to look at what sis is doing."
        "It's looks like she is reading a novel and..."
        show vid_mia_masturbate at top
        "Whoa, better get out of here before she sees me."
        hide vid_mia_masturbate with d3

        $ v_time = 900

        menu:
            "Go away":
                jump lbl_home_room_mc

    elif v_time == 900:
        show npc_portrait_mia_06 at top with d1
        mia "Hey bro, what's up?"
        me "Nothing much, what are you doing?"
        mia "I'm reading this book."
        me "What is it called?"
        mia "\"Grey's Shades of Red\", I'm loving it."
        me "Oh whoa, isn't that a erotic novel?"
        mia "It is, yeah, why?"
        me "Oh nothing, nothing."
        mia "Listen, it looks like mom thinks you could use some help on interacting with girls. She is planning on teaching you how to kiss I think."
        me "What, are you serious?"
        mia "Yes. But it's no fair she does it alone, so I'm teaching you too what do you think?"
        me "Can we maybe talk about this some other time?"
        mia "Sure, but..."
        me "Sorry sis, I just can't think about it right now."
        mia "Okay, okay... so want to talk about something else?"
        hide npc_portrait_mia_06 with d3
        "We talk for a time, but when I'm about to leave I knock her book off the bed."
        me "Shit, sorry."
        mia "It's okay let me get it."
        show img_mia_ass_02 with d1
        "Then she turns around..."
        "Shit... No don't look, just leave."
        me "Sorry sis, bye!"
        hide img_mia_ass_02

        menu:
            "My room":
                jump lbl_home_room_mc

## MIA ROOM - DAY 3 ##
label lbl_home_room_mia_day3:
    if v_time >= 900 and v_time < 1020 and tb_event[3]["home_room_mia"]["mia_finger"] == 0:
        me "Hey Mia what are you doing?"
        show img_mia_book with d1
        mia "Hey bro, I'm just reading a book."
        me "Another erotic book?"
        mia "Yeah, my favorite kind."
        "That was true even before Nina came along, but she kept that fact hidden."
        me "I don't know why you read those, wouldn't be simpler to just watch porn?"
        hide img_mia_book with d1
        show npc_portrait_mia_16 with d1
        mia "Bro you don't get it, reading makes you put your imagination to work and..."
        "She then goes on a rant about how books are the best entertainement medium that exist. I block most of it out."
        mia "...and that is why Scarlett is better than Angelina ever was."
        me "Fascinating sis."
        mia "I'm glad you agree. I love to live this adventures in my head, the touching, the kissing..."
        me "So you prefer thinking about kissing rather than doing it?"
        mia "I didn't say that, if it's the right person, it's much better in real life."
        "She starts to get a little flustered and look down. Even a virgin like me gets the clue. I put my hand on her cheek and bring her face closer."
        hide npc_portrait_mia_16 with d1
        show img_mia_kiss_01 at top with d1
        "Mia's lips are soft and so moist. Her scent is somehow better than it has ever been."
        "Her tongue starts to dance in my mouth driving me crazy. In that state, I start to rub her pussy through her shorts. She then stops."
        hide img_mia_kiss_01 at top with d1
        mia "Bro please we can't go any further, if we do I won't be able to stop..."
        me "Mia, do you trust me?"
        mia "I do."
        me "Then turn around."
        "She does as I requested, so I proceed to kiss her neck and explore her body with my hands. She can't stop moaning. I then start fingering her. The moans only increase."
        show vid_mia_finger at top with d1
        mia "Bro, I-I'm..."
        me "It's ok Mia."
        "She let out a loud moan and her legs get weak, so I put her on the bed. She is almost in catatonic state. I will let her rest for now."
        hide vid_mia_finger with d1

        $ tb_event[3]["home_room_mia"]["mia_finger"] = 1
        $ v_time += 15

    elif v_time >= 900 and v_time < 1020 and tb_event[3]["home_room_mia"]["mia_finger"] == 1:
        "Mia is sleeping with a smile on her face."

    elif v_time >= 1080:
        show vid_mia_masturbate at top with d1
        "Mia's is busy..."
        hide vid_mia_masturbate with d1

    else:
        "Mia's room is empty, she must be somewhere else."

    menu:
        "Go back":
            jump lbl_home_living_room

### POOL ###
## POOL - DAY 3 ##
label lbl_home_pool_day3:
    if v_time >= 900 and v_time < 960:
        "Lisa is swimming here."
        show img_lisa_pool_01 at top with d1
        "Wow!"
        hide img_lisa_pool_01 with d1

    else:
        "This is our pool. Lots of memories here."

    menu:
        "Go back":
            jump lbl_home_living_room