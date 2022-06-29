label ch0_en:

    $ persistent.splash_random = True
    scene hiroki_room with dissolveslow2
    window auto
    play music a1 loop fadein 2.0
    $ quick_menu = True
    "......"
    "{i}*yawn*{/i}"
    "I wake up like any other day."
    "I prepare to go to school with a goal to achieve..."
    "Getting a girlfriend before my senior year is over and not ending up being the virgin boy who thinks he's cute and never got a girlfriend in school."
    "I have been having trouble talking to a girl for years, my confidence vanishes when I talk to one, I feel like it's normal for me."
    "Well, but I don't have to think negatively."
    "You always have to have positive thoughts, today will be the day that I propose to one of the prettiest girls and of course it will be Hana Junko."
    "The most beautiful, popular and intelligent girl in the whole school."
    "Okay..."
    "That's how they consider her because of the way she is."
    "She's not a girl who thinks she's better than everyone else."
    "And that's why so many are drawn to her."
    "Including other girls and of course..."
    "Me."
    "She's one of my childhood friends, I only started feeling attracted to her a couple of years ago."
    "She doesn't know that yet."
    "And that's why I'll try to tell you today."
    "I'm not one of those responsible guys."
    "I mean, I'm the forgetful type and I might not even remember going to talk to her today."
    "{i}*sigh*{/i}"
    "But just thinking about her..."
    window hide(None)
    play audio punch
    scene hiroki_room with hpunch
    "No, don't think about weird things."
    "You're not that desperate to get a girlfriend."
    "..."
    "{cps=40}Well...{/cps}{nw=2.0}"
    stop music fadeout 1.0
    play audio knock
    pause 1.2
    $ e_name = "???"
    "Someone knocks at my door..."
    "Really? {w=2}, so early?"
    e "Brother you're going to be late."
    "Late? {w=2.0}, Late for what?"
    e "If you don't get up now..."
    e "You're going to be late for school."
    "One moment..."
    "..."
    "WHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!{nw}"
    play music a2 loop fadein 2.0
    pr "Gosh!"
    pr "I had forgotten {w=2.0}, I'm running late."
    "I quickly get out of bed to put on my uniform."
    pr "Where did I put my shoes?"
    "After a few minutes of searching, I finally found them."
    e "Little brother, aren't you going to take a bath?"
    pr "Gosh{w=2.0}, why are there so many steps to go to school?"
    "After I've put on my uniform and shoes, I have to undress and make my way to the bathroom."
    "{i}*sigh*{/i}"
    "I'm really going to be late."
    window hide(Dissolve(.2))
    pause 3.0
    window auto
    "I hate taking a bath in the mornings the water is very cold."
    scene black with dissolve
    pause 1.0
    "After I shower, I head to my room to put my uniform and shoes back on."
    scene hiroki_room with wipeleft
    "Ready again, if I hurry I can get there early."
    "I leave my room and head to the living room."
    scene hiroki_livingroom with wipeleft
    show emi nc02 at c11
    e "Hello little brother, have you had a bath yet?"
    show emi nc01
    pr "Yes, I already took a bath, and because of you I'm going to be late."
    show emi dc03
    "She is my little sister, Emi."
    $ e_name = _("Emi")
    "Luckily this week he didn't have school, and he stayed home."
    e nc02 "Are you ready for breakfast?"
    show emi nc01
    pr "Yes, but I'm going to take it, I'm running late."
    e n1c03 "Okay, I'll make it for you, just don't complain when it gets cold."
    show emi at hidetr
    hide emi
    pr "It is the price to pay for not being late."
    window hide(Dissolve(.2))
    pause 2.0
    window auto
    show emi nc01 at c11
    "After a while Emi hands me breakfast."
    pr "Well, I'm leaving now."
    e nc02 "Okay."
    e "I love you."
    "{i}*sigh*{/i}"
    pr "Emi I already told you many times, we are brothers."
    show emi dc04 at j11
    e "Awwww, but there's nothing wrong with a sister saying {i}'I love you'{/i} to her brother."
    show emi dc01
    pr "It doesn't have it, but you use it in another way and I don't like it."
    e dc06 "So I'll never be your wife?"
    show emi dc01
    pr "No and you'll make me late."
    "I quickly leave the apartment and head to school."
    show emi at hidetr
    hide emi
    scene black with wipeleft
    pause 0.5
    play audio dooropen
    scene apartment_exterior with wipeleft
    stop music fadeout 2.0
    window auto
    "Dude, I'm really going to be late."
    "I'll have to run."
    pause 1.0
    scene schoolen with wipeleft
    "After a few minutes, I get there."
    "I don't know if in time."
    "But I feel like my chest is going to explode."
    "I'm out of breath."
    "I ran too much."
    "I take a minute to catch my breath and continue to the classroom."
    scene classroom with wipeleft_scene
    play music a3 fadein 2.0
    $ i_name = "???"
    $ k_name = _("Professor")
    pause 0.5
    "As I enter the classroom I can see that the teacher is not there."
    "Will you be in the infirmary?"
    "I heard you have back problems."
    "Ah well, we'll have to wait, luckily he won't notice that I'm late."
    pause 2.0
    "A few minutes later, the teacher enters the classroom."
    "He seems to be nervous."
    show kaito n03 at ar11
    k "Sorry I'm late, I was in the hospital wing."
    "Wow, what a coincidence."
    "But..."
    "Why is he nervous?"
    k n02 "Ah [player!t], I see you're late."
    k "But don't worry, I'll let it slide this time."
    show kaito n01
    "He discovered me."
    show kaito at alhide
    hide kaito
    pause 0.5
    i "Friend, well done, you were lucky he didn't call you a foul, obviously he was late too."
    show issei ns03 at c11
    i "He's been going to the infirmary a lot lately, he should go to the hospital, he might be sick."
    pr "Yes, that may be it."
    show issei ns01
    "No, it is not."
    "Many of you should already know what I mean..."
    "Uh....{w}No?"
    "Please, he's dating the nurse, that shows a lot."
    "Am I the only one who realizes that?"
    pr "Did you solve the task I sent yesterday?"
    i ns03 "If{w}, why?"
    show issei ns04
    pr "LET ME COPY IT!"
    i ns05 "No."
    i "You should have done it, you probably stayed up all night playing or watching anime."
    show issei ns06
    pr "Please! Do you want to see your friend die?"
    i ns07 "No, but your suffering is perfect punishment."
    show issei ncs08
    pr "PLEASE! I'll lend you my Nintendo Switch."
    i ncs07 "Ugh, ok, but can you lend it to me for a week."
    pr "Done."
    i ns03 "Okay, but copy it quickly."
    show issei ns04
    j "Issei shouldn't just sell yourself for a Nintendo Switch."
    $ i_name = _("Issei")
    show jenni as01 at c22
    show issei at c21
    i ns05 "Look who's talking, the one who sold her notebook yesterday for a state-of-the-art sound system."
    show issei at z21
    i nbs05 "Besides, I think it was a bad investment, since they only lent it to you yesterday."
    show issei ns06 at c21
    show jenni at z22
    j nbs03 "Yes, but I can't do anything."
    j nbs04 "I love music!"
    "I imagine she spent the whole night listening to music."
    "By the way, those two are my friends Issei and Jenni."
    $ j_name = _("Jenni")
    "Late presentation but wanted to wait for Jenni to show up."
    "She's my other childhood friend along with Hana."
    "Issei is my best friend."
    j nbs05 "Also you don't have to accept the irresponsibility of [player!t]."
    j "You play games and watch anime, but at least you do your homework, [player!t] doesn't."
    show jenni nbs06
    pr "Hey, sometimes it's really boring to do homework, but it was only yesterday."
    j ns07 "You've been like this for a month."
    show jenni ns06
    "Gosh, I can't go against your logic."
    "Sometimes I don't like doing homework."
    "..."
    "Although I'm not the only teenage boy who sometimes neglects his study regimen to play video games."
    show jenni ns01
    show issei ns01
    k "Well students it's time to start class, everyone get out your notebooks."
    show issei nbs02 at z21
    show jenni ns01 at c22
    i "Well bro, see you later."
    show issei ns01 at hidetr
    hide issei
    show jenni at c11
    j ns02 "See ya [player!t]."
    show jenni ns01 at hidetr
    hide jenni
    pause 2.0
    window hide(Dissolve(0.2))
    show black with dissolve
    stop music fadeout 2.0
    pause 2.0
    window show(Dissolve(0.2))
    "I'm glad I was able to copy the homework."
    "It wasn't too complicated anyway, just a few small but important concepts."
    window hide(Dissolve(0.2))
    pause 3.0
    scene classroom with wipeleft_scene
    show kaito n02 at c11
    k "...And you always have to be careful about what websites you visit on the internet."
    show kaito n01
    play audio schoolbell
    pause 2.0
    play music a4 fadein 2.0
    "Classes were just as boring, but at least they're over for today."
    k n02 "Good students, it's time to go."
    k "But first I have to make an announcement."
    k nb02 "This week it was the turn of this class to help bring the week's assignment folder to Akemi Yumi."
    k n02 "Let's see who will be the one to wear it."
    "Akemi Yumi{w}, who is it?..."
    "Isn't that the girl who doesn't attend classes?"
    k "Since even if she is not from this room, we must collaborate with this."
    k "Let me see."
    k "This week's shift belongs to..."
    if not player == _("Hiroki"):
        k "[player!t]."
    if player == _("Hiroki"):
        k "Maki [player!t]."
    show kaito n05
    pr "WHAAAAT!!!{nw}"
    pr "But,{w} why me?"
    k n06 "It's your turn are the rules."
    show kaito n05
    "{i}*sigh*{/i}"
    "I should go?"
    window auto
    menu:
        "Yes, if I go.":
            $ persistent.yumihelp = 0
        "I'm not going no.":
            $ persistent.yumihelp = 1

    if persistent.yumihelp == 0:

        pr "Well I'll go, I have no choice."
        "I get up from my seat and walk over to the teacher's desk and grab the folder with the week's assignments in it."
        "After taking it I head to the door and leave the room."
        "But before..."
        pr "Say hello to the nurse."
        k n03 "Y-Yeah, O-Okay."
        show kaito at hidetr
        hide kaito
        pause 2.0

    if persistent.yumihelp == 1:

        pr "I will not go, I have many things to do."
        k nb07 "You have to go{w}, it's your turn."
        show kaito n08
        pr "No, I have a lot of things to do."
        k n09 "I guess those things are: watching Anime and playing video games all afternoon."
        show kaito n10
        "Ugh, he found me out."
        window hide(Dissolve(.1))
        scene classroom 
        show kaito n07 at j11
        with hpunch
        k "You're going because it's the rules!"
        show kaito n08
        pr "Okay, but don't get mad."
        "I get up from my seat and walk over to the teacher's desk and grab the folder with the week's assignments in it."
        "After taking it I head to the door."
        "But before..."
        pr "Professor, I've been wondering, how's your back?"
        k n03 "F-Fine, why do you ask?"
        pr "For nothing, you should go see a doctor, knowing that the nurse is the cause of everything."
        "The last thing I said in a low voice so as not to get into arguments."
        show kaito at j11
        k "Y-Yes, Y-Yes, I'll keep that in mind t-thank you."
        pr "You're welcome, I'm leaving, send my regards to the nurse."
        show kaito n03 at j11
        k "O-Okay."
        show kaito n11
        "After that I leave the room."
        pause 2.0
        show kohana ns03 at c31
        show kaito n05 at c32
        show natsumi ns03 at c33
        ko "Professor by the way{w}, how's your back?"
        show natsumi ns04 at z33
        show kohana ns04
        nat "Right, because he's going to the infirmary a lot."
        show natsumi ns03 at c33
        show kohana ns03 at z31
        ko "Are you really okay?"
        show kohana ns04 at c31
        show kaito n03 at z32
        k "Y-Yes I'm really fine."
        show natsumi ns01
        show kohana ns01
        k n12 "{i}What trouble did you get me into.{/i}"
        window hide(Dissolve(0.2))
        pause 2.0

    stop music fadeout 2.0
    scene city1 with wipeleft
    window auto
    "......"
    "On the way home I almost forgot that I have to..."
    "What was it?..."
    "So, I have to take this, to that girl's house...."
    "What was her name?"
    "Yu...{w}Yum...{w}Y..."
    "Oh yeah{w}, her name is Yumi."
    "Well, I'll have to go to his house with the address the teacher gave me."
    "I read the address the teacher gave me{w}, and I notice that..."
    "One moment..."
    "This girl..."
    "He lives in the same building as me!"
    "..."
    "And in the apartment below!"
    "What the hell."
    "I never noticed."
    "How is this possible?"
    "..."
    "This must be a huge coincidence."
    "I've never seen her so that's why I was surprised."
    "..."
    "I don't know what this Yumi looks like."
    "I'm sure he doesn't go out much and that's why we've never seen each other."
    "Yes, that must be it."
    "Well, I just go and go."
    "Since he lives in the same building I don't think it will take long."
    window hide(Dissolve(.2))
    pause 3.0
    scene city2 with wipeleft
    window show(Dissolve(.2))
    "I...{w}I can't..."
    "I want to read the folder...{w}But...{w}I shouldn't."
    "It's none of my business..."
    "BUT!"
    "Curiosity is killing me!"
    "I can't help it!"
    "I open the folder and take a sheet from it."
    scene city2_blur with dissolve
    call shownote(note_yumi_en, True, "page1") from _call_shownote_9
    scene city2 with dissolve
    "Damn, I thought I'd have a picture to see what it looks like."
    "This girl looks like she's in trouble, but I'm still shocked that she didn't get a picture."
    "Since we've never met, I don't want to get to her house and she's a crazy girl or worse."
    "Well{w}, what else{w}, I'll have to take my chances."
    window hide(Dissolve(.2))
    pause 2.0
    window show(Dissolve(.2))
    "A few minutes later I arrive at my building."
    scene apartment_exterior with wipeleft_scene
    "She lives in the same building."
    "So I'll just walk up to the third floor which is where he lives."
    pause 2.0
    scene apartment_exterior with wipeleft_scene
    pause 1.5
    "Well, I'm here now."
    "I go to the door and ring the bell."
    pause 1.0
    play audio doorbell
    pause 2.0
    "There's no answer."
    "I'll ring the bell again."
    play audio doorbell
    pause 2.0
    "Any."
    "What's going on in there?"
    "When I go to knock on the door, I notice that it is open."
    "I really don't want to go in..."
    "But I'll have to."
    "I don't want to get in trouble if I don't turn in the folders."
    "Although I'll get into more trouble if they find out I entered an apartment without permission."
    "{i}*sigh*{/i}"
    "I lightly push the door open."
    stop audio fadeout 0.5
    play audio doorcreak3
    scene black with wipeleft_scene
    play music a5 fadein 2.0
    $ renpy.music.set_volume(0.15, channel="music")
    scene yumi_livingroom_dark with dissolve
    "When I enter I don't know why, but everything is very dark."
    "And that is daytime."
    "I feel a little chilly."
    "I do not see anyone."
    pr "YUMI!"
    "I call out his name, but no one answers."
    "I'll have to look for her."
    "I'll go first to..."
    $ kitchenfirstRun = None

