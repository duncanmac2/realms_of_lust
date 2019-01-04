#### LOCATIONS ####
label lbl_college_class:
    call main_show
    scene loc_college_class

    if v_day == 1:
        jump lbl_college_class_day1
    elif v_day == 2:
        jump lbl_college_class_day2
    elif v_day == 3 and v_time < 720:
        jump lbl_college_class_day3
    elif v_day == 4:
        jump lbl_college_class_day4

label lbl_college_corridor:
    call main_show
    scene loc_college_corridor

    if v_day == 4:
        jump lbl_college_corridor_day4

label lbl_college_garden:
    call main_show
    scene loc_college_garden

    if v_day == 1:
        jump lbl_college_garden_day1
    elif v_day == 2:
        jump lbl_college_garden_day2
    elif v_day == 3:
        jump lbl_college_garden_day3

label lbl_college_gym:
    call main_show
    scene loc_college_gym

    if v_day == 3:
        jump lbl_college_gym_day3

label lbl_college_locker_room:
    call main_show
    scene loc_college_locker_room

    if v_day == 1:
        jump lbl_college_locker_room_day1
    elif v_day == 2:
        jump lbl_college_locker_room_day2
    elif v_day == 3:
        jump lbl_college_locker_room_day3

label lbl_college_nurse:
    call main_show
    scene loc_college_nurse

    if v_day == 2:
        jump lbl_college_nurse_day2
    elif v_day == 3:
        jump lbl_college_nurse_day3

label lbl_college_office_ellie:
    call main_show
    scene loc_college_office_ellie

    if v_day == 3:
        jump lbl_college_office_ellie_day3

label lbl_college_shower_men:
    call main_show
    scene loc_college_shower_men

    if v_day == 1:
        jump lbl_college_shower_men_day1

label lbl_college_teacher_office:
    call main_show
    scene loc_college_teacher_office

    if v_day == 3:
        jump lbl_college_office_ellie

label lbl_college_yard:
    $ v_localisation = "college_yard"

    call main_show
    scene loc_college_yard

    if v_day == 1:
        jump lbl_college_yard_day1
    elif v_day == 2:
        jump lbl_college_yard_day2
    else:
        call screen scr_navigation

#### EVENTS ####
### SCHOOLYARD ###
## SCHOOLYARD - DAY 1 ##
label lbl_college_yard_day1:
    "We reach the campus several minute too late."
    mia "See you guys later."
    me "See you sis."
    "Mia has different classes from Marcus and I, lucky her her teacher is much less strict than ours."
    me "So Marcus... what was that business that you had to take care of?"
    marcus "Well you see... Carly, our neighbour has no curtain on her bedroom and she was changing and..."
    me "Damn it man, she didn't see you spying on her did she? We already have this reputation on campus, don't want to get the cheerleader thinking you and by extension me are complete creeps."
    marcus "But we kinda are..."
    me "You are my friend, you are."

    menu:
        "Go to class":
            jump lbl_college_class

## SCHOOLYARD - DAY 2 ##
label lbl_college_yard_day2:
    if v_time == 720:
        mia "Hey bro are you going to eat with us?"

        menu:
            "Yes":
                jump lbl_college_garden
            "No I'm going home":
                jump lbl_city_street_1st

    else:
        "We are on time today, first time in the year."
        marcy "[me] you have been ogling me all the way here."
        me "Oh sorry, I didn't mean to..."
        marcy "I know I'm beautiful but come on man at least buy me dinner first, hahaha."
        "I can't help but to see my old friend now, even if \"he\" is a \"she\" now it's the same person on the inside... But with some big tits attached..."
        mia "I'm going to meet Veronica, see you guys later."
        "Mia always gives me a kiss on the cheek before we go to our classes so I approach her..."
        show img_mia_kiss_01 at top with d3
        "That's not what I thought would happen... It's strangely pleasant"
        hide img_mia_kiss_01 with d3
        me "W-what... bye Mia..."
        "Mia goes on her way, she just kissed me... what..."
        marcy "[me], are we going?"
        me "Oh right. Wait do you think I should go see the nurse? I'm feeling a bit off today?"
        marcy "It's your call, If you want to I will warn Mr. Smith, you can take my notes later."

        menu:
            "Class":
                jump lbl_college_class
            "Nurse":
                jump lbl_college_nurse

### CLASS ###
## CLASS - DAY 1 ##
label lbl_college_class_day1:
    "As fast as we could run we were not fast enough, we are 10 minutes late, waiting for the worst we enter the classroom ready to have our heads chopped off, but..."
    marcus "Where is he? You don't think that he is also late right?"
    me "Well he is not here, everyone else is, he must be."
    marcus "Man, we caught a break for once, how lucky are we? He is never late."
    me "Right!?"
    "As I start to ponder why is everyone late today, he come through the door out of breath."
    show npc_portrait_mr_smith_01 at top with d3
    mr_smith "I'm sorry class, I had a problem at home today and could not get here on time, let's start right away then."
    "The class goes at the usual pace, a very boring and slow, but no one is even thinking about sleeping, that would be a very bad idea. Mr Smith is not only ponctual but also very strict."
    "Once he caught a poor guy sleeping, he made him try to solve a extremely complex equation, and when he couldn't he failed him. We never saw him again."
    "After what feels like an eternity the class end, both of us start making our way to the garden to eat lunch with Mia and, that's when the stereotypical bully enter the scene."
    hide npc_portrait_mr_smith_01
    show npc_portrait_jason_01 at top with d3
    "This is Jason, he is a douche."
    jason "Hey loser, where is that hottie you sister she hasn't been answering my messages."
    me "Sorry to hear that Jason, maybe she changed her number again because she doesn't want to be harassed by you."
    "He is not happy with my answer, hope I didn't go too far, he could probably could break me like a twig if he wanted..."
    jason "What a shame, then maybe you can give me some money for a beer so I can go forget about her and her annoying brother."
    kyle "That's enough Jason. Leave him alone."
    "I'm saved, this is the captain of the football team and the only person that can keep Jason in check. Unlike most of his peers he is a really nice guy to us nerds and lost souls (that's me and Marcus on that order)."
    "I knew him in fifth grade he was the fat kid everyone made fun of, except Marcus and I, so when we met again in college he started watching our back. Doesn't mean Jason is not picking on me when he is not looking but other guys have it much worse."
    jason "As you wish \"captain\", see you later nerd."
    hide npc_portrait_jason_01 with d3

    if f_day1_lisa_bathroom_incident:
        kyle "Hey [me], here is the key to the men's shower, should be empty now. Don't worry man we all have woken up too late to take a shower before."
        "If I was a chick I would be in love, but since I'm a dude I just thank him and go there to take the shower that was denied to me today."

        menu:
            "Men's shower":
                jump lbl_college_shower_men

    else:
        kyle "He is such a pain in the ass. Your sister is wise not to go out with him. See you later guys I will see to it that he does not shove people in their locker."
        "If I was a chick I would be in love, but since I'm a dude I just thank him and go meet Mia and Veronica at the garden."
        marcus "[me], go on ahead I have business to attend."
        me "Sure see you later man."

        menu:
            "Lunch":
                jump lbl_college_garden

