# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default mp = ""
default gender = ""
image mc female = "images/sprites/mc female.png"
image mc male = "images/sprites/mc male.png"
define mc_sprite = None
define mc_female = Character("Commander")
define mc_male = Character("Commander")
default mc = None
image bg openning = "images/background/bg openning.png"
image bg neatholm = "images/background/bg neatholm.png"
default _current_choices = []
default _last_npc = ""
default _wendu_in_party = None
default _lann_in_party = None
transform middle:
    yalign  0.5
    xalign  0.5
transform mc_pos:
    yalign  0.5
    xalign  0.2
transform npc_pos:
    yalign  0.5
    xalign  0.8

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg openning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    menu:
        "Are you a boy or a girl?"
        "Male":
            $ gender = "male"
            $ mc = mc_male
            $ mc_sprite = "mc male"
            show mc male at middle
        "Female":
            $ gender = "female"
            $ mc = mc_female
            $ mc_sprite = "mc female"
            show mc female at middle
    # This ends the game.
    "You chose [gender]"
    jump openning

define slh = Character("Seelah")
define cam = Character("Camellia")
define dae = Character("Daeran")
define tren = Character("Terendelev")
image cam = "images/sprites/cam.png"
image dae = "images/sprites/daeran.png"
image terendelev = "images/sprites/terendelev.png"

label openning:
    scene black

    show text "Your journey start at the quaint little town of kenabres" at truecenter
    pause
    hide text
    show text "You are carted into the town festival by a gnome\nYou hear the noise of a festival ringing inside your ears\nYou finally woke up" at truecenter
    pause
    hide text
    scene bg openning
    $ _history_list[:] = []
    show expression mc_sprite at mc_pos
    show seelah at npc_pos
    slh "Help!! Anybody Help!! HELP!!!!"
    menu:
        "Would you please shut it!":
            mc "Would you please shut it!"
            slh "Well there is no need to be rude"
        "nghh... where am I?":
            mc "nghh... where am I?"
            slh "Ah good, you're finally awake"
        "Is this hell?":
            mc "Is this hell?"
            slh "Haha.. funny"

    slh "You are now in the kenabres square. Hold on here while I search around for lady terendelev"
    hide seelah
    show cam at npc_pos
    cam "Ugh.. why should we waste our lady time with this philistine"
    hide cam
    show dae at npc_pos
    dae "Now now my lady... even us nobles still have to help from time to time. Ofcourse a beautiful lady such as yourself should not be troubled by this"
    hide dae
    show cam at npc_pos
    cam "Thank you my count!"
    hide cam
    show dae at npc_pos
    menu:
        "I can still hear you, you know!":
            mc "I can still hear you, you know!"
            dae "And?"
        "How nice! A taste of the countryside nobilities":
            mc "How nice! A taste of the countryside nobilities"
            dae "Well you haven't seen all of it yet"
        "You got a problem with me?!":
            mc "You got a problem with me?!"
            dae "Tchk.. Such boorish way to solve a problem"
    hide dae
    show terendelev at npc_pos
    tren "What happened?! I came as quickly as i could!"
    hide terendelev
    show seelah at npc_pos
    slh "Here my lady. This person is in need of critical aid"
    "As she said that, the wound in your chest gapes open and spews even more blood"
    hide seelah
    show terendelev at npc_pos
    tren "This is no ordinary wound. I will do what I can"
    "The lady puts her hand on your chest and starts chanting"
    tren "GAVELA'GLAN"
    "As the chant finishes, the wound on your chest starts to close up. Although, you feel like this wont be the end of it"
    tren "There I did all I could."
    menu:
        "Thank you my lady. May I know your name?":
            mc "Thank you my lady. May I know your name?"
            tren "Your welcome."
        "Thank god. I was about to follow the light!":
            mc "Thank god. I was about to follow the light!"
            "The lady chuckles ever so slightly"
        "Who asked for your help noble wench":
            mc "Who asked for your help noble wench"
            tren "Im sorry if i bothered you, but I did what needs to be done"
    tren "My name is Terendelev. I am the guardian dragon of kenabres."
    tren "You are welcome to stay here. Please, enjoy the festival. Atleast until your wound heals up"
    mc "Thank you!"
    hide terendelev
    show seelah at npc_pos
    slh "Whew.. that was a heck of a ride! My name is Seelah by the way. Its nice to meet you! You should probably wander around and enjoy the festival. I heard that the wine here is especially good!"
    mc "Sure!"
    jump deskari
