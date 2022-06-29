init -1 python:

    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")
    def DefaultName():
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")
    def DeleteData():
        delete_all_saves()
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.utter_restart()

screen dialog(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action
            
screen language(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        vbox:
        
            style_prefix "radio"

            textbutton _("Español") action SetVariable("persistent.language", None), Language(None)
            textbutton _("English") action SetVariable("persistent.language", "english"), Language("english")

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Ok") action ok_action

screen name_input(message, ok_action, defaultname_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action, defaultname_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow _("ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz")

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Usar nombre predeterminado") action defaultname_action
            textbutton _("Ok") action ok_action


screen aparience_notify(message, ok_action):

    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5
        label _("{size=+1}Apariencia"):
            style "confirm_prompt"
            xalign 0.0

        hbox:
            xalign 0.0
            spacing 100
            hbox:
                label _("Permitir el desenfocado")
                textbutton _("?"):
                    action Show(screen="dialog", message=_("Esto permite mejorar la apariencia del juego durante el mismo\nDesenfocando ciertas áreas que sean compatibles con esto como algunos CG, el BG cuando aparece la pantalla NVL y otras áreas.\nNota: En algunos dispositivos puede causar Lag."), ok_action=Hide(screen="dialog")) 
            vbox:
                textbutton _("Sí"):
                    action SetVariable("persistent.blur_on", True)
                textbutton _("No"):
                    action SetVariable("persistent.blur_on", None)
        
        label _("Ajusta el tiempo de duración de las notificaciones"):
            style "confirm_prompt"
            xalign 0.0
        hbox:
            xalign 0.0
            spacing 100

            textbutton "3.25s":
                action SetVariable("persistent.time_notify", 3.25)
            textbutton "5s":
                action SetVariable("persistent.time_notify", 5)
            textbutton "8s": 
                action SetVariable("persistent.time_notify", 8)
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Ok") action ok_action