## CLASS - DAY 2 ##
label lbl_college_class_day2:
    "Once inside I notice that there are some new faces, girl faces in class, and we are missing a few guys... shit I hoped Marcy was an isolated case."
    me "So... do you remember why you were late yesterday?"
    marcy "Oh right my neighbor, sorry about that, it's just rare for her to change in her room and then I..."
    me "Ok, never mind, let's just sit."
    "We chat a bit, it seems that most of what made Marcus, well Marcus is the same with Marcy, that's good, she doesn't feel like a complete stranger."
    show npc_portrait_mr_smith_02 at top with d3
    "A few minutes later Mr. Smith arrived, he looks a little younger... Well that's the least strange thing I saw today."
    hide npc_portrait_mr_smith_02 with d1
    "Jason on the other hand looks smaller than normal, less muscular, he is still a beast however. That's the first good change of the day."
    "The class goes on as usual until a late student comes to class."
    unknown "I'm sorry Mr. Smith, the bus was late and..."
    mr_smith younger "Well I sorry to hear that, but you know the rules miss."
    "He points to his lap."
    unknown "Yes."
    mr_smith "Well then?"
    show vid_college_spanking at top with d1
    "What the fuck. Why is he? He never... god damn it, I just can't go for five minutes without something strange happening."
    marcy "Nice ass huh?"
    me "Yes... I mean... Oh fuck it."
    hide vid_college_spanking with d1
    "After the class end I decide to see Aunt Lily. She might know something about what is happening, Nina said it was something in my blood, our blood.I have to go there."

    menu:
        "Aunt Lily":
            jump lbl_city_home_lily

## CLASS - DAY 3 ##
label lbl_college_class_day3:
    show vid_college_run at top
    marcy "We will no get there in time."
    me "Less talking more running."
    mia "This is my stop good luck guys."
    hide vid_college_run with d3
    show npc_portrait_ellie_01 with d3
    "Mia continues running to her class, while we run to ours. We open the door and everyone is on their seats. The bell goes of as soon as we enter the classroom. A strange woman looks at us, is she..."
    ellie "That was close guys, you need wake a little earlier, specially you Marcy, with your grades you can't afford to be late."
    marcy "Sorry Ms. Smith."
    "That confirms it. Mr. Smith is Miss now."
    ellie "And you [me], if you have some time come see me in my office after lunch."
    me "Yes Miss Smith."
    hide npc_portrait_ellie_01 with d3
    "I don't think I'm in trouble, she said \"if\" I have the time, what does she want?"
    "We sit, and than I take a look at the rest of the class. There are more girls than ever here, Nina did not disappoint. And my old nemesis is nowhere to be seen, I wonder which of the new girls he is... Oh nevermind he is still here, but now he looks really pathetic... that's a good sign."
    "The class goes on as normal, and at the end of it Jason of all people come to talk to me."
    show npc_portrait_jason_02 at top with d3
    jason "[me], my man, so tell me is your sister still single?"
    "This guy... well he won't be a guy for much longer by the looks of it, and I'm pretty sure he can't kick my ass, not easily at least, so..."
    me "Listen Jason, Mia doesn't want to go out with you, get this through your thick skull."
    jason "Sorry dude, I know, but come on grease the wheels for me a bit, I will own you one."
    "This gives me a idea, if he owns me one, when he becomes a she, she might still own me..."
    me "Ok, how about this, I will talk to her, but no promises and you will own me, independent of her answear, deal?"
    jason "Ok.. ok deal, thanks dude."
    hide npc_portrait_jason_02 at top with d3
    "Marcy comes to talk to me after he goes away."
    marcy "You know she will say no, right?"
    me "Yes, but he thinks there is a chance, and now he will own me a favor."
    marcy "That's harsh, dude, but I can't say he doesn't deserve it, he likes to bully anyone he sees as weak. If you were not so big I think he would be demanding you, not asking."
    "Spot on, let's get out of here now."

    $ v_time = 730

    menu:
        "College":
            jump lbl_college_yard

## CLASS - DAY 4 ##
label lbl_college_class_day4:
    "Well we are here the class is normal except there is a lot more girls now. Maybe Jason is not Jason anymore. What would \"he\" be called now?"
    "I notice the trend were the names they get as a girl is similar to the names they had as a guy. If this was some sort of story that would be lazy of the writer..."
    if tb_event[3]["city_home_lily"]["lily_sex"] == 1:
        "Marcy is already here."
    me "Hey Marcy."
    #
    marcy "Hey [me] what are you thinking about?"
    me "Nothing... Hey Marcy do you think it's weird this town has so much more women than men?"
    marcy "Nah, it's always been that way."
    me "Okay..."
    marcy "Hey do you want to do something really crazy?"
    me "Not particulary, no."
    marcy "Come on it will be fun."
    me "All right what do you have in mind."
    show obj_pills at top with d1
    marcy "Ellie is usually late, we could put these in her coffe."
    hide obj_pills with d1
    me "What are those?"
    marcy "They are some pills I got from my friend Jenny, she said the will make anyone who consumes them instantly horny, and Ellie bottle of water is right there in the table."
    if tb_event[3]["college_office_ellie"]["aphrodisiac"] == 1:
        "If those pill are the same as that liquid Ellie showed me yesterday it will work, but if my guess is correct that will react with the water and create a gas that will affect every woman in the room in time."
    else:
        "I don't know what those are but they look like they could react with the water and release some gas."
    me "Are you saying you want to put that in the teacher's water?"

    menu:
        "Let's do this":
            "Marcy sneaks to the table and drops a pill in the bottle and leaves it barely closed. Ellie arrives a few seconds later. She starts her class as normal, but then she starts to strugle, like someone lit a fire in her pants."
            "She then tells the class to read from the books and sits on her table and starts to... you know. On that moment a girl I've never seen comes to talk to me."
            #
            jane "Hey [me]."
            me "Hey... uhh..."
            jane "Jane."
            me "Yes, hey Jane."
            "Jane, could it be Jason?"
            jane "So did you talk to Mia? Will she be my friend?"
            "That's him. But what is this friend stuff. Maybe since Jason is a she, she wants to just be friends instead of going out with her."
            me "Look Jane can we talk when the class is over?"
            #
            jane "Sure [me], sorry to bother you... What is that smell?"
            "The gas from the reaction has finally reached the back of the class, they all start to fell the effects. Soon all girls are touching themselfs shamelessly."
            #
            "I take the decision to take Marcy out off the class. Jane follow us."
            marcy "Why are we leaving all the fun behind [me]?"
            me "Let's just say I want to just watch this time, what about you Jane, why are you following us?"
            #
            jane "I feel funny, I-I need..."
            "Oh the gas got her, Marcy is also rubbing herself but that could just be Marcy being Marcy."
            me "Ok, come here both of you."
            "We enter a closed room."
            me "I don't feel like participating, so why don't you guys have some fun?"
            marcy "Great idea!"
            jane "But I want you!"
            me "You heard what I said, get on with it Jane."
            jane "I... yes sir."
            #
            "After the fun we leave the room."

            menu:
                "Leave the room":
                    jump lbl_college_corridor

        "Let's not do this":
            "The class goes a usual... if usual included a few handjobs and a blowjob when the teacher isn't looking."
            "At the end of the class a girl comes to talk to me."
            #
            jane "[me] did you talk to Mia, is she going to be my friend?"
            "That has to be Jason, but what that about friends?"
            me "Hey... huh..."
            jane "Jane!"
            me "Jane, I haven't talked to her yet... sorry."
            "I thought I was going to see some of Jason atitude from her, but she looks super sad."
            #
            jane "I see, when you have the time then..."
            me "Wait, can I ask you why do you want to be friends with her so bad?"
            jane "That's... I don't have any friends ok, I don't know why but most people don't like me very much, but you and Mia always were... not mean to me. So I thought..."
            #
            "Poor Jane, she inherited Jason's sins, and now because everyone hated him, they also hate her."
            me "But why don't you ask her directly?"
            jane "I tried, but I blew it, I said something really stupid, and now I'm scared she hates me too, but if you talked to her..."
            "Jason was an asshole to her the first time he asked her out. Shit I feel bad for her, she looks like a sweet girl that was dealt a bad hand because of who she was before all this."
            me "Hey, Jane, I don't know what Mia will say, but if you want I will be your friend from now on."
            jane "Really? You will?"
            "She starts tearing up and gives me a hug. Then thanks me again and leaves, crying."
            me "Marcy, let's... are you crying?"
            marcy "No, it's just a there is something in my eyes..."
            me "Oh I believe you, let's go."

            $ f_day4_jane_friend = True
            $ v_time = 660

            menu:
                "Outside":
                    jump lbl_college_corridor

