#### LOCATIONS ####
label lbl_college_class:
    scene loc_college_class

    if v_day == 1:
        jump lbl_college_class_day1
    elif v_day == 2:
        jump lbl_college_class_day2

label lbl_college_garden:
    scene loc_college_garden

    if v_day == 1:
        jump lbl_college_garden_day1

label lbl_college_locker_room:
    scene loc_college_locker_room

    if v_day == 1:
        jump lbl_college_locker_room_day1

label lbl_college_nurse:
    scene loc_college_nurse

    if v_day == 2:
        jump lbl_college_nurse_day2

label lbl_college_shower_men:
    scene loc_college_shower_men

    if v_day == 1:
        jump lbl_college_shower_men_day1

label lbl_college_yard:
    scene loc_college_yard

    if v_day == 1:
        jump lbl_college_yard_day1
    elif v_day == 2:
        jump lbl_college_yard_day2

#### EVENTS ####
### YARD ###
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

label lbl_college_yard_day2:
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
label lbl_college_class_day1:
    "As fast as we could run we were not fast enough, we are 10 minutes late, waiting for the worst we enter the classroom ready to have our heads chopped off, but..."
    marcus "Where is he? You don't think that he is also late right?"
    me "Well he is not here, everyone else is, he must be."
    marcus "Man, we caught a break for once, how lucky are we? He is never late."
    me "Right!?"
    "As I start to ponder why is everyone late today, he come through the door out of breath."
    show npc_portrait_mr_smith at top with d3
    mr_smith "I'm sorry class, I had a problem at home today and could not get here on time, let's start right away then."
    "The class goes at the usual pace, a very boring and slow, but no one is even thinking about sleeping, that would be a very bad idea. Mr Smith is not only ponctual but also very strict."
    "Once he caught a poor guy sleeping, he made him try to solve a extremely complex equation, and when he couldn't he failed him. We never saw him again."
    "After what feels like an eternity the class end, both of us start making our way to the garden to eat lunch with Mia and, that's when the stereotypical bully enter the scene."
    hide npc_portrait_mr_smith
    show npc_portrait_jason at top with d3
    "This is Jason, he is a douche."
    jason "Hey loser, where is that hottie you sister she hasn't been answering my messages."
    me "Sorry to hear that Jason, maybe she changed her number again because she doesn't want to be harassed by you."
    "He is not happy with my answer, hope I didn't go too far, he could probably could break me like a twig if he wanted..."
    jason "What a shame, then maybe you can give me some money for a beer so I can go forget about her and her annoying brother."
    kyle "That's enough Jason. Leave him alone."
    "I'm saved, this is the captain of the football team and the only person that can keep Jason in check. Unlike most of his peers he is a really nice guy to us nerds and lost souls (that's me and Marcus on that order)."
    "I knew him in fifth grade he was the fat kid everyone made fun of, except Marcus and I, so when we met again in college he started watching our back. Doesn't mean Jason is not picking on me when he is not looking but other guys have it much worse."
    jason "As you wish \"captain\", see you later nerd."
    hide npc_portrait_jason with d3

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

### GARDEN ###
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
                jump lbl_city_home_marcus

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

### LOCKER ROOM ###
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
    show vid_college_shower at truecenter
    "This is heaven, we take turns looking at the girls in the shower."
    hide vid_college_shower
    figgs "Who is there?"
    marcus "Shit is old figgs the janitor, we can't let him find us... quickly the windows, jump."
    "We land on the bushes outside the windows, I think he didn't see us."
    marcus "That sucks man, but hey wanna go play some games on my house?"
    me "Sure, why not?"

    menu:
        "Go to Marcus's":
            jump lbl_city_home_marcus

### SHOWER ###
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

    menu:
        "Leave":
            jump lbl_college_garden