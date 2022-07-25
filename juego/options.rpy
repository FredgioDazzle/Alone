## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Lonely Imagination")

##Esta variable muestra el estado actual del juego Alpha o BETA
##Los números que le siguen a el estado del juego osea "_1" significa
##Que el juego podrá o no tener varias versiones según el estado en el que este.

define game_status = "Alpha_1"

define renpyversionl = renpy.version().split()[1]

## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para esconder el título.

define gui.show_name = True

## Versión del juego.

define config.version = "0.1"

## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""Lonely Imagination es un videojuego libre y de código abierto creado por Quetzalcoutl, Joack Kenny y Neto Ilutra

    El código fuente del juego, está disponible en {a=https://github.com/QuetzalcoutlDev/Alone/}{color=#7a7b8d}GitHub{/color}{/a}

    Apóyanos en {a=https://quetzalcoutl.itch.io//Alone}{color=#cf2d9f}Itch.io{/color}{/a}

        {a=https://twitter.com/ElQuetzalcoutl}{color=#2dbacf}@ElQuetzalcoutl{/color}{/a}

        {a=https://youtube.com/channel/UC8XkxdSKbDkxRWPPpImD_Ng}{color=#ff0000}JoackKenny{/color}{/a}

        {a=https://youtube.com/channel/UCHsWBmT-NCGmmAG1sVQe23g}{color=#ff0000}NetoIlutra{/color}{/a}

    Este juego usa arte que pertenece a los siguientes artistas:

        {a=https://twitter.com/NoranekoGames}{color=#2dbacf}@NoranekoGames{/color}{/a}

        {a=https://min-chi.material.jp/}{color=#5fd016}Min-chi{/color}{/a}

    Este juego está hecho con mucho cariño, no olvides eso :)

    Para más información lea el archivo "READ.md"
""")

## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "Alone"
define build.directory_name = "Lonely_Imagination-" + str(config.version)

## Sonidos y música ############################################################

## Estas tres variables controlan los mezcladores mostrados por defecto al
## jugador. Ajustar alguno a 'False' para esconderlo.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Para permitir al usuario probar el volumen de los canales de sonido o voz,
## descomenta la línea más abajo y ajústala a un sonido de ejemplo.

define config.sample_sound = "audio/sfx/sample-sound.ogg"
# define config.sample_voice = "audio/sfx/sample-voice.ogg"


## Descomenta la línea siguiente para ajustar un archivo de audio que sonará en
## el menú principal. Este archivo seguirá sonando en el juego hasta que sea
## detenido o se reproduzca otro archivo.

define config.main_menu_music = audio.m1


## Transiciones ################################################################
##
## Estas variables ajustan transiciones usadas ante ciertos eventos. Cada
## variable debe indicar una transición o bien 'None', cuando no se desea usar
## ninguna transición.

## Entrar o salir del manú del juego.

define config.enter_transition = None
define config.exit_transition = None

## Entre pantallas del menú del juego.

define config.intra_transition = dissolve
## Tras la carga de una partida

define config.after_load_transition = dissolve

## Transición de acceso al menú principal tras finalizar el juego.

define config.end_game_transition = fade

## No existe la variable que ajusta la transición cuando el juego comienza. Para
## ello se usa la sentencia 'with' al mostrar la escena inicial.


## Gestión de ventanas #########################################################
##
## Esto controla cuándo se muestra la ventana de diálogo. Si es "show", es
## siempre visible. Si es "hide", solo se muestra cuando hay diálogo presente.
## Si es "auto", la ventana se esconde antes de las sentencias 'scene' y se
## muestra de nuevo cuando hay diálogo que presentar.
##
## Una vez comenzado el juego, esto se puede ajustar con las sentencias "window
## show", "window hide", y "window auto".

define config.window = "auto"

## Transiciones usadas para mostrar o esconder la ventana de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 50
define config.rollback_enabled = config.developer
define config.allow_skipping = True

## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 15

default preferences.music_volume = 0.7
default preferences.sfx_volume = 1.00

## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "Alone"

## Ícono #######################################################################
##
## El ícono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"

define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"
define config.nvl_adv_transition = Dissolve(.2)

## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:

    ## Las funciones siguientes toman patrones de archivos. No son relevantes
    ## las mayúsculas o minúsculas. Son relativos al directorio base, con o sin
    ## una / inicial. Si corresponden más de un patrón, se usa el primero.
    ##
    ## En un patrón:
    ##
    ## / es el separador de directorios.
    ##
    ## * corresponde a todos los carácteres, excepto el separador de
    ##   directorios.
    ##
    ## ** corresponde a todos los carácteres, incluynedo el separador de
    ##    directorios.
    ##
    ## Por ejemplo, "*.txt" corresponde a los archivos .txt en el directorio
    ## de base, "game/**.ogg" corresponde a los archivos .ogg del directorio
    ## 'game' y sus subdirectorios y "**.psd" corresponde a los archivos .psd en
    ## cualquier parte del proyecto.

    ## Clasifica archivos como 'None' para excluirlos de la distribución.

    ## Para archivar, se clasifican como 'archive'.

    ## No hay nada que esconder, ¿Verdad?, no descomentes las siguientes lineas 
    #build.archive("scripts", "all")
    #build.archive("images", "all")
    #build.archive("audio", "all")
    #build.archive("fonts", "all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.svg', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.gitignore', None)

    build.include_old_themes = False

    ## Los archivos que corresponden a patrones de documentation se duplican en
    ## la distribución de mac; aparecerán en los archivos app y zip.

    build.documentation('*.html')
    build.documentation('*.txt')

## Es necesaria una clave de licencia Google Play para descargar archivos de
## expansión y realizar compras en la aplicación. Se puede encontrar en la
## página "Services & APIs" de la consola de desarrollador de Google Play.

# define build.google_play_key = "..."


## Los nombres de usuario y de proyecto asociados con un proyecto itch.io,
## separados por una barra.

define build.itch_project = "fredgiodazzle/alone"
