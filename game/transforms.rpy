

define wipeleft = ImageDissolve("images/transitions/wipeleft.jpg", 0.5, ramplen=64)

define wiperight = ImageDissolve("images/transitions/wiperight.jpg", 0.5, ramplen=64)

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.jpg", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.jpg", 0.5, ramplen=64),
    True])

define wiperight_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wiperight.jpg", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wiperight.jpg", 0.5, ramplen=64, ),
    True])

define eyein = ImageDissolve("images/transitions/eye.jpg", 1.0, 8, reverse=True)

define eyeout = ImageDissolve("images/transitions/eye.jpg", 1.0, 8)

define eyein_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eye.jpg", 1.0, 8, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/eye.jpg", 1.0, 8),
    True])

define eyeout_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eye.jpg", 1.0, 8),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/eye.jpg", 1.0, 8, reverse=True),
    True])

define eyeinslow_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eye.jpg", 1.0, 8, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/eye.jpg", 3.0, 8),
    True])

define eyeoutslow_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eye.jpg", 1.0, 8),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/eye.jpg", 3.0, 8, reverse=True),
    True])

define circlein = ImageDissolve("images/transitions/circle.jpg", 1.0, 8, reverse=True)

define circleout = ImageDissolve("images/transitions/circle.jpg", 1.0, 8)

define circlein_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/circle.jpg", 1.0, 8, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/circle.jpg", 1.0, 8),
    True])

define circleout_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/circle.jpg", 1.0, 8),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/circle.jpg", 1.0, 8, reverse=True),
    True])

define clockwiperight = ImageDissolve("images/transitions/clockwiperight.jpg", 1.0, ramplen=64)

define clockwipeleft = ImageDissolve("images/transitions/clockwipeleft.jpg", 1.0, ramplen=64)

define clockwiperight_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/clockwiperight.jpg", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/clockwiperight.jpg", 0.5, ramplen=64),
    True])

define clockwipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/clockwipeleft.jpg", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/clockwipeleft.jpg", 0.5, ramplen=64),
    True])

define dissolve = Dissolve(0.25)
define dissolveslow = Dissolve(1.25)
define dissolveslow2 = Dissolve(2.0)
define fadeslow = Fade(1.0, 2.0, 1.0, color='#000000')

define flash = Fade(1.0, 2.0, 1.0, color='#fff')