label questions_en:
    menu:
        "The kitchen.":
            jump kitchen_en
        "Hallway.":
            jump con_en

label kitchen_en:
        
    if kitchenfirstRun == True:
        "There's no point in going back to the kitchen because I already checked there."
        jump questions_en
    else:
        "Being here scares me a little, why is it so dark?"
        scene yumi_kitchen_dark with wipeleft_scene
        "When I look around the kitchen and notice leftover food in the sink, I also smell something rotten."
        "What a horrible smell."
        "What will happen to this girl?"
        $ kitchenfirstRun = True
        scene yumi_livingroom_dark with wipeleft_scene
        jump questions_en

label con_en:

    "When I look to my right I notice a corridor."
    "It looks very dark."
    "But I'll have to get closer."
    scene black with dissolve
    pause 1
    scene yumi_hall
    show black zorder 500:
        ease 10 alpha 0.5
    pause 1
    "I wait for my eyes to get used to the dark."
    pause 1
    "I see I have two doors on my sides."
    window hide(Dissolve(.2))
    scene yumi_hall:
        xcenter 640
        ease 1,000 xoffset 80
        pause 1.0
        ease 1,000 xoffset -80
        pause 1.0
        ease 1.00 x offset 20
    show black zorder 500:
        alpha 0.5
    pause 5.0
    "One is the bathroom and the other is Yumi's room."
    "I know because they have signs with their names on them."
    "I should go into..."
    $ bathroomfirst = None

