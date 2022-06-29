
label ch1_en:
    
    scene black
    "..."
    play audio alarm
    "Hmm..."
    "What's happening?"
    "What time is it?"
    stop sound
    e "9:00 AM."
    pr "what?"
    scene hiroki_room
    show black zorder 500:
        ease 1.0 alpha 0.00
    show emi nc01 at superclose
    pause 1.0
    e nc02 "Little brother, get up."
    show emi nc01
    pr "Uh...."
    show emi nc04 at j11
    pr "Ahhhhhh!"
    e "Hehe."
    play music a4 fadein 2.0
    pr "What are you doing in my room so early?"
    e nc02 "Well, I just came to wake you up for breakfast."
    show emi nc01
    pr "Have you made breakfast yet?"
    e nc05 "Yes, I got up early to make breakfast, because my friends are coming to the house today."
    show emi nc04
    pr "Today?"
    e nc02 "Yes, why?"
    show emi nc01
    pr "You should have told me yesterday."
    e nc02 "Okay little brother."
    e nc05 "The next time they come I'll tell you in advance."
    show emi nc04
    pr "Okay."
    pr "I'm going out anyway."
    e nc02 "Really?"
    e nc11"Where to?"
    pr "I'll go talk to Issei or Jenni."
    e nc02 "Of what?"
    show emi nc01
    pr "Emi."
    e nc02 "Yes?"
    show emi nc01
    pr "You don't have to interrogate me."
    pr "Your friends can come if they don't cause a mess."
    e n1c03 "Don't worry, nothing will happen."
    show emi n1c15
    pr "Really?"
    show emi nc16 at tr11
    pr "And what about that time they left the kitchen a mess and...{nw=3.0}"
    show emi n1c03 at c11
    e "Please little brother...."
    e "We only left the kitchen dirty..."
    e "I don't grow up."
    show emi n1c15
    pr "Really?"
    pr "Because I don't remember it that way."
    pr "As far as I remember{nw}"
    show emi nc16 at tr11
    extend "You almost burned down the house."
    pr "And we had to call the fire department."
    show emi at j11
    e "Okay, okay."
    show emi at j11
    e "It won't happen again."
    pr "So be it."
    pr "Because you'll be in big trouble if it happens again."
    show emi at j11
    e "It won't happen again I swear."
    e "Don't worry."
    pr "Fine."
    show emi nc01
    pr "Well, let's eat."
    pr "Because I'm hungry."
    e nc05 "Me too."
    scene hiroki_livingroom with wipeleft_scene
    pause 0.24
    show emi nc01 at c11
    pr "And why are your friends coming?"
    show emi dc04 at j11
    e "Hey!"
    e "You're going to talk to Issei and Jenni and I'm not going to question you."
    show emi dc01
    pr "I'm your older brother and you have to respect me."
    pr "And I ask you because I need to know."
    show emi nc08 at tr11
    e "Oh sorry."
    e "It's just that I thought you were asking about something bad."
    show emi nc02 at c11
    e "Well..."
    e "They come to do some homework."
    show emi nc01
    pr "Perfect."
    pr "Then let's eat, because I don't want it to be done later."
    e nc05 "Okay."
    show emi nc04 at hidetr
    hide emi
    pause 1.0
    scene black with clockwiperight_scene
    pause 2.0
    scene hiroki_livingroom with clockwipeleft_scene
    show emi nc01 at c11
    pr "Thanks for the food Emi."
    e nc02 "You're welcome little brother."
    show emi nc01
    pr "Well, I'm leaving."
    e nc02 "Okay little brother."
    e "Good luck to you."
    show emi nc01
    pr "Thank you."
    pr "Goodbye."
    pr "See you later."
    e nc05 "Goodbye little brother."
    show emi nc04
    scene black with wipeleft
    pause 2.0
    play audio dooropen
    scene apartment_exterior with wipeleft
    stop music fadeout 2.0
    pr "Okay.."
    pr "I'll send a message to Issei to see if I can go to his house."
    "Since Saturday and Sunday, Jenni is not at home."
    "And that's why I won't send a message to her."
    window hide(Dissolve(.2))
    if persistent.blur_on:
        scene apartment_exterior_blur with dissolve
    nvl show dissolve
    nvlpr "Hey bro."
    nvlpr "How are you?"
    nvlpr "Are you home?"
    pause 0.25
    nvli "Hello bro, yes I'm at home."
    nvli "What's up?"
    nvli "Is something wrong?"
    pause 0.25
    nvlpr "Nothing, it's just that I wanted to chat with you or Jenni about something very strange that happened to me yesterday."
    pause 0.25
    nvli "Strange....{w=1.5}How?"
    pause 0.25
    nvlpr "I'll tell you later-{nw}"
    nvli "If you like you can come to my house, Jenni is here too."
    pause 0.25
    nvlpr "{i}You deleted this message.{/i}{nw}"
    pause 0.25
    nvlpr "Yeah okay, I'm on my way."
    pause 0.25
    nvli "Okay, we are waiting for you."
    nvl hide dissolve
    if persistent.blur_on:
        scene apartment_exterior with dissolve
    pause 1.0
    window auto
    pr "...."
    pr "I hope Issei and Jenni don't make fun of me for what happened to me yesterday."
    window hide(Dissolve(.2))
    pause 2
    scene city2 with wipeleft_scene
    "During the way, I think..."
    "How the hell am I going to explain to Issei and Jenni what happened to me?!"
    "I'm not going to tell them...."
    "{i}Yesterday a girl told me that I was her boyfriend{/i}."
    "Sounds ridiculous just thinking about it."
    "As a beautiful girl I don't even know names me as her boyfriend without me knowing her."
    "But..."
    "For what reason did he tell me that?"
    "..."
    "All the more reason I have to talk to Issei and Jenni."
    "Not because they have an answer."
    "I just want to tell you."
    "Only a few minutes go by when I arrive at Issei's house."
    window auto
    scene isseihouse with wipeleft_scene
    "It's weird actually how Issei and Jenni literally live near me."
    "The truth when I visited Issei's house for the first time, I couldn't believe that he lived only four blocks away."
    $ renpy.notify("Note: " + player + " lives in apartment 402, Jenni lives in apartment 406")
    "Instead, Jenni lives literally next door."
    "And that I know Jenni long before I met Issei and just a couple of years ago I realized that she lived in the same building as me."
    "And on the same floor."
    "Sometimes I don't understand coincidences."
    pause 0.5
    scene isseihouse_front with dissolve
    "As I approach the door I feel great anxiety..."
    "WHAT THE HELL AM I GOING TO TELL THEM!"
    "I'm already panicking just knowing if I don't explain well what happened with Yumi..."
    "Issei and Jenni will end up making fun of me and they will surely say…"
    "{i}You wanted a girlfriend so badly and here she is, although not the way you wanted{/i} or...{w=1.0}{i}You must have done something to that poor girl to make her notice a guy like you{/i}."
    "The last would be Jenni, but…"
    "*I inhale*{w=1.4} *I exhale*{nw=2.2}"
    "I calm down a bit and I dare to ring the doorbell of the house."
    play audio doorbell
    pause 2.0
    "Heavens..."
    "I'm starting to feel nervous."
    "Anyone would take this more calmly."
    "But knowing Issei and Jenni they will surely make fun of me."
    "Besides this is so weird that anyone would get nervous if they had to say that an unknown girl proclaims you as her boyfriend."
    "And that would make anyone nervous."
    play audio door2c
    "I hear the door open in front of me."
    show issei np02 at c11
    i "Hey bro, you got here pretty quick."
    show issei np01
    pr "H-Hello Issei."
    "I'm starting to feel dizzy."
    i np03 "Friend, are you alright?"
    i "You look very tired."
    pr "I..."
    "I can't even stand up anymore."
    i np04 "[player!t]?"
    "This...{w=1.5}{cps=10}is...{/cps}{nw}"
    scene isseihouse_front_blur
    show issei np04 at ins11
    show vignette1 zorder 100
    with dissolve
    "My vision gets blurry...."
    "How ridiculous I must look now."
    pause 2.0
    "Now I fall exhausted on the ground.{nw=1.0}"
    window hide(None)
    scene black
    play audio fall
    pause 1.0
    i "[player!t]!!"
    window hide(Dissolve(.2))
    pause 3
    scene issei_livingroom with eyeinslow_scene
    window auto
    pr "Hmm..."
    pr "Where am I?"
    show issei nbp02 at c11
    i "You're at my house friend."
    show issei np01
    pr "What time is it?"
    i nbp02 "10:20 AM, you haven't passed out for so long."
    show issei np01
    play music a3 fadein 3.0
    pr "Ugh..."
    pr "My head hurts."
    pr "Do you have anything for that?"
    pr "Any medicine or something?"
    i np03 "Eeehh....{w=2.0}Yes."
    i nbp07 "Jenni!"
    show issei np08
    pause 1.4
    show jenni np08 at c22
    show issei np01 at c21
    j "What's up my am-{nw}"
    show jenni np10 at j22
    j "[player!t]!!"
    show jenni nbp11 at z22
    j "What are you doing here?"
    pr "I just came to talk to you."
    show jenni np13
    show issei np04
    j "Really?"
    j np14 "Of what?"
    show jenni np13
    pr "Well...{w}I want to tell you something super strange that happened to me yesterday."
    show issei np03 at z21
    i "You're talking about what you were going to tell me on the phone."
    show issei np04
    pr "Yes..."
    pr "But first give me something for the headache, since it's killing me."
    show jenni np14 at z22
    show issei np04 at c21
    j "Sure."
    show jenni at hidetr
    hide jenni
    pause 2.0
    show jenni nbp14 at c22
    j "Here."
    show jenni nbp13 
    pr "Thank you."
    pause 1.0
    show issei nbp03 at z21
    i "What's the weird thing that happened to you?"
    show issei np04
    pr "Well, before I tell you, I'm going to ask you something..."
    show jenni nbp14 at z22
    show issei at c21
    j "And what would that be?"
    show jenni nbp13 
    pr "Don't let them laugh at me when I finish telling them."
    j nbp12 "I'll try not to laugh if it's too funny."
    j "But I don't promise anything."
    show jenni np09 at c22
    pr "Hey!"
    show issei nbp02 at z21
    i "Don't worry friend, I'll try not to laugh."
    show issei np01 at c21
    pr "Well...."
    show jenni np01
    stop music fadeout 2.0
    pr "{i}*sigh*{/i}"
    "First I calm down...."
    "*Inhale*{w=1.4} *Exhale*"
    "Okay..."
    pr "Well, you know who Akemi Yumi is, right?"
    show issei np03 at z21
    i "Yes, it's the girl who doesn't attend classes, everyone knows her."
    show issei np04
    pr "Well..."
    pr "The strange thing that happened to me was with her."
    pr "After leaving school and going home, I..."
    show jenni np14 at z22
    show issei at c21
    j "You what?"
    show jenni np13
    pr "After checking the assignment folder and reading the address I realized that...."
    show jenni np14
    j "Of what?"
    show jenni np13
    pr "Okay, but don't interrupt me."
    show jenni np06
    pr "After reviewing the folder and reading the address I realized that she..."
    pr "He lives in the same building as me."
    show jenni np13 at c22
    show issei np03 at z21
    i "Wow, really?"
    i nbp03 "According to rumours, she never leaves her house."
    i np03 "And that's probably why you haven't seen it."
    show issei np04
    pr "And he lives in the apartment below."
    i np03 "What a strange coincidence."
    show issei np04
    pr "Well..."
    pr "When I got home I rang the bell several times and no one answered so..."
    show jenni np10 at ztj22
    show issei at c21
    j "You entered a girl's house without her permission!"
    pr "Well, but no one answered so I went in to investigate."
    j nbp12 "Ah well, because I was about to beat you unconscious."
    pr "Yes, of course."
    show jenni nbp06
    pr "If they had been there..."
    pr "There was a foul smell."
    pr "Dirty dishes, spoiled food, dust everywhere and there was a running water tap in her bathroom."
    pr "Being inside her house felt like being in a cemetery because of how dark and lonely the environment was."
    pr "It was very scary."
    j np14 "And Yumi?"
    show jenni np13
    pr "That's what I'm going to do."
    pr "On entering his room.{nw}"
    show jenni np10 at ztj22
    j "You came into his room!"
    pr "Well, but I heard some cries and some voices from his room and I had to go in to see what was happening!"
    j np14 "Oh ok."
    show jenni np13
    pr "As I entered her room, I saw her."
    pr "And I said in my mind...{w=2.0}Why does such a pretty girl spend her time locked up in her house?"
    show issei np01
    show jenni np01
    pr "Although I got very nervous and the worst of all was when..."
    show issei np03 at z21
    show jenni np01 at c22
    i "Wait a minute..."
    i nbp03 "Did she tell you something?"
    show issei np04
    pr "Yes..."
    pr "That's what I was going for."
    pr "The worst of all was when I was going to try to tell him my name.... "
    pr "So she..."
    pr "She..."
    show jenni nbp05 at z22
    show issei at c21
    j "Speak at once!"
    show jenni nbp06
    pr "S-She...."
    show jenni at c22
    show issei nbp03 at z21
    i "Dude, what happened?"
    show issei np04
    pr "{size=-6}{cps=80}She told me I was her boyfriend{/cps}{/size}."
    show jenni nbp05 at z22
    show issei at c21
    j "Come on [player!t] speak louder, I couldn't hear anything you said!"
    show jenni nbp06
    pr "He told me...."
    show jenni np15 at ztj22
    show issei np09 at ztj21
    ji "YEAH IT!{nw=0.30}"
    pr "HE TOLD ME I WAS HIS BOYFRIEND!"
    show jenni np13 at c22
    show issei np04 at c21
    pr "Okey{w}...I already said it."
    ji "..."
    show jenni np14 at z22
    j "You {w}....Did {w}...say that you were her boyfriend?"
    j np13 "....."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    play music a4 fadein 2.0
    ji "HAHAHAHAHA!"
    show issei np11 at c21
    j "Like she told you you were her boyfriend!"
    j "You're so desperate for a girlfriend that...."
    show jenni at ztj22
    j "That you invent this kind of thing!"
    show jenni at ztj22
    j "HAHAHAHA!"
    show issei np10 at z21
    show jenni np09 at c22
    i "Come on bro, tell us something else{w}...."
    show issei at ztj21
    extend "more realistic!"
    show issei np11
    pr "That's why I didn't want to tell you!"
    pr "I knew they were going to end up laughing at me!"
    show issei np02 zorder 2
    i "Because what you told us is quite unreal."
    i "And if that were true."
    i np07 "If I were you, I wouldn't be here talking, I'd be having fun-{nw=0.80}"
    show jenni nbp17 zorder 1 at j11
    with truewhite
    play audio punch
    j "Hey!{nw=2.0}"
    show issei np12 zorder 2 at z21
    i "Ouch!"
    i "I'm sorry!"
    i "Hehe."
    show jenni ap02 at z22
    show issei np13 at c21
    j "Keep on with your bad taste jokes, I'll knock you out."
    show issei np12 at z21
    show jenni ap01 at c22
    i "Okay that's fine."
    show jenni n1p02 at z22
    show issei np01 at c21
    j "Returning to the theme of Yumi."
    pr "You're scary when you change from one attitude to another."
    show jenni nbp04
    j "You do what you can."
    j nbp01 "Well...."
    j n1p02 "Is this what you told us {w=1.0} true?"
    show jenni np01
    pr "Of course it's true."
    pr "I'm not going to lie about something so serious."
    show jenni nbp18 
    j "Seriously?"
    show jenni nbp20 at ztj22
    j "HA!"
    j "Don't make me laugh."
    j nbp03 "Furthermore, if that were true."
    j "Why didn't you stay with her?"
    show jenni np13
    pr "Because it caught me off guard."
    pr "Besides..."
    pr "Why am I staying with a girl I don't even know?"
    j np02 "Well, it was your chance to get a girlfriend."
    j "False, but you were still going to have a girlfriend."
    j ncp02 "Also, didn't you say she was cute?"
    show jenni nbp01
    pr "So what?"
    j np08 "Well, at least you said something about a girl without looking at the size of her breasts first."
    j np06 "Wait a minute..."
    j nbp07 "How big were her breasts?"
    show jenni np06
    pr "Why are you asking me that?!"
    j nbp07 "Because it's the first thing you see when you meet a girl."
    "She already looks like Emi."
    "Asking the wrong thing."
    show jenni nbp07 zorder 2 at superclose
    with dissolve
    j "What size?"
    show jenni nbp06
    pr "What do you care?"
    pr "Are you afraid they will compete with you?"
    show issei np06
    show jenni nbp11 zorder 2
    j "Ehh{w=1.0}.....No!"
    j nbp07 "Besides...."
    j nbp17 "You keep looking at me!"
    pr "Of course."
    pr "There is no way that when talking to you, I cover my eyes."
    j nbp16 "I don't talk that idiotic way!"
    pr "Calm down."
    pr "You're going to have a fit."
    pr "Besides, I'm not the only one looking at you."
    pr "You know that I would never look at you in a bad way for fear that Issei hit me."
    show jenni nbp21 
    show issei np10 zorder 1 at j21
    i "That's true!"
    show jenni nbp12 zorder 2 at c22
    j "Well, you're right."
    show jenni np01
    show issei np01
    pr "Okay."
    pr "Returning to the topic of Yumi."
    stop music fadeout 2.0
    pr "She telling me that I am her boyfriend."
    pr "I didn't think twice and ran out of his house."
    show issei nbp02 at z21
    i "No wonder you were so nervous you passed out."
    show issei np01
    pr "And I wanted to ask you..."
    pr "Is it a good idea to go to Yumi's house and apologize to her for leaving like this?"
    pr "It's just that if I don't, I know my mind won't leave me alone."
    pr "And if I go I'll feel weird being in that house again."
    i np03 "Well..."
    i "I think so."
    show issei np01
    pr "What do you say Jenni?"
    show jenni np02 at z22
    show issei at c21
    j "Well, I agree with Issei."
    j "It was really bad of you to leave her house like that."
    j "She must have had her reasons for telling you that..."
    j "What..."
    show jenni nbp20 at ztj22
    extend "That you were her boyfriend!"
    show jenni at ztj22
    j "HA!"
    pr "Come on Jenni!"
    pr "It doesn't work."
    pr "Don't keep laughing at me."
    j nbp08 "How do you want me not to laugh..."
    j "Yeah that sounds so illogical."
    j nbp05 "Besides, you must have done something to that poor girl to make her notice a guy like you."
    "He said it."
    show jenni nbp06
    pr "I didn't do anything to him!"
    pr "I don't even know her!"
    j nbp12 "Well, well."
    j "I'm just kidding with you."
    j "Leaving that aside."
    j ncp12 "When do you plan to go apologize to her?"
    show jenni nbp22 
    pr "I intend to go today, but...."
    j np14 "But...?"
    show jenni np13
    pr "I was wondering if you could join me."
    show issei np02 at z21
    show jenni np01 at c22
    i "Sure, why not?"
    i nbp02 "Jenni?"
    show jenni nbp02 at z22
    show issei np01 at c21
    play music a7 fadein 2.0
    j "Of course."
    j "As long as she's not some crazy freak trying to hurt me she's fine."
    show jenni np01
    pr "Don't worry, she's the opposite."
    j np02 "Well, I'll go to the bathroom for a moment."
    j "When I get back, we're going to Yumi's house."
    show jenni np01
    pr "Okay."
    show jenni at hidetr
    hide jenni
    show issei np02 at c11
    i "Okay Jenni."
    i "We are waiting for you."
    i np14 "Hmm..."
    i np02 "Hey Bro."
    show issei np01
    pr "What's wrong Issei?"
    i nbp02 "How is Yumi?"
    show issei np01
    pr "Well..."
    pr "Her hair is short and dark purple."
    pr "Purple eyes."
    pr "Very bright, by the way."
    pr "Very light colored skin."
    pr "She was wearing a blue nightgown."
    pr "And her body has its nice curves."
    i nbp02 "You literally analyzed the whole thing."
    show issei np01
    pr "Yes, although the question of what..."
    pr "How does such a pretty girl spend her time locked up in her house?"
    i nbp02 "As you described her, this Yumi sounds pretty."
    show issei np01
    pr "Although it actually seemed strange to me that..."
    pr "Although her house was neglected, she did not seem to need food."
    pr "She didn't look too fat or too thin."
    pr "You have a nice body."
    pr "Although, the largest of his body were his-{nw=0.30}"
    show issei np04 at c21
    show jenni nbp04 at j22
    j "What are you talking about?!{nw=0.5}"
    pr "Ahhhhh!"
    pr "Don't do that!"
    show jenni np13
    show issei np01
    "Good thing he interrupted me because I was about to say something I didn't mean to."
    pr "You almost gave me a heart attack!"
    show jenni np02 at z22
    j "Sorry, sorry."
    j np01 "What were they talking about?"
    pr "You're welcome."
    j np14 "Really?"
    show jenni np13
    pr "Yes, don't worry."
    j np01 "Okay."
    j np02 "Shall we go?"
    show jenni np01
    pr "Of course."
    show issei at hidetr
    show jenni at hidetr
    hide issei
    hide jenni
    scene black with wipeleft_scene
    pause 0.30
    play audio dooropen
    scene isseihouse with wiperight_scene
    pause 0.25
    show issei np01 at c21
    show jenni np01 at c22
    pause 1.0
    show jenni np02 at z22
    j "And...?"
    j ncp02 "Where is Yumi's house?"
    show jenni nbp01
    pr "I told you she lives in our building."
    j nbp09 "Yes it is true."
    j nbp08 "I forgot."
    show issei np02 at z21
    show jenni np01 at c22
    i "Well, let's start walking, because we'll be late."
    show issei np01
    pr "You're right."
    pr "Let's go."
    stop music fadeout 2.0
    scene city2 with wipeleft
    "As we walk..."
    "I'm starting to think about what to say to Yumi."
    "Heavens..."
    "Seriously{w}, what am I going to tell him?!"
    "I'm not going to just tell him...{w=1.0}{i}'Sorry for leaving your house like that, bye-bye'{/i}"
    "I must explain further."
    "..."
    "Besides asking him why he told me I was his boyfriend."
    "But{w}...I don't know what to tell him."
    "Could it be that... {w} Shall I ask Issei I Jenni?"
    "But..."
    "Which one of them shall I ask."
    "Hmm..."
    "Although for this I should have an answer."
    "But there's nothing wrong with getting a little help."
    "TRUE?"
    menu:
        "I'll ask..."
        "Issei.":
            "I better ask Issei."
            pr "Issei!"
            pr "Come closer for a moment."
            show issei np01 at c11
            play music a7 fadein 2.0
            i "What's up bro?"
            pr "I don't know what I should say to Yumi to apologize."
            i np03 "Well, I think you should tell him you're sorry and that's it."
            i nbp03 "There is no special way to apologize."
            i np03 "But..."
            i nbp02 "Yes the problem is that you want to apologize for leaving her house like that after her almost 'confession'."
            i np02 "Then tell him you didn't know how to react to his 'confession'."
            show issei np01
            pr "Makes sense."
            pr "But the doubt remains that if I don't know her..."
            pr "Why did you tell me I was your boyfriend?"
            i np04 "Well..."
            i np03 "I can't answer that."
            i nbp03 "Since you don't even know why."
            show issei np01
            pr "You're right."
            pr "Thank you Issei."
            i np02 "You're welcome bro."
            show issei np01
            pause 0.4
            show issei at hidetr
            hide issei
        "Jenni.":
            "I better ask Jenni."
            "Though I hope you don't call me 'idiot' for not figuring this out on my own."
            pr "Jenni!"
            pr "Come."
            pr "Come a little closer."
            play music a7 fadein 2.0
            show jenni np01 at c11
            j "What's wrong [player!t]?"
            pr "I don't know what I should say to Yumi to apologize."
            j np06 "The truth is I don't see why you mortify yourself so much."
            j np12 "Apologizing shouldn't be difficult."
            j nbp02 "If you do it in a good way, your apology will be well received."
            show jenni np01
            pr "You're right."
            pr "But I still have the doubt that..."
            j np14 "Of what?"
            show jenni np13
            pr "De, why should I apologize if she literally made fun of me?"
            j nbp06 "First..."
            j "She didn't make fun of you."
            j "No one in life actually tells a person {i}'You are my boyfriend'{/i}."
            j "Without even knowing him."
            j nbp07 "I still think you did something to him to make him tell you that."
            "He said it again."
            pr "That I didn't do anything!!"
            pr "I barely knew his name."
            j nbp06 "Yeah, whatever."
            j nbp02 "If you want to apologize for leaving her house without saying goodbye…"
            j "Then just say you're sorry and that's it."
            j "It's not very complicated."
            show jenni np01
            pr "Okay..."
            pr "Thank you Jenni."
            j np02 "You're welcome idiot."
            show jenni nbp20 at ztj11
            j "HA!"
            show jenni at hidetr
            hide jenni
            pr "Hey!"
    pause 2.0
    pr "Well..."
    stop music fadeout 2.0
    "The only thing I need now is to stop being nervous."
    "Asking for an apology is not something super complicated."
    "The problem is how Yumi is going to react."
    "Well, I'll have to prepare myself for the reaction I take."
    pause 2.0
    "A few more steps and we reach the building."
    scene apartment_exterior with wipeleft_scene
    show issei np01 at c21
    show jenni np01 at c22
    pause 1.0
    pr "Well, I'll go to Yumi's house."
    show issei np06
    show jenni np13
    pr "You guys go up to my house and wait for me."
    show jenni np14 at z22
    j "Do you want us to stay at your house?"
    j ap02 "But we also want to meet Yumi."
    j "Besides, you said to come with you."
    show jenni ap01
    pr "But I prefer to go alone before they make fun of me."
    j nbp11 "Too bad."
    show issei np01
    j nbp01 "Well...."
    j nbp02 "You know it's really just the students in our class who know what Yumi looks like."
    play music a1 fadein 2.0
    j ap03 "But it doesn't matter if you don't want us to meet her yet."
    show issei np01
    j "We'll meet her very soon anyway..."
    j ap06 "When they formalize their relationship."
    show jenni nbp20 at ztj22
    j "HA!"
    pr "Hey!"
    show jenni np01
    pr "We will not formalize anything."
    j np12 "Yes or no."
    j np02 "I would take this opportunity if I were you."
    j "So that you at least finish high school with at least one relationship."
    show jenni np01 at c22
    show issei np02 at z21
    i "Jenni is right."
    i "You should try to get close to him."
    i np02 "From what you told me, I can imagine how pretty Yumi must be."
    i np15 "So take the opportunity."
    pr "You two are pretty crazy."
    show issei np01
    pr "I better go before they spread their madness to me."
    pr "Goodbye."
    show issei np02
    show jenni np02
    ji "Goodbye [player!t]."
    stop music fadeout 2.0
    scene apartment_exterior with wipeleft_scene
    "Issei and Jenni, they stayed downstairs for a few minutes."
    "While I went up to Yumi's apartment."
    "I hope this time I don't have to put up with such a scary environment."
    window hide(Dissolve(.2))
    pause 1.0
    window auto
    "Just a few more steps and I'm standing in front of your door."
    "Okay..."
    "I ring the bell just in case."
    pause 0.5
    play audio doorbell
    pause 2.0
    "There's no answer."
    "I ring the bell again."
    play audio doorbell
    pause 2.0
    "Nothing new."
    stop audio fadeout 0.5
    "I'm going to have to go back inside."
    play audio doorcreak3
    scene black with wipeleft_scene
    $ renpy.music.set_volume(0.15, channel="music")
    play music a5 loop fadein 2.0
    scene yumi_livingroom_dark with dissolve
    "The house is still the same."
    "This time I feel even more nervous."
    "I'm sure it's because I have to apologize to her."
    pause 1.0
    scene black with dissolve
    "I'll go straight to your room because I don't have anything else to do here."
    pause 1.0
    scene yumi_hall
    show black zorder 500:
        ease 10 alpha 0.5
    pause 1
    "I feel strange again inside this house."
    "Being here feels very strange."
    "I'm going to sneak up to the door."
    scene yumi_door
    show black zorder 500:
        ease 4 alpha 0.5
    with dissolve
    "This time I'll try to get closer to hear what's going on in there."
    scene yumi_room_door_1
    show black zorder 500:
        ease 4 alpha 0.5
    show vignette1 zorder 100
    with dissolve
    "As I get closer, I hear a cry."
    play audio yumi_cry
    pause 2.0
    "I imagine it must be Yumi who is crying."
    "I'm going to open the door carefully."
    play audio doorcreak4
    scene yumi_room_door_2
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with dissolve
    "Heavens!"
    "I almost had a heart attack."
    "She's sitting there."
    "What is he doing?"
    pause 1.4
    y "because?"
    pause .30
    y "Why doesn't anyone love me?"
    pause .30
    y "Am I not a good girl?"
    y "Why is life so mean to me?"
    y "Why do I have to put up with being in a world where no one loves me?"
    y "{i}*sigh*{/i}"
    y "Sometimes I wish I could feel a little happiness like everyone else."
    y "I wish these thoughts didn't haunt me every day."
    pause 1.0
    stop music fadeout 2.0
    "Heavens..."
    "Yumi..."
    $ renpy.music.set_volume(1.0, channel="music")
    play music a9 fadein 2.0
    "Yumi has depression?"
    "It makes me a little sad to know that..."
    "Such a cute girl…"
    "And with depression."
    "I'm not saying that any pretty girl can't develop depression."
    "But it makes me a little sad…"
    "Heavens…"
    y "Even my imagination plays tricks on me."
    y "That boy from yesterday, disappeared as he appeared."
    y "Super fast."
    y "To think that I had at least imagined someone who loved me."
    y "Even if it's a little."
    "Does she think I'm a figment of her imagination?"
    "That hurts..."
    "I feel as if a hundred knives were plunged into my heart."
    "Yumi is so alone to believe in that kind of thing."
    "Well this is not the time to think about that…"
    "Poor Yumi..."
    "I imagine how he must be suffering every day."
    "Well, actually I don't know how depression works."
    "What I can imagine is that the brain of someone with depression makes them think that they are worthless."
    "I don't know if that's true."
    "Although there are pills to counteract depression."
    "But I still think it's something to be taken seriously."
    "Though it pains me to think about the fact that Yumi thinks everyone around her doesn't appreciate her."
    "Perhaps I can investigate how a person with depression is treated."
    "If I don't forget, of course."
    "I'm not saying that people with depression should be treated like they're crazy."
    "I'm already repeating everything I say again."
    "{i}*sigh*{/i}"
    "I'm going to pluck up my courage and help Yumi out of this."
    "I'll try to close the door carefully-{nw}"
    stop music fadeout 0.2
    play audio doorcreak3
    "Gosh, I made too much noise!"
    "I hope there is no listening-{nw}"
    scene yumi_room_door_3
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with dissolve
    window hide(Dissolve(.2))
    pause 1.0
    window auto
    pr "Uh...."
    y "Hmmm...."
    y "you....?"
    pr "H-Hello."
    "Heavens."
    "I got in trouble."
    y "Vol...{w=1.0}vol..."
    window hide(Dissolve(.2))
    scene hiroki_surprise:
        zoom 1.30
        xoffset -10
        pause 3.30
        linear 30.000 zoom 1.0 xoffset 0
    with flash
    window auto
    play music a2 fadein 4.0
    y "You're back!"
    y "I thought you'd never come back."
    y "I'm so happy."
    y "Yeeey!"
    "What the hell is going on?"
    "This..."
    "This feels..."
    "A little good..."
    "And at the same time very uncomfortable."
    "I do want to help Yumi..."
    "I'll have to play along that I'm her imaginary boyfriend."
    "Even though it makes me uncomfortable."
    scene yumi_door
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with dissolve
    pause 0.3
    show yumi fsl05 at c11
    y "I thought you weren't coming back, honey."
    y fsl06 "I knew my imagination hadn't let me down."
    "That sounds very sad."
    "It hurts me so much to think that she believes I don't exist."
    "And it makes me uncomfortable at the same time."
    show yumi fsl02 at jr11
    play music a3 fadeout 2.0
    y "And what do you want to do today?"
    show yumi fsl01
    pr "E-Ehhh...."
    "Gosh, I don't know what to answer..."
    "I've never really been in a relationship in my life."
    "How should I answer that?"
    "..."
    "I'll see if this works..."
    pr "Ehh, I don't know..."
    pr "W-We can do whatever you want..."
    show yumi fsl04 at c11
    y "Hmm...."
    y fsl02 "Would you mind having some coffee?"
    show yumi fsl01
    pr "E-Ehh, sure, why not?"
    "I have to calm down a bit."
    "This is actually very difficult."
    "I feel like I'm in a cliche scene from some anime."
    show yumi fsl05 at j11
    y "Come on!"
    show yumi at rhide
    hide yumi
    "Well{w=1.5}, who cares..."
    stop music fadeout 2.0
    "I follow Yumi to the living room."
    pause 1.0
    scene yumi_livingroom_dark
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with wipeleft_scene
    pause 0.20
    show yumi fsl02 at c11
    y "Sorry if my house is a little dark, I'll go open the curtains."
    show yumi fsl01 at lhide
    hide yumi
    pause 0.30
    scene yumi_livingroom with wiperight
    "That!"
    "What a difference."
    "It's weird how her house looks so dark when it's dark."
    show yumi fsl05 at l11
    pause 0.20
    y "better?"
    show yumi fsl06
    pr "Yes."
    "Yumi's house doesn't look as bad as I had imagined."
    show yumi fsl02 at j11
    y "And what kind of coffee do you like, honey?"
    show yumi fsl01
    play music a7 fadein 2.0
    pr "Huh?"
    pr "Oh."
    pr "I like coffee with milk."
    show yumi fsl02
    y "Would you like to try others?"
    show yumi fsl01
    pr "It's never too late for new experiences."
    pr "But in this case, new cafes."
    show yumi fsl05 at j11
    y "HAHA!"
    y "You're so funny."
    y fsl01 "Well, I can offer you…"
    y fslb02 "Espresso, latte…"
    show yumi fsl06 at j11
    y "The one you like."
    y fslb02 "Iced coffee, cappuccino, regular coffee…"
    show yumi fsl05 at j11
    y "Hehe."
    y fsl02 "And I think those are the only ones I can offer you."
    show yumi fsl01
    pr "Mmm...."
    pr "Well..."
    "I think answering would be the most appropriate thing to do."
    menu:
        pr "I would like a..."
        "Regular coffee.":
            pr "I would like a regular coffee."
            pr "I prefer the everyday."
        "Coffee express.":
            pr "I would like an espresso."
            pr "I like the foam it has."
        "Coffee with milk.":
            pr "I would like a coffee with milk."
            pr "It is good to eat with bread."
        "Iced coffee.":
            pr "I would like an iced coffee."
            pr "They say it's very good for these hot days."
        "Cappuccino.":
            pr "I would like a cappuccino."
            pr "It would be the first time I tried it."
    
    y fsl05 "I'm preparing it right now."
    show yumi fsl06 at hidetr
    hide yumi
    pr "Okay, I'll wait here."
    "I sneak around the room and see that it's a bit dirty."
    "I can also see cups of instant noodles and some paper on the floor."
    "Well it was not to be expected since she has her house neglected."
    "She is very pretty and a good person."
    "How did his depression develop?"
    "Or...{w=2.0}Is it Bipolar?"
    "Well, later I research on the internet how people can develop depression or bipolarity."
    "Even if it doesn't end up being of any use, because I'm not a psychologist."
    "And how did Issei say{w=1.0} and well{w=2.0} also Jenni..."
    "I'm going to try to get closer to her."
    "Even if it doesn't end up in a relationship."
    "It would be nice to end up being her real boyfriend."
    "Since this pretending to be the imaginary boyfriend thing won't count, for the record."
    pause 1.0
    show yumi fsl01 at c11
    "A while later Yumi comes back with our coffees."
    "She made herself a latte."
    show yumi fsl05 at j11
    y "Here, honey."
    show yumi fsl06
    "I take the cup of coffee from your hand."
    pr "T-Thank you."
    "Let's go and sit at the dining room table."
    "She sits across from me."
    scene ycobg
    show yco a1 zorder 1
    show ycodesk1 zorder 10
    show ycolight zorder 100
    with Dissolve(.3)
    pause 0.50
    yc "And....?"
    yc a2 "What's your name?"
    yc "Because I've been saying 'honey' to you without knowing it."
    yc a5 "Hehe."
    yc a6 "I still can't figure it out."
    yc "Although you must already have one, right?"
    show yco a5 zorder 1 with dissolve
    "Imagination doesn't work that way, Yumi."
    "I really don't see why you haven't realized that I am a person of flesh and blood."
    "Although it's better that you don't realize it because if you do, the first thing you'll do is call the police..."
    "And I'll be arrested for trespassing."
    "And I really don't want to be put in jail."
    if not player == _("Hiroki"):
        pr "My name is [player!t]."
    if player == _("Hiroki"):
        pr "My name is Maki [player!t]."
    yc a6 "Nice [player!t]."
    yc "My name is Akemi Yumi."
    yc a5 "Hehe."
    "I already know that."
    yc a1 "Y.....{nw=2}"
    show yco b1 zorder 1
    hide ycodesk1
    show ycodesk2 zorder 2
    with Dissolve(.2)
    "She takes a sip of her coffee before continuing her sentence."
    hide ycodesk2
    show ycodesk1 zorder 2
    show yco a2 zorder 1
    with Dissolve(.2)
    yc "What do you normally do?"
    show yco a1
    pr "How so?"
    yc a17 "What, what do you do in your day?"
    yc a2 "How's it going?"
    yc "What are you doing?"
    show yco a1
    pr "Oh ok."
    pr "When it's weekdays..."
    pr "I go to school, I talk to my friends..."
    pr "And when I return home, I start to do my homework."
    pr "Yes, there is."
    if game_reference == "Geometry Dash":
        pr "And then I start playing Geometry Dash."
    else:
        pr "And then I start playing Friday Night Funkin'."
    yc a3 "[game_reference]?"
    yc a18 "What is that?"
    show yco a19
    pr "Ah, it's my favorite video game."
    pr "Maybe you don't know him."
    show yco b1 zorder 1
    hide ycodesk1
    show ycodesk2 zorder 2
    with Dissolve(.2)
    "She takes another sip of her coffee."
    hide ycodesk2
    show ycodesk1 zorder 2
    show yco a2 zorder 1
    with Dissolve(.2)
    yc "What grade are you in?"
    show yco a1
    pr "Huh?"
    yc a17 "What year do you go to school?"
    pr "Ahhh..."
    pr "In the tenth grade."
    yc a6 "How curious, me too.."
    yc a5 "Hehe."
    yc a6 "How well I imagined you."
    yc "You're the boyfriend any girl wants to have."
    "Yumi..."
    "That's not how imagination works."
    "Honestly, it really hurts me when she says I'm a figment of her imagination."
    "And as I said, this makes me uncomfortable."
    "..."
    "My coffee has been a while since Yumi gave it to me."
    "I'd better have some so I don't be rude."
    pause 1.0
    pr "Yumi?"
    yc a2 "What's up, honey?"
    show yco a1
    pr "Can I ask you a question?"
    yc a2 "Sure, ask."
    show yco a1
    "Hmmm..."
    "I must think I should ask him."
    "Because if I don't watch my words I can make her angry."
    menu:
        "....?"
        "Why do you wear such a transparent nightgown?":
            $ persistent.yumquestions = 0
        "Why is your house so dirty?":
            $ persistent.yumquestions = 1
        "Why are you locked up?":
            $ persistent.yumquestions = 2
        "Why do you call me 'honey'?":
            $ persistent.yumquestions = 3
        "Because you are alone?":
            $ persistent.yumquestions = 4

    if persistent.yumiquestions == 0:
        "This question is a bit weird."
        "Since I'm just barely noticing that she's wearing a semi-sheer nightgown."
        "He must be very old or he must be very battered."
        "I can see them!"
        "I hope it doesn't start circulating blood in the wrong place."
        pr "Why do you wear such a transparent nightgown?"
        yc a2 "Well, I just don't like to wear a bra a lot."
        show yco a1
        pr "That's not the question."
        yc a2 "Well I like to be dressed like this."
        yc "It's cooler."
        yc a21 "Have you been looking at me?"
        yc a6 "Oops, you pervert."
        yc a5 "Hehe."
        pr "You know that if you receive a guest you can't go around dressed like that."
        yc a2 "It's just that I don't have clean clothes."
        yc "Besides if I wear these clothes I am not required to wear a bra."
        yc "Since it's too tight."
        show yco a1
        "There are two big reasons for that."
        pr "B-but..."
        pr "I can see your...{nw=0.40}"
        yc a2 "Breasts?{w=2.0} Nipples?"
        yc "There's nothing wrong if you look at me."
        yc a6 "You are my boyfriend after all."
        show yco a5
        "Nope."
        "I'm not."
        "Although in reality this opportunity to see a pair of big breasts is not going to be repeated."
        "What am I saying?"
        "I sound like quite the pervert."
        "Gosh, being with Yumi makes me think things I shouldn't."
        show yco a1 with Dissolve(.2)

    if persistent.yumquestions == 1:
        "This question should be a bit easy to answer."
        pr "Why is your house so dirty?"
        yc a2 "It's just that I don't like to clean."
        yc a22 "I'm lazy."
        show yco a23
        pr "Cleaning doesn't have to be boring."
        show yco a1
        pr "You can put some of the music you like and the atmosphere can be better."
        pr "And in the end you will see that by cleaning it it will look better."
        yc a2 "The truth is I don't listen to music."
        yc "But I'll think about it."
        show yco a1 with Dissolve(.2)

    if persistent.yumquestions == 2:
        "This question is a bit personal."
        "I don't know how he's going to take it."
        pr "Why are you locked up?"
        yc a19 "Hmm...."
        yc a24 "It's just that I don't like people."
        yc a25 "I get nervous when there are many people around me."
        yc a6 "I think I'm personiphobic."
        yc a5 "Hehe."
        "I don't think that's what other people call the phobia."
        "Well, I don't know what it's called either."
        "..."
        "Maybe I'll google it later."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 3:

        "I think this question would be weirder for Yumi than for me."
        pr "Why do you call me 'honey'?"
        yc a2 "Well, a girlfriend should say nice things to her boyfriend."
        yc "One of them is to say: 'honey', 'my love', 'sweetheart', 'my love', 'my prince'."
        yc a27 "Why...?"
        yc a26 "Does it bother you?"
        show yco a27
        pr "E-Ehhhhh..."
        pr "N-No."
        pr "It's just that I have to get used to it."
        yc a5 "Okay."
        "The truth bothers me a bit."
        "But at the same time it makes me feel good."
        "I can get used to that."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 4:

        "This question must be very strong."
        pr "Why are you alone?"
        yc a19 "Hmm..."
        stop music fadeout 2.0
        yc a27 "Well...."
        yc a26 "It is that..."
        pr "You don't have to tell me yes-{nw}"
        play music a9 fadein 2.0
        yc a28 "I had to move away from my family for about three years."
        yc a29 "I didn't want to be a burden to them anymore."
        yc a27 "I.."
        yc a26 "Here...."
        yc a30 "I have depression."
        "I didn't think she would say it just like that."
        "Because a lot of people with depression don't feel like it's okay to tell someone they have it."
        yc a26 "I was diagnosed when I was eight years old."
        yc "Back then nothing motivated me."
        yc a27 "Nothing amused me."
        yc a26 "I didn't like making friends anymore."
        yc a29 "My parents lived very sad because of me."
        yc "They couldn't have fun anymore."
        yc "Because they had to keep an eye on me."
        yc a27 "From....{w}"
        extend a26 "That he didn't do something crazy."
        yc a29 "That's why when I turned fourteen I came to live here."
        yc "And since then I live with one of my aunts."
        "This is very sad."
        "Yumi felt like a burden."
        "I hold back tears so I don't look pathetic."
        "Since I'm very sensitive to these situations."
        yc a27 "I don't like to make people feel sorry for me."
        yc a26 "But one day my aunt took me to therapy..."
        yc a31 "After several sessions..."
        yc "I started to get better and I was encouraged to go back to school."
        yc a27 "But..."
        yc a32 "It was horrible."
        yc "All my classmates treated me like a crazy person."
        yc a33 "They mocked, they laughed..."
        yc a27 "And...."
        yc a26 "No one wanted me."
        yc a28 "The boys in my class just harassed me."
        yc a26 "One day, one tried to outdo me."
        yc "And from that day I stopped attending that school."
        yc a27 "Until my aunt re-enrolled me in another school."
        yc a26 "This was different…"
        yc a31 "Everyone treated me well."
        yc "They greeted me."
        yc a27 "Until one day I realized that nobody wanted to be my friend."
        yc "I was the prettiest girl in the room."
        yc "All my classmates envied me."
        yc a26 "My classmates did not approach me for fear of being rejected."
        yc "It was like I was on an unreachable podium."
        yc a26 "And my hopes of being accepted are gone."
        yc a29 "Slowly stop going to school."
        yc a26 "I didn't want to be seen as the girl no one can get close to."
        yc "And little by little I stopped being remembered at school."
        yc a31 "I received visitors very often."
        yc a26 "But then they began to do less constants."
        yc a27 "Until nobody visited me."
        yc a34 "But…"
        yc a8 "Now I have you."
        yc a35 "You will be the sun that shines on my rain clouds and allows me to see the way."
        yc a8 "I hope you either leave me or push me aside."
        "Gosh, Yumi has suffered so much."
        "I feel a little bad for her."
        "How can someone put up with so much?"
        "I hold back tears."
        "Heavens..."
        stop music fadeout 2.0
        yc a6 "Let's put sadness aside."
        yc a2 "Better have your coffee."
        yc "That you almost didn't take it."
        show yco a1
        pr "Oh right, my coffee."
        pause 2.0
            
    "We were quiet for a while and just had our coffees."
    window auto
    stop music fadeout 2.0
    pause 3.0
    scene yumi_livingroom with wipeleft_scene
    "After I've had my coffee I look at the time and realize I've been here for over an hour."
    "Heavens!"
    "Issei and Jenni are going to kill me!"
    pr "Yumi?"
    show yumi fsl01 at c11
    y "What's up, honey?"
    pr "W-What..."
    pr "I-I have to go."
    show yumi fsl07 at tr11
    y "Aww.."
    y fsl08 "So soon?"
    show yumi fsl07
    pr "Yes, I have to go."
    pr "It's just that I forgot that I had to do something at home and I didn't do it."
    y fsl08 "Aww..."
    show yumi fsl01 at j11
    y "Well, I'll see you later."
    pr "Thank you for understanding."
    pr "See you later."
    y fsl05 "Goodbye darling."
    scene black with wipeleft_scene
    pause 1.0
    play audio dooropen
    scene apartment_exterior with wiperight_scene
    "I kept Issei and Jenni waiting too long."
    "They're going to kill me!"
    "Heavens..."
    "..."
    "Though..."
    "Talking with Yumi wasn't that bad."
    "It made me..."
    "Feel good..."
    "Can I just say that it made me feel good?"
    "..."
    "I do not know."
    "Okay..."
    "What are Issei and Jenni doing?"
    "S-Surely they must be planning how they're going to annoy me."
    pause 2.0
    scene apartment_exterior with wipeleft_scene
    "I don't understand how time flies so fast."
    "Well, I guess they say time goes by quickly when you're doing something you enjoy."
    "But...."
    "Did you enjoy being with Yumi?"
    "..."
    "I think so."
    "Hanging out with Yumi if I liked it."
    "Okay..."
    "I better not waste any more time and go into my house."
    play audio dooropen
    scene hiroki_livingroom with wiperight_scene
    pause 0.20
    show issei nbp03 at c11
    i "Bro, what happened to you that took you so long?"
    show issei np04 at c21
    show jenni ap02 at c22
    j "Yeah, why did you take so long?"
    show jenni at z22
    j "We've been waiting for you for over an hour."
    show jenni ap01 at c32
    show issei at c31
    show emi n1c17 at c33
    e "YES!"
    show emi at z33
    e "WHAT DID YOU DO?!"
    play music a1 fadein 2.0
    pr "Nothing."
    show emi dc03
    pr "I did nothing wrong."
    show emi dc04 at ztj33
    e "So, why did you take so long?!"
    show emi dc03
    pr "Because I was chatting and having coffee with Yumi."
    e nc14 "Yumi?"
    e n1c09 "Who is Yumi?"
    show emi nc14 at c33
    show jenni np12 at z32
    show issei np01
    j "Oohhh."
    j "So you already formalized your relationship with Yumi."
    j "I imagine what you did in that hour you were at his house."
    show jenni nbp20 at ztj11
    j "HA!"
    pr "Hey!"
    show jenni np01
    pr "We did nothing wrong."
    pr "We were just talking and having coffee."
    pr "Not that he was a pervert who wants to flirt with every girl who comes in front of him."
    show issei np07
    show jenni np18
    show emi n1c18 
    al "Yes you are a pervert!"
    show issei np01
    show jenni np01
    show emi nc01
    pr "Well, now!"
    pr "I am not a sexual predator."
    pr "We were just talking and having coffee."
    show jenni nbp11 at z32
    j "Too bad."
    j "I lost the bet."
    show jenni nbp01
    e nc18 "Well Jenni, it's your turn to pay."
    show emi nc20 
    pr "Wait…"
    pr "Did they bet?!"
    show jenni at c32
    show emi nc02 at z33
    e "Yes."
    e "But it wasn't bad at all."
    e n3c02 "I bet you didn't do anything sexual with Yumi."
    e "And Jenni bet you would end up taking her to bed."
    show emi nc01
    show jenni nbp23 at j32
    pr "Jenni!"
    show emi at c33
    show jenni nbp11 at z32
    j "Sorry, sorry."
    j np08 "It's just that we were so bored that we decided to make this bet."
    j nbp24 "Which I lost."
    show jenni nbp23 
    pr "It's just that I'm not upset about the bet."
    j np14 "No?"
    show jenni np13
    pr "Well{w=2.0}, a little."
    pr "I'm upset that they're teaching Emi bad things."
    show emi n1c05 at z33
    show jenni at c32
    e "Please little brother."
    e "I'm not a little girl."
    show emi nc20 
    pr "Yes you are."
    pr "You are 13 years old."
    show emi ac01 at ztj33
    e "That I'm not a little girl!"
    show emi at ztj33
    e "I'm too old to hear this kind of stuff!"
    show emi dc01
    pr "No."
    pr "You are not."
    e dc06 "But I want to hear what they are going to talk about."
    show emi dc08
    pr "No."
    pr "You know I told you that listening to other people's conversations is rude."
    pr "So to your room."
    e dc12 "But..."
    show emi dc13
    pr "No buts."
    pr "Those fake tears won't convince me."
    pr "To your room."
    show emi dc01 at ztj33
    e "Hmph..."
    show emi ac01 at ztj33
    e "I hate you."
    pr "Yes, me too."
    pr "But to your room."
    show emi dc01 at ztj33
    e "Hmph..."
    show emi at hidetr
    hide emi
    show issei np01 at c21
    show jenni np01 at c22
    pr "No tantrums!"
    show issei nbp02 at z21
    i "Is Emi always like this?"
    show issei np01
    pr "Yes, but I still love her very much."
    pr "Although sometimes she behaves like a little girl."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    e "I'M NOT A LITTLE GIRL!"
    pr "Up there did you hear me?"
    pr "What a super ear."
    pr "Hehe."
    show jenni np01
    show issei np01
    pause 2.0
    show jenni nbp02 at z22
    show issei at c21
    j "And...?"
    j ncp02 "How did it go with Yumi?"
    show jenni nbp01
    pr "Fine."
    j ap03 "Don't tell me just 'fine'."
    j "You had to do something besides drink coffee to last that long in his house."
    show jenni nbp22 
    pr "I did nothing wrong."
    pr "We just talked and had coffee."
    pr "That's all."
    j np14 "Seriously that was it."
    show jenni np13
    pr "I'm telling you yes."
    show issei np02 at z21
    show jenni at c22
    i "Bro, I don't think you just did that."
    pr "We didn't do anything sexual!"
    show issei np04
    show jenni np01
    pr "Yes that's what they wanted to hear."
    i np12 "Well, if we wanted to know that."
    i np02 "So what did you do besides drink coffee?"
    show issei np01
    pr "Speak and nothing else."
    i np03 "Really?"
    i nbp03 "So it must have been really boring being there with Yumi."
    show issei np01
    pr "It wasn't boring."
    pr "I really enjoyed talking with her."
    i nbp03 "And you apologized?"
    show issei np04
    show jenni np13
    stop music fadeout 2.0
    pr "Ehh..."
    pr "No."
    show issei np01 at c21
    show jenni np14 at z22
    j "But that's why you went to Yumi's house."
    show jenni np13
    pr "Yes, but...."
    j nbp07 "But...?"
    show jenni nbp06
    pr "She was so happy to see me that I didn't even touch that subject."
    pr "The one about me running from her house ignoring her."
    j np14 "And why is that?"
    show jenni np13
    show issei np04
    pr "It's just that I found out something very delicate."
    j nbp14 "What's so delicate?"
    show jenni nbp13
    pr "Well...."
    pr "I really shouldn't tell anyone this."
    pr "..."
    pr "Yumi...."
    j nbp14 "Yumi what..?"
    show jenni nbp13
    pr "Yumi has depression."
    j nbp14 "What?"
    j np14 "So it is very delicate."
    j n1p14 "How did you know?"
    show jenni np13
    pr "She confessed it to me."
    j np14 "Just like that?"
    show jenni np13
    pr "Yes."
    pr "I was very surprised."
    if persistent.yumiquestions == 4:
        pr "I could barely hold back the tears with everything he told me about how his life was a couple of years ago."
        pr "The truth made me feel very sad."
    else:
        pr "And it made me very sad."
    pr "Besides, she lives alone."
    pr "And the worst thing was that she said...."
    show issei nbp03 at z21
    show jenni at c22
    i "What did he tell you?"
    show issei np04
    pr "That no one loved her."
    pr "What if she wasn't a good girl."
    pr "And what..."
    show issei nbp03 at z21
    show issei np04
    e "what?"
    pr "He told me that I was a product of his imagination."
    pr "Created so that she would not feel alone."
    pr "And that when I ran away she said that even her imagination had abandoned her too."
    pr "But when he saw me he jumped for joy."
    show issei np03
    i "Did he really tell you that you were a figment of his imagination?"
    show issei np04
    i "....."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    play music a7 fadein 2.0
    ji "HAHAHA!"
    i "Did he really tell you that you were a product{nw}"
    show issei at ztj21
    extend "of your imagination?!"
    show issei at ztj21
    i "HA!"
    pr "Come on Issei!"
    pr "Jenni!"
    pr "That was true."
    show issei np16
    show jenni np25
    stop music fadeout 2.0
    pr "I'm not lying about that."
    pr "This is serious."
    show jenni nbp26 at z22
    show issei at c21
    j "Well yes, you're right."
    j "It made us laugh that you said that."
    j "We weren't laughing at Yumi."
    j "I'm sorry."
    pr "Well..."
    show issei np04
    j np14 "So.."
    j "She must have a very high depression."
    j nbp26 "I don't know how to classify depression."
    pause 1.0
    show jenni nbp13 
    pr "Continuous..."
    pr "What made me very sad was knowing that Yumi thinks she is alone."
    pr "Or that no one loves her."
    pr "So I told myself..."
    pr "{i}If I want to help Yumi, I'll have to play along that I'm her imaginary boyfriend.{/i}"
    pr "To support her in whatever she wants."
    pr "And so I will do."
    pr "Although it bothers me a lot."
    play music a7 fadein 2.0
    show issei np01
    show jenni np01
    pr "I'm going to make Yumi believe in the people around her again."
    pr "Make her feel dear."
    pr "And above all that she no longer believes that she is alone."
    show issei np02 at z21
    show jenni at c22
    i "That would be very nice of you."
    i "That's how you talk bro."
    show issei np01 at c21
    show jenni nbp02 at z22
    j "And here I thought you were a pervert who only thinks of himself."
    j "That's good."
    show jenni np01
    pr "And you are going to help me."
    show jenni np10 at ztj22
    j "WHAT!"
    j "Do you want us to help you?!"
    j np14 "And what would you need from us?"
    show jenni np13
    pr "Well..."
    pr "I would like your help on how to treat your partner."
    pr "Because if I'm going to help Yumi I have to know that."
    j np11 "And why do you ask us that?"
    j "We wouldn't know how to answer you."
    show jenni np13
    pr "Jenni don't act like you don't know."
    pr "Of course you should know."
    pr "You and Issei have been dating for a few years."
    pr "They must already know that sort of thing."
    pr "Or are you going to tell me that you conquered Issei only with your {i}'charms'{/i}"
    show jenni nbp17 at ztj22
    show issei np10 at j21
    j "Hey!"
    show jenni nbp06
    show issei at j21
    i "HA!"
    i "You're right [player!t]."
    show issei zorder 2 at j21
    i "HA!"
    show jenni nbp17 zorder 1 at j11
    with truewhite
    play audio punch
    j "Hey!{nw=0.80}"
    show issei np12 zorder 2 at z21
    i "Ouch!"
    show issei np12 zorder 2 at ztj21
    i "Sorry! Sorry!"
    i "Hehe."
    show jenni nbp12 zorder 2 at z22
    show issei np01 zorder 1 at c21
    j "Well, what should we do?"
    show jenni np01
    pr "I don't know..."
    pr "How should I talk to a girl?"
    pr "Because if I'm going to pretend I'm Yumi's boyfriend, I have to know how to talk to a girl."
    j nbp21 "Hmm...."
    play music a4 fadeout 3.0
    j nbp12 "Well, par-{nw}"
    show issei np07 at z11
    show jenni np10 at c44
    i "I can easily answer that for you, bro."
    show jenni np17
    i ncp07 "To talk to a girl you must be persevering and intelligent."
    i np07 "Why?"
    i ncp07 "Because many girls are like vipers."
    i "They only want you for the money and your body."
    i "And they will always be controlling you, who do you talk to and stuff."
    show jenni nbp15 at z11
    show issei np04 at c41
    j "That's not true!"
    j ap02 "I'm not like that with you."
    j "And why do you say stupid things if I was the one who conquered you, Issei."
    show jenni ap01
    i np07 "Of course, because I was the only one who agreed to go out with you, besides nobody."
    show issei np08
    show jenni np17 at ztj11
    j "Ugh."
    j "Better continue before I beat you up."
    show jenni np01
    j nbp02 "Well...{nw=2.0}"
    j "To treat us girls you have to be nice..."
    j nbp08 "Listen, know how to respond."
    j nbp09 "And above all..."
    j nbp08 "Tell us nice things."
    j nbp05 "Not like others who just talk to you nicely when they want something and that's it."
    show issei np05 at z11
    show jenni np17 at c44
    i "That's not true!"
    show jenni at c22
    show issei np06 at z21
    j "Of course!"
    j nbp05 "You just say nice things to me when you want to have...{nw}"
    show issei np04
    show jenni np13
    pr "STOP FIGHTING NOW!"
    pr "That we're not getting anywhere."
    show jenni np26 at z22
    show issei np17 at c21
    ji  "Sorry."
    j "It's just that we got carried away by the moment."
    show jenni np01
    show issei np01
    pr "What I want to know is how I should treat Yumi."
    pr "I don't know..."
    pr "How to talk to him?"
    pr "How to treat it?"
    pr "Hmm...."
    pr "How to help her?"
    j np14 "Well..."
    j "How to talk to her and treat her if we can help you."
    j "But.{w=2.0}...as far as how to help her, I don't think so."
    j "Well, yes we can, but just giving you advice and that's it."
    j nbp26 "Since this is such a strange situation that all we can do is give you some advice and nothing else."
    show jenni np13
    pr "That's all I need."
    pr "And I will be very grateful if you help me."
    pause 1.0
    show jenni np01
    pr "I think we've been standing here for a while."
    pr "Would you like to stay for lunch?"
    j np02 "Sure."
    j "Why not?"
    show jenni np01 at c22
    show issei np02 at z21
    i "No problem."
    show issei np01
    pr "I'll go find Emi to help me cook."
    i np02 "Okay, we'll wait for you."
    show issei np01
    window hide(Dissolve(.2))
    stop music fadeout 2.0
    scene black with wipeleft_scene
    pause 1.0
    "After cooking we sit at the table to eat."
    pause 3.0
    window auto
    scene hiroki_livingroom with wipeleft_scene
    show jenni np01 at c31
    show emi nc01 at c32
    show issei np01 at c33
    pause 1.0
    pr "Emi, thanks for the food."
    pr "It was delicious."
    play music a7 fadein 2.0
    show emi nc05 at z32
    e "Thank you little brother."
    e nc02 "I work hard at every meal I eat."
    show issei np02 at z33
    show emi nc01 at c32
    i "That's very noticeable."
    i "I prefer to eat your food every day..."
    i np07 "Than eating Jenni's awful food."
    pause 1.0
    show issei np12
    i "Did I say it or did I think it?"
    show issei np13
    pr "You said it."
    show emi nc04 at c31
    show jenni nbp17 at z32
    show issei at c33
    j "So my food seems horrible to you."
    j "But well you swallow it."
    show jenni nbp16 at ztj32
    j "HEY!"
    show issei np12 at tr33
    i "Sorry, sorry."
    i "I didn't mean that."
    i "I swear."
    j nbp07 "You better be."
    j "Because if you keep saying bad things about me..."
    j "You'll see what will happen to you."
    show jenni nbp16 at ztj32
    j "YOU GOT IT!"
    show issei np17
    i "Y-Yes."
    i "Sorry, sorry."
    show issei np16
    show emi nc01 at c32
    show jenni nbp02 at z31
    j "Well Emi, [player!t]."
    j "Issei and I have to go."
    j "The food was very delicious."
    j "There are things we have to do."
    show issei np05 at z33
    show jenni np13 at c31
    i "But we have nothing to do."
    show emi nc04 at c31
    show jenni nbp07 at z32
    show issei np16 at c33
    j "What did you say?"
    show issei np17 at tr33
    i "W-What if we have things to do."
    "Checked."
    "Jenni is very scary."
    show jenni np02
    show issei np16
    j "Cleared up the matter."
    j "Issei and I went to retire."
    j np08 "Goodbye Emi."
    j "Goodbye [player!t]."
    show jenni np09
    pr "Goodbye Jenni."
    e nc05 "Goodbye Jenni."
    show emi nc04
    j nbp07 "Let's go Issei."
    show jenni nbp06
    i np17 "Goodbye [player!t]."
    show issei np16
    pr "Goodbye Issei."
    show jenni at rhide
    hide jenni
    show issei at rhide
    hide issei
    window auto
    "Issei and Jenni leave my house."
    "After this weird goodbye."
    "..."
    "Your discussions can be heard from here."
    j "WHO GAVE YOU THE RIGHT TO INSULT MY FOOD!"
    i "IT'S NOT MY FAULT YOU COOK SO BAD!"
    "But then you don't hear anything anymore."
    pause 3.0
    show emi nc01 at c11
    "After a few minutes I finish my lunch."
    "Jenni didn't finish hers."
    "Emi ended up eating Issei's lunch."
    "He didn't eat it either."
    "And I finished eating Jenni's."
    pr "Issei and Jenni are the perfect couple."
    pr "Don't you think so?"
    show emi nc05 at j11
    e "Yeah, hehe."
    e "Even though they fight so much, they love each other very much."
    show emi nc01
    pr "Yes it is true."
    pr "Although it is proven that you have to be afraid of Jenni."
    e n1c16 "That's true."
    show emi n1c21
    pause 2.0
    "We were quiet for a while."
    "Until Emi decides to break the silence."
    e nc02 "Little brother..."
    e "..."
    e "How did it go with Yumi?"
    show emi nc01
    pr "How do you know I was with her?"
    pr "Besides..."
    pr "How do you know who it is?"
    e nc05 "Issei and Jenni told me."
    show emi nc04
    pr "..."
    "When I see Issei and Jenni again, I'll talk to them about telling Emi what we talked about."
    "If I don't forget."
    show emi nc01
    pr "A while ago you asked who Yumi was."
    e nc16 "Sorry, I didn't know if we were talking about the same Yumi."
    show emi nc01
    pr "And what did they tell you?"
    e nc22 "That she told you that you are her boyfriend."
    show emi dc06 at j11
    e "That's not fair little brother!"
    show emi dc04 at j11
    e "I want to be your wife!"
    show emi dc01
    pr "Emi I've already told you a million times."
    pr "We are! {w=2.0}BROTHERS!"
    e dc04 "That Yumi is going to have to compete with me for your love."
    show emi ac01 at j11
    e "And I won't let myself be defeated!"
    show emi dc01
    pr "Yes, whatever you say."
    pr "I'm going to my room to investigate some things."
    e nc05 "Okay little brother."
    e "Don't watch triple X movies."
    show emi nc04
    pr "What's wrong with you?!"
    pr "Are you crazy or what?!"
    pr "I don't watch adult movies!"
    pr "And..."
    pr "What are you doing looking at my history?!"
    show emi nc16 at tr11
    e "E-Ehhhh..."
    show emi nc05 at j11
    e "{cps=90}I have to go to my room to do something.{/cps}{nw=0.50}"
    show emi nc04 at j11
    e "Goodbye.{nw=0.50}"
    show emi at rhide
    hide emi
    pr "Emi!"
    pr "Stop going through my stuff!"
    pr "That girl."
    pause 3.0
    "I've been standing here for a while."
    "I better go to my room and take advantage and investigate what depression and bipolarity are."
    "To get out of doubt."
    pause 1.0
    stop music fadeout 2.0
    scene hiroki_room with wipeleft_scene
    pause 1.0
    "Okay..."
    "To which I came to my room."
    "I walk over to the desk where my computer is and turn it on."
    window hide(Dissolve(.2))
    scene pc_off_event_day
    show pcev_light zorder 10
    show snow2 zorder 8
    with dissolve
    pause 1.0
    $ renpy.call_screen("confirm", message="Computer startup scene can be skipped\nDo you want to skip the scene?", yes_action=Jump("pc_on_ok"), no_action=Jump("pc_on "))
    jump pc_on_en

