## LOCATIONS
label lbl_college_class:
    scene loc_college_class

    if v_day == 1:
        jump lbl_college_class_day1

label lbl_college_yard:
    scene loc_college_yard

    if v_day == 1:
        jump lbl_college_yard_day1

## EVENTS
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
    kyle "He is such a pain in the ass. Your sister is wise not to go out with him. See you later guys I will see to it that he does not shove people in their locker."
    "If I was a chick I would be in love, but since I'm a dude I just thank him and go meet Mia and Veronica at the garden."
    marcus "[me], go on ahead I have business to attend."
    me "Sure see you later man."

    menu:
        "Lunch":
            jump lbl_college_garden