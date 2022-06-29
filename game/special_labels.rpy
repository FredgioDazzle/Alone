
label after_load:

    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    
    if persistent.firstload == None:
        jump firstload

label firstload:

    if persistent.playthrough == 0 and not persistent.firstload:
        $ persistent.firstload = True
        call screen dialog(_("Consejo: Puedes usar el boton \"Saltar\" para \nsaltar el texto que ya viste."), ok_action=Return())
    return

label firstRun:

    scene white with dissolve
    pause 0.25
    scene warning2 with dissolveslow
    $ quick_menu = False
    "Este juego contiene lenguaje no apto para menores de 18 años."
    "No recomendamos jugar [config.name!t] si sufre de..."
    "Depresión o ansiedad, estás dos condiciones podrán afectarlo de una u otra manera."
    "[config.name!t] contiene arte que es propiedad intelectual de los artistas Min-chi y NoranekoGames."
    if persistent.language == "english":
        "The English translation is not verified and it is not known if it is 100% correct, do not forget to notify us of any interpretation error :)"
    menu:
        "Al jugar [config.name!t], acepta tener 18 años de edad y que no padece ninguna de las condiciones ya mencionadas que pueden afectar su experiencia jugando este juego."
        "De acuerdo.":
            pass
    window hide(Dissolve(.2))
    scene warning with dissolveslow
    $ persistent.firstRun = True
    pause 2.0
    scene white with dissolveslow
    jump splashscreen

label readonly:
    scene black
    "No se a podido acceder a ciertos archivos del juego porque estás intentando ejecutarlo desde una ubicación de sólo lectura."
    "Mueva el juego a otra ubicación accesible y vuelva a intentarlo."
    $ renpy.quit()
    return