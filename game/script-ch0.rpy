label ch0:

    $ persistent.splash_random = True
    scene hiroki_room with dissolveslow2
    window auto
    play music a1 loop fadein 2.0
    $ quick_menu = True
    "...."
    "{i}*bostezo*{/i}"
    "Me despierto como cualquier otro día." 
    "Me preparo para ir a la escuela con una meta a lograr..."
    "Conseguir una novia antes de que termine mi último año en la escuela y no terminar siendo el chico virgen que se cree guapo y que nunca ha conseguido una novia en la escuela."
    "Desde hace años tengo problemas para hablar con una chica, mi confianza se desvanece cuando hablo con una, siento que es normal en mí."
    "Bueno, pero no tengo que pensar negativamente."
    "Siempre hay que tener pensamientos positivos, hoy será el día en el que me le declarare a una de las chicas más lindas y por supuesto será a Hana Junko."
    "La chica más hermosa, popular e inteligente de toda la escuela."
    "Bueno..."
    "Así la consideran por su forma de ser."
    "No es una chica que se cree mejor que los demás."
    "Y es por eso que muchos se sienten atraídos por ella."
    "Incluyendo a otras chicas y por supuesto..."
    "Yo."
    "Ella es una de mis amigas de la infancia, comencé a sentirme atraído por ella hasta hace un par de años."
    "Ella no sabe eso aún."
    "Y por eso intentare decírselo hoy."
    "No soy de esos chicos responsables."
    "Digo, soy del tipo olvidadizo y puede ser que ni siquiera recuerde el ir a hablar con ella hoy."
    "{i}*suspiro*{/i}"
    "Pero el solo pensar en ella..."
    window hide(None) 
    play audio punch
    scene hiroki_room with hpunch
    "No, no pienses en cosas raras."
    "No estás tan desesperado por conseguir una novia."
    "..."
    "{cps=40}Bueno...{/cps}{nw=2.0}"
    stop music fadeout 1.0
    play audio knock
    pause 1.2
    $ e_name = "???"
    "Alguien toca a mi puerta..."
    "¿Enserio?{w=2}, ¿Tan temprano?"
    e "Hermanito vas a llegar tarde."
    "¿Tarde?{w=2.0}, ¿Tarde para qué?"
    e "Si no te levantas ahora..."
    e "Se te va a hacer tarde para ir a la escuela."
    "Un momento..."
    "..."
    "¡QUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!{nw}"
    play music a2 loop fadein 2.0
    pr "¡Cielos!"
    pr "La había olvidado{w=2.0}, se me hace tarde."
    "Rápidamente me levanto de la cama a ponerme mi uniforme."
    pr "¿Dónde puse mis zapatos?"
    "Después de unos minutos de búsqueda, al fin los encuentro."
    e "Hermanito, ¿No piensas darte un baño?"
    pr "Cielos{w=2.0}, ¿Por qué hay tantos pasos para ir a la escuela?"
    "Después de haberme puesto el uniforme y los zapatos, tengo que desvestirme y trazar mi camino hacia el baño."
    "{i}*suspiro*{/i}"
    "Enserio voy llegar a tarde."
    window hide(Dissolve(.2))
    pause 3.0
    window auto
    "Odio bañarme en las mañanas el agua está muy fría."
    scene black with dissolve
    pause 1.0
    "Después de bañarme, me dirijo a mi habitación a ponerme de nuevo mi uniforme y mis zapatos."
    scene hiroki_room with wipeleft
    "Otra vez listo, si me apresuro podre llegar temprano."
    "Salgo de mi habitación y me dirijo a la sala."
    scene hiroki_livingroom with wipeleft
    show emi nc02 at c11
    e "Hola hermanito, ¿Ya te bañaste?"
    show emi nc01
    pr "Sí, ya me bañé, y por tu culpa voy a llegar tarde."
    show emi dc03
    "Ella es mi hermana menor, Emi."
    $ e_name = _("Emi")
    "Que por suerte esta semana no tuvo escuela, y se quedó en casa." 
    e nc02 "¿Estás listo para desayunar?"
    show emi nc01 
    pr "Sí, pero me lo voy a llevar, se me hace tarde."
    e n1c03 "Okey ya te lo preparo, solo no te quejes cuando se te enfrié."
    show emi at hidetr
    hide emi 
    pr "Es el precio que hay que pagar para no llegar tarde."
    window hide(Dissolve(.2))
    pause 2.0
    window auto
    show emi nc01 at c11
    "Después de un rato Emi me entrega el desayuno."
    pr "Bueno, ya me voy."
    e nc02 "Okey."
    e "Te amo."
    "{i}*suspiro*{/i}"
    pr "Emi ya te lo dije muchas veces, somos hermanos."
    show emi dc04 at j11
    e "Awwww, pero no tiene nada de malo que una hermana le diga {i}'Te amo'{/i} a su hermano."
    show emi dc01
    pr "No lo tiene, pero tú lo usas de otra forma y no me gusta."
    e dc06 "Entonces, ¿Nunca seré tu esposa?"
    show emi dc01
    pr "No y me harás llegar tarde."
    "Salgo rápidamente del apartamento y me dirijo a la escuela."
    show emi at hidetr
    hide emi
    scene black with wipeleft
    pause 0.5
    play audio dooropen
    scene apartment_exterior with wipeleft
    stop music fadeout 2.0
    window auto
    "Amigo, enserio voy a llegar tarde."
    "Tendré que correr."
    pause 1.0
    scene schoolen with wipeleft
    "Después de unos minutos, consigo llegar."
    "No sé si a tiempo."
    "Pero siento que mi pecho va a explotar."
    "Me falta el aire."
    "Corrí demasiado."
    "Tomo un minuto para recuperar el aliento y sigo hasta el salón de clases."
    scene classroom with wipeleft_scene
    play music a3 fadein 2.0
    $ i_name = "???"
    $ k_name = _("Profesor")
    pause 0.5
    "Al entrar al salón puedo notar que el profesor no está."
    "¿Estará en la enfermería?"
    "Escuche que tiene problemas en la espalda."
    "Ah bueno, habrá que esperar, para mi suerte el no notará que llegue tarde."
    pause 2.0
    "Unos minutos después, el profesor entra al aula."
    "Parece estar nervioso."
    show kaito n03 at ar11
    k "Lo siento por llegar tarde, estaba en la enfermería."
    "Vaya, que coincidencia."
    "Pero..."
    "¿Por qué estará nervioso?"
    k n02 "Ah [player!t], veo que llegaste tarde."
    k "Pero descuida, lo dejare pasar por esta vez."
    show kaito n01
    "Me descubrió."
    show kaito at alhide
    hide kaito
    pause 0.5
    i "Amigo, vaya salvada, tuviste suerte que no te marcara la falta, obvio el también llego tarde."
    show issei ns03 at c11
    i "Últimamente está yendo mucho a la enfermería, debería ir al hospital, puede que esté enfermo."
    pr "Sí, puede ser eso."
    show issei ns01
    "No, no lo es."
    "Ya muchos deberían saber a qué me refiero..."
    "Eh....{w}¿No?"
    "Por favor, está saliendo con la enfermera, eso se nota mucho."
    "¿Acaso soy el único que se da cuenta de eso?"
    pr "¿Resolviste la tarea que mando ayer?"
    i ns03 "Si{w}, ¿Por?"
    show issei ns04
    pr "¡DÉJAME COPIARLA!"
    i ns05 "No."
    i "Debiste haberla hecho, seguro te quedaste toda la noche jugando o viendo anime."
    show issei ns06
    pr "¡Por favor! ¿Quieres ver morir a tu amigo?"
    i ns07 "No, pero tu sufrimiento es perfecto castigo."
    show issei ncs08
    pr "¡POR FAVOR!, te prestare mi Nintendo Switch."
    i ncs07 "Agh, okey, pero me la prestaras una semana."
    pr "Hecho."
    i ns03 "Okey, pero cópiala rápido."
    show issei ns04
    j "Issei no debes venderte solo por una Nintendo Switch."
    $ i_name = _("Issei")
    show jenni as01 at c22
    show issei at c21
    i ns05 "Mira quién habla, la que vendió su cuaderno ayer por un equipo de sonido último modelo."
    show issei at z21
    i nbs05 "Además creo que fue una mala inversión, ya que solo te lo prestaron ayer."
    show issei ns06 at c21
    show jenni at z22
    j nbs03 "Sí, pero no puedo hacer nada."
    j nbs04 "¡Me encanta la música!"
    "Me imagino que ella paso toda la noche escuchando música."
    "Por cierto, ellos dos son mis amigos Issei y Jenni."
    $ j_name = _("Jenni")
    "Tarde la presentación pero quería esperar a que Jenni apareciera."
    "Ella es mi otra amiga de la infancia junto con Hana."
    "Issei es mi mejor amigo."
    j nbs05 "Además no tienes que aceptar las irresponsabilidades de [player!t]."
    j "Tu juegas y ves anime, pero al menos haces tú tarea, en cambio [player!t] no."
    show jenni nbs06
    pr "¡Oye!, a veces es muy aburrido hacer la tarea, pero solo fue ayer."
    j ns07 "Desde hace un mes estas así."
    show jenni ns06
    "Cielos, no puedo ir contra su lógica."
    "A veces no me gusta hacer la tarea."
    "..."
    "Aunque no soy el único chico adolescente que a veces descuida su régimen de estudios por jugar videojuegos."
    show jenni ns01
    show issei ns01
    k "Bueno, estudiantes es hora de comenzar la clase, todos saquen sus cuadernos."
    show issei nbs02 at z21
    show jenni ns01 at c22
    i "Bueno bro, nos vemos después."
    show issei ns01 at hidetr
    hide issei
    show jenni at c11
    j ns02 "Nos vemos [player!t]."
    show jenni ns01 at hidetr
    hide jenni
    pause 2.0
    window hide(Dissolve(0.2))
    show black with dissolve
    stop music fadeout 2.0
    pause 2.0
    window show(Dissolve(0.2))
    "Qué bueno que pude copiar la tarea."
    "De todas formas no era algo muy complicado, solo unos pequeños pero importantes conceptos."
    window hide(Dissolve(0.2))
    pause 3.0
    scene classroom with wipeleft_scene
    show kaito n02 at c11
    k "...Y siempre hay que tener cuidado con los sitios web que visitemos en internet."
    show kaito n01
    play audio schoolbell
    pause 2.0
    play music a4 fadein 2.0
    "Las clases fueron igual de aburridas, pero al menos ya se acabaron por hoy."
    k n02 "Buenos estudiantes ya es hora de irse."
    k "Pero antes tengo que hacer un anuncio."
    k nb02 "Esta semana le tocó el turno a este salón de colaborar con llevar la carpeta de asignaciones de la semana a Akemi Yumi."
    k n02 "Veamos quien será el que la llevará."
    "Akemi Yumi{w}, ¿Quién es?..."
    "¿No es esa la chica que no asiste a clases?"
    k "Ya que aunque ella no sea de este salón, debemos colaborar con esto."
    k "Déjenme ver."
    k "El turno de esta semana le corresponde a..."
    if not player == _("Hiroki"):
        k "[player!t]."
    if player == _("Hiroki"):
        k "Maki [player!t]."
    show kaito n05
    pr "¡QUEEEEEEEEEEEEEEE!{nw}"
    pr "Pero,{w} ¿Por qué yo?"
    k n06 "Es tu turno son las reglas."
    show kaito n05
    "{i}*suspiro*{/i}"
    "¿Debería ir?"
    window auto
    menu:
        "Sí, si voy.":
            $ persistent.yumihelp = 0
        "No, no voy.":
            $ persistent.yumihelp = 1

    if persistent.yumihelp == 0:

        pr "Bueno iré, no me queda de otra."
        "Me levanto de mi asiento y me dirijo hasta el escritorio del profesor y tomo la carpeta donde están las asignaciones de la semana."
        "Después de tomarla me dirijo a la puerta y salgo del salón."
        "Pero antes..."
        pr "Salúdeme a la enfermera."
        k n03 "S-Sí, O-Okey."
        show kaito at hidetr
        hide kaito
        pause 2.0

    if persistent.yumihelp == 1:

        pr "No iré, tengo muchas cosas que hacer."
        k nb07 "Tienes que ir{w}, es tu turno."
        show kaito n08
        pr "No, tengo muchas cosas que hacer."
        k n09 "Me imagino que esas cosas son: ver Anime y jugar videojuegos toda la tarde."
        show kaito n10
        "Agh, me descubrió."
        window hide(Dissolve(.1))
        scene classroom
        show kaito n07 at j11
        with hpunch
        k "¡Vas a ir porque son las reglas!"
        show kaito n08
        pr "Bueno, pero no se enoje."
        "Me levanto de mi asiento y me dirijo hasta el escritorio del profesor y tomo la carpeta donde están las asignaciones de la semana."
        "Después de tomarla me dirijo a la puerta."
        "Pero antes..."
        pr "Profesor, me he estado preguntando, ¿Cómo sigue su espalda?"
        k n03 "B-Bien, ¿Por qué lo preguntas?"
        pr "Por nada, debería ir a ver un médico, sabiendo que la enfermera es la causante de todo."
        "Lo último lo dije en voz baja para no entrar en discusiones."
        show kaito at j11
        k "S-Sí, S-Sí, lo tomare en cuenta g-gracias."
        pr "De nada, ya me voy, mándele saludos de mi parte a la enfermera."
        show kaito n03 at j11
        k "O-Okey."
        show kaito n11
        "Después de eso salgo del salón."
        pause 2.0
        show kohana ns03 at c31
        show kaito n05 at c32
        show natsumi ns03 at c33
        ko "Profesor por cierto{w}, ¿Cómo está su espalda? "
        show natsumi ns04 at z33
        show kohana ns04
        nat "Cierto, porque está yendo mucho a la enfermería."
        show natsumi ns03 at c33
        show kohana ns03 at z31
        ko "¿Enserio se encuentra bien?"
        show kohana ns04 at c31
        show kaito n03 at z32
        k "S-Sí de verdad estoy bien."
        show natsumi ns01
        show kohana ns01
        k n12 "{i}En qué problema me metió.{/i}"
        window hide(Dissolve(0.2))
        pause 2.0

    stop music fadeout 2.0
    scene city1 with wipeleft
    window auto
    "...."
    "Durante el camino a mi casa casi se me olvida que tengo que..."
    "¿Qué era?..."
    "Así, tengo que llevar esto, hasta la casa de la chica esa...."
    "¿Cómo era que se llamaba?"
    "Yu...{w}Yum...{w}Y..."
    "Ah sí{w}, se llama Yumi."
    "Bueno, tendré que ir a su casa con la dirección que me dio el profesor."
    "Leo la dirección que el profesor me dio{w}, y noto que..."
    "Un momento..."
    "Esta chica..."
    "¡Vive en el mismo edificio que yo!"
    "..."
    "¡Y en el apartamento de abajo!"
    "Que rayos."
    "Nunca lo note."
    "¿Cómo es esto posible?"
    "..."
    "Esto debe ser una gran coincidencia."
    "Nunca la he visto así que por eso me sorprendió."
    "..."
    "No sé cómo se ve esta Yumi."
    "Seguro no sale mucho y por eso nunca nos hemos visto."
    "Si, eso debe ser."
    "Bueno, solo voy y listo."
    "Como vive en el mismo edificio no creo que tardare mucho."
    window hide(Dissolve(.2))
    pause 3.0
    scene city2 with wipeleft
    window show(Dissolve(.2))
    "No...{w}No puedo..."
    "Quiero leer la carpeta...{w}Pero...{w}No debo."
    "No es de mi incumbencia..."
    "¡PERO!"
    "¡La curiosidad me está matando!"
    "¡No puedo evitarlo!"
    "Abro la carpeta y de ella tomo una hoja."
    scene city2_blur with dissolve
    call shownote(note_yumi, True, "page1") from _call_shownote
    scene city2 with dissolve
    "Rayos, creí que tendría una foto para ver como se ve."
    "Esta chica se ve que tiene problemas, pero aún me choca que no haya tenido una foto."
    "Ya que como nunca nos hemos visto, no quiero llegar a su casa y que ella sea una chica loca o algo peor."
    "Bueno{w}, qué más da{w}, tendré que arriesgarme."
    window hide(Dissolve(.2))
    pause 2.0
    window show(Dissolve(.2))
    "Unos minutos después llego a mi edificio."
    scene apartment_exterior with wipeleft_scene
    "Ella vive en el mismo edificio."
    "Así que solo caminare hasta el tercer piso que es donde vive."
    pause 2.0
    scene apartment_exterior with wipeleft_scene
    pause 1.5
    "Bueno, ya estoy aquí."
    "Me acerco a la puerta y toco el timbre."
    pause 1.0
    play audio doorbell
    pause 2.0
    "No hay respuesta."
    "Volveré a tocar el timbre."
    play audio doorbell
    pause 2.0 
    "Nada."
    "¿Que estará pasando ahí adentro?"
    "Cuando voy a tocar la puerta, noto que está abierta."
    "La verdad no quiero entrar..."
    "Pero tendré que hacerlo."
    "No quiero meterme en problemas si no entrego las carpetas."
    "Aunque en más problemas me meteré si se enteran que entre a un apartamento sin permiso."
    "{i}*suspiro*{/i}"
    "Ligeramente empujo la puerta."
    stop audio fadeout 0.5
    play audio doorcreak3
    scene black with wipeleft_scene
    play music a5 fadein 2.0
    $ renpy.music.set_volume(0.15, channel="music")
    scene yumi_livingroom_dark with dissolve
    "Al entrar no sé porque, pero todo se encuentra muy oscuro."
    "Y eso que es de día."
    "Siento un poco de escalofríos."
    "No veo a nadie."
    pr "¡YUMI!"
    "Grito su nombre, pero nadie responde."
    "Tendré que buscarla."
    "Iré primero a..."
    $ kitchenfirstRun = None