### GARDEN ###
## GARDEN - DAY 1 ##
label lbl_college_garden_day1:
    if f_day1_lisa_bathroom_incident:
        mia "[me] why took you so long?"
        me "Kyle gave me a key to go take a shower."
        show npc_portrait_veronica_01
        veronica "He is always nice, and handsome, a shame he is gay."
        "This is Veronica, Mia's best friend, she is kind of a slut, she bedded the whole football team acording to some rumors."
        "She is not a bad person, she just can't control her urges, also she has this strange respect for me, never ever flirted with me, don't know if that's good or bad."
        me "He's what now?"
        veronica "Gay, he has to be, I hit on him more times then I can count and he never even blinked."
        hide npc_portrait_veronica_01
        show npc_portrait_mia_06 at top with d3
        mia "V, not all guys that don't want to be with you are gay."
        veronica "You're so naive Mia, please never change."
        me "He is? I never knew, does anyone else knows? Doens't matter even if he is gay it's none of my business. Where is Marcus?"
        veronica "He came by a while ago, asked us to tell you to meet him..."
        mia "Wait he is coming back here."
        marcus "Hello guys, I'm back."
        veronica "That's terrible news. What with that smile on your face?"
        marcus "It's a secret between men only."
        hide npc_portrait_mia_06 with d3
        show npc_portrait_veronica_01 with d3
        veronica "Fine no need to tell us, by the way Mia come here, let me tell you about the incident in the girl's shower last week."
        marcus "What incident?"
        veronica "Sorry, Marcus it's a secret between women only."
        "The curiosity is going to eat him alive now, it's almost too cruel."
        "After we eat Marcus call me to his house, but I was thinking of going to the mall with Mia, it's been some time since we went there to eat some ice cream. Where do I go?"

        menu:
            "Mall with Mia":
                jump lbl_city_mall
            "Marcus's house":
                jump lbl_city_home_marcy

    else:
        "I approach the girls"
        show npc_portrait_veronica_01
        "This is Veronica, Mia's best friend. I now what you are thinking, he must have a crush on her... No I'm not some cliche main character, also she is kind of a slut, she beded the whole football tem acording to some rumors."
        "She is not that bad but she knows her way around a cock... not mine though, she has this strange respect for me, never ever flirted with me, don't know if that's good or bad."
        hide npc_portrait_veronica_01
        show npc_portrait_mia_06 at top with d3
        mia "Hey bro..."
        veronica "Hey [me], how was you class?"
        me "Boring, yours?"
        mia "Same, hahaha, where is Marcus?"
        me "Don't know, said he had a business meeting."
        "(Both of them) Ewwww!"
        me "No I don't think it was a code for faping, he must have bought something from someone he does that sometimes."
        mia "What he usually buy?"
        me "Awwww... ahhh... things..."
        "(Again both of them) Ewwww..."
        hide npc_portrait_mia_06 with d3
        show npc_portrait_veronica_01 with d3
        veronica "Why do we go out with him?"
        mia "Because he is bro best friend..."
        veronica "Yeahhh..."
        hide npc_portrait_veronica_01
        show npc_portrait_marcus at top
        "While we talk about him, Marcus appears out of nowhere."
        me "Speaking of the devil."
        marcus "Hey girls, Veronica beautiful as ever..."
        veronica "You would be almost charming if you didn't had that problem with being too pervy."
        marcus "I'm hurt hahaha, but I came to talk to [me], come with me dude."
        me "But I didn't eat yet..."
        marcus "Trust me this is better than food."
        me "Okay..."

        menu:
            "Go with him":
                jump lbl_college_locker_room

## GARDEN - DAY 2 ##
label lbl_college_garden_day2:
    me "Yes, I'm a starving."
    mia "Ok how was class today?"
    me "I went to see the nurse today, don't worry I fine just a bit stressed out that's all, where is Veronica?"
    mia "She will be here any minute now, oh, there she is!"
    show npc_portrait_veronica_02 with d3
    veronica "Hey, sorry I'm late, was just talking to Kim."
    mia "It's ok, why don't you tell bro what you told me."
    veronica "Well, my friend Karen told me something interesting, it looks like she thinks you are very cute, and wouldn't mind going out with you."
    me "Really?"
    veronica "Yes she works at a store in the mall, I bet she would love for you to come visit."
    hide npc_portrait_veronica_02
    show npc_portrait_marcy_02 with vpunch
    marcy "Good for you man."
    veronica "HOLY SHIT! Where did you came from? One of these days you are going to give someone a heart attack."
    marcy "Sorry, I didn't mean to scare you Veronica. But [me], how about we go celebrate, then come with me."
    "Why not, it's probably a good chance to see if Marcy remembers having a penis."
    me "Ok, let's go."
    hide npc_portrait_marcy_02 with d3

    menu:
        "Follow Marcy":
            jump lbl_college_locker_room

