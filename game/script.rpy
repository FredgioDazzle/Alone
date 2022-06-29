image end_demo = Text(_("Continuara...\nGracias por jugar Lonely Imagination"), style="demo_text", xalign=0.5, yalign=0.5)

style demo_text:
    size 34
    color "#ffffff"
    text_align 0.5
    outlines []

label start:
    
    if player == "":
        $ player =  _("Hiroki")
        $ persistent.playername = player
        
    stop music fadeout 2.0
    with dissolve_scene_full
    
    init python:
        config.keymap['dismiss'].append('mouseup_1')
    
    $ j_name = "???"
    $ i_name = "???"
    $ e_name = "???"
    $ y_name = "???" 
    #$ h_name = "???"
    #$ s_name = "???"
    $ k_name = _("Profesor")
    #$ ay_name = _("Profesora")
    #$ sg_name = _("Profesor")
    #$ na_name = "???"
    #$ mi_name = "???"
    $ ko_name = "???"
    $ nat_name = "???"
    #$ ao_name = "???"

    $ yumi_perspective = 0
    $ cap = 0

    $ quick_menu = True
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ _dismiss_pause = config.developer
    $ persistent.splash_random = True
    
    if persistent.playthrough == 0:

        $ cap = 0
        if persistent.language == "english":
            call ch0_en from _call_ch0_en
        else:
            call ch0 from _call_ch0

        $ cap = 1
        if persistent.language == "english":
            call ch1_en from _call_ch1_en
        else:
            call ch1 from _call_ch1

        ##Perdón pero esta versión Lonely solo tiene dos capitulos
label endgame:
    
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end_demo
    with dissolve_scene_full
    pause 4.0
    $ quick_menu = True
    return