init python:
    
    CGS_DIR = "cg/"

    YDOORSCENE_DIR = CGS_DIR + "yumi_room_door/"
    for ydoorscene in range(1,4):
        renpy.image("yumi_room_door_" + str(ydoorscene), YDOORSCENE_DIR + "yumi_room_door_" + str(ydoorscene) + ".jpg")

image hiroki_surprise = CGS_DIR + "hiroki_surprise/hiroki_surprise_cg.jpg"

###############################################################################

init python:

    YCGCOFFEE_DIR = CGS_DIR + "yumi_coffeevent/"

    renpy.image("coffeeventbg", YCGCOFFEE_DIR + "coffeevent_bg.jpg")
    renpy.image("coffeechairs", YCGCOFFEE_DIR + "chairs.png")
    renpy.image("coffeedesk", YCGCOFFEE_DIR + "desk.png")
    renpy.image("ycotears", YCGCOFFEE_DIR + "tears.png")
    renpy.image("coffeelight", YCGCOFFEE_DIR + "light.png")
    renpy.image("ycoblush", YCGCOFFEE_DIR + "blush.png")

    for ycoeyebrowss in range(1,5):
        renpy.image("ycoeyebrows" + str(ycoeyebrowss), YCGCOFFEE_DIR + "eyebrows_" + str(ycoeyebrowss) + ".png")

    for ycoeyes in range(1,5):
        renpy.image("ycoeye" + str(ycoeyes), YCGCOFFEE_DIR + "eye_" + str(ycoeyes) + ".png")

    for ycomouths in range(1,7):
        renpy.image("ycomouth" + str(ycomouths), YCGCOFFEE_DIR + "mouth_" + str(ycomouths) + ".png")

    for coffees in range(1,4):
        renpy.image("coffee_" + str(coffees), YCGCOFFEE_DIR + "coffee_" + str(coffees) + ".png")

    for ycos in range(1,3):
        renpy.image("yco" + str(ycos), YCGCOFFEE_DIR + "yumi_" + str(ycos) + ".png")