## GARDEN - DAY 3 ##
label lbl_college_garden_day3:
    if tb_event[3]["college_garden"]["veronica"] == 0 and v_time < 780:
        show img_mia_bikini with d3
        me "Hey, guys how were your class? And why are you in a bikini?"
        mia "Hey. We are sunbathing."
        hide img_mia_bikini with d1
        show img_veronica_bikini with d1
        "That's a strange thing to do in the garden of our college, but now that they mentioned it they are not the only ones, I guess since the beach is a nudist heaven, this is the place for some tan marks."
        veronica "Did you know some student was caught fucking in a class earlier today."
        me "What are you serious, shit what happend?"
        veronica "Well the cleaning lady entered a class room, this morning and it looks like they were doing it on the teacher's desk."
        mia "Whoa, so what happened to them?"
        veronica "Ms. Figgs scolded them and took them to the dean, they got a suspension for a day."
        marcy "Just out of curiosity, which classroom was it?"
        me "Yeah, do you know who it was?"
        veronica "I do... it's a guy from the football team, and me."
        me "I'm sorry did you just say \"me\"?"
        veronica "I did..."
        mia "V, what are you thinking, what if they expelled you?"
        veronica "Come on Mia, I'm not the first to get caught during some sexy time in here, if they didn't fire the coach of the football team after they caught him with a cheerleader, they will not expel me. Besides it's fun to run the risk of being caught."
        "Veronica was never this open with her private activities before, it's not like she hides it, but she never boasted in public before. It looks like the more naughty you were before Nina started working her magic, the faster you get corrupted."
        veronica "I took some pics, do you guys want to see it?"
        marcy "YES!!!"
        veronica "Calm down Marcy, it's nothing explicit just pics of the guy in question."
        marcy "AWWW..."
        me "No thanks. No offense, but I don't want to know who you sleep with."
        veronica "Are you jealous [me]? Aww... don't worry, when you and Mia get finally together, do what your heart command, I will be happy to be your second."
        hide img_veronica_bikini with d1
        show npc_portrait_mia_05 at top with d1
        mia "Veronica!!!"
        veronica "What? You know it's true, you are one of the most beautiful girls in the college Mia, the only reason you are still a virgin is because deep inside you want your big bro to be your first..."
        mia "THAT'S ENOUGH."
        "Wow, I never saw Mia this angry before, Veronica is even more shocked than me, I think she must be a few days ahead of the rest of us in the corruption department. Mia is not even considering the possibility of us doing it yet. Shit I think Veronica is going to cry."
        veronica "Mia... sorry, I..."
        mia "Guys, can you give us some privacy."
        marcy "Come on [me], time for us to leave."
        hide npc_portrait_mia_05 with d3

        $ tb_event[3]["college_garden"]["veronica"] = 1
        $ v_time += 10

    else:
        "There is no one I know here right now."

    menu:
        "College":
            jump lbl_college_yard

### GYM ###
## GYM - DAY 3 ##
label lbl_college_gym_day3:
    if tb_event[3]["college_gym"]["bonnie"] == 0 and v_time < 840 and f_day1_lisa_bathroom_incident:
        show npc_portrait_bonnie_01 at top with d3
        "Here is were the cheerleader train on most days, but it's mostly empty now, except for..."
        me "Hey you, you are the pervert that interrupted my shower."
        hide npc_portrait_bonnie_01 with d1
        show img_bonnie_ass with d1
        bonnie "Me? Oh right, you are that guy in the locker room, what are you doing here?"
        me "Don't try to change the subject, I think you own me an apology."
        bonnie "Why? If I remember right, you had a great time looking at me."
        me "Well that is true..."
        bonnie "See, we both benefit from that, so let's leave it at that."
        me "But... fine. But at least tell me why you were in such a hurry?"
        bonnie "It's complicated, but maybe some day I will tell you, you seem like a nice guy and don't have many friends, so tell me [me], want to be my friend?"
        me "Uhh sure, why not."
        hide img_bonnie_ass with d1
        show npc_portrait_bonnie_01 at top with d1
        bonnie "Great, let me give you my number... there. Now I need to go, but I'm here everyday from 12 to 14 hours. Come here and we can talk."
        "She is leaving. Maybe she is going to take another shower. I wouldn't mind seeing it again."
        me "Hey Bonnie, are you going to take a shower?"
        bonnie "That's right."
        me "Well as your friend, I think I should escort you, I mean if some creep enters the showers and you are there alone... who know what might happen."
        bonnie "Hahaha... if you want to see me naked so badly all you need is ask. But you do have a point, there is this guy that... nevermind, come on my noble friend, protect this young madam..."
        me "You got it."
        hide npc_portrait_bonnie_01 with d3

        menu:
            "Follow her":
                pass

        scene loc_college_locker_room

        show img_bonnie_undress with d3
        bonnie "Well here we are..."
        "With only those words spoken she starts stripping..."
        me "You are very comfortable being naked around people."
        hide img_bonnie_undress with d1
        show img_bonnie_shower_05 with d1
        bonnie "I just am, I don't care about nudity that much..."
        me "Oh, I see..."
        bonnie "Come on you can't protect me if you stay here here."
        hide img_bonnie_shower_05 with d1
        show img_bonnie_shower_06 at top with d1
        "We enter the showers and she starts wash herself, she is as hot as I remember."
        bonnie "I'm almost done, it looks like no creep is comming here today... maybe because I locked the door."
        me "Did you know?"
        hide img_bonnie_shower_06 with d1
        show img_bonnie_shower_07 with d1
        bonnie "Indeed, but you were willing to protect me, I think you deserve a reward..."
        "She goes down on her knees and opens my zipper."
        me "Even better than I remember..."
        hide img_bonnie_shower_07 with d1
        show vid_bonnie_blowjob_01 at top with d1
        "She is amazing, she know how to work my weak spots... her tongue is doing things I could never have imagined."
        me "Bonnie... that's..."
        hide vid_bonnie_blowjob_01 with d1
        show vid_bonnie_blowjob_02 at top with d1
        "She starts to suck so hard it feels like she is going to take my soul with her."
        me "I-I'm..."
        hide vid_bonnie_blowjob_02 with d1
        bonnie "Wow, that's a lot, how was the reward?"
        me "It was amazing!"
        bonnie "Glad you liked it, but now I have to go. Let's put some clothes."
        "After a few minutes we say our goodbyes and she leaves. I think we will be great friend."

        $ tb_event[3]["college_gym"]["bonnie"] = 1
        $ v_time += 15

    elif tb_event[3]["college_gym"]["bonnie"] == 0 and v_time < 840 and not f_day1_lisa_bathroom_incident:
        show npc_portrait_bonnie_01 at top with d3
        "This place is empty, why did I come here again? Oh wait there is a girl here. Why is she reading a book in the gymnasium? And eating a sandwich?"
        bonnie "Hey, you!"
        me "Me?"
        bonnie "Yes you, come here."
        me "Okay, what is it?"
        bonnie "Hey, I'm Bonnie, to make a long story short, I'm need to take a shower and I don't want to throw away my sandwich, do you want it?"
        me "What? Are you offering me a half eaten sandwich? To a stranger? Why?"
        bonnie "Well it would be a waste to throw it on the trash, and we are alone here so..."
        me "No thanks, I don't even like ham."
        bonnie "It's not ham, here..."
        "She comes closer to show me whats inside, but loses her balance, I manage to catch her but the sandwich lands on my shirt, my white shirt... there was mustard in it..."
        bonnie "Shit, I'm so sorry, come on, let's wash it before it stained."
        hide npc_portrait_bonnie_01 with d1

        menu:
            "Follow her":
                pass

        scene loc_college_locker_room

        bonnie "Take your shirt off I will wash it."
        me "Okay..."
        "She run to the showers with my shirt and a few moments later I hear water running... and running... She is taking a really long time, let's see what is happening."
        show img_bonnie_shower_04 with d1
        bonnie "Oh sorry, I'm almost finished."
        me "I thought you were going to wash my shirt, why are you taking a shower?"
        bonnie "I told you I have to leave soon, sooo... two birds, one stone."
        me "Really, now it's soaked, good thing I have a spare in my backpack."
        hide img_bonnie_shower_04 with d1
        show img_bonnie_shower_07 with d1
        bonnie "I'm really sorry about your shirt, but hey think of this as my most sincere apologies."
        hide img_bonnie_shower_07 with d1
        show img_mc_bulge at top with d1
        "There is a massive bulge on my pants, I mean she is pretty hot, I can't lie."
        hide img_mc_bulge at top with d1
        bonnie "You know, I think you deserve a reward for being so nice to a clut like me."
        show img_bonnie_handjob_01 at top with d1
        "She knees and open my pants, and slowly massages my cock with her soft hands."
        hide img_bonnie_handjob_01 with d1
        window hide
        show vid_bonnie_handjob_02 at top with d1
        pause
        hide vid_bonnie_handjob_02 with d1
        me "Consider yourself forgiven Bonnie, I'm [me] by the way."
        bonnie "Well [me], if you want to talk some more I'm here on the gymnasium everyday before 14 o'clock."
        me "I will come visit when I have the time."

        $ tb_event[3]["college_gym"]["bonnie"] = 1
        $ v_time += 15

    else:
        "There is nobody here right now."

    menu:
        "College":
            jump lbl_college_yard

