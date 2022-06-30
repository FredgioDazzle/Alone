image first_bg = "first/bg.png"
image first_bg_gray = im.Grayscale("first/bg.png")

image yumi_animation:
    "first/1.png"
    pause 2.0
    "first/2.png"
    pause 2.0
    "first/1.png"
    repeat

image yumi_animation_gray:
    im.Grayscale("first/1.png")
    pause 2.0
    im.Grayscale("first/2.png")
    pause 2.0
    im.Grayscale("first/1.png")
    repeat

image yumi_animation2:
    "yumi_animation"
    zoom 0.7

image yumi_animation2_gray:
    "yumi_animation_gray"
    zoom 0.7

image warning = LiveComposite((1280,720), (0,0), "first_bg", (360,50), "yumi_animation2")
image warning2 = LiveComposite((1280,720), (0,0), "first_bg_gray", (360,50), "yumi_animation2_gray")