define des = Character("Deskari")
image des = "images/sprites/deskari.png"
define gnome = Character("Gnome")
label deskari:
    scene black
    show text "you then wander around the festival. Enjoying the festivities.\nYou tried the throwing knives, drank wine, and enjoy other delights the festival has to offer." at truecenter
    pause
    hide text
    show text "Until..." at truecenter
    pause
    hide text
    scene bg openning
    $ _history_list[:] = []
    show text "\"Behold Crusader Gods! Behold Iomedae you poor impostor! Your city will fall to ME! Your Followers will feed my hunger!\"" at truecenter
    pause
    hide text
    show expression mc_sprite at mc_pos
    "You saw the sky starts to turn red."
    "Suddenly, the ground beneath the square burst open forming a crevase."
    "From the bottom, out flies a demonic locust-like demon the size of a building."
    "Demons overflow kenabres square. People screaming, runnig for their lives."
    show deskari at npc_pos
    des "HAHAHAHAHHA.... I HAVE COME MORTALS. RENDER YOUR SOUL TO ME, AND YOU SHALL BE INCLUDED IN MY SWARM OF LOCUST"
    "You hid behind a table with the gnome that saved you."
    hide mc
    show terendelev at mc_pos
    tren "DESKARI, LORD OF LOCUST. LEAVE. MY. CITY!!"
    "Within a second, The once ladylike Terendelev has changed into a humongous silver dragon"
    tren "RETURN TO WHERE YOU CAME FROM, FOR I CARRY THE WRATH OF MY LADY IOMEDAE WITH ME"
    "With a swift slice, deskari cuts off Lady Terendelev's head"
    hide terendelev
    des "YOU DARE CHALLENGE ME, WITH THIS POWER!?"
    des "LET THE FEAST BEGIN!"
    "The once noble Terendelev, guardian of Kenabres, has fallen"
    "The demon lord deskari then slice a pillar in the middle of the square, and throws it far into a fortress"
    des "Without your precious wardstone, you mortals are nothing!"
    hide deskari
    show expression mc_sprite at mc_pos
    gnome "Blimey! Deskari himself.. Here in Kenabres! One minute we had a dragon, the next - BAM! She was Gone!"
    gnome "What're you gonna do? Flee? Fight? If Fleeing's your plan, I have a useful scroll here with me!"
    menu:
        "Care to lend me a weapon? I'll try to fight the demons":
            mc "Care to lend me a weapon? I'll try to fight the demons"
            gnome "I've got nothin on me but this crossbow. Best of luck to ya!"
            "With a swift glance, the gnome has turned invisible with the spell he has on the scroll"
            mc "Take this you ugly bastard!"
            "You shot a bolt towards the demon lord"
        "I think im looking for a way out of here! Give me that scroll":
            mc "I think im looking for a way out of here! Give me that scroll"
            gnome "Alright. Do be careful, these demons are not here to play!"
    "Before you could even do anything, the demon lord deskari slices his scythe and the ground beneath you crumbles"
    "You fall down into the dark crevice and knock yourself out"
    jump neatholm
