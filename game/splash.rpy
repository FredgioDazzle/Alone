
init -100:
    $ secretcode = renpy.random.randint(1000, 9999)  

init python:
    splash_message_default = "Este juego no es adecuado para niños\nTampoco para personas con depresión y ansiedad."
    splash_message_default_en = "This game is not suitable for children\nNor for people with depression and anxiety."
    
    splash_messages = [
    "Este juego no es adecuado para niños\nTampoco para personas con depresión y ansiedad.",
    "Inspirado por Doki Doki Literature Club!",
    "La banda sonora del juego está compuesta por Joack Kenny\nApóyalo en Youtube :)",
    "Este juego es libre y de código abierto",
    "Apóyanos en itch.io",
    "Mis juegos favoritos son:\nFriday Night Funkin', Geometry Dash\nFive Nights At Freddy's y Doki Doki Literature Club!\n¿Cuales son los tuyos?",
    "Relájate con la buena música de Joack Kenny\nAl estilo del Chill Out.",
    "Ren'Py es amor, Ren'Py es vida.",
    ":)",
    "Nuestras redes sociales están en el archivo 'Read' en el directorio del juego."
    ]

    splash_messages_en = [
    "This game is not suitable for children\n Nor for people with depression and anxiety.",
    "Inspired by Doki Doki Literature Club!",
    "The soundtrack of the game is composed by Joack Kenny\nSupport him on Youtube :)",
    "This game is free and open source",
    "Support us on Itch.io",
    "My favorites games are:\nFriday Night Funkin', Geometry Dash\nFive Nights At Freddy's and Doki Doki Literature Club!\nWhat are yours?",
    "Relax with the good music of Joack Kenny\nIn the style of Chill Out.",
    "Ren'Py is love, Ren'Py is life.",
    ":)",
    "Our social networks are in the 'Read' file in the game directory."
    ]

    secret_splash_message = [
    "[secretcode]",
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

style splash_text:
    size 28
    color "#000"
    text_align 0.5
    outlines []

style splash_text:
    variant "small"
    size 33

image splash:
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5
    
label splashscreen:

    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)

        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.firstRun:
            $ quick_menu = False
            scene black
            menu:
                "Se encontró un guardado previo. ¿Te gustaría borrarlo y empezar desde cero?"
                "Si, borrar los datos existentes.":
                    "Borrando datos...{nw}"
                    python:
                        DeleteData()
                "No, dejar todo como está.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")
    scene white
    stop music
    
    $ config.allow_skipping = False

    if persistent.firstRun == None:
        scene black
        stop music
        menu:
            "Selecciona tú idioma/Select your language."
            "Español.":
                $ renpy.change_language(None)
            "English.":
                $ renpy.change_language("english")
        pause 2.0
        jump firstRun
    else:
        with Pause(0.5)
    
    play music m1 loop
    if persistent.language == "english":
        $ splash_message = splash_message_default_en
    else:
        $ splash_message = splash_message_default
    show splash with Dissolve (0.5, alpha=True)
    pause 2.5
    hide splash with Dissolve (0.5, alpha=True)
    if persistent.splash_random == True:
        if persistent.language == "english":
            $ splash_message = renpy.random.choice(splash_messages_en)
        else:
            $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0 
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ persistent.firstrunS = True
    $ config.allow_skipping = True
    
    init python:
        config.keymap['dismiss'].append('mouseup_1')

    return
