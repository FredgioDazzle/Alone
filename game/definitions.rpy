
transform gout_appear:
    alpha 0.0 yoffset -10 
    ease 1.12 yoffset 0 alpha 1.0

init python:

    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_los_files():
        import os
        try:os.remove(config.basedir + "/game/archive.los")
        except: pass
        try:os.remove(config.basedir + "/game/value.los")
        except: pass

    """Esta función define las partes del cuerpo de X personaje, no es capaz de definir las expresiones."""
    def make_sprites(char="", char_dir="",char_short="", head_num=1, eyebrows_num=1, eye_num=1, eyeexp_num=1, mouth_num=1, tears_num=1, blush_num=1, glasses=False, gout=True, body_num=True):
        """El nombre del personaje debe estar en minuscula."""
        if char == "":
            renpy.error(_("Es necesario colocar el nombre del personaje."))
        if char_dir == "" or char_dir == None:
            sprite = "/sprites/" + char + "/"
        else:
            sprite = "/sprites/" + char + "/" + char_dir + "/"
        """No se porque pero Ren'Py no toma en cuenta el numero que se coloca en el ciclo "for", es decir hay "10" heads pero Ren'Py
        solo toma en cuenta "9" y por eso se le suma un número más a los ciclos."""
        if head_num == 1:
            if renpy.exists("images" + sprite + "Head.png"):
                renpy.image(char_short + "head", sprite + "Head.png") #jnhead
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'head.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        if head_num == None:
            pass
        if head_num > 1:
            for heads in range(1, head_num + 1):
                if renpy.exists("images" + sprite + "Head" + str(heads) + ".png"):
                    renpy.image(char_short + "head" + str(heads), sprite + "Head" + str(heads) + ".png") #jnhead1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'head_") + str(heads) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
       
        for eyebrowss in range(1, eyebrows_num + 1):
            if renpy.exists("images" + sprite + "eyebrows_" + str(eyebrowss) + ".png"):
                renpy.image(char_short + "eyebrows" + str(eyebrowss), sprite + "eyebrows_" + str(eyebrowss) + ".png") #jneyebrows1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eyebrows_") + str(eyebrowss) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
            
        for eyes in range(1, eye_num + 1):
            if renpy.exists("images" + sprite + "eye_" + str(eyes) + ".png"):
                renpy.image(char_short + "eye" + str(eyes), sprite + "eye_" + str(eyes) + ".png") #jneye1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eye_") + str(eyes) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
            
        if eyeexp_num >= 1:
            for eyeexps in range(1, eyeexp_num + 1):
                if renpy.exists("images" + sprite + "eye_exp" + str(eyeexps) + ".png"):
                    renpy.image(char_short + "eyeexp" + str(eyeexps), sprite + "eye_exp" + str(eyeexps) + ".png") #jneyeexp1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eye_exp") + str(eyeexps) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        elif eyeexp_num == None:
            pass

        for mouths in range(1, mouth_num + 1):
            if renpy.exists("images" + sprite + "mouth_" + str(mouths) + ".png"):
                renpy.image(char_short + "mouth" + str(mouths), sprite + "mouth_" + str(mouths) + ".png") #jnmouth1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'mouth_") + str(mouths) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        if tears_num == 1:
            if renpy.exists("images" + sprite + "tears.png"):
                renpy.image(char_short + "tears", sprite + "tears.png") #jntears
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'tears.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        if tears_num == None:
            pass
        if tears_num > 1:
            for tearss in range(1, tears_num + 1):
                if renpy.exists("images" + sprite + "tears" + str(tearss) + ".png"):
                    renpy.image(char_short + "tears" + str(tearss), sprite + "tears" + str(tearss) + ".png") #jntears1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'tears" + str(tearss) + ".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        if blush_num == 1:
            if renpy.exists("/images" + sprite + "blush.png"):
                renpy.image(char_short + "blush", sprite + "blush.png") #jnblush
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'blush.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        if blush_num == None:
            pass
        if blush_num > 1:
            for blushs in range(1, blush_num + 1):
                if renpy.exists("/images" + sprite + "blush" + str(blushs) + ".png"):
                    renpy.image(char_short + "blush" + str(blushs), sprite + "blush" + str(blushs) + ".png") #jnblush1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'blush") + str(blushs) + _("png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        if glasses == True:
            if renpy.exists("/images" + sprite + "glasses.png"):
                renpy.image(char_short + "glasses", sprite + "glasses.png") #koglasses
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'glasses.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        if gout == True:
            if renpy.exists("/images" + sprite + "gout.png"):
                renpy.image(char_short + "gout", At(sprite + "gout.png", gout_appear)) #kogout
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'gout.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        if body_num == True:
            if renpy.exists("/images" + sprite + "1.png"):
                renpy.image(char_short + "1", sprite + "1.png") #ko1
                if renpy.exists("/images" + sprite + "2.png"):
                    renpy.image(char_short + "2", sprite + "2.png") #ko2
                else:
                    pass
                    if renpy.exists("/images" + sprite + "3.png"):
                        renpy.image(char_short + "1", sprite + "1.png") #ko3
                    else:
                        pass
            else:
                for bodys in range(2):
                    renpy.image(char_short + str(bodys) + "al", sprite + str(bodys) + "_a_l.png")
                    renpy.image(char_short + str(bodys) + "ar", sprite + str(bodys) + "_a_r.png")
                    renpy.image(char_short + str(bodys) + "bl", sprite + str(bodys) + "_b_l.png")
                    renpy.image(char_short + str(bodys) + "br", sprite + str(bodys) + "_b_r.png")
                    if renpy.exists("/images" + sprite + str(bodys) + "_c.png"):
                        renpy.image(char_short + str(bodys) + "c", sprite + str(bodys) + "_c.png")
                    else:
                        renpy.image(char_short + str(bodys) + "cl", sprite + str(bodys) + "_c_l.png")
                        renpy.image(char_short + str(bodys) + "cr", sprite + str(bodys) + "_c_r.png")
        else:
            for bodys in range(body_num + 1):
                renpy.image(char_short + str(bodys) + "al", sprite + str(bodys) + "_a_l.png")
                renpy.image(char_short + str(bodys) + "ar", sprite + str(bodys) + "_a_r.png")
                renpy.image(char_short + str(bodys) + "bl", sprite + str(bodys) + "_b_l.png")
                renpy.image(char_short + str(bodys) + "br", sprite + str(bodys) + "_b_r.png")
                if renpy.exists("/images" + sprite + str(bodys) + "_c.png"):
                    renpy.image(char_short + str(bodys) + "c", sprite + str(bodys) + "_c.png")
                else:
                    renpy.image(char_short + str(bodys) + "cl", sprite + str(bodys) + "_c_l.png")
                    renpy.image(char_short + str(bodys) + "cr", sprite + str(bodys) + "_c_r.png")