### LOCKER ROOM ###
## LOCKER ROOM - DAY 1 ##
label lbl_college_locker_room_day1:
    show loc_college_locker_room_men at top
    "He brings me to mens locker room, I have a bad feeling about this..."
    marcus "Did you know that some jocks can be reasonable and no assholes? For a price that is."
    me "What are you talking about?"
    marcus "You see they have a very well guarded secret between themselves, but for the low price of 50 dollar they gave me access to this amazing artifact."
    me "What???"
    marcus "Behold!!!"
    "He points at a hole in the wall, wait a minute..."
    me "Is that...?"
    marcus "Yes, it the legendary girls shower spy hole!"
    me "My god dude, that's amazing let's take a look!"
    marcus "Wait, tere must be some kind of ritual of ritual or speach for this kind of occasion and..."
    me "I'm already looking through the hole."
    hide loc_college_locker_room_men
    show vid_college_shower_01 at truecenter
    "This is heaven, we take turns looking at the girls in the shower."
    hide vid_college_shower_01
    figgs "Who is there?"
    marcus "Shit is old figgs the janitor, we can't let him find us... quickly the windows, jump."
    "We land on the bushes outside the windows, I think he didn't see us."
    marcus "That sucks man, but hey wanna go play some games on my house?"
    me "Sure, why not?"

    menu:
        "Go to Marcus's":
            jump lbl_city_home_marcy

## LOCKER ROOM - DAY 2 ##
label lbl_college_locker_room_day2:
    me "So where are we going?"
    marcy "Where do you think?"
    me "Oh no!"
    marcy "Yes, the locker room, spy on the girls."
    me "Why do you need me to spy on them? You are a girl you can just enter their shower."
    marcy "Yes, but then it would be no fun."
    me "*Sigh* Let's go then."
    marcy "Where is your excitement dude, cheer up."
    "The place is empty."
    me "Ladies first."
    "She spends a few seconds looking and when she moves away I decide to take a look."
    show vid_college_shower_02 at top
    me "Whoa!"
    marcy "I know right."
    hide vid_college_shower_02 with d3
    "Maybe this was a bad idea, I feel like my dick is on fire, I can barely think straight... I have to get out of here."
    me "Marcy I..."
    show img_marcy_boobs_01 at top
    me "Wha..."
    marcy "Sorry I just had to..."
    me "Okay... Gotta go!"
    hide img_marcy_boobs_01
    "I stand up and run away from there before I do something stupid."

    $ v_time = 840

    menu:
        "Home":
            jump lbl_city_street_1st