label questions2_en:
    menu:
        "Enter the bathroom.":
            jump bathroom_en
        "Enter the room.":
            jump Dcon2_en

label bathroom_en:

    if bathroomfirst == True:
        "I'm not going back into the bathroom, there's no point wasting time there."
        jump questions2_en
        
    else:
        scene yumi_hall:
            xcenter 665
            ease 1,000 xoffset 80
        show black zorder 500:
            alpha 0.5
        pause 1.0
        play audio doorcreak3
        scene yumi_bathroom_dark:
            xcenter 640
        with dissolve
        "As I enter I hear a jet of water."
        play audio dripper
        pause 4.0
        scene yumi_bathroom_dark:
            xcenter 640
            ease 1,000 xoffset -40
        "I take the key and lock it."
        "There is nobody here."
        "So there's nothing else to check."
        "I'm coming out of the bathroom."
        stop audio fadeout 0.5
        scene yumi_hall:
            xcenter 640
            xoffset 80
            ease 1,000 xoffset -80
        show black zorder 500:
            alpha 0.5
        with wipeleft_scene
        $ bathroomfirst = True
        jump questions2_en

label Dcon2_en:
        
    "I think you should go into the room."
    scene yumi_hall:
        xcenter 550
        ease 1.25 xoffset -20
    show black zorder 500:
        alpha 0.5
    "I sneak up to the door."
    scene yumi_door with dissolve
    "I open it slightly."
    play audio doorcreak2
    "I don't know but I hear a light cry."
    play audio yumi_cry
    pause 2.0
    "Will it be her?"
    y "{i}Why?....{w=2.0}Why?{/i}"
    "Now I hear a voice."
    y "..."
    "I should go in and see what happens."
    play audio door2c
    scene yumi_room_dark with wipeleft_scene
    pause .25
    pr "Yu..."
    show yumi fsl03 at c11
    y "{cps=15}This...{w=1.2}You...{nw=3.0}{/cps}"
    y"who are you?"
    show yumi fsl04
    pr "I...{w=1.2}Uh...{w=1.2}I..."
    "Is this Yumi?"
    $ y_name = "Yumi"
    "But if it is...."
    "..."
    "BEAUTIFULL!"
    "How does a girl like that get locked up?"
    show yumi fsl05 at j11
    y "Oh yeah...I know who you are..."
    show yumi fsl06
    pr "This..{w=1.2}What?..."
    y fsl02 "I really don't know how this kind of thing works."
    y fslb02 "But you showed up at just the right time."
    y fsl02 "So can I say..."
    y "That from this day on, you will be my boyfriend."
    stop music fadeout 2.0
    show yumi fsl01
    "What?...."
    "One moment..."
    "{cps=15}........{/cps}{nw=2.0}"
    "WHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!{nw}"
    pr "WHAT!....{w=1.0}WHAT!...{w=1.0}W-What did you say?"
    y fsl05 "That you are now my boyfriend, silly."
    show yumi fsl06
    "I feel like my face turns red."
    "T-This girl{w=1.2}, is she trying to play with me?"
    y fsl02 "Since I haven't thought of your name yet, I'll say 'Honey'."
    y "Do you think so?"
    show yumi fsl01
    "Right now, I don't know what to do."
    "I'm super nervous."
    "This girl, is she crazy or what's wrong with her?"
    y fsl03 "Hey honey, what you got?"
    y "You look very pale."
    show yumi fsl04
    pr "I..."
    "Without a second thought, I run out of the room as fast as I can."
    scene black with wipeleft_scene
    pause 1.0
    y "wait!"
    "Without looking back I leave Yumi's apartment."
    pause 3.0
    scene apartment_exterior with wipeleft
    pause 2.0
    "I run as fast as I can up the stairs of the building to my floor."
    "What the hell is wrong with that girl?!"
    window auto
    pause 3.0
    scene apartment_exterior with wipeleft_scene
    "When I get home, I rush into my room, ignoring my surroundings."
    scene hiroki_livingroom with wipeleft
    pause 0.25
    "I go into my room and close the door."
    scene hiroki_room with wipeleft_scene
    pr "*pant*{w=1.0} *pant*{w=1.0} *pant*{nw=1.4}"
    pr "What...{w=1.5}What just....{w=1.5}Happened?"
    e "Little brother, is something wrong?"
    e "I saw you go into your room very nervous."
    pr "Nothing happens Emi, don't worry."
    e "I hear you nervous, did something happen?"
    pr "E-Ehhhh.{nw=1.5}"
    pr "No, nothing happened."
    "I do tell him about what happened with Yumi."
    "Is going to kill me."
    "Not literally."
    "But she doesn't want me to have a girlfriend."
    "Not that it was my mother."
    e "Tell me when you feel good."
    pr "O-Okay."
    "{i}*sigh*{/i}"
    "Goodness."
    "If I tell her what happened to me, she'll go crazy."
    "He'll say, {i}Why didn't you take advantage of the situation?{/i}{w=2.0} or {i}Why didn't you play along?{/i}."
    "And I don't want to listen to your sermons."
    "Tomorrow I should go to Yumi's house and apologize for leaving like this."
    "But...."
    "It would feel weird walking into her house again."
    "Well...{w}My mind won't leave me alone until I apologize to her."
    "{i}*sigh*{/i}"
    "But for now I should just do my homework, because I have a lot of it."
    pause 2.0
    $ renpy.music.set_volume(1.0, channel="music")
    play music a1 loop fadein 2.0
    e "Little brother, it's time for lunch!"
    "But, first I must eat, no one can think on an empty stomach, right?"
    "I change my clothes and go."
    pr "I'll be right Emi, I'm going to change my clothes!"
    e "Okay!"
    pause 3.0
    scene hiroki_room with wipeleft_scene
    "Okay, I'm ready now."
    "I walk out of my room into the kitchen."
    scene hiroki_livingroom with wipeleft_scene
    show emi nc01 at c11
    e "Hello again little brother."
    e nc02 "How was your day?"
    show emi nc01
    pr "Well, well, why do you ask?"
    e nc02 "Well, it didn't seem that way a while ago."
    pr "W-Well...{w=1.3}I...{w=2.0}Eh..."
    "I'm already caught."
    "At this rate I'll get out of my mouth, what happened to me today."
    e nc02 "Come on you can tell me."
    e "It's not a bad thing, is it?"
    e nc14 "Or is that.."
    e nc04 "Did you get a girlfriend?"
    "I don't know why but when Emi said that I felt strange."
    "Spooky."
    "I felt like those words were embedded in my ears like some kind of parasite."
    pr "What do you care if I have a girlfriend or not?"
    show emi dc04 at j11
    e "I just want to be your wife!"
    show emi dc01
    pr "Emi, that's just a childish whim, the sister who wants to marry her brother."
    show emi dc06 at tr11
    e "Awwwww, but you can't?"
    show emi dc08
    pr "No, I've told you many times."
    "What world do you think we live in, Emi?"
    "Sibling relationships are only seen in anime."
    "And we already know which ones."
    pr "And what did you cook today?"
    show emi ac01 at j11
    e "Don't change the subject!"
    pr "You don't care if I have a girlfriend or not!"
    show emi dc08 at tr11
    e "Awww..."
    show emi dc01 at j11
    e "Well..."
    e nc04 "Today cook pavilion."
    pr "{i}Pavilion?{/i} What is that?"
    $ renpy.notify(_("Pavilion: Venezuelan traditional food, composed of white rice, black beans, fried plantain, and shredded meat"))
    e nc02 "It is a traditional Venezuelan food."
    show emi nc01
    pr "Why did you do that, if you don't even know what it is."
    e nc02 "I wanted to broaden my culinary knowledge."
    e "The food is simple but very delicious."
    show emi nc01
    pr "Well, that's fine."
    pr "Let's eat."
    pr "Let's see how it goes."
    show emi nc04 at j11
    e "Okay!"
    show emi at hidetr
    hide emi
    "We sat down at the table, and started eating."
    pause 2.0
    "What a treat!"
    "The food is simple like Emi said."
    "But it's very delicious."
    "I should tell Emi to cook this more often."
    "And also to investigate the traditional foods of other countries."
    "To taste them."
    window auto
    pause 2.0
    pr "Hmm..."
    pr "What a delight."
    pr "You put a lot of effort into this Emi."
    show emi nc05 at c11
    e "Thank you."
    e n1c02 "You see."
    show emi n1c01
    pr "See what?"
    e n1c05 "That I am perfect to be your wife."
    show emi n1c04
    pr "{i}*sigh*{/i}"
    pr "Emi I already told you, we are brothers."
    show emi dc06 at tr11
    e "Awww, but then..."
    show emi dc05 at j11
    extend "So..."
    show emi ac01 at j11
    e "Why do I cook you like a slave!"
    show emi dc01
    pr "First, don't yell at me and second...."
    pr "I ask you to cook, because your seasoning doesn't compare to mine."
    pr "Also, you are very good at cooking, don't you remember that I burned my arm just by cooking a fried egg?"
    show emi dc09 at tr11
    e "{i}Yesss{/i}, you're really bad at cooking."
    show emi dc08
    pr "Besides, I think if I cook, you'll end up regretting eating my food every day."
    e dc09 "O-Okay, sorry for yelling at you little brother."
    show emi dc10
    pr "Don't worry, no problem."
    e dc09 "Yes, but you should learn to cook, so that the day you get a girlfriend, you can cook for her."
    pr "Well, I have the best teacher."
    show emi nc04 at j11
    e "Hehe."
    e nc05 "Thank you."
    show emi nc04
    pr "You know, something super strange happened to me today."
    show emi nc06 at j11
    e "I knew it!"
    e n1c06 "And you and that nothing was wrong with you."
    show emi n1c07
    pr "Don't get emotional, I'm telling you so you don't feel bad for having scolded you."
    e n1c08 "O-Okay."
    show emi nc01
    pr "Well..."
    "I'm starting to tell her what happened to me today with Yumi, I don't mention her name so she doesn't think I have something with her."
    "I feel uncomfortable just telling you."
    "At the end, I expected what he had said."
    show emi dc05 at j11
    e "Seriously, you're dumb."
    show emi dc04 at j11
    e "Why didn't you take advantage of the situation?!"
    show emi at j11
    e "Why didn't you play along?!"
    "There it is, I knew you were going to say that."
    e nc05 "How were her breasts?"
    show emi nc04
    pr "WHEEEEEEEEEEEEEEEEEEEE!{nw}"
    pr "Why the hell are you asking me that question?!"
    e nc05 "Well, because it's the first thing you see when you meet a girl."
    e "How big were they?"
    e nc02 "She was a lolita."
    e nc11 "A middle ground."
    e nc14 "Or..."
    e nc05 "Did you have them too big?"
    show emi nc04
    pr "Well..."
    pr "{i}Do I really have to answer?{/i}"
    e nc02 "Of course, this is a conversation that a brother and sister should have every day."
    show emi nc01
    "YOU HAVE THE REVERSED THOUGHTS!"
    "That is a conversation of friends, but it would be very strange to talk about it."
    "And it would be very bad to talk about it."
    pr "Well, I'll tell you."
    "I sound like quite the pervert."
    "I don't deny that I did see them."
    "But I hope I don't have to tell someone else about this."
    pr "{i}Were{/i}..."
    pr "Ehhh..."
    pr "{cps=30}{i}Large...{/i}{/cps}"
    e nc04 "Oh! Really?"
    pr "They were a little bigger than Jenni's."
    show emi nc05 at j11
    e "You're a pervert! Hehe."
    show emi nc04
    pr "That's why I didn't want to tell you!"
    show emi nc05 at j11
    e "You're looking at Jenni's boobs too!"
    show emi at jr11
    e "You're a pervert! {w=1.0}You're a pervert!~"
    pr "SHUT UP!"
    show emi at j11
    "Agh, now I look like a total pervert."
    "Why is life so mean to me?"
    pr "I'm going to my room."
    show emi at j11
    e "Okay pervert."
    scene hiroki_room with wipeleft_scene
    stop music fadeout 2.0
    "When I get to my room I lock the door so that Emi doesn't come in and continue making fun of me."
    pr "What would Issei think if I told him that sometimes I stare at Jenni's breasts?"
    pr "I sure wouldn't live after that day."
    pr "And if I told Jenni, I think it wouldn't kill me, but it would make me look bad with everyone."
    pr "And Issei would end up killing me for looking at his girlfriend's breasts."
    pr "But{w}, why would it be my fault?"
    pr "It's not my fault Jenni has them so big."
    pr "Seriously, those breasts are there like a couple of melons in a greengrocer."
    pr "You can look at them, but not touch them."
    pr "Well, at least you're going to buy them."
    "What the hell am I saying?"
    pr "I really sound like a pervert."
    "{i}*sigh*{/i}"
    $ game_reference = renpy.random.choice(["Geometry Dash", "Friday Night Funkin'"])
    pr "I better start playing [game_reference] to clear my mind and not think about how bad I feel right now."
    window hide(Dissolve(.2))
    pause 5
    scene hiroki_room_afternoon with dissolveslow
    window auto
    if game_reference == "Geometry Dash":
        pr "GREAT! I finally completed that level."
    else:
        pr "GREAT! I finally completed that song."
    "Hmm..."
    "Looking up, I notice that I played for a long time."
    "..."
    pr "Shit!{nw}"
    pr "I have to do homework."
    "I quickly start looking for my notebooks to start doing homework."
    "Since it's from the computer class it's easier for me."
    window hide(Dissolve(.2))
    pause 3
    scene hiroki_room_night with dissolveslow
    play music a1 fadein 2.0
    window auto
    "When I finish doing my homework I notice that it's already night."
    pr "Gosh, was it really this late?"
    "And I remember it lasted like three hours playing [game_reference]."
    pr "Emi sure made dinner already."
    pr "What will he have cooked?"
    pause 2.0
    scene hiroki_livingroom with wipeleft_scene
    pr "Emi!"
    show emi nc12 at c11
    e "What's up?!"
    pr "Nothing, I just wanted to know what you cooked."
    e nc02 "Oh ok."
    e nc04 "I ordered pizza."
    pr "Now what happened Emi? You didn't want to cook."
    show emi dc08 at tr11
    stop music fadeout 2.0
    e "Well..."
    e "Uhh..."
    e dc11 "I didn't feel motivated enough to cook after the discussion we had in the afternoon."
    "Discussion?"
    "..."
    "Uh..."
    show emi dc08
    pr "Emi I told you not to worry about it."
    pr "Well, I guess I didn't tell you."
    pr "But I'm telling you now..."
    pr "Don't worry about it, I'm not mad at you."
    e dc06 "Really?"
    show emi nc13
    pr "Really."
    pr "Besides, it wasn't such a bad argument that you didn't want to cook."
    pr "But don't worry, I'll understand you when you don't want to."
    play music a4 fadein 2.0
    pause 2.0
    pr "And..."
    pr "Did you order dessert?"
    show emi nc05 at j11
    e "Sure!"
    show emi nc04
    pr "Shall we eat?"
    show emi nc05 at j11
    e "Yes!"
    show emi at hidetr
    hide emi
    pause 3.0
    pr "Because I love pizza."
    pr "But do not abuse."
    pr "We can't eat a lot of junk food."
    show emi nc02 at c11
    e "You're right."
    show emi nc01
    pr "Emi, do you want to see something before sleeping?"
    pr "I don't know, a movie, an anime..."
    e nc02 "Well I don't know, you're the one who proposed to see something."
    e "You decide."
    e "I like anime and movies anyway."
    show emi nc01
    pr "Okay."
    menu:
        "We will see..."
        "A movie.":
            $ persistent.selectevent = 0
        "An anime.":
            $ persistent.selectevent = 1

    if persistent.selectevent == 0:

        pr "It would be nice to see a movie."
        pr "Don't you think so?"
        e nc02 "Yes, I would like to."
        e "I've always wanted to see that movie that came out recently."
        show emi nc01
        pr "Do we see her?"
        show emi nc04 at j11
        e "Yes!"
        window hide(Dissolve(.25))
        scene black with dissolveslow2
        pause 3.0
        window auto
        scene hiroki_livingroom with dissolveslow
        pr "How good the movie was."
        show emi nc05 at c11
        e "Yes, I really liked it."
        show emi nc04
        pr "Emi, what time is it?"
        e nc02 "About 11:30 PM."
        show emi nc01
        pr "WHAT!"
        pr "I have to go to sleep, I have classes tomorrow."
        e n1c02 "But tomorrow is Saturday."
        show emi nc01
        pr "Uff..."
        pr "That's good, and I was already worrying."
        pr "Is it the custom?"
        pr "Well."
        pr "We'll still go to sleep, it's too late."
        show emi nc08 at tr11
        e "Awww..."
        pr "It doesn't matter what you say."
        pr "To sleep young lady."
        show emi dc01 at j11
        e "Hmph..."
        pr "I'm going to my room and you, go to yours."
        e dc04 "Okay."
        pr "See you tomorrow."
        e nc05 "See you tomorrow little brother."
        show emi at hidetr
        hide emi

    if persistent.selectevent == 1:

        pr "It would be nice to see an anime."
        pr "Research one named {i}Tejina-senpai{/i}."
        pr "It sounds very funny."
        e nc11 "I haven't seen that one."
        e nc05 "Let's see what."
        show emi nc04
        pr "Let's go."
        window hide(Dissolve(.25))
        scene black with dissolveslow2
        pause 3.0
        window auto
        scene hiroki_livingroom with dissolveslow
        pr "Too bad we can't finish it all in one day."
        pr "Emi, how many episodes did we see?"
        show emi nc02 at c11
        e "Like 4."
        show emi nc01
        pr "Although they don't last long, and it has 12 chapters."
        pr "Well, what can be done."
        pr "What time is it?"
        e nc02 "9:40 PM."
        show emi nc01
        pr "Well, I'm going to sleep."
        pr "I have to go to school tomorrow."
        e nc02 "To school on Saturday?"
        show emi nc01
        pr "Wow."
        pr "Well, I'll go somewhere else."
        pr "Maybe I'll call Issei or Jenni to go out."
        e nc04 "Okay."
        e nc05 "Good night little brother."
        show emi nc04
        pr "Good evening."
        pr "Go to bed early, you heard me."
        e nc02 "Don't worry."
        show emi nc01
        pr "Goodbye."
        e nc02 "Goodbye little brother."
        show emi at hidetr
        hide emi

    stop music fadeout 2.0
    scene hiroki_room_night with wipeleft_scene
    "When I get to my room I put on my pajamas and go to bed."
    window hide(Dissolve(.25))
    scene black with dissolveslow
    pause 1.0
    window auto
    "What a strange thing happened to me today."
    "What's wrong with that girl?!"
    "Though..."
    "She's very cute."
    "How does such a pretty girl spend her time locked up?"
    "I think tomorrow I should go to his house and apologize for leaving like this."
    "Maybe I'll dial Issei to tell him."
    "I better not think about it anymore."
    "Tomorrow I'll see what to do."
    window hide(dissolve)
    scene black with dissolve_scene_full
    pause 3.0

    return