label pc_on_en:
    #PC power up scene
    pause 1.0
    show pc_on_event_day with (Dissolve(.15))
    pause 1.0
    show pc_scene_1 zorder 2
    pause 3.0
    hide pc_scene_1
    show pc_scene_2 zorder 2
    with Dissolve(.1)
    pause 2.0
    show system_loading zorder 5 with Dissolve(.2)
    pause 5.0
    hide pc_scene_2
    hide system_loading
    show pc_scene_1 zorder 2
    with Dissolve(.3)
    pause 1.0
    show pc_scene_3 zorder 2
    pause 3.0
    jump pc_on_ok_en

label pc_on_ok_en:
    hide pc_scene_3
    show pc_scene_4 zorder 2
    pause 1.0
    "Okay..."
    "It's already lit {w}, I'll start investigating."
    pause 1.4
    hide pc_scene_4
    show pc_scene_5 zorder 2
    with Dissolve(.1)
    pause 1.0

label systemevent2_en:
    if persistent.first_browser == 0:
        $ renpy.call_screen("dialog", message="Next you will be shown\nSome options of what you want to investigate either about:\nDepression, Bipolarity or DID.", ok_action=Return())
    elif persistent.first_browser == 1:
        pass
label browser_search_en:
    pause 1.0
    if persistent.investigationcomp == 3:
        jump ch13_en
    if persistent.investigationcomp == 0:
        $ investigationtext = "I will investigate first on..."
    if persistent.investigationcomp > 0:
        $ investigationtext = "Now I will investigate..."
    menu:
            
        "[investigationtext!t]"
        "Depression":
            $ persistent.browseresearch = 0
            $ renpy.jump("ch12_en")
        "Bipolarity":
            $ persistent.browseresearch = 1
            $ renpy.jump("ch12_en")
        "DID(Dissociative Identity Disorder)":
            $ persistent.browseresearch = 2
            $ renpy.jump("ch12_en")