## LOCKER ROOM - DAY 3 ##
label lbl_college_locker_room_day3:
    if tb_event[3]["college_gym"]["bonnie"] == 0 and v_time >= 840 and v_time < 900 and f_day1_lisa_bathroom_incident:
        "Maybe that girl is here again today, what's her name? Bonnie. Let's take a look."
        show img_bonnie_shower_04 with d3
        "There she is."
        "Since we are alone here I have to take advantage of the situation."
        hide img_bonnie_shower_04 with d1
        show img_bonnie_shower_06 at top with d1
        bonnie "Enjoying the show [me]?"
        me "Oh shit, you knew I was here?"
        bonnie "You are not as stealthy as you think. Come here."
        "No point in trying to hide what I'm doing now."
        bonnie "So you were having some fun huh. But I have a better idea, take those clothes off and come here, I will wash your back."
        "What is she going to do? Well might as well do it. I enter the hot water under the shower, Bonnie then gives me a hug from the back, her body is pressed again mine, I can fell her tits on my back."
        bonnie "Now relax."
        hide img_bonnie_shower_06 with d1
        show img_bonnie_handjob_01 at top with d1
        "She knees and open my pants, and slowly massages my cock with her soft hands."
        "Her hands reach around to my cock and she starts jerking me off."
        "I don't know what is better, her naked body rubbing again my back or her hands playing with my dick."
        hide img_bonnie_handjob_01 with d1
        show vid_bonnie_handjob_02 at top with d1
        "After I climax, I turn to her to ask her the obvious question."
        hide vid_bonnie_handjob_02 with d1
        me "That's was amazing, don't get me wrong... but why?"
        bonnie "I've wanted to do this since I saw you monday... When I want to do something I just do it."
        me "Okay, I guess."
        bonnie "I have to go now, but hey come see me in the gym after lunch some times, you look like a nice guy, we could be friends."
        me "Sure why not."
        "What a weird girl."

        $ tb_event[3]["college_gym"]["bonnie"] = 1
        $ v_time += 5

    elif tb_event[3]["college_gym"]["bonnie"] == 0 and v_time >= 840 and v_time < 900 and not f_day1_lisa_bathroom_incident:
        show img_bonnie_shower_04 with d3
        "There is someone in the shower, but... the hell, it's a girl. Why is she here?"
        "She is so hot... wow, my dick is on fire! There is no one here right now besides us and she hasn't seen me."
        hide img_bonnie_shower_04 with d1
        show img_bonnie_shower_06 at top with d1
        "After a few minutes of choking the chicken, she turns to me and says."
        bonnie "I hope you liked the show..."
        "Shit, she saw me? Okay let's stay calm, she is not freaking out, maybe she likes being watched."
        bonnie "Hey are you listening?"
        me "Yeah... I'm sorry for spying on you."
        bonnie "Why are you apologizing? I asked if you liked the show."
        me "Well I did yeah."
        bonnie "Good, for you... uhhh... what's your name again?"
        me "[me]."
        hide img_bonnie_shower_06 with d1
        show img_bonnie_shower_07 with d1
        bonnie "[me], I'm Bonnie. Look I'm late for something but now I think it's only fair if you do something for me don't you think? Come back here tomorrow."
        me "I... ok, I will be here if I have the time."
        bonnie "I will be waiting."
        hide img_bonnie_shower_07 with d1
        "She puts her clothes and leaves. What a strange girl."

        $ tb_event[3]["college_gym"]["bonnie"] = 1
        $ v_time += 5

    else:
        "This place is empty."

    menu:
        "College":
            jump lbl_college_yard

### SHOWER ###
## SHOWER - DAY 1 ##
label lbl_college_shower_men_day1:
    "It's empty just as Kyle said, luckyly I have a shirt on my backpack, let's take a quick shower."
    "I take my clothes off an enter the cold, cold water... better this than nothing I guess."
    "Not even a minute in I hear someone enter the shower."
    show img_bonnie_shower_01 with d3
    bonnie "Shit, what are you doing here, this place is supposed to be empty."
    me "What am I doing? What are YOU doing in the men's shower!"
    bonnie "Sure that why I'm here, those fucking cheerleaders think they own the girls washroom, so now I have to shower here after the training. All because I said their ponpon's were ridiculous."
    me "DO YOU MIND, I'm still naked here."
    bonnie "What's the big deal, you shy or something. Look I have no time, I have to get home in half an hour and I smell like shit, so I will use the last on right over there. You can leave if you want."
    hide img_bonnie_shower_01 with d3
    show img_bonnie_shower_02 at top with d3
    "Before I can say a word she finishes taking off her clothes and walks in, I'm kind of speechlees now so I just continue to shower without looking at her... it's not as easy as I thought... maybe just a peek."
    hide img_bonnie_shower_02 with d3
    show img_bonnie_shower_03 with d3
    "Shit, I get hard almost instantly, hope she doesn't notice."
    bonnie "Woah... you're not bad at all."
    me "What?"
    bonnie "Your dick, I thought you were hidding it because it was small, but its not bad at all."
    me "I'm leaving now."
    hide img_bonnie_shower_03 with d3
    show img_bonnie_shower_04 with d3
    bonnie "Suit yourself, I'm Bonnie by the way."
    me "[me]."
    "I leave as fast as I can, after that awkward exchange, best to forget it. There is still time to eat lunch with everyone."

    menu:
        "Leave this place":
            jump lbl_college_garden

### NURSE ###
## NURSE - DAY 2 ##
label lbl_college_nurse_day2:
    "Just in case I'm sick it's best to talk to Megan the nurse."
    show npc_portrait_megan_01 with d3
    megan "Hello [me], what's your problem?"
    me "I don't know to be honest, maybe I'm going crazy, but people are acting strange today."
    megan "What do you mean?"
    me "Like, I don't know, like if the world has changed and now everyone is... I don't know, different? Like I don't know them anymore."
    megan "[me], it's normal to feel lost, like the world has been flipped upside down. College is a stressful experience."
    "Just as I thought... she is going to blame stress. I can't blame say that a magic goddess of lust is changing the world is not an option."
    megan "How long has it been?"
    me "What? How long since..."
    megan "Since you had sex?"
    me "Where did that came from?"
    megan "Like I said sexual frustration can lead to high level of stress."
    me "Well... I-I'm... a virgin."
    megan "Oh! I see... well the best advice I can give you is to masturbate frequently and maybe ask a friend for help with finding a girlfriend... or a professional."
    me "Are you really telling me to go look for a prostitute?"
    megan "If it help you what is the problem... I mean you clearly need it."
    "She looks at my crotch, and I realize there is a bulge... When did this happened?"
    megan "I don't have any magazines here... But if you need some help..."
    me "Help, with what exactly?"
    megan "Well you can just leave it like this young man, it could be really bad for your health. Also I could use a sperm sample to see the effects of stress on your body."
    me "You want a-a sample?"
    megan "Yes, and like I said no magazines so if you need some help..."
    hide npc_portrait_megan_01 with d3
    show npc_portrait_megan_02 at top with d3
    "She starts taking her top off, I'm mesmerized I can't believe what im about to see. She hands me a cup and..."
    megan "Go on ahead."
    "You know what, FUCK IT, a hot nurse is telling me to masturbate while showing me her tits, I'm not wasting this opportunity."
    "It doesn't take long for my climax... then comes the guilt."
    me "I should go..."
    megan "Wait [me]..."

    $ f_day2_nurse = True

    menu:
        "Leave":
            scene loc_college_yard
            pass

    "What did I do? WHAT did I do??? I need to clear my head... Aunt Lily! She might know something about what is happening. Nina said it was something in my blood, our blood. I have to go there."

    menu:
        "Aunt Lily":
            jump lbl_city_home_lily