label cuestions:
    menu:
        "La cocina.":
            jump kitchen
        "Pasillo.":
            jump con

label kitchen:
    
    if kitchenfirstRun == True:
        "No tiene sentido ir de nuevo a la cocina porque ya revisé allí."
        jump cuestions
    else:
        "Estar aquí me da un poco de miedo, ¿Por qué estará tan oscuro?"
        scene yumi_kitchen_dark with wipeleft_scene
        "Al echar un vistazo en la cocina y noto sobras de comida en el fregadero, también huelo algo que está descompuesto."
        "Que horrible olor."
        "¿Qué le pasara a esta chica?"
        $ kitchenfirstRun = True
        scene yumi_livingroom_dark with wipeleft_scene
        jump cuestions

label con:

    "Al ver a mi derecha noto un pasillo."
    "Se ve muy oscuro."
    "Pero me tendré que acercar."
    scene black with dissolve
    pause 1
    scene yumi_hall
    show black zorder 500:
        ease 10 alpha 0.5
    pause 1
    "Espero a que mis ojos se acostumbren a la oscuridad."
    pause 1
    "Veo que tengo dos puertas a mis costados."
    window hide(Dissolve(.2))
    scene yumi_hall:
        xcenter 640
        ease 1.000 xoffset 80
        pause 1.0
        ease 1.000 xoffset -80
        pause 1.0
        ease 1.00 xoffset 20
    show black zorder 500:
        alpha 0.5
    pause 5.0
    "Una es el baño y la otra es la habitación de Yumi."
    "Lo sé porque tienen carteles con sus nombres."
    "Debería entrar primero en..."
    $ bathroomfirst = None