label ch12_en:
    if persistent.browseresearch == 0:
        if persistent.depressiofinishsearch == 1:
            "I already did a lot of research on depression."
            "I should do some research on something else."
            jump browser_search_en
    if persistent.browseresearch == 1:
        if persistent.bipolarityfinishsearch == 1:
            "I already did a lot of research on bipolarity."
            "I should do some research on something else."
            jump browser_search_en
    if persistent.browseresearch == 2:
        if persistent.dissociativfinishsearch == 1:
            "Dissociative identity disorder doesn't convince me."
            jump browser_search_en
    scene black with Dissolve(2)
    window auto
    "Let's see what interesting results can come out."
    window hide(Dissolve(.2))
    pause 3.0
    scene pc5_on_event_day with Dissolve(1.4)
    if persistent.browseresearch == 0:
        window auto
        "Well, here I found one on Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show depressio at is55
        call shownote(info_depression_en, False, "page2") from _call_shownote_10
        show depressio at hidetr
        hide depressio
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "Well, this doesn't tell me much about depression."
        "It's just his concept."
        "Also, I'm getting a bit confused."
        "Let's see what it says below."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_depression_2_en, False, "page2") from _call_shownote_11
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "..."
        "Yumi must have seen her depression develop from...."
        "Wait..."
        "Yes she said she was diagnosed at eight years old."
        "Then I don't know why he would have developed it."
        "Well, it could be that I suffered from a lot of bullying in school when I was little."
        "Or she wasn't accepted by her classmates."
        "That would be one of the factors by which it develops."
        "I'll have to investigate further."
        pause 2.0
        "Treatment...."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_depression_3_en, False, "page2") from _call_shownote_12
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "Yumi sure doesn't take antidepressants."
        "..."
        "Enough about depression."
        pause 1.0
        $ persistent.depressionfinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search_en

    if persistent.browseresearch == 1:
        scene pc5_on_event_day
        window auto
        "Well, here I found one on Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show TwoFaces at is55
        call shownote(info_bipolarity_en, False, "page2") from _call_shownote_13
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        show TwoFaces at hidetr
        hide TwoFaces
        "Could it be that Yumi is bipolar?"
        "Since it's kind of weird that she was sitting around crying..."
        "And he jumped up and was happy to see me."
        "I think I'm saying things without knowing."
        pause 1.0
        "Here you don't tell me how it unfolds."
        "Let's see..."
        "Classification..."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_bipolaridad_2_en, False, "page2") from _call_shownote_14
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "Well, I'm not going to stay and read the entire classification."
        "It's too long and it makes me lazy."
        "....."
        "Depressive period...."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show depressio at is55
        call shownote(info_bipolaridad_3_en, False, "page2") from _call_shownote_15
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        show depressio at hidetr
        hide depressio
        "Hmm..."
        "Okay...."
        "Actually, since I saw Yumi, I think she must be bipolar."
        "Treatment..."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_bipolaridad_4, False, "page2") from _call_shownote_16
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "..."
        "What a long drug list."
        "Enough about bipolarity."
        pause 1.0
        $ persistent.bipolarityfinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search_en

    if persistent.browseresearch == 2:
        scene pc5_on_event_day
        window auto
        "Well, here I found one on Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show TID at is55
        call shownote(info_dissociativ_en, False, "page2") from _call_shownote_17
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        hide TID at hidetr
        hide TID
        "I really don't think Yumi suffers from dissociative identity disorder."
        "It says here it's 90 percent caused by childhood trauma."
        "And the truth is that Yumi doesn't see that she has suffered one."
        pause 1.0
        $ persistent.dissociativfinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search_en