image nevi = "images/sprites/anevia.png"
define nev = Character("Anevia")
define lann = Character("Lann")
image lann = "images/sprites/lann.png"
define wen = Character("Wenduag")
image wendu = "images/sprites/wenduag.png"
image bg war = "images/background/bg war.png"
default neatholm_path_demon = False
define sull = Character("Chief Sull")
label neatholm:
    scene black
    show text "You woke up after being knocked cold for an hour" at truecenter
    pause
    hide text
    scene bg neatholm
    show expression mc_sprite at mc_pos
    "You fell a long way from kenabes squares. As you look around, all you can see is glowing underground plants to guide your way."
    "You heard a noise not far from here. As you follow that noise, you met a familiar face."
    show seelah at npc_pos
    slh "One. Two. Three. HEAVE!"
    "You saw the paladin of Iomedae struggling to lift a heavy boulder from a woman"
    hide seelah
    show nevi at npc_pos
    nev "Forget it seelah. You should probably leave me. Demons are still running around Kenabres. I'll figure something out by myself"
    menu:
        "You guys need a hand?":
            mc "You guys need a hand?"
            nev "Ah thank god someone is here. Please help us!"
            "With difficulty, you and seelah lifts the boulder pinning Anevia's leg."
            nev "Well thank you my friend, the name's Nevi."
        "I'm pretty sure Seelah got this":
            mc "I'm pretty sure Seelah got this"
            nev "Well it wouldn't hurt for you to help!"
            mc "Nahh im good"
            "With horrid difficulty, Seelah managed to lift the boulder pinning Anevia's leg, unfortunately breaking it in the process"
    hide nevi
    show seelah at npc_pos
    slh "Now that that's done, lets go and get out of here. This place is giving me the creeps!"
    hide seelah
    "You then traveled with the group to find a way out of this underground cave system."
    mc "I can't believe that there is a cave this big under Kenabres"
    show nevi at npc_pos
    nev "I know, this is what people call the neatholm. The homeland of the mongrels."
    hide nevi
    "After a while, our party met someone on the road."
    show cam at npc_pos
    cam "*mumbles* hehehehe..."
    cam "Oh i did not see you there!"    
    "The cheery elf looks friendly, although you have a gnawing feeling inside your heart, you brushed it aside thinking nothing of it"
    hide cam
    show seelah at npc_pos
    slh "Is that a body behind your back? What happened to him? It does not look like the wound from falling."
    hide seelah
    show cam at npc_pos
    cam "I don't know, it's been like that ever since I found it."
    hide cam
    show seelah at npc_pos
    slh "Oh well. I'm usually prone to the idea but, we should probably loot what left of the remain."
    "You looted the body and found a key which opens a chest beside the body. Inside are weapons and armors."
    hide seelah
    show cam at npc_pos
    cam "You know, we should probably go together. I know a couple of spells and im sure my druidic power will be useful on our path ahead."
    mc "Sure!"
    scene black
    show text "The party of four then continued their journey throughout neatholm until they found themselves infront of an old temple." at truecenter
    pause
    hide text
    show text "Within it, there stands 2 mongrels, Lann and Wenduag." at truecenter
    pause
    hide text
    "The well mannered half lizard Lann then gets closer to you."
    scene bg neatholm
    show expression mc_sprite at mc_pos
    show lann at npc_pos
    lann "Hey there traveler!"
    lann "The names Lann. Im a mongrel"
    lann "I heard some stuff upstairs and figures Kenabres's in danger"
    lann "Me and my friend wenduag here is trying to find the sword of an angel. Our ancestor."
    hide lann
    show wendu at npc_pos
    wen "What are you doing Lann. These outsiders does not need to know about our problems."
    wen "They have been ignoring us for thousands of gongs. They don't deserve to know our powers."
    hide wendu
    show lann at npc_pos
    lann "Cmon wendu, lighten up! I mean 6 pair of hands are better than 2 you know."
    hide lann
    show wendu at npc_pos
    wen "Whatever"
    "You then searched the area for the sword"
    "At the corner of your eyes, you saw something glimmers in the dust."
    "As you approached, visions of angels and 'evil' angels invaded your minds"
    "As you held the hilt of the sword. You suddenly fell to a trance."
    scene bg war
    show text "Within your vision, you saw how this sword came to be.\n An angel, fighting in the war against the demons in the first crusade was the original owner of the sword. \n With its power, the angel slain all the demons in kenabres. \n Unfortunately, he was deeply wounded and their group was chased inside the cave beneath Kenabres." at truecenter
    pause
    hide text
    show text "As they were escaping further into the cave, the angel saw his comrades fell one by one to the demons.\n Seeing this, the angel..." at truecenter
    pause
    hide text
    menu:
        "Turns in anger and annihilates all demons who stands in his way (Demonic path)":
            show text "Turns in anger and annihilates all demons who stands in his way (Demonic path)." at truecenter
            pause
            hide text
            $ neatholm_path_demon = True
        "Pray in humility and lets out a light of heaven (Angelic Path).":
            show text "Pray in humility and lets out a light of heaven (Angelic Path)." at truecenter
            pause
            hide text
    show text "You then regain your consience." at truecenter
    pause
    hide text
    scene bg neatholm
    show expression mc_sprite at mc_pos
    "As you regain your consciousness, you saw that you are raising the sword and the sword is shining."
    show lann at npc_pos
    lann "This is it, this is the light in the stories. You are the one they talks in those myths!"
    lann "We need to go to the village and inform chief Sull of this!"
    hide lann
    show wendu at npc_pos
    wen "Don't you think thats too reckless Lann. This person is an outsider. They don't know a single thing about our myth yet you want to just bring them to our village and give false hope to them"
    hide wendu
    show lann at npc_pos
    lann "Oh cmon now Wendu. Outsider or not, this person is the one that will bring our people back to the surface!!"
    hide lann
    "After a fierce debate, they agree to bring me to their village. However, Wenduag talked to me right before we set off"
    show wendu at npc_pos
    wen "Hey. I know we just met but I want you to do me a favour"
    wen "Please do not show that light to the chief."
    wen "The people on our village has lost all hope and cannot suffer through another false hope."
    wen "Lann is a nice guy, but he has the tendency to play the hero. So please, for my people, do not show the light to chief Sull."
    hide wendu
    show text "The party then travelled to the village." at truecenter
    pause
    hide text
    show lann at npc_pos
    lann "Chief. We found them. We found the hero that will lead our people to the surface."
    sull "Child, we have been here for such a long time. What makes you think this person can bring our kind back to the surface?"
    lann "Show him what you did at the temple! The chief would definitely believe it if he sees the light with his own eye."
    menu:
        "It's true, here you go  (Show the light)":
            mc "It's true, here you go  (Show the light)"
            sull "By the gods"
            jump neatholm_lann
        "Lights? What lights?":
            mc "Lights? What lights?"
            lann "The ones that you showed me in the temple!"
            mc "I think you're starting to see things"
            lann "Dont play with me! I know what I saw!"
            jump neatholm_wendu