python early:
    import singleton
    me = singleton.SingleInstance()

#Los personajes que empiezan con "#" no se usan en esta versión del juego y no deben ser descomentados
define narrator = Character(ctc="ctc", ctc_position="fixed")
define e = DynamicCharacter("e_name", image="emi" , what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#b0e3fa")
define k = DynamicCharacter("k_name", image="kaito", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#546cfa")
define i = DynamicCharacter("i_name", image="issei", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#af6003")
define j = DynamicCharacter("j_name", image="jenni", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#06ed00")
define y = DynamicCharacter("y_name", image="yumi", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#5207b9")
#define h = DynamicCharacter("h_name", image="hana", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#f30606")
define ay = DynamicCharacter("ay_name", image="ayami", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#fe182f")
#define sg = DynamicCharacter("sg_name", image="sergio", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#1e0dd8")
define nat = DynamicCharacter("nat_name", image="natsumi", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#d1c113")
define ko = DynamicCharacter("ko_name", image="kohana", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#f7feff")
#define na = DynamicCharacter("na_name", image="nanami", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#9e04d5")
#define mi = DynamicCharacter("mi_name", image="miu", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#f81bca")
#define ao = DynamicCharacter('ao_name', image="arato", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#0fc531")
#define s = DynamicCharacter('s_name', image="sakura", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#fc47ed")
define pr = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#b0e3fa")
#define prh = Character("[h_name] & [player]" , what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#b0e3fa")
define al = Character(_("Todos"), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#737373")
define ale = Character(_("Estudiantes"), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#737373")
define ji = Character(_("Issei & Jenni"), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#38ed00")
define girl = Character(_("Chica"), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#5f5f5f")
define boy = Character(_("Chico"), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#5f5f5f")
#define mom = DynamicCharacter("mom_name", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#ed06c9")
#define dad = DynamicCharacter("dad_name", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#13168c")
define unk = Character("???", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_color="#5f5f5f")

define nvle = DynamicCharacter("e_name", image="emi", kind=nvl, who_color="#b0e3fa")
define nvly = DynamicCharacter("y_name", image="yumi", kind=nvl, who_color="#5207b9")
define nvlh = DynamicCharacter("h_name", image="hana", kind=nvl, who_color="#f30606")
define nvli = DynamicCharacter("i_name", image="issei", kind=nvl, who_color="#af6003")
define nvlj = DynamicCharacter("j_name", image="jenni", kind=nvl, who_color="#06ed00")
define nvlpr = DynamicCharacter('player', kind=nvl, who_color="#b0e3fa")
define nvlmom = DynamicCharacter("mom_name", kind=nvl, who_color="#ed06c9")
define nvldad = DynamicCharacter("dad_name", kind=nvl, who_color="#f50720")

#Default names
#Estas variables contienen los nombres por defecto de los personajes, las variables que empiezan por # no se usan en esta versión
#del juego y no deben ser descomentadas.
default e_name = _("Emi")
default i_name = _("Issei")
default j_name = _("Jenni")
default y_name = _("Yumi")
#default h_name = _("Hana")
#default na_name = _("Nanami")
default k_name = _("Kaito")
#default ay_name = _("Ayami")
#default sg_name = _("Sergio")
#default s_name = _("Sakura")
#default mom_name = _("Kazumi")
#default dad_name = _("Seiya")
default nat_name = _("Natsumi")
default ko_name = _("Kohana")
#default ao_name = _("Arato")

image black = "#000000"
image white = "#ffffff"
image ctc:
    xalign 0.81 yalign 0.98 yoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 yoffset 0
        pause 1.0
        easein 0.75 alpha 0.0 yoffset -5
        repeat
image logo:
    2.0
    "gui/logo.png"
    xcenter 0.5
    ycenter 0.22
    logo_fadeout

image menu_fade:
    "white"
    menu_fadeout

image menu_bg:
    topleft
    "gui/menu_bg.jpg"
    menu_bg_move
    
image yumi_art:
    subpixel True
    "gui/yumi_art.png"
    xcenter 100
    ycenter 495
    zoom 0.80
    Art_move(100, -260)

image issei_art:
    subpixel True
    "gui/issei_art.png"
    xcenter 280
    ycenter 335
    zoom 0.60
    Art_move(290, -400)

image jenni_art:
    subpixel True
    "gui/jenni_art.png"
    xcenter 980
    ycenter 350
    zoom 0.57
    Art_move(990, 450)

image hana_art:
    subpixel True
    "gui/hana_art.png"
    xcenter 1120
    ycenter 540
    zoom 0.92
    Art_move(1150, 320)

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        time 1.500
        ease 1.7 xoffset -100 yoffset -170
    parallel:
        xpan 0
        linear 52 xpan 360
        repeat

transform Art_move(x,  x2):
    subpixel True
    alpha 0.0
    xoffset x2
    time 1.0
    parallel:
        pause 0.75
        ease 1.7 xoffset 0 xpos x alpha 1.0

transform menu_fadeout:
    easeout 0.90 alpha 0

transform logo_fadeout:
    alpha 0.0
    easeout 0.90 alpha 1.0

image vignette0 = im.MatrixColor("gui/vignette.png", im.matrix.opacity(0.8))

image vignette1:
    "vignette0"
    block:
        ease 0.5 alpha 0.4
        pause 0.2
        ease 1 alpha 1.0
        pause 1
        repeat

#Others variables
#Estás variables contienen valores que controlan ciertos puntos del juego, las variables que empiezan por # no se usan en esta versión
#del juego y no deben ser descomentadas.

default persistent.playername = ""
default player = persistent.playername
default persistent.browsersearch = ""
default search = ""
define _dismiss_pause = config.developer
define config.mouse = None
default allow_skipping = True
default persistent.playthrough = 0
default persistent.firstload = None
default basedir = config.basedir
default cap = 0
default persistent.selectevent = 0
default persistent.investigationcomp = 0
default persistent.first_browser = 0
define others = 0
default persistent.splash_random = False
#define roomsclean = 0
#define yumibathfinish = None
#define yumisleephm = 0
#define cleanfirst = 0
#define yumiroomclean = 0
#define yumilivingroomclean = 0
#define yumikitchenclean = 0
#define yumibathclean = 0
define yumi_perspective = 0
#define friendspartych4 = 0
#define special1 = 0
#define persistent.streetdecision = 0
#define persistent.finals = 0
#define persistent.act1final = 0
#define persistent.act2 = 0
#define persistent.nanamiresidence = None
define -1 persistent.time_notify = 3.25
define -1 persistent.blur_default = 1.5
define -1 persistent.blur_on = True
#define response_time = None
#define progress = 0
#define GoodResponses = 0
#define BadResponses = 0
#define QUESTIONS = 10
#define question = ""
#define persistent.workgame_quest = 0
#define workgamewinner = None
define -3 HA = None
define -3 ER = None
define config.developer = "auto"
#define config.enable_language_autodetect = False