label cuestions2:
    menu:
        "Entrar en el baño.":
            jump bathroom
        "Entrar en la habitación.":
            jump Dcon2

label bathroom:
    if bathroomfirst == True:
        "No voy a volver a entrar al baño no tiene sentido perder el tiempo allí."
        jump cuestions2
    
    else:
        scene yumi_hall:
            xcenter 665
            ease 1.000 xoffset 80
        show black zorder 500:
            alpha 0.5
        pause 1.0
        play audio doorcreak3
        scene yumi_bathroom_dark:
            xcenter 640
        with dissolve 
        "Al entrar oigo un chorro de agua."
        play audio dripper
        pause 4.0
        scene yumi_bathroom_dark:
            xcenter 640
            ease 1.000 xoffset -40
        "Tomo la llave y lo cierro."
        "No hay nadie aquí."
        "Así que no hay nada más que revisar."
        "Salgo del baño."
        stop audio fadeout 0.5
        scene yumi_hall:
            xcenter 640
            xoffset 80
            ease 1.000 xoffset -80
        show black zorder 500:
            alpha 0.5
        with wipeleft_scene
        $ bathroomfirst = True
        jump cuestions2

label Dcon2:
    
    "Creo que debería entrar en la habitación."
    scene yumi_hall:
        xcenter 550
        ease 1.25 xoffset -20
    show black zorder 500:
        alpha 0.5
    "Me acerco sigilosamente a la puerta."
    scene yumi_door with dissolve
    "La abro ligeramente."
    play audio doorcreak2
    "No sé pero escucho un ligero llanto."
    play audio yumi_cry
    pause 2.0
    "¿Será ella?"
    y "{i}¿Por qué?....{w=2.0}¿Por qué?{/i}"
    "Ahora escucho una voz."
    y "..."
    "Debo entrar y ver qué pasa."
    play audio door2c
    scene yumi_room_dark with wipeleft_scene
    pause .25
    pr "Yu..."
    show yumi fsl03 at c11
    y "{cps=15}Este...{w=1.2}Tú...{nw=3.0}{/cps}"
    y "¿Quién eres?"
    show yumi fsl04
    pr "Yo...{w=1.2}Eh...{w=1.2}Yo..."
    "¿Ella es Yumi?"
    $ y_name = "Yumi"
    "Pero si es...."
    "..."
    "¡HERMOSA!"
    "¿Cómo una chica así se la pasa encerrada?"
    show yumi fsl05 at j11
    y "Ah sí...Ya sé quién eres..."
    show yumi fsl06
    pr "Este..{w=1.2}¿Qué?..."
    y fsl02 "La verdad yo no sé cómo funcionan este tipo de cosas."
    y fslb02 "Pero apareciste en el momento justo."
    y fsl02 "Así que puedo decir..."
    y "Que desde el día de hoy, tú serás mi novio."
    stop music fadeout 2.0
    show yumi fsl01
    "¿Qué?...."
    "Un momento..."
    "{cps=15}.........{/cps}{nw=2.0}"
    "¡QUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!{nw}"
    pr "¡QUE!....{w=1.0}¡QUE!...{w=1.0}¿Q-Qué dijiste?"
    y fsl05 "Que ahora eres mi novio, tontito."
    show yumi fsl06
    "Siento como mi cara se tiñe de rojo."
    "E-Esta chica{w=1.2}, ¿trata de jugar conmigo?"
    y fsl02 "Como aún no he pensado tu nombre, te diré 'Cariño'."
    y "¿Te parece?"
    show yumi fsl01
    "En este momento, no sé qué hacer."
    "Estoy súper nervioso."
    "Esta chica, ¿Está loca o qué le pasa?"
    y fsl03 "Oye cariño, ¿qué tienes?"
    y "Te ves muy pálido."
    show yumi fsl04
    pr "Yo..."
    "Sin pensarlo dos veces, salgo de la habitación los más rápido que puedo."
    scene black with wipeleft_scene
    pause 1.0
    y "¡Espera!"
    "Sin mirar atrás salgo del apartamento de Yumi."
    pause 3.0
    scene apartment_exterior with wipeleft
    pause 2.0
    "Subo lo más rápido que puedo las escaleras del edificio hasta mi piso."
    "¡¿Qué rayos le pasa a esa chica?!"
    window auto
    pause 3.0
    scene apartment_exterior with wipeleft_scene
    "Al llegar a mi casa, entro rápido a mi cuarto, ignorando mi alrededor."
    scene hiroki_livingroom with wipeleft
    pause 0.25
    "Entro a mi habitación y cierro la puerta."
    scene hiroki_room with wipeleft_scene
    pr "*jadeo*{w=1.0} *jadeo*{w=1.0} *jadeo*{nw=1.4}"
    pr "¿Qué...{w=1.5}Qué acaba de....{w=1.5}Pasar?"
    e "Hermanito, ¿Te ocurre algo?"
    e "Te vi entrar muy nervioso a tu habitación."
    pr "No ocurre nada Emi, descuida."
    e "Te escucho nervioso, ¿Ocurrió algo?"
    pr "E-Ehhhh.{nw=1.5}"
    pr "No, no pasó nada."
    "Sí le cuento sobre lo que paso con Yumi."
    "Me va a matar."
    "No literalmente."
    "Pero ella no quiere que tenga una novia."
    "Ni que fuera mi madre."
    e "Dime cuando te sientas bien."
    pr "O-Okey."
    "{i}*suspiro*{/i}"
    "Menos mal."
    "Sí le digo lo que me sucedió, se volverá loca."
    "Dirá, {i}¿Por qué no aprovechaste la situación?{/i}{w=2.0} o {i}¿Por qué no le seguiste el juego?{/i}."
    "Y no quiero escuchar sus sermones."
    "Mañana debería ir a la casa de Yumi y disculparme por irme así."
    "Pero...."
    "Me sentiría extraño entrando en su casa otra vez."
    "Bueno...{w}Mi mente no me dejaría en paz hasta que me disculpe con ella."
    "{i}*suspiro*{/i}"
    "Pero por ahora solo debería hacer mi tarea, porque tengo mucha."
    pause 2.0
    $ renpy.music.set_volume(1.0, channel="music")
    play music a1 loop fadein 2.0
    e "¡Hermanito, es hora de almorzar!"
    "Pero, primero debo comer, nadie puede pensar con el estómago vacío, ¿verdad?"
    "Me cambio de ropa y voy."
    pr "¡Enseguida voy Emi, me voy a cambiar la ropa!"
    e "¡Okey!"
    pause 3.0
    scene hiroki_room with wipeleft_scene
    "Okey, ya estoy listo."
    "Salgo de mi habitación hacia la cocina."
    scene hiroki_livingroom with wipeleft_scene
    show emi nc01 at c11
    e "Hola de nuevo hermanito."
    e nc02 "¿Cómo estuvo tu día?"
    show emi nc01
    pr "Bien, bien, ¿Por qué lo preguntas?"
    e nc02 "Bueno, es que hace un rato no lo parecía."
    pr "B-Bueno es que...{w=1.3}Yo...{w=2.0}Eh..."
    "Ya me atrapo."
    "A este paso me sacara de la boca, lo que me sucedió hoy."
    e nc02 "Vamos puedes contarme."
    e "No es nada malo, ¿verdad?"
    e nc14 "O es que.."
    e nc04 "¿Conseguiste una novia?"
    "No sé porque pero cuando Emi dijo eso me sentí extraño."
    "Que miedo."
    "Sentí como esas palabras se incrustaban en mis oídos como algún tipo de parásito."
    pr "¿Qué te importa si tengo novia o no?"
    show emi dc04 at j11
    e "¡Es que yo quiero ser tu esposa!"
    show emi dc01
    pr "Emi, eso solo es un capricho infantil, la hermana que se quiere casar con su hermano."
    show emi dc06 at tr11
    e "Awwwww, ¿Pero no se puede?"
    show emi dc08
    pr "No, te lo he dicho muchas veces."
    "¿En qué mundo crees que vivimos, Emi?"
    "Las relaciones entre hermanos solo se ven en los animes."
    "Y ya sabemos en cuales."
    pr "¿Y qué cocinaste hoy?"
    show emi ac01 at j11
    e "¡No cambies el tema!"
    pr "¡Que no te importa, si tengo novia o no!"
    show emi dc08 at tr11
    e "Awww..."
    show emi dc01 at j11
    e "Bueno..."
    e nc04 "Hoy cocine pabellón."
    pr "{i}¿Pabellón?{/i} ¿Qué es eso?"
    $ renpy.notify(_("Pabellón: Comida tradicional venezolana, compuesta de arroz blanco, frijoles negros, plátano frito, y carne mechada"))
    e nc02 "Es una comida tradicional venezolana."
    show emi nc01
    pr "Para que hiciste eso, si ni siquiera conoces que es."
    e nc02 "Es quería ampliar mis conocimientos culinarios."
    e "La comida es sencila pero muy deliciosa."
    show emi nc01
    pr "Bueno, está bien."
    pr "Vamos a comer."
    pr "A ver qué tal."
    show emi nc04 at j11
    e "¡Okey!"
    show emi at hidetr
    hide emi
    "Nos sentamos en la mesa, y comenzamos a comer."
    pause 2.0
    "¡Que delicia!"
    "La comida es sencilla como dijo Emi."
    "Pero es muy deliciosa."
    "Debería decirle a Emi, que cocine esto más a menudo."
    "Y también que investigue sobre las comidas tradicionales de otros países."
    "Para probarlas."
    window auto
    pause 2.0
    pr "Mmm....."
    pr "Que delicia."
    pr "Te esforzaste mucho en esto Emi."
    show emi nc05 at c11
    e "Gracias."
    e n1c02 "Ves."
    show emi n1c01
    pr "¿Ver qué?"
    e n1c05 "Que soy perfecta para ser tu esposa."
    show emi n1c04
    pr "{i}*suspiro*{/i}"
    pr "Emi ya te lo he dicho, somos hermanos."
    show emi dc06 at tr11
    e "Awww, pero entonces..."
    show emi dc05 at j11
    extend "Entonces..."
    show emi ac01 at j11
    e "¡Por qué te cocino como una esclava!"
    show emi dc01
    pr "Primero, no me grites y segundo...."
    pr "Te pido que cocines tú, porque tu sazón no se compara con el mío."
    pr "Además, eres muy buena cocinando, ¿No recuerdas que me queme el brazo por solo cocinar un huevo frito?"
    show emi dc09 at tr11
    e "{i}Siiii{/i}, eres muy malo cocinando."
    show emi dc08
    pr "Además, creo que si cocino yo, terminaras arrepintiéndote de comer mi comida todos los días."
    e dc09 "O-Okey, perdón por haberte gritado hermanito."
    show emi dc10
    pr "Descuida no hay problema."
    e dc09 "Sí, pero deberías aprender cocinar, para que el día que tengas una novia, puedas cocinarle."
    pr "Bueno, tengo a la mejor maestra."
    show emi nc04 at j11
    e "Jeje."
    e nc05 "Gracias."
    show emi nc04
    pr "Sabes, hoy si me ocurrió algo súper extraño."
    show emi nc06 at j11
    e "¡Lo sabía!"
    e n1c06 "Y tú y que no te pasaba nada."
    show emi n1c07
    pr "No te emociones, te lo estoy contando para que no te sientas mal por haberte regañado."
    e n1c08 "O-Okey."
    show emi nc01
    pr "Bueno..."
    "Le empiezo a contar lo que me paso hoy con Yumi, no le menciono el nombre para que no crea que tengo algo con ella."
    "Me siento incómodo con solo contárselo."
    "Al terminar, me esperaba lo que había dicho."
    show emi dc05 at j11
    e "Enserio, eres tonto."
    show emi dc04 at j11
    e "¡¿Por qué no aprovechaste la situación?!"
    show emi at j11
    e "¡¿Por qué no le seguiste el juego?!"
    "Ahí está, sabía que iba a decir eso."
    e nc05 "¿Cómo eran sus pechos?"
    show emi nc04
    pr "¡QUEEEEEEEEEEEEEEEEEEEE!{nw}"
    pr "¡¿Por qué rayos me haces esa pregunta?!"
    e nc05 "Bueno, porque es lo primero que ves al conocer a una chica."
    e "¿De qué tamaño eran?"
    e nc02 "Era una lolita."
    e nc11 "Una término medio."
    e nc14 "O..."
    e nc05 "¿Los tenía muy grandes?"
    show emi nc04
    pr "Bueno..."
    pr "{i}¿Enserio tengo que responder?{/i}"
    e nc02 "Pues claro, esta es una conversación que un hermano y una hermana deberían tener a diario."
    show emi nc01
    "¡TIENES LA IDEAS INVERTIDAS!"
    "Esa es una conversación de amigos, pero sería muy raro hablar de eso."
    "Y sería muy malo hablar de eso."
    pr "Bueno, te lo diré."
    "Sueno como todo un pervertido."
    "No niego que si se los vi."
    "Pero espero no tener que contarle esto alguien más."
    pr "{i}Eran{/i}..."
    pr "Ehhh..."
    pr "{cps=30}{i}Grandes...{/i}{/cps}"
    e nc04 "¡Oh! ¿Enserio?"
    pr "Eran un poco más grandes que los de Jenni."
    show emi nc05 at j11
    e "¡Eres un pervertido! Jeje."
    show emi nc04
    pr "¡Por eso no quería decírtelo!"
    show emi nc05 at j11
    e "¡También le miras los pechos a Jenni!"
    show emi at jr11
    e "¡Eres un pervertido! {w=1.0}¡Eres un pervertido!~"
    pr "¡CALLATE!"
    show emi at j11
    "Agh, ahora quede como todo un pervertido."
    "¿Por qué la vida es tan mala conmigo?"
    pr "Me voy a mi habitación."
    show emi at j11
    e "Okey pervertido."
    scene hiroki_room with wipeleft_scene
    stop music fadeout 2.0
    "Al llegar a mi habitación cierro la puerta con llave para que Emi no entre y continué burlándose de mí."
    pr "¿Qué pensaría Issei si le dijera que a veces me quedo mirando los pechos de Jenni?"
    pr "Seguro no viviría después de ese día."
    pr "Y si se lo digo a Jenni, creo que no me mataría, pero si me hiciera quedar mal con todos."
    pr "Y Issei terminaría matándome por contemplarle los pechos a su novia."
    pr "Pero{w}, ¿Por qué sería mi culpa?"
    pr "No tengo la culpa que Jenni los tenga tan grandes."
    pr "Enserio, esos pechos están ahí como si fuesen un par de melones en una frutería."
    pr "Se pueden mirar, pero no tocar."
    pr "Bueno, al menos que los vayas a comprar."
    "¿Qué rayos estoy diciendo?"
    pr "Enserio sueno como un pervertido."
    "{i}*suspiro*{/i}"
    $ game_reference = renpy.random.choice(["Geometry Dash", "Friday Night Funkin'"])
    pr "Mejor me pongo a jugar [game_reference] para despejar mi mente y no pensar en lo mal que me siento ahora."
    window hide(Dissolve(.2))
    pause 5
    scene hiroki_room_afternoon with dissolveslow
    window auto
    if game_reference == "Geometry Dash":
        pr "¡QUE BIEN!, por fin complete ese nivel."
    else:
        pr "¡QUE BIEN!, por fin complete esa canción."
    "Hmm..."
    "Al mirar hacia arriba, noto que jugué por un gran rato."
    "Y..."
    pr "¡Mierda!{nw}"
    pr "Tengo que hacer la tarea."
    "Rápidamente comienzo a buscar mis cuadernos para comenzar hacer la tarea."
    "Como es de la clase de informática es más fácil para mí."
    window hide(Dissolve(.2))
    pause 3
    scene hiroki_room_night with dissolveslow
    play music a1 fadein 2.0
    window auto
    "Al terminar de hacer la tarea noto que ya es de noche."
    pr "Cielos, ¿Enserio tarde tanto?"
    "Y recuerdo que dure como tres horas jugando [game_reference]."
    pr "Emi de seguro ya hizo la cena."
    pr "¿Qué habrá cocinado?"
    pause 2.0
    scene hiroki_livingroom with wipeleft_scene
    pr "¡Emi!"
    show emi nc12 at c11
    e "¡¿Qué pasa?!"
    pr "Nada, solo quería saber que cocinaste."
    e nc02 "Ah okey." 
    e nc04 "Pedí pizza."
    pr "¿Ahora que paso Emi? Que no quisiste cocinar."
    show emi dc08 at tr11
    stop music fadeout 2.0
    e "Bueno..."
    e "Ehhh..."
    e dc11 "No me sentí lo suficientemente motivada para cocinar después de la discusión que tuvimos en la tarde."
    "¿Discusión?"
    "..."
    "Ah..."
    show emi dc08
    pr "Emi te dije que no te preocuparas por eso."
    pr "Bueno, creo que no te lo dije."
    pr "Pero te lo digo ahora..."
    pr "No te preocupes por eso, no estoy enojado contigo."
    e dc06 "¿Enserio?"
    show emi nc13
    pr "Enserio."
    pr "Además no fue una discusión muy mala como para que no quisieras cocinar."
    pr "Pero tranquila, te voy a entender cuando no quieras hacerlo."
    play music a4 fadein 2.0
    pause 2.0
    pr "Y....."
    pr "¿Pediste postre?"
    show emi nc05 at j11
    e "¡Claro!"
    show emi nc04
    pr "¿Comemos?"
    show emi nc05 at j11
    e "¡Sí!"
    show emi at hidetr
    hide emi
    pause 3.0
    pr "Como me encanta la pizza."
    pr "Pero no hay que abusar."
    pr "No podemos comer mucha comida chatarra."
    show emi nc02 at c11
    e "Tienes razón."
    show emi nc01
    pr "Emi, ¿Quieres ver algo antes de dormir?"
    pr "No sé, una película, un anime..."
    e nc02 "Bueno no sé, tú eres el que propuso ver algo."
    e "Decide tú."
    e "De todas formas me gusta el anime y las películas."
    show emi nc01
    pr "Okey."
    menu:
        "Veremos..."
        "Una película.":
            $ persistent.selectevent = 0
        "Un anime.":
            $ persistent.selectevent = 1

    if persistent.selectevent == 0:

        pr "Sería bueno ver una película."
        pr "¿No crees?"
        e nc02 "Sí, me gustaría."
        e "Siempre he querido ver esa película que se estrenó hace poco."
        show emi nc01 
        pr "¿La vemos?"
        show emi nc04 at j11
        e "¡Sí!"
        window hide(Dissolve(.25))
        scene black with dissolveslow2
        pause 3.0
        window auto
        scene hiroki_livingroom with dissolveslow
        pr "Que buena estuvo la película."
        show emi nc05 at c11
        e "Sí, me gustó mucho."
        show emi nc04
        pr "Emi, ¿Qué hora es?"
        e nc02 "Como las 11:30 PM."
        show emi nc01
        pr "¡QUEEEE!"
        pr "Tengo que irme a dormir, mañana tengo clases."
        e n1c02 "Pero si mañana es sábado."
        show emi nc01
        pr "Uff..."
        pr "Que bueno, y yo ya me estaba preocupando."
        pr "¿Será la costumbre?"
        pr "Bueno."
        pr "Igual nos iremos a dormir ya es muy tarde."
        show emi nc08 at tr11
        e "Awwww..."
        pr "No importa lo que digas."
        pr "A dormir jovencita."
        show emi dc01 at j11
        e "Hmph…"
        pr "Voy a ir a mi cuarto y tú, ve al tuyo."
        e dc04 "Okey."
        pr "Hasta mañana."
        e nc05 "Hasta mañana hermanito."
        show emi at hidetr
        hide emi

    if persistent.selectevent == 1:

        pr "Sería bueno ver un anime."
        pr "Investigue una llamado {i}Tejina-senpai{/i}."
        pr "Se oye muy cómico."
        e nc11 "Ese no lo he visto."
        e nc05 "Veamos lo."
        show emi nc04
        pr "Vamos."
        window hide(Dissolve(.25))
        scene black with dissolveslow2
        pause 3.0
        window auto
        scene hiroki_livingroom with dissolveslow
        pr "Que mal que no nos lo podemos terminar todo en un solo día."
        pr "Emi, ¿Cuantos capítulos vimos?"
        show emi nc02 at c11
        e "Como 4."
        show emi nc01
        pr "Aunque no duran mucho, y tiene 12 capítulos."
        pr "Bueno, que se puede hacer."
        pr "¿Qué hora es?"
        e nc02 "Las 9:40 PM."
        show emi nc01
        pr "Bueno, me voy a dormir."
        pr "Tengo que ir a la escuela mañana."
        e nc02 "¿A la escuela en sábado?"
        show emi nc01
        pr "Vaya."
        pr "Bueno, iré a otro lugar."
        pr "Quizá llame a Issei o a Jenni para salir."
        e nc04 "Okey."
        e nc05 "Buenas noches hermanito."
        show emi nc04
        pr "Buenas noches."
        pr "Acuéstate temprano, me oíste."
        e nc02 "No te preocupes."
        show emi nc01
        pr "Adiós."
        e nc02 "Adiós hermanito."
        show emi at hidetr
        hide emi

    stop music fadeout 2.0
    scene hiroki_room_night with wipeleft_scene
    "Al llegar a mi habitación me coloco la pijama y me acuesto en la cama."
    window hide(Dissolve(.25))
    scene black with dissolveslow
    pause 1.0
    window auto
    "Que cosa más extraña me ocurrió hoy."
    "¡¿Qué le pasa a esa chica?!"
    "Aunque..."
    "Es muy linda."
    "¿Cómo una chica tan linda se la pasa encerrada?"
    "Creo que mañana debería ir a su casa y disculparme por haberme ido así."
    "Quizás le marque a Issei para contarle."
    "Mejor no pienso más en eso."
    "Mañana veré que hacer."
    window hide(dissolve)
    scene black with dissolve_scene_full
    pause 3.0

    return