label ch13_en:

    scene pc5_on_event_day
    "I think I wasted my time researching this."
    "Since I'm not a psychologist to know if Yumi has depression or not."
    "But it's good to do a little research on something we don't know about."
    "..."
    "I will continue investigating to see what other results appear."
    window hide(Dissolve(.2))
    stop music fadeout 4.0
    scene black with Dissolve(4.0)
    pause 2.0
    scene pcev_cg_night with Dissolve(1.0)
    window auto
    "...British scientists say they have clear evidence of a link between bipolar disorder and intelligence..."
    "I'm already bored."
    pause 1.0
    "I look at my watch and notice I've been doing research for like 4 hours."
    "Heavens."
    "I let out a big yawn..."
    pause 1.5
    "Enough for today."
    "I'm a little tired."
    "I close my eyes to rest for a moment."
    scene black with eyeinslow_scene
    "..."
    "..."
    "..."
    window hide(Dissolve(.2))
    pause 3.0
    window auto
    e "Little brother....."
    pause 1.0
    e "Little brother....."
    pause 1.0
    scene hiroki_room_night
    show emi nc12 at j11
    e "LITTLE BROTHER!"
    pr "AHHHHHH!"
    pr "WHAT'S WRONG?!"
    e n1c16 "Sorry little brother I didn't mean to scare you."
    e "It's just that you weren't getting up and it was scaring me."
    show emi nc21
    play music a1 fadein 2.0
    pr "Almost...{w=1.5}You make...{w=1.5}I have a heart attack."
    e nc16 "I'm sorry little brother, I really didn't want to scare you."
    show emi nc21
    pr "Don't worry."
    show emi nc01
    pr "It's just that I had fallen asleep."
    pr "And what are you doing in my room?"
    e nc02 "I came to tell you that the food is ready."
    show emi nc01
    pr "..."
    pr "And what did you cook?"
    e nc02 "I made a pork and soy ramen soup."
    show emi nc01
    pr "That's good."
    pr "Let's eat then."
    show emi nc05 at j11
    e "YES!"
    show emi nc04
    stop music fadeout 2.0
    scene black with wipeleft
    pause 3.0
    "Upon reaching the room..."
    "We sat at the table to eat."
    "Emi had a very delicious ramen soup."
    "After eating we went to see a movie."
    pause 1.0
    play music a7 fadein 2.0
    scene hiroki_livingroom with wipeleft
    show emi nc05 at c11
    e "It was great, right?"
    show emi nc04
    pr "Yes, I loved it."
    pause 1.0
    pr "Well..."
    pr "I'll go to bed."
    pr "For today I'll let you sleep late."
    pr "Good evening Emily."
    show emi at hidetr
    hide emi
    pause 1.0
    show emi nc02 at c11
    e "Little brother?"
    show emi nc01
    pr "What's wrong Emi?"
    e dc11 "C-Can we{w}....talk?"
    show emi dc08
    pr "Uh..."
    pr "Yes."
    pr "What's going on?"
    show emi dc11 at tr11
    stop music fadeout 2.0
    e "What's wrong with Yumi that you didn't let me listen?"
    show emi dc08
    pr "Te...{nw}"
    pr "...."
    "I think I should tell her what's up with Yumi."
    "I don't want him to think that something very bad is going on."
    "Or that I got in trouble with her."
    "I don't want him to see me as our parents."
    "That they hid everything that happened from us."
    pr "Emi."
    show emi dc14 at c11
    e "Hmm?"
    pr "Look..."
    pr "The thing about Yumi is that..."
    pr "{i}*sigh*{/i}"
    pr "Look, Yumi has depression."
    show emi nc23 at tr11
    "Well, I keep saying she has depression because I don't know exactly if she's bipolar."
    pr "She is very lonely and thinks that nobody loves her."
    pr "And that's why I promised to help her."
    e nc24 "I didn't know that."
    e n1c24 "And how do you intend to help her?"
    show emi nc23
    pr "Well, I have to play along that I'm her boyfriend."
    e nc25 "...."
    e"I...."
    pause 1.0
    play music a4 fadein 2.0
    show emi nc12 at j11
    e "I WON'T GET BEAT!"
    e dc04 "That Yumi won't beat me."
    e "I will be your wife one way or another."
    e "You'll see."
    show emi dc01
    pr "YOU...{nw}"
    pr "You know what, I better not tell you anything."
    pr "I'm going to look like a broken record."
    pr "Always saying the same thing."
    pr "I better go to my room to sleep."
    pr "Good evening."
    e nc05 "Good night little brother."
    show emi nc04
    pause 1.0
    show emi at lhide
    hide emi
    "After this Emi goes to her room."
    "This girl."
    "Always with the same."
    "Well, that's just a childish whim."
    "I'm sure when I grow up not even the word will want to direct me."
    "..."
    "Better I go to sleep."
    "Today was a long day."
    scene hiroki_room_night with wipeleft_scene
    pause 1.0
    "When I get to my room I lie down on my bed."
    stop music fadeout 2.0
    scene black with dissolve
    pause 3.0
    "Yumi..."
    "Why the hell do you say I'm your boyfriend?"
    "This is so weird."
    "She would be my first girlfriend."
    "Even if it's just a lie."
    "......"
    "I hope I can help you."
    "Since I don't want her to be alone."
    "No one deserves to be alone."
    "..."
    "{i}*sigh*{/i}"
    "I better fall a sleep."
    window hide(Dissolve(.2))
    pause 3.0
    scene hiroki_room_night
    play audio stopper
    pause 1.0
    window show(None)
    pr "Wait a minute..."
    pr "Yes today is Saturday."
    pr "And yesterday was Friday."
    pr "DON'T TALK TO HANA!"
    pr "I got distracted going to Yumi's house."
    e "Little brother! Is something wrong?!"
    pr "Nothing happens!"
    pr "Don't worry!"
    e "Okay!"
    pause 1.0
    pr "Monday I should talk to Hana."
    pr "{i}*sigh*{/i}"
    pr "I hate when I forget things."
    pr "I better lie down to sleep."
    pr "Tomorrow is another day."
    stop music fadeout 1.0
    window hide(Dissolve(.2))
    scene black with Dissolve(3.0)
    pause 3.0

    return