define yc = DynamicCharacter("y_name", image="yco", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#5207b9")

image ycogout:
    YCGCOFFEE_DIR + "gout.png"
    gout_appear

image ycoffeepicturebg:
    choice:
        YCGCOFFEE_DIR + "pictures_1.png"
    choice:
        YCGCOFFEE_DIR + "pictures_1.png"
    choice:
        YCGCOFFEE_DIR + "pictures_1.png"
    choice:
        YCGCOFFEE_DIR + "pictures_1.png"
    choice:
        YCGCOFFEE_DIR + "pictures_2.png"

image ycolight:
    "coffeelight"
    ycolight_animation

transform ycolight_animation:
    alpha 1.0
    block:
        linear 15 alpha 0.3
        linear 7 alpha 0.5
        linear 15 alpha 0.7
        linear 15 alpha 1.0
        repeat

image coffee_animation:
    "coffee_1"
    pause 2.0
    "coffee_2" with Dissolve(0.30)
    pause 2.0
    "coffee_3" with Dissolve(0.30)
    pause 2.0
    "coffee_1" with Dissolve(0.30)
    pause 1.0
    repeat

image ycobg = LiveComposite((1280, 720), (0,0), "coffeeventbg", (0,0), "ycoffeepicturebg", (0,0), "coffeechairs")
image ycodesk1 = LiveComposite((1280, 720), (0,0), "coffeedesk", (0,0), "coffee_animation")
image ycodesk2 = "coffeedesk"

image yco a1 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows1", (0,0), "ycomouth1")
image yco a2 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows1", (0,0), "ycomouth2")
image yco a3 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows1", (0,0), "ycomouth3")
image yco a4 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows3", (0,0), "ycomouth3")
image yco a5 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows1", (0,0), "ycomouth1")
image yco a6 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows1", (0,0), "ycomouth2")
image yco a7 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows1", (0,0), "ycomouth4")
image yco a8 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth1", (0,0), "ycoblush")
image yco a9 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth2", (0,0), "ycoblush")
image yco a10 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth3", (0,0), "ycoblush")
image yco a11 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth3", (0,0), "ycoblush")
image yco a12 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth1", (0,0), "ycoblush")
image yco a13 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth2", (0,0), "ycoblush")
image yco a14 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth2", (0,0), "ycoblush")
image yco a15 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth3", (0,0), "ycotears")
image yco a16 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth6", (0,0), "ycotears")
image yco a17 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows4", (0,0), "ycomouth3")
image yco a18 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows1", (0,0), "ycomouth5")
image yco a19 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows1", (0,0), "ycomouth6")
image yco a20 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows4", (0,0), "ycomouth1")
image yco a21 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows4", (0,0), "ycomouth2")
image yco a22 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows2", (0,0), "ycomouth2", (0,0), "ycogout")
image yco a23 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows2", (0,0), "ycomouth4", (0,0), "ycogout")
image yco a24 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth2", (0,0), "ycogout")
image yco a25 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth4", (0,0), "ycogout")
image yco a26 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth3")
image yco a27 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth6")
image yco a28 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth6")
image yco a29 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth3")
image yco a30 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth6", (0,0), "ycotears")
image yco a31 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth2")
image yco a32 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye1", (0,0), "ycoeyebrows2", (0,0), "ycomouth3", (0,0), "ycotears")
image yco a33 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth6", (0,0), "ycotears")
image yco a34 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye2", (0,0), "ycoeyebrows2", (0,0), "ycomouth1")
image yco a35 = LiveComposite((1280, 720), (0,0), "yco1", (0,0), "ycoeye3", (0,0), "ycoeyebrows1", (0,0), "ycomouth2", (0,0), "ycoblush", (0,0), "ycotears")

image yco b1 = LiveComposite((1280, 720), (0,0), "yco2", (0,0), "ycoeye3", (0,0), "ycoeyebrows1")

###############################################################################

init python:

    PCEV_DIR = CGS_DIR + "pc_event/"

    renpy.image("light", PCEV_DIR + "light.png")
    renpy.image("pcev_bg_day", PCEV_DIR + "pc_event_bg_day.jpg")
    renpy.image("pcev_cg_night", PCEV_DIR + "pc_event_cg_night.jpg")

    renpy.image("pcev_on", PCEV_DIR + "pc_on.png")
    renpy.image("pcev_off", PCEV_DIR + "pc_off.png")

    for pc_scenes in range(1,6):
        renpy.image("pc_scene_" + str(pc_scenes), PCEV_DIR + "pc_scene_" + str(pc_scenes) + ".png")

image pcev_light:
    "light"
    block:
        linear 15 alpha 0.3
        linear 7 alpha 0.5
        linear 15 alpha 0.7
        linear 15 alpha 1.0
        repeat

image system_loading:
    PCEV_DIR + "system_loading.png"
    pos(610, 530)
    sys_loading

image depressio = "depressio.png"
image TwoFaces = "TwoFaces.png"
image TID = "TID.png"

transform sys_loading:
    rotate 0
    ease 1.5 rotate 360
    repeat
    
image pc_on_event_day = LiveComposite((1280, 720), (0,0), "pcev_bg_day", (0,0), "pcev_on")
image pc_off_event_day = LiveComposite((1280, 720), (0,0), "pcev_bg_day", (0,0), "pcev_off")
image pc5_on_event_day = LiveComposite((1280, 720), (0,0), "pcev_bg_day", (0,0), "pcev_on", (0,0), "pc_scene_5", (0,0), "snow2", (0,0), "pcev_light")
image pc5_on_event_day_blur = im.Composite((1280, 720), (0,0), im.Blur(PCEV_DIR + "pc_event_bg_day.jpg", persistent.blur_default), (0,0), im.Blur(PCEV_DIR + "pc_on.png", persistent.blur_default), (0,0),  im.Blur(PCEV_DIR + "pc_scene_5.png", persistent.blur_default), (0,0),  im.Blur(PCEV_DIR + "light.png", persistent.blur_default))