define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_fullslow = MultipleTransition([
    False, Dissolve(2.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])
define truewhite = MultipleTransition([
    Solid("#ffffff"), Pause(0.05),
    Solid("#ffffff")
    ])

transform transitions(x=640, z=0.82):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.94 alpha 0.00
        xcenter x yoffset -25
        ease .20 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            ease .30 xcenter x zoom z*1.00
        parallel:
            ease .30 yoffset 0 ypos 1.03

transform c51:
    transitions(160,0.70)
transform c52:
    transitions(410,0.70)
transform c53:
    transitions(630,0.70)
transform c54:
    transitions(890,0.70)
transform c55:
    transitions(1130,0.70)
transform c41:
    transitions(200,0.80)
transform c42:
    transitions(493,0.80)
transform c43:
    transitions(786,0.80)
transform c44:
    transitions(1080,0.80)
transform c31:
    transitions(240,0.80)
transform c32:
    transitions(640,0.80)
transform c33:
    transitions(1040,0.80)
transform c21:
    transitions(400,0.80)
transform c22:
    transitions(880,0.80)
transform c11:
    transitions(640,0.80)

transform imagesshow(x=640, y=0.50, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.94 alpha 0.00
        xcenter x ycenter y
        ease .18 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            ease .18 xcenter x zoom z*1.00

transform is51:
    imagesshow(160,z=0.70)
transform is52:
    imagesshow(410,z=0.70)
transform is53:
    imagesshow(630,z=0.70)
transform is54:
    imagesshow(890,z=0.70)
transform is55:
    imagesshow(1130,z=0.70)
transform is41:
    imagesshow(200,z=0.80)
transform is42:
    imagesshow(493,z=0.80)
transform is43:
    imagesshow(786,z=0.80)
transform is44:
    imagesshow(1080,z=0.80)
transform is31:
    imagesshow(240,z=0.80)
transform is32:
    imagesshow(640,z=0.80)
transform is33:
    imagesshow(1040,z=0.80)
transform is21:
    imagesshow(400,z=0.80)
transform is22:
    imagesshow(880,z=0.80)
transform is11:
    imagesshow(640,z=0.80)

transform instance(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform ins51:
    instance(160,0.70)
transform ins52:
    instance(410,0.70)
transform ins53:
    instance(630,0.70)
transform ins54:
    instance(890,0.70)
transform ins55:
    instance(1130,0.70)
transform ins41:
    instance(200,0.80)
transform ins42:
    instance(493,0.80)
transform ins43:
    instance(786,0.80)
transform ins44:
    instance(1080,0.80)
transform ins31:
    instance(240,0.80)
transform ins32:
    instance(640,0.80)
transform ins33:
    instance(1040,0.80)
transform ins21:
    instance(400,0.80)
transform ins22:
    instance(880,0.80)
transform ins11:
    instance(640,0.80)

transform zoomtalk(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -25
        ease .18 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            ease .18 xcenter x zoom z*1.05
        parallel:
            ease .15 yoffset 0

transform z51:
    zoomtalk(160,0.70)
transform z52:
    zoomtalk(410,0.70)
transform z53:
    zoomtalk(630,0.70)
transform z54:
    zoomtalk(890,0.70)
transform z55:
    zoomtalk(1130,0.70)
transform z41:
    zoomtalk(200,0.80)
transform z42:
    zoomtalk(493,0.80)
transform z43:
    zoomtalk(786,0.80)
transform z44:
    zoomtalk(1080,0.80)
transform z31:
    zoomtalk(240,0.80)
transform z32:
    zoomtalk(640,0.80)
transform z33:
    zoomtalk(1040,0.80)
transform z21:
    zoomtalk(400,0.80)
transform z22:
    zoomtalk(880,0.80)
transform z11:
    zoomtalk(640,0.80)

transform trist(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    ease .5 ypos 1.06

transform tr51:
    trist(160,0.70)
transform tr52:
    trist(410,0.70)
transform tr53:
    trist(630,0.70)
transform tr54:
    trist(890,0.70)
transform tr55:
    trist(1130,0.70)
transform tr41:
    trist(200,0.80)
transform tr42:
    trist(493,0.80)
transform tr43:
    trist(786,0.80)
transform tr44:
    trist(1080,0.80)
transform tr31:
    trist(240,0.80)
transform tr32:
    trist(640,0.80)
transform tr33:
    trist(1040,0.80)
transform tr21:
    trist(400,0.80)
transform tr22:
    trist(880,0.80)
transform tr11:
    trist(640,0.80)

transform jumping(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform j51:
    jumping(160,0.70)
transform j52:
    jumping(410,0.70)
transform j53:
    jumping(630,0.70)
transform j54:
    jumping(890,0.70)
transform j55:
    jumping(1130,0.70)
transform j41:
    jumping(200,0.80)
transform j42:
    jumping(493,0.80)
transform j43:
    jumping(786,0.80)
transform j44:
    jumping(1080,0.80)
transform j31:
    jumping(240,0.80)
transform j32:
    jumping(640,0.80)
transform j33:
    jumping(1040,0.80)
transform j21:
    jumping(400,0.80)
transform j22:
    jumping(880,0.80)
transform j11:
    jumping(640,0.80)

transform jumpingrepeat(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0
    pause 0.10
    repeat

transform jr51:
    jumpingrepeat(160,0.70)
transform jr52:
    jumpingrepeat(410,0.70)
transform jr53:
    jumpingrepeat(630,0.70)
transform jr54:
    jumpingrepeat(890,0.70)
transform jr55:
    jumpingrepeat(1130,0.70)
transform jr41:
    jumpingrepeat(200,0.80)
transform jr42:
    jumpingrepeat(493,0.80)
transform jr43:
    jumpingrepeat(786,0.80)
transform jr44:
    jumpingrepeat(1080,0.80)
transform jr31:
    jumpingrepeat(240,0.80)
transform jr32:
    jumpingrepeat(640,0.80)
transform jr33:
    jumpingrepeat(1040,0.80)
transform jr21:
    jumpingrepeat(400,0.80)
transform jr22:
    jumpingrepeat(880,0.80)
transform jr11:
    jumpingrepeat(640,0.80)

transform zoomtalkwithjump(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -23
    easeout .1 yoffset 0

transform ztj51:
    zoomtalkwithjump(160,0.70)
transform ztj52:
    zoomtalkwithjump(410,0.70)
transform ztj53:
    zoomtalkwithjump(630,0.70)
transform ztj54:
    zoomtalkwithjump(890,0.70)
transform ztj55:
    zoomtalkwithjump(1130,0.70)
transform ztj41:
    zoomtalkwithjump(200,0.80)
transform ztj42:
    zoomtalkwithjump(493,0.80)
transform ztj43:
    zoomtalkwithjump(786,0.80)
transform ztj44:
    zoomtalkwithjump(1080,0.80)
transform ztj31:
    zoomtalkwithjump(240,0.80)
transform ztj32:
    zoomtalkwithjump(640,0.80)
transform ztj33:
    zoomtalkwithjump(1040,0.80)
transform ztj21:
    zoomtalkwithjump(400,0.80)
transform ztj22:
    zoomtalkwithjump(880,0.80)
transform ztj11:
    zoomtalkwithjump(640,0.80)

transform downsweet(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .23 yoffset 0

transform dw51:
    downsweet(160,0.70)
transform dw52:
    downsweet(410,0.70)
transform dw53:
    downsweet(630,0.70)
transform dw54:
    downsweet(890,0.70)
transform dw55:
    downsweet(1130,0.70)
transform dw41:
    downsweet(200,0.80)
transform dw42:
    downsweet(493,0.80)
transform dw43:
    downsweet(786,0.80)
transform dw44:
    downsweet(1080,0.80)
transform dw31:
    downsweet(240,0.80)
transform dw32:
    downsweet(640,0.80)
transform dw33:
    downsweet(1040,0.80)
transform dw21:
    downsweet(400,0.80)
transform dw22:
    downsweet(880,0.80)
transform dw11:
    downsweet(640,0.80)

transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    ease .65 xcenter x

transform l51:
    leftin(160,0.70)
transform l52:
    leftin(410,0.70)
transform l53:
    leftin(630,0.70)
transform l54:
    leftin(890,0.70)
transform l55:
    leftin(1130,0.70)
transform l41:
    leftin(200,0.80)
transform l42:
    leftin(493,0.80)
transform l43:
    leftin(786,0.80)
transform l44:
    leftin(1080,0.80)
transform l31:
    leftin(240,0.80)
transform l32:
    leftin(640,0.80)
transform l33:
    leftin(1040,0.80)
transform l21:
    leftin(400,0.80)
transform l22:
    leftin(880,0.80)
transform l11:
    leftin(640,0.80)

transform rightin(x=640, z=0.80):
    xcenter 1200 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    ease .65 xcenter x

transform r51:
    rightin(160,0.70)
transform r52:
    rightin(410,0.70)
transform r53:
    rightin(630,0.70)
transform r54:
    rightin(890,0.70)
transform r55:
    rightin(1130,0.70)
transform r41:
    rightin(200,0.80)
transform r42:
    rightin(493,0.80)
transform r43:
    rightin(786,0.80)
transform r44:
    rightin(1080,0.80)
transform r31:
    rightin(240,0.80)
transform r32:
    rightin(640,0.80)
transform r33:
    rightin(1040,0.80)
transform r21:
    rightin(400,0.80)
transform r22:
    rightin(880,0.80)
transform r11:
    rightin(640,0.80)

transform alphaleftin(x=640, z=0.80):
    xcenter -60 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 0.00 subpixel True
    ease .65 xcenter x alpha 1.00

transform al51:
    alphaleftin(160,0.70)
transform al52:
    alphaleftin(410,0.70)
transform al53:
    alphaleftin(630,0.70)
transform al54:
    alphaleftin(890,0.70)
transform al55:
    alphaleftin(1130,0.70)
transform al41:
    alphaleftin(200,0.80)
transform al42:
    alphaleftin(493,0.80)
transform al43:
    alphaleftin(786,0.80)
transform al44:
    alphaleftin(1080,0.80)
transform al31:
    alphaleftin(240,0.80)
transform al32:
    alphaleftin(640,0.80)
transform al33:
    alphaleftin(1040,0.80)
transform al21:
    alphaleftin(400,0.80)
transform al22:
    alphaleftin(880,0.80)
transform al11:
    alphaleftin(640,0.80)

transform alpharightin(x=640, z=0.80):
    xcenter 1000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 0.00 subpixel True
    ease .65 xcenter x alpha 1.00

transform ar51:
    alpharightin(160,0.70)
transform ar52:
    alpharightin(410,0.70)
transform ar53:
    alpharightin(630,0.70)
transform ar54:
    alpharightin(890,0.70)
transform ar55:
    alpharightin(1130,0.70)
transform ar41:
    alpharightin(200,0.80)
transform ar42:
    alpharightin(493,0.80)
transform ar43:
    alpharightin(786,0.80)
transform ar44:
    alpharightin(1080,0.80)
transform ar31:
    alpharightin(240,0.80)
transform ar32:
    alpharightin(640,0.80)
transform ar33:
    alpharightin(1040,0.80)
transform ar21:
    alpharightin(400,0.80)
transform ar22:
    alpharightin(880,0.80)
transform ar11:
    alpharightin(640,0.80)

transform hidetr(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        ease .25 zoom z*0.88 alpha 0.00 yoffset -25

transform hidedown(z=0.80):
    subpixel True
    on hide:

        easeout .60 yoffset 750

transform lhide:
    subpixel True
    on hide:
        easeout .50 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout .40 xpos 1900

transform alhide:
    subpixel True
    on hide:
        easeout .50 xcenter -300 alpha 0.00

transform arhide:
    subpixel True
    on hide:
        easeout .50 xpos 1700 alpha 0.00

transform superclose(z=0.80, y=500, x=640):
    subpixel True
    xcenter x
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform ssc22:
    superclose(0.80, 500, 0.80)
transform ssc21:
    superclose(0.80, 500, 0.30)
transform ssc11:
    superclose(0.80, 500, 640)

transform superclose2(z=0.80, y=720, x=640):
    subpixel True
    xcenter x
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform ssc222:
    superclose(0.80, 500, 0.80)
transform ssc221:
    superclose(0.80, 500, 0.30)
transform ssc211:
    superclose(0.80, 500, 640)

transform close(z=0.60, y=450, x=640):
    subpixel True
    xcenter x
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform cc33:
    close(0.60, 450, 0.90)
transform cc32:
    close(0.60, 450, 0.50)
transform cc31:
    close(0.60, 450, 0.10)
transform cc22:
    close(0.60, 450, 0.75)
transform cc21:
    close(0.60, 450, 0.25)
transform cc11:
    close(0.60, 450, 640)