label neatholm_lann:
    sull "You are right Lann. This person can help use reach the surface."
    sull "Please honored one, rest up here for a day before going back up to Kenabres."
    sull "We shall help you get back up to the surface come sunrise"
    hide lann
    show wendu at npc_pos
    wen "You will regret this. I hope you are fine with dooming the fate of a whole tribe."
    hide wendu
    jump shield_maze_lann

label neatholm_wendu:
    hide lann
    show wendu at npc_pos
    wen "I think little old Lann cannot wait to play the hero again."
    wen "We cannot go to the surface Lann. Our tribe cannot handle it."
    hide wendu
    show lann at npc_pos
    sull "I agree with wenduag. In times like these, we need to keep our head cool to survive"
    lann "Good job. Congratulation on dooming an entire tribe because of your selfishness."
    jump shield_maze_wendu

image bg shieldmaze = "images/background/bg shieldmaze.png"
define hos = Character("Hosilla")
default _demon_path_1 = False
default _angel_path_1 = False
label shield_maze_lann:
    scene black
    show text "You then rest at the tribe until sunrise" at truecenter
    pause
    hide text
    show text "Come sunrise, Wenduag was gone. The party of five then went to the chief's hut"
    pause
    hide textbox
    $ _wendu_in_party = False
    $ _lann_in_party = True
    scene bg neatholm
    $ _history_list[:] = []
    show expression mc_sprite at mc_pos
    sull "Alright, we are ready for the expidition to the shield maze"
    mc "The shield maze?"
    show lann at npc_pos
    lann "The shield maze is the one and only entrance or exit from neatholm. Atleast before the ground starts cracking above us."
    lann "Unfortunately, the shield maze is filled with dangerous creatures and cultists."
    mc "Alright then lets head to the shield maze"
    scene black
    "As the party arrives at the shiled maze, we can see that many other tribes has already joined the convoy"
    scene bg shieldmaze
    show expression mc_sprite at mc_pos
    sull "I think you guys should scout ahead first. Some of our youngins has gone inside before us!"
    show seelah at npc_pos
    slh "Sounds good to me!"
    hide seelah
    "The party then opened the door into the shield maze and went inside."
    "As they go depeer and deeper inside, the creature they meet are increasingly more disturbing."
    "After hacking through demons and cultist. They finally comes to the end of the shield maze."
    "There at the exit the party saw something they should not have"
    "A cultist was offering the blood of her demon master to 5 young mongrels"
    hos "Well, well, well... Look what we have here"
    hos "All of you will need to drink this blood or die"
    "Youngin 1" "You demonic bastard. We will never be corrupted. Our blood carries the will of the first crusaders!"
    "Youngin 2, 3, 4" "Yeah!!"
    hos "So be it."
    "Hosilla attacks one of the youngins with her halberd. The youngin's head roll on the ground without so much of a blink"
    hos "See the power that was given by our gracious lord Savamalekhh!!"
    hos "Rejoice for he has given us this blessing"
    "Scared of what's going to happen, the other mongrel youngins start drinking the blood of their brethren."
    show lann at npc_pos
    lann "HEY STOP THAT!!"
    lann "What are you guys doing!? And you! You will die here by my hands"
    "As Hosilla saw us, she called to her lord and summoned demons."
    menu:
        "You feel an unbridled rage inside you. Taps into the power and unleash hell on the cultist (Demonic path)":
            mc "As you take in the power of the demon, you went to battle significantly stronger."
            hos "YES, THAT IS THE POWER."
            $ _demon_path_1 = True
        "You feel an unbridled rage inside you. Refuse to let the power control you and accepts the light within you (Angel path)":
            mc "As you show the light of heaven, the youngins snaps out of their frenzy."
            hos "NO! THIS CANNOT BE!"
            $ _angel_path_1 = True
    "After a fierce battle, Hosilla is at the jaws of defeat"
    lann "You are too dangerous to keep alive. May you find peace in the afterlife"
    "Just as lann was about to execute her, Wenduag swoops in out of nowhere"
    hide mc
    show wendu at mc_pos
    wen "Im afraid you cannot do that Lann"
    lann "What are you doing Wendu!? This demon tries to sacrifice our young to the demons"
    wen "This is exactly why we never gets out! We keep on hoping for some old fairytale hero to save us."
    wen "Meanwhile, real power has been here all along."
    wen "We are demons! Lann!"
    wen "We need this power so that no one in the surface can bother us"
    wen "That is why I have been leading the youngins to Hosilla. That's why I accepted lord Svamalekhh"
    lann "YOU! YOU ARE THE CAUSE FOR ALL THIS!"
    lann "HOW MANY HAVE DIED BY YOUR HANDS!"
    lann "I CANNOT STAND BY AND WATCH YOU SCHEME BEHIND THE SCENE ANYMORE!"
    "Lann shoots his arrow at Wenduag. Wenduag skillfully dodge tha arrow and runs off into the cave"
    hide wendu
    show expression mc_sprite at mc_pos
    lann "I hope we dont have to see her again."
    "After sometimes, chieff sull joins us at the exit to Kenabres"
    sull "What happened here? Why are the youngins fainted?"
    lann "Wenduag happened. She has been leading our youngins to be turned into frenzied demon"
    sull "By Iomedae. Where is she now?"
    lann "She is long gone now."
    sull "Well you have done the right thing son. I hope you will keep travelling with our hero."
    lann "That is the plan."
    "You and the party then leaves the shieldmaze to continue to the battle for Kenabres"
    jump chap_1