## NURSE - DAY 3 ##
label lbl_college_nurse_day3:
    if f_day2_nurse and tb_repeatable[3]["college_nurse"]["bj"] == 0 and v_time < 1020:
        "Let's go see Megan again, I want to see how far I can push her today."
        show npc_portrait_megan_04 with d3
        megan "[me]! It's good you are here, I have the results of your exams."
        me "What exams?"
        megan "From the sperm sample."
        me "Oh, right, so what are the results?"
        megan "You have an exceptional sperm count, great mobility, taste... great numbers all across the board. So good in fact that the lab scientists think that you are a great candidate for being a donor in their research to cure for male impotence."
        me "That's... wow... ({i}did she just say taste?{/i})"
        megan "I know right, and here I was thinking the results would be below average because of all the stress. Anyway they asked me to retrieve some more samples, I'm allowed to give you a monetary compensation in exchange for your semen. So do we have a deal?"
        me "Sure, sign me up, do you want some samples right now?"
        megan "That would be preferred, yes."
        me "I don't suppose you bought some magazines have you?"
        hide npc_portrait_megan_04 with d1
        show vid_megan_boobs_01 at top with d1
        megan "No, but I could always show you some real breasts if you like."
        hide vid_megan_boobs_01 with d1
        show img_megan_boobs_02 at top with d1
        me "Well how about something more?"
        megan "What do you mean, more?"
        me "Well, nurse my hands are hurting so maybe you could do the job for me..."
        "She looks surprised by my suggestion, maybe I went too far."
        megan "Look I don't go around giving handjobs to my patients, but since your hands are hurting, I will make an exception. Now let me see it."
        hide img_megan_boobs_02 with d3
        show img_megan_taste at top with d3
        megan "Wow, it's bigger than I remember."
        "Her hands are warm... and she is great at this, maybe I'm not her first after all."
        megan "You heard what I said about taste?"
        me "Well I did, do you have some tasting machine or something like that?"
        megan "No, after you left, I had some stuck in my clothes, and when I smelled it, it was like nothing I have ever smelled before so I tasted it."
        me "You, tasted it?"
        megan "Yes, and ever since I can't stop thinking about it..."
        "She is fixated on my penis, that's a great chance."
        me "Do you want to taste some more?"
        megan "Yes."
        me "What are you waiting for then."
        hide img_megan_taste with d1
        show vid_megan_blowjob at top with d1
        "She does not hesitate, she goes straight for my dick. Wow... she is good, I can feel her tongue dancing around the tip of my cock."
        me "Megan, I'm..."
        hide vid_megan_blowjob with d3
        megan "She was lost in the moment, so she was caught by surprise. Even so she swallows every single drop."
        me "So how was it?"
        megan "Amazing, be careful [me], I might get addicted to it, if you keep feeding me."
        me "That doesn't sound so bad."
        megan "Haha, for you maybe, but you have to go now, I have a patient waiting but please come back some other time."
        me "Oh I will."

        $ tb_repeatable[3]["college_nurse"]["bj"] = 1
        $ tb_repeatable[3]["college_nurse"]["hj"] = 1

    elif not f_day2_nurse and tb_repeatable[3]["college_nurse"]["hj"] == 0 and v_time < 1020:
        "If I remember correctly Megan, the nurse is gathering sperm sample for a research lab, it could be fun to see what she is willing to do to get them."
        show npc_portrait_megan_04 with d3
        megan "Hello [me], anything I can help you with?"
        me "I saw the poster, you are looking for volunteers to gatter semen right."
        megan "Correct, we pay a small fee for each sample, do you want to donate?"
        me "Sure, sign me up. I don't suppose you have some magazines have you?"
        hide npc_portrait_megan_04 with d1
        show vid_megan_boobs_01 at top with d1
        "No, but I could always show you some real breasts if you like."
        hide vid_megan_boobs_01 with d1
        show img_megan_boobs_02 at top with d1
        me "Well how about something more?"
        megan "What do you mean, more?"
        me "Well, nurse my hands are hurting so maybe you could do the job for me..."
        "She looks surprised by my suggestion, maybe I went to far."
        megan "Look I don't go around giving handjobs to my patients, but since your hands are hurting, I will make an exception. Now let me see it."
        hide img_megan_boobs_02 with d3
        show img_megan_taste at top with d3
        megan "Wow, that's pretty big..."
        "Her hands are warm... and she is great at this, maybe I'm not her first after all."
        hide img_megan_taste at top with d1
        show img_megan_handjob with d1
        megan "That's a lot, when was the last... No matter, thanks for your help [me], that was actually pretty fun. Come back when you can, and if your hands are still hurting then, I guess I wouldn't mind helping you again."
        hide img_megan_handjob with d1
        me "I would love that, bye Megan."
        megan "Bye [me]."

        $ tb_repeatable[3]["college_nurse"]["hj"] = 1

    elif tb_repeatable[3]["college_nurse"]["hj"] == 1 and v_time < 1020:
        menu:
            "Blowjob" if tb_repeatable[3]["college_nurse"]["bj"] == 1:
                show npc_portrait_megan_04 with d3
                me "Can I get a..."
                hide npc_portrait_megan_04 with d1
                show vid_megan_blowjob at top with d1
                "She does not hesitate, she goes straight for my dick. She is so good, I can feel her tongue dancing around the tip of my cock."
                me "Megan, I'm..."
                hide vid_megan_blowjob with d3
                megan "Mmmmm... thanks [me], come back when you can."

            "Handjob" if tb_repeatable[3]["college_nurse"]["hj"] == 1:
                show npc_portrait_megan_04 with d3
                me "Can I get a..."
                hide npc_portrait_megan_04 with d1
                show img_megan_taste at top with d1
                "Her hands are warm... and she is great at this, maybe I'm not her first after all."
                hide img_megan_taste at top with d1
                show img_megan_handjob with d1
                megan "That's a lot as always, thanks for your help [me], come back when you can."
                hide img_megan_handjob with d1
                me "I will!"

    elif v_time >= 1020:
        "Megan is with someone, the door isn't locked, let's take a peek."
        show vid_megan_lesbian at top with d3
        "Wow... nice!"
        hide vid_megan_lesbian with d3

    $ v_time += 10

    menu:
        "College":
            jump lbl_college_yard

