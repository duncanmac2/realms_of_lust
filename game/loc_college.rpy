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

label lbl_college_garden:
    call main_show
    scene loc_college_garden

    if v_day == 1:
        jump lbl_college_garden_day1
    elif v_day == 2:
        jump lbl_college_garden_day2

label lbl_college_locker_room:
    call main_show
    scene loc_college_locker_room

    if v_day == 1:
        jump lbl_college_locker_room_day1
    elif v_day == 2:
        jump lbl_college_locker_room_day2

label lbl_college_nurse:
    call main_show
    scene loc_college_nurse

    if v_day == 2:
        jump lbl_college_nurse_day2
    elif v_day == 3:
        jump lbl_college_nurse_day3

label lbl_college_shower_men:
    call main_show
    scene loc_college_shower_men

    if v_day == 1:
        jump lbl_college_shower_men_day1

label lbl_college_yard:
    call main_show
    scene loc_college_yard

    $ v_localisation = "college_yard"

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

    menu:
        "Follow Marcy":
            jump lbl_college_locker_room

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
    if f_day2_nurse and tb_repeatable[3]["college_nurse"]["bj"] == 0:
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

    elif not f_day2_nurse and tb_repeatable[3]["college_nurse"]["hj"] == 0:
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

    else:
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

    $ v_time += 10

    menu:
        "College":
            jump lbl_college_yard