label shield_maze_wendu:
    scene black
    show text "You then rest at the tribe until sunrise" at truecenter
    pause
    hide text
    show text "Come sunrise, Lann was gone. The party of five then went to the chief's hut"
    pause
    hide textbox
    $ _wendu_in_party = False
    $ _lann_in_party = True
    scene bg neatholm
    $ _history_list[:] = []
    show expression mc_sprite at mc_pos
    sull "Alright, we are ready for the expidition to the shield maze"
    mc "The shield maze?"
    show wendu at npc_pos
    wen "The shield maze is the one and only entrance or exit from neatholm. Atleast before the ground starts cracking above us."
    wen "Unfortunately, the shield maze is filled with dangerous creatures and cultists."
    mc "Alright then lets head to the shield maze"
    scene black
    "As the party arrives at the shiled maze, we can see that many other tribes has already joined the convoy"
    scene bg shieldmaze
    show expression mc_sprite at mc_pos
    sull "I think you guys should scout ahead first. Some of our youngins has gone inside before us!"
    show seelah at npc_pos
    slh "Sounds good to me!"
    hide seelah
    "The party then opened the door into the shield maze and went inside."
    "As they go depeer and deeper inside, the creature they meet are increasingly more disturbing."
    "After hacking through demons and cultist. They finally comes to the end of the shield maze."
    "There at the exit the party saw something they should not have"
    "A cultist was offering the blood of her demon master to 5 young mongrels"
    hos "Well, well, well... Look what we have here"
    hos "All of you will need to drink this blood or die"
    "Youngin 1" "You demonic bastard. We will never be corrupted. Our blood carries the will of the first crusaders!"
    "Youngin 2, 3, 4" "Yeah!!"
    hos "So be it."
    "Hosilla attacks one of the youngins with her halberd. The youngin's head roll on the ground without so much of a blink"
    hos "See the power that was given by our gracious lord Savamalekhh!!"
    hos "Rejoice for he has given us this blessing"
    "Scared of what's going to happen, the other mongrel youngins start drinking the blood of their brethren."
    show wendu at npc_pos
    wen "HAHAHAHAHA.. Yes eat my children. Be strong enough to kill everyone!!"
    "Suddenly, Lann shows up"
    hide wendu
    show lann at npc_pos
    lann "YOU! WHAT IS THIS! WHAT IS HAPPENING!!"
    "As Hosilla saw us, she called wenduag and her lord and summoned demons."
    menu:
        "You feel an unbridled rage inside you. Taps into the power and unleash hell on the cultist (Demonic path)":
            mc "As you take in the power of the demon, you went to battle significantly stronger."
            hos "YES, THAT IS THE POWER."
            $ _demon_path_1 = True
        "You feel an unbridled rage inside you. Refuse to let the power control you and show the light of heaven (Angel path)":
            mc "As you show the light of heaven, the youngins snaps out of their frenzy."
            hos "NO! THIS CANNOT BE!"
            $ _angel_path_1 = True
    hide lann
    "After a fierce battle, Hosilla is at the jaws of defeat"
    show wendu at npc_pos
    wen "WHAT IS THIS! WHY ARE YOU SO WEAK."
    "wenduag executes Hosilla right in front of your eyes"
    wen "Now I see it. YOU are my true mistress!"
    wen "Please dont leave me mistress!"
    hide mc
    show lann at mc_pos
    lann "What are you doing Wendu!? This demon tries to sacrifice our young to the demons"
    wen "This is exactly why we never gets out! We keep on hoping for some old fairytale hero to save us."
    wen "Meanwhile, real power has been here all along."
    wen "We are demons! Lann!"
    wen "We need this power so that no one in the surface can bother us"
    wen "That is why I have been leading the youngins to Hosilla. That's why I accepted lord Svamalekhh"
    lann "YOU! YOU ARE THE CAUSE FOR ALL THIS!"
    lann "HOW MANY HAVE DIED BY YOUR HANDS!"
    lann "I CANNOT STAND BY AND WATCH YOU SCHEME BEHIND THE SCENE ANYMORE!"
    wen "AND WHAT ARE YOU GONNA DO ABOUT IT!"
    wen "YOU ARE A WEAKLING TRYING TO PLAY HERO!"
    wen "YOUR ACTIONS HAS COST THE TRIBE ENOUGH!!"
    "Wenduag shots at lann while missing. Lann used this chance to run back to the caves"
    lann "THIS ISN'T OVER WENDU"
    hide lann
    show expression mc_sprite at mc_pos
    wen "I hope we dont have to see him again."
    "After sometimes, chieff sull joins us at the exit to Kenabres"
    sull "What happened here? Why are the youngins fainted?"
    wen "This is the power of our demonic blood. We should be happy this youngins gained new power!"
    sull "By Iomedae. I hope this is the right choice wenduag. Where is Lann?"
    wen "He is long gone now. That coward does not know a thing about keeping the tribe safe"
    sull "Well you have done the right thing. I hope you will keep travelling with our hero."
    wen "That is the plan."
    "You and the party then leaves the shieldmaze to continue to the battle for Kenabres"
    jump chap_1
label chap_1:
    scene black
    show text "TO BE CONTINUED" at truecenter
    pause
    hide text

return