### ELLIE OFFICE ###
## ELLIE OFFICE - DAY 3 ##
label lbl_college_office_ellie_day3:
    if tb_event[3]["college_office_ellie"]["aphrodisiac"] == 0 and v_time < 780:
        "I want to talk to Miss Smith, her office is right here. I knock on the door."
        show npc_portrait_ellie_02 with d3
        me "Hello Miss Smith."
        ellie "[me], come in, this is my daughter Dakota."
        hide npc_portrait_ellie_02 with d1
        show npc_portrait_dakota_01 with d1
        dakota "Hi."
        hide npc_portrait_dakota_01 with d1
        me "Hey. What did you want to talk about Miss Smith?"
        ellie "Call me Ellie, [me] you are making me feel old. What I wanted to talk is about is about a project, I'm studying pheromones, and I want you as my assistant."
        me "Whoa that's interesting, what are studying exactly?"
        "She pull a vial from a drawer."
        ellie "This chemical has the ability to cause intense lust in females, there is a company that wants to sell it as a aphrodisiac and they asked me to refine the formula. Here take it, it's safe for you to smell it, it only works on women."
        show npc_portrait_ellie_03 at top with d1
        "I smell nothing, and give it back to Ellie, but in that exact moment something goes wrong and the vial falls and breaks splashing the liquid all over mother and daughter."
        ellie "OH SHIT! Dakota are you okay?"
        dakota "I-I think so... but I feel a little... tigly."
        hide npc_portrait_ellie_03 with d1
        show img_ellie_undress_02 with d1
        "Maybe unconsciously both of them start to rub their panties..."
        ellie "[me]...can you l-leave us... please."
        hide img_ellie_undress_02 with d1
        show img_ellie_dakota_01 with d1
        "You don't have time to answer, before you can say anything Dakota lunges towards her mother and both of them start to tear each other clothes apart."
        "You think you are in heaven... but Ellie manage to summon the last of her will to say..."
        ellie "LEAVE!"
        "It's best to do as she says."
        hide img_ellie_dakota_01 with d1

        $ tb_event[3]["college_office_ellie"]["aphrodisiac"] = 1
        $ v_time += 10

    elif tb_event[3]["college_office_ellie"]["aphrodisiac"] == 0 and v_time >= 780:
        "I want to talk to Miss Smith, her office is right here. I knock on the door."
        show npc_portrait_ellie_02 with d3
        "Hello Miss Smith."
        ellie "[me], come in."
        me "What did you want to talk about Miss Smith?"
        ellie "Call me Ellie, [me] you are making me feel old. What I wanted to talk is about is about a project, I'm studying pheromones, and I want you as my assistant."
        me "Whoa that's interesting, what are studying exactly?"
        "She pull a vial from a drawer."
        ellie "This chemical has the ability to cause intense lust in females, there is a company that wants to sell it as a aphrodisiac and they asked me to refine the formula. Here take it, it's safe for you to smell it, it only works on women."
        hide npc_portrait_ellie_02 with d1
        show npc_portrait_ellie_03 at top with d1
        "I smell nothing, and give it back to Ellie, but in that exact moment something goes wrong and the vial falls and breaks splashing the liquid all over her."
        ellie "OH SHIT! [me] you need to..."
        hide npc_portrait_ellie_03 with d1
        show img_ellie_undress_01 with d1
        "She stops before finishing her sentence and starts to rub herself and undress."
        hide img_ellie_undress_01 with d1
        show img_ellie_undress_02 with d1
        ellie "[me]... you know as my assistant you have a obligation to help me in whatever I need."
        me "Is that so?"
        ellie "Yes and right now..."
        hide img_ellie_undress_02 with d1
        show img_ellie_undress_03 with d1
        ellie "...I need..."
        hide img_ellie_undress_03 with d1
        show img_ellie_undress_04 with d1
        ellie "...YOU..."
        hide img_ellie_undress_04 with d1
        show img_ellie_spread with d1
        ellie "To lick me..."
        me "Well you see Ellie I'm never accepted the position, so I don't have to do shit..."
        ellie "But..."
        me "However if you ask nicely I will be happy to help my lovely teacher."
        "She is a bit displeased to have lost control, but she is way too horny to hold back now."
        ellie "P-Please..."
        me "Please what?"
        ellie "Please lick me [me]..."
        "I decide to \"help her before she explodes\"."
        hide img_ellie_spread with d1
        show vid_ellie_cuni at top with d1
        "All she does is moan and gasp, I'm new at this, but the god's blood seems to be guiding me."
        hide vid_ellie_cuni with d1
        "Finally..."
        "Ellie is on a catatonic state, barely moving, I will let her be for now."

        $ tb_event[3]["college_office_ellie"]["aphrodisiac"] = 1
        $ v_time += 10

    elif tb_event[3]["college_office_ellie"]["aphrodisiac"] == 1:
        if v_time >= 780:
            "Let Ellie rest."
        else:
            "I can't enter right now."

    menu:
        "College":
            jump lbl_college_yard

### CORRIDOR ###
## CORRIDOR - DAY 4 ##
label lbl_college_corridor_day4:
    if v_time == 0:
        jane "What happened to us?"
        #
        me "Well if I had to guess, the pill reacted with water and release a gas that affected everyone in the class."
        jane "What pill?"
        me "The one's Marcy put in Ellie's water."
        jane "She did what?"
        #
        marcy "Come on guys it was fun wasn't it?"
        me "Yes!"
        jane "I...I had never done it with a girl before, and the way you commanded us, it was... arousing."
        me "You like being ordered around huh."
        jane "I... maybe..."
        #
        me "Well I have a great proposition for you then. I will get Mia to be your friend, in turn we will play master and slave, we can discuss the specifics later after you think hard about what you are about to..."
        jane "DEAL!"
        me "Wow, that's it? You don't want to think this over?"
        jane "After what just happened... the idea of you ordering me, to do naughty things, it's just... I want it. Even if Mia doesn't not agree, I'm yours now Master."
        me "Okay your eagerness has been noticed (and it is a little creepy). Just out of curiosity, why are you so desperate for Mia to be your friend?"
        jane "Because I don't have any friends and everyone hates me for some reason, but you and Mia are nice to me sometimes so..."
        "Poor Jane, she inherited Jason's sins, no one liked him, now they don't like her either."
        me "I will tell you what, even if Mia refuses, I will be your friend... you know outside the Master play."
        "She looks like she is about to cry, then she huggs me and kisses me in the cheek. To think that asshole would become such a sweet girl..."
        marcy "Soooo... you are into BDSM stuff [me]. Good to know."
        me "Yeah yeah, let's go smartass."

        $ v_time = 660

        menu:
            "Outside":
                jump lbl_college_corridor

    elif v_time == 660:
        if f_day1_lisa_bathroom_incident or tb_event[3]["college_gym"]["bonnie"] == 1:
            "On the way out, I bump into my Bonnie."
            #
            bonnie "Hey [me], going to spy on some innocent girl shower?"
            me "If I remember correctly you were the one that entered the mens shower while it was in use."
            bonnie "Details... I'm going to eat my lunch at the gymnasium and read come on by if you want to talk."
            me "I will, see you later."
            bonnie "Bye."

        else:
            "On the way out, I bump into a girl and she drops her books."
            #
            me "Sorry I was with my head in the clouds."
            "I kneel down to help her grab her things."
            bonnie "It's okay, I was not looking either, I'm Bonnie by the way."
            me "I'm [me], that is some... ehh... interesting litterature."
            "Is everyone reading erotica now? And this one has very graphical pictures."
            bonnie "Yeah, I just love those, they have such passion..."
            me "I bet."
            bonnie "Also I masturbate while no one is looking."
            me "You do huh."
            #
            bonnie "No, but I got you didn't I? I will tell you what, why don't you come to the gymnasium before two o'clock, so we can talk?"
            me "You sure are friendly to a stranger, but sure why not."
            bonnie "Cool, I will be waiting. Bye."
            "Huh, people are very friendly today."

        "My phone? I just received a message, I think it's from Jane."
        "{i}Sorry I ran off, Marcy told me to give you my address so here it is.{/i}"
        "Oh, nice. It's close to aunt Lily's house."

        $ v_time = 720

        menu:
            "Outside":
                jump lbl_college_yard