
label ch1:
    
    scene black
    "..."
    play audio alarm
    "Hmm....."
    "¿Qué pasa?"
    "¿Qué hora es?"
    stop audio
    e "Las 9:00 AM."
    pr "¿Qué?"
    scene hiroki_room
    show black zorder 500:
        ease 1.0 alpha 0.00
    show emi nc01 at superclose
    pause 1.0
    e nc02 "Hermanito ya levántate."
    show emi nc01
    pr "Eh...."
    show emi nc04 at j11
    pr "¡Ahhhhhh!"
    e "Jeje."
    play music a4 fadein 2.0
    pr "¿Qué haces en mi cuarto tan temprano?"
    e nc02 "Bueno, es que vine a despertarte para que desayunes."
    show emi nc01
    pr "¿Ya hiciste el desayuno?"
    e nc05 "Si, es que me levante temprano para hacer el desayuno, porque mis amigas van a venir hoy a la casa."
    show emi nc04
    pr "¿Hoy?"
    e nc02 "Si, ¿Por?"
    show emi nc01
    pr "Tuviste que habérmelo dicho ayer."
    e nc02 "Okey hermanito."
    e nc05 "La próxima vez que vengan te digo con anticipación."
    show emi nc04
    pr "Okey."
    pr "De todas formas voy a salir."
    e nc02 "¿Enserio?"
    e nc11"¿A dónde?"
    pr "Iré a hablar con Issei o Jenni."
    e nc02 "¿De qué?"
    show emi nc01
    pr "Emi."
    e nc02 "¿Si?"
    show emi nc01
    pr "No tienes que interrogarme."
    pr "Tus amigas pueden venir si no causan ningún desastre."
    e n1c03 "Descuida, no pasara nada."
    show emi n1c15
    pr "¿Enserio?"
    show emi nc16 at tr11
    pr "Y qué me dices de aquella vez que dejaron la cocina hecha un desastre y...{nw=3.0}"
    show emi n1c03 at c11
    e "Por favor hermanito...."
    e "Solo dejamos la cocina sucia..."
    e "No llego a mayores."
    show emi n1c15
    pr "¿Enserio?"
    pr "Porque yo no lo recuerdo así."
    pr "Según lo que yo recuerdo{nw}"
    show emi nc16 at tr11
    extend " casi quemaste la casa."
    pr "Y tuvimos que llamar a los bomberos."
    show emi at j11
    e "Okey, okey."
    show emi at j11
    e "No volverá a pasar."
    pr "Que así sea."
    pr "Porque estarás en graves problemas si vuelve a pasar."
    show emi at j11
    e "No volverá a pasar te lo juro."
    e "Descuida."
    pr "Bien."
    show emi nc01
    pr "Bueno, vamos a comer."
    pr "Porque tengo hambre."
    e nc05 "Yo también."
    scene hiroki_livingroom with wipeleft_scene
    pause 0.24
    show emi nc01 at c11
    pr "¿Y a que vendrán tus amigas?"
    show emi dc04 at j11
    e "¡Hey!"
    e "Tú vas a hablar con Issei y Jenni y no te interrogo."
    show emi dc01
    pr "Soy tu hermano mayor y me tienes que respetar."
    pr "Y te pregunto porque necesito saberlo."
    show emi nc08 at tr11
    e "Ah perdón."
    e "Es que creí que lo preguntabas por algo malo."
    show emi nc02 at c11
    e "Bueno..."
    e "Vienen a hacer unas tareas."
    show emi nc01
    pr "Perfecto."
    pr "Entonces comamos, porque no quiero que se me haga más tarde." 
    e nc05 "Okey."
    show emi nc04 at hidetr
    hide emi
    pause 1.0
    scene black with clockwiperight_scene
    pause 2.0
    scene hiroki_livingroom with clockwipeleft_scene
    show emi nc01 at c11
    pr "Gracias por la comida Emi."
    e nc02 "De nada hermanito."
    show emi nc01
    pr "Bueno, me voy."
    e nc02 "Okey hermanito."
    e "Que te vaya bien."
    show emi nc01
    pr "Gracias."
    pr "Adiós."
    pr "Nos vemos más tarde."
    e nc05 "Adiós hermanito."
    show emi nc04
    scene black with wipeleft
    pause 2.0
    play audio dooropen
    scene apartment_exterior with wipeleft
    stop music fadeout 2.0
    pr "Okey.."
    pr "Le enviare un mensaje a Issei para ver si puedo ir hasta su casa."
    "Ya que los Sábado y Domingo, Jenni no está en su casa."
    "Y por eso no le enviare un mensaje a ella."
    window hide(Dissolve(.2))
    if persistent.blur_on:
        scene apartment_exterior_blur with dissolve
    nvl show dissolve
    nvlpr "Hola bro."
    nvlpr "¿Cómo estás?"
    nvlpr "¿Estás en tu casa?"
    pause 0.25
    nvli "Hola bro, si estoy en mi casa."
    nvli "¿Qué pasa?"
    nvli "¿Ocurre algo?"
    pause 0.25
    nvlpr "Nada, es solo que quería charlar contigo o con Jenni de algo muy extraño que me ocurrió ayer."
    pause 0.25
    nvli "Extraño....{w=1.5}¿Cómo?"
    pause 0.25
    nvlpr "Te lo digo desp-{nw}"
    nvli "Sí gustas puedes venir a mi casa, Jenni también está aquí."
    pause 0.25
    nvlpr "{i}Eliminaste este mensaje.{/i}{nw}"
    pause 0.25
    nvlpr "Sí está bien, estoy en camino."
    pause 0.25
    nvli "Okey, te esperamos."
    nvl hide dissolve
    if persistent.blur_on:
        scene apartment_exterior with dissolve
    pause 1.0
    window auto
    pr "...."
    pr "Espero que Issei y Jenni no se burlen de mi por lo que me ocurrió ayer."
    window hide(Dissolve(.2))
    pause 2
    scene city2 with wipeleft_scene
    "Durante el camino, pienso..."
    "¡¿Cómo rayos les voy a explicar a Issei y Jenni lo que me ocurrió?!"
    "No les voy a decir...."
    "{i}Ayer una chica me dijo que yo era su novio{/i}."
    "Suena ridículo de solo pensarlo."
    "Como una hermosa chica que ni conozco me nombra como su novio sin yo conocerla."
    "Pero..."
    "¿Por qué razón me dijo eso?"
    "..."
    "Con más razón debo hablar con Issei y Jenni."
    "No porque ellos tengan una respuesta."
    "Solo quiero contarles."
    "Solo unos minutos pasan cuando llego a la casa de Issei."
    window auto
    scene isseihouse with wipeleft_scene
    "Es raro en realidad en como Issei y Jenni viven literalmente cerca de mí."
    "La verdad cuando visite la casa de Issei por primera vez, no pude creer que viviera a solo cuatro cuadras."
    $ renpy.notify(_("Nota: " + player + " vive en el apartamento 402, Jenni vive en el apartamento 406"))
    "En cambio Jenni vive literalmente al lado."
    "Y eso que conozco a Jenni mucho antes de conocer a Issei y apenas hace un par de años me di cuenta que ella vivía en el mismo edificio que yo."
    "Y en el mismo piso."
    "A veces no entiendo las coincidencias."
    pause 0.5
    scene isseihouse_front with dissolve
    "Al acercarme a la puerta me entra una gran ansiedad...."
    "¡QUE RAYOS LES VOY A DECIR!"
    "Ya estoy entrando en pánico de solo saber si no explico bien lo que ocurrió con Yumi...."
    "Issei y Jenni terminaran burlándose de mí y seguro dirán...."
    "{i}Tanto que querías una novia y aquí la tienes, aunque no como querías{/i} o...{w=1.0}{i}Seguro le hiciste algo a esa pobre chica para que se fijara en un tipo como tú{/i}."
    "Lo último lo diría Jenni, pero....."
    "*Inhalo*{w=1.4} *Exhalo*{nw=2.2}"
    "Me calmo un poco y me atrevo a tocar el timbre de la casa."
    play audio doorbell
    pause 2.0
    "Cielos..."
    "Me estoy comenzando a sentir nervioso."
    "Cualquiera tomaría esto de manera más calmada."
    "Pero conociendo a Issei y a Jenni seguro se burlaran de mí."
    "Además esto es tan extraño que cualquiera se pusiera nervioso si tuviera que decir que una chica desconocida te proclama cómo su novio."
    "Y eso pondría nervioso a cualquiera."
    play audio door2c
    "Escucho como se abre la puerta frente a mí."
    show issei np02 at c11
    i "Hola bro, llegaste bastante rápido."
    show issei np01
    pr "H-Hola Issei."
    "Comienzo a sentirme mareado."
    i np03 "Amigo, ¿Estas bien?"
    i "Te ves muy cansado."
    pr "Yo....."
    "Ya ni siquiera me puedo mantener en pie."
    i np04 "¿[player!t]?"
    "Esto...{w=1.5}{cps=10}es...{/cps}{nw}"
    scene isseihouse_front_blur
    show issei np04 at ins11
    show vignette1 zorder 100
    with dissolve
    "Mi visión se pone borrosa...."
    "Que ridículo me debo ver ahora."
    pause 2.0
    "Ahora caigo rendido en el suelo.{nw=1.0}"
    window hide(None)
    scene black
    play audio fall
    pause 1.0
    i "¡¡[player!t]!!"
    window hide(Dissolve(.2))
    pause 3
    scene issei_livingroom with eyeinslow_scene
    window auto
    pr "Mmm....."
    pr "¿Dónde estoy?"
    show issei nbp02 at c11
    i "Estas en mi casa amigo."
    show issei np01
    pr "¿Qué hora es?"
    i nbp02 "Las 10:20 AM, no te desmayaste por tanto tiempo."
    show issei np01
    play music a3 fadein 3.0
    pr "Agh..."
    pr "Me duele la cabeza."
    pr "¿Tienes algo para eso?"
    pr "¿Algún medicamento o algo?"
    i np03 "Eeehh....{w=2.0}Sí."
    i nbp07 "¡Jenni!"
    show issei np08
    pause 1.4
    show jenni np08 at c22
    show issei np01 at c21
    j "¿Qué pasa mi am-{nw}"
    show jenni np10 at j22
    j "¡¡[player!t]!!"
    show jenni nbp11 at z22
    j "¿Qué haces aquí?"
    pr "Es que vine a hablar con ustedes."
    show jenni np13
    show issei np04
    j "¿Enserio?"
    j np14 "¿De qué?"
    show jenni np13
    pr "Bueno...{w}Quiero contarles algo súper extraño que me ocurrió ayer."
    show issei np03 at z21
    i "Hablas de lo que me ibas a decir por teléfono."
    show issei np04
    pr "Sí..."
    pr "Pero primero denme algo para el dolor de cabeza, ya que me está matando."
    show jenni np14 at z22
    show issei np04 at c21
    j "Claro."
    show jenni at hidetr
    hide jenni
    pause 2.0
    show jenni nbp14 at c22
    j "Ten."
    show jenni nbp13
    pr "Gracias."
    pause 1.0
    show issei nbp03 at z21
    i "¿Qué es lo extraño que te ocurrió?"
    show issei np04
    pr "Bueno, antes de contarles les voy a pedir algo..."
    show jenni nbp14 at z22
    show issei at c21
    j "¿Y qué sería eso?"
    show jenni nbp13
    pr "Que no se rían de mi cuando les termine de contar."
    j nbp12 "Tratare de no reírme si es que es algo muy cómico."
    j "Pero no prometo nada."
    show jenni np09 at c22
    pr "¡Oye!"
    show issei nbp02 at z21
    i "Descuida amigo, tratare de no reírme."
    show issei np01 at c21
    pr "Bueno...."
    show jenni np01
    stop music fadeout 2.0
    pr "{i}*suspiro*{/i}"
    "Primero me calmo...."
    "*Inhalo*{w=1.4} *Exhalo*"
    "Okey..."
    pr "Bueno, ustedes saben quién es Akemi Yumi, ¿verdad?"
    show issei np03 at z21
    i "Si, es la chica que no asiste a clases, todos la conocen."
    show issei np04
    pr "Bueno..."
    pr "Lo extraño que me ocurrió fue con ella."
    pr "Después de salir del colegio e ir hacia su casa, yo..."
    show jenni np14 at z22
    show issei at c21
    j "¿Tú qué?" 
    show jenni np13
    pr "Después de revisar la carpeta de asignaciones y leer la dirección me di cuenta que...."
    show jenni np14
    j "¿De qué?" 
    show jenni np13
    pr "Bueno, pero no me interrumpas."
    show jenni np06
    pr "Después de revisar la carpeta y leer la dirección me di cuenta que ella..."
    pr "Vive en el mismo edificio que yo."
    show jenni np13 at c22
    show issei np03 at z21
    i "Vaya, ¿enserio?"
    i nbp03 "Según los rumores, ella nunca sale de su casa."
    i np03 "Y seguro por eso no la has visto."
    show issei np04
    pr "Y vive en el apartamento de abajo."
    i np03 "Que coincidencia más extraña."
    show issei np04
    pr "Bueno..."
    pr "Al llegar a su casa toque varias veces el timbre y nadie respondía así que..."
    show jenni np10 at ztj22
    show issei at c21
    j "¡Entraste a la casa de una chica sin su permiso!" 
    pr "Bueno, pero nadie respondía y entre a investigar."
    j nbp12 "Ah bueno, porque ya estaba a punto de golpearte hasta dejarte inconsciente."
    pr "Si, como no."
    show jenni nbp06
    pr "Sí fueran estado allí..."
    pr "Había un olor asqueroso."
    pr "Platos sucios, comida descompuesta, polvo por todos lados y había un chorro agua abierto en su baño."
    pr "Estar adentro de su casa se sentía como estar en un cementerio de lo oscuro y solitario que estaba el ambiente." 
    pr "Era muy aterrador." 
    j np14 "¿Y Yumi?" 
    show jenni np13
    pr "A eso voy."
    pr "Al entrar en su cuarto.{nw}"
    show jenni np10 at ztj22
    j "¡Entraste en su cuarto!" 
    pr "¡Bueno, pero escuche unos llantos y unas voces desde su cuarto y tuve que entrar para ver qué ocurría!"
    j np14 "Ah okey."
    show jenni np13
    pr "Al entrar en su cuarto, la vi."
    pr "Y dije en mi mente...{w=2.0}¿Por qué una chica tan linda se la pasa encerrada en su casa?"
    show issei np01
    show jenni np01
    pr "Aunque me puse muy nervioso y lo peor de todo fue cuando..." 
    show issei np03 at z21
    show jenni np01 at c22
    i "Un momento... "
    i nbp03 "¿Ella te dijo algo?"
    show issei np04
    pr "Sí..."
    pr "A eso iba."
    pr "Lo peor de todo fue cuando le iba a tratar de decirle mi nombre.... "
    pr "Entonces ella..."
    pr "Ella..."
    show jenni nbp05 at z22
    show issei at c21
    j "¡Habla de una vez!" 
    show jenni nbp06
    pr "E-Ella....."
    show jenni at c22
    show issei nbp03 at z21
    i "Amigo, ¿Qué paso?"
    show issei np04
    pr "{size=-6}{cps=80}Me dijo que yo era su novio{/cps}{/size}."
    show jenni nbp05 at z22
    show issei at c21
    j "¡Vamos [player!t] habla más fuerte que no se te escucho nada de lo que dijiste!" 
    show jenni nbp06
    pr "Me dijo....."
    show jenni np15 at ztj22
    show issei np09 at ztj21
    ji "¡YA DILO!{nw=0.30}"
    pr "¡ME DIJO QUE YO ERA SU NOVIO!"
    show jenni np13 at c22
    show issei np04 at c21 
    pr "Ya{w}...Ya lo dije."
    ji "..."
    show jenni np14 at z22
    j "¿Te{w}....Dijo{w}...Que tú eras su novio?"
    j np13 "....."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    play music a4 fadein 2.0
    ji "¡JAJAJAJAJA!"
    show issei np11 at c21
    j "¡Como que te dijo que eras su novio!"
    j "¡Tan desesperado estás por conseguir una novia que...."
    show jenni at ztj22
    j "¡Que inventas este tipo de cosas!"
    show jenni at ztj22
    j "¡JAJAJAJA!"
    show issei np10 at z21
    show jenni np09 at c22
    i "¡Vamos bro, dinos algo más{w}...."
    show issei at ztj21 
    extend "más realista!"
    show issei np11
    pr "¡Por eso no quería decirles!"
    pr "¡Yo sabía que iban a terminar riéndose de mí!"
    show issei np02 zorder 2
    i "Porque eso que nos dijiste es bastante irreal."
    i "Y si eso fuera cierto."
    i np07 "Yo que tú, no estaría aquí hablando, estaría haya divirtien-{nw=0.80}"
    show jenni nbp17 zorder 1 at j11
    with truewhite
    play audio punch
    j "¡Heyy!{nw=2.0}"
    show issei np12 zorder 2 at z21
    i "¡Ouch!"
    i "¡Ya perdón!"
    i "Jeje."
    show jenni ap02 at z22
    show issei np13 at c21
    j "Sigue con tus chistes de mal gusto que te dejare inconsciente."
    show issei np12 at z21
    show jenni ap01 at c22
    i "Vale está bien."
    show jenni n1p02 at z22
    show issei np01 at c21
    j "Retomando el tema de Yumi."
    pr "Das miedo cuando cambias de una actitud a otra."
    show jenni nbp04
    j "Se hace lo que se puede."
    j nbp01 "Bueno...."
    j n1p02 "Esto que nos contaste{w=1.0}, ¿Es verdad?"
    show jenni np01
    pr "Pues claro que es verdad."
    pr "No voy a mentir sobre algo tan serio."
    show jenni nbp18
    j "¿Serio?"
    show jenni nbp20 at ztj22
    j "¡JA!"
    j "No me hagas reír."
    j nbp03 "Además, si eso fuera verdad."
    j "¿Por qué no te quedaste con ella?"
    show jenni np13
    pr "Porque me agarro con la guardia baja."
    pr "Además..."
    pr "¿Por qué me voy a quedar con una chica que ni conozco?"
    j np02 "Bueno, es que era tu oportunidad para tener una novia."
    j "Falsa, pero igual ibas a tener una novia."
    j ncp02 "Además, ¿No dijiste que ella era linda?"
    show jenni nbp01
    pr "¿Y eso qué?"
    j np08 "Bueno, que al menos dijiste algo de una chica sin fijarte primero en el tamaño de sus pechos."
    j np06 "Un momento..."
    j nbp07 "¿De qué tamaño eran sus pechos?"
    show jenni np06
    pr "¡¿Por qué me preguntas eso?!"
    j nbp07 "Porque es lo primero que ves al conocer una chica."
    "Ya se parece a Emi."
    "Preguntando lo que no debe."
    show jenni nbp07 zorder 2 at superclose
    with dissolve
    j "¿De qué tamaño?"
    show jenni nbp06
    pr "¿Qué te importa?"
    pr "¿Temes que te hagan competencia?"
    show issei np06
    show jenni nbp11 zorder 2
    j "Ehh{w=1.0}.....¡No!"
    j nbp07 "Además...."
    j nbp17 "¡Te la pasas mirándome!"
    pr "Pues claro."
    pr "Ni modo que al hablar contigo, me cubra los ojos."
    j nbp16 "¡No hablo de esa forma idiota!"
    pr "Cálmate."
    pr "Te va a dar un ataque."
    pr "Además no soy el único que te mira."
    pr "Tu sabes que jamás te miraría de mala manera por temor a que Issei me golpee."
    show jenni nbp21
    show issei np10 zorder 1 at j21 
    i "¡Eso es verdad!"
    show jenni nbp12 zorder 2 at c22
    j "Bueno, tienes razón."
    show jenni np01
    show issei np01
    pr "Okey."
    pr "Retomando otra vez el tema de Yumi."
    stop music fadeout 2.0
    pr "Ella al decirme que yo soy su novio."
    pr "No lo pensé dos veces y salí corriendo de su casa."
    show issei nbp02 at z21
    i "Con razón estabas tan nervioso que te desmayaste."
    show issei np01
    pr "Y les quería preguntar..."
    pr "¿Es buena idea ir a la casa de Yumi y disculparme con ella por irme así?"
    pr "Es que si no lo hago, sé que mi mente no me dejaría en paz."
    pr "Y si voy me sentiré extraño estando en esa casa de nuevo."
    i np03 "Bueno..."
    i "Creo que sí."
    show issei np01
    pr "¿Tu que dices Jenni?"
    show jenni np02 at z22
    show issei at c21
    j "Bueno, concuerdo con Issei."
    j "La verdad fue muy malo de tu parte salir así de su casa."
    j "Ella debió tener sus razones para decirte que..."
    j "Que..."
    show jenni nbp20 at ztj22
    extend "¡Que tú eras su novio!"
    show jenni at ztj22
    j "¡JA!"
    pr "¡Vamos Jenni!"
    pr "No se vale."
    pr "No te sigas riendo de mí."
    j nbp08 "Como quieres que no me ría..."
    j "Sí eso suena tan ilógico."
    j nbp05 "Además, seguro le hiciste algo a esa pobre chica para que fijara en un tipo como tú."
    "Lo dijo."
    show jenni nbp06
    pr "¡Yo no le hice nada!"
    pr "¡Ni siquiera la conozco!"
    j nbp12 "Bueno, bueno."
    j "Solo estoy bromeando contigo."
    j "Dejando eso de lado."
    j ncp12 "¿Cuándo planeas ir a disculparte con ella?"
    show jenni nbp22
    pr "Tengo la intención de ir hoy, pero...."
    j np14 "¿Pero..?"
    show jenni np13
    pr "Me preguntaba, si pueden acompañarme."
    show issei np02 at z21
    show jenni np01 at c22
    i "Seguro, ¿Por qué no?"
    i nbp02 "¿Jenni?"
    show jenni nbp02 at z22
    show issei np01 at c21
    play music a7 fadein 2.0
    j "Por supuesto."
    j "Siempre y cuando ella no sea una loca desquiciada que intentara hacer daño por mi está bien."
    show jenni np01
    pr "Descuida ella es todo lo contrario."
    j np02 "Bueno, iré al baño un momento."
    j "Cuando regrese, nos vamos a la casa de Yumi."
    show jenni np01
    pr "De acuerdo."
    show jenni at hidetr
    hide jenni
    show issei np02 at c11
    i "Vale Jenni."
    i "Nosotros te esperamos."
    i np14 "Mmm..."
    i np02 "Oye Bro."
    show issei np01
    pr "¿Qué pasa Issei?"
    i nbp02 "¿Cómo es Yumi?"
    show issei np01
    pr "Bueno..."
    pr "Su cabello es corto y de color purpura oscuro."
    pr "Ojos de color purpura."
    pr "Muy brillantes, por cierto."
    pr "Piel de color muy clara."
    pr "Vestía un camisón azul."
    pr "Y su cuerpo tiene sus buenas curvas."
    i nbp02 "Literalmente la analizaste toda."
    show issei np01
    pr "Si, aunque todavía me pasa por mi mente la pregunta de qué..."
    pr "¿Cómo una chica tan linda se la pasa encerrada en su casa?"
    i nbp02 "Como la describiste si se oye bonita esta Yumi."
    show issei np01
    pr "Aunque en realidad se me hizo raro que..."
    pr "Aunque tenía la casa descuidada, ella no se veía que le hacía falta comida."
    pr "No se veía ni muy gorda ni muy delgada."
    pr "Tiene un buen cuerpo."
    pr "Aunque, lo más grande de su cuerpo eran sus-{nw=0.30}"
    show issei np04 at c21
    show jenni nbp04 at j22
    j "¡¿De qué están hablando?!{nw=0.5}"
    pr "¡Ahhhhh!"
    pr "¡No hagas eso!"
    show jenni np13
    show issei np01
    "Menos mal que me interrumpió porque ya estaba a punto de decir algo que no quería."
    pr "¡Casi me causas un infarto!"
    show jenni np02 at z22
    j "Perdón, perdón."
    j np01 "¿De qué estaban hablando?"
    pr "De nada importante."
    j np14 "¿Enserio?"
    show jenni np13
    pr "Si, descuida."
    j np01 "Okey."
    j np02 "¿Nos vamos?"
    show jenni np01
    pr "Claro."
    show issei at hidetr
    show jenni at hidetr
    hide issei
    hide jenni
    scene black with wipeleft_scene
    pause 0.30
    play audio dooropen
    scene isseihouse with wiperight_scene
    pause 0.25
    show issei np01 at c21
    show jenni np01 at c22
    pause 1.0
    show jenni np02 at z22
    j "¿Y....?"
    j ncp02 "¿Dónde queda la casa de Yumi?"
    show jenni nbp01
    pr "Te dije que ella vive en nuestro edificio."
    j nbp09 "Sí es cierto."
    j nbp08 "Se me olvido."
    show issei np02 at z21
    show jenni np01 at c22
    i "Bueno, comencemos a caminar, porque se nos hará tarde."
    show issei np01
    pr "Tienes razón."
    pr "Vámonos."
    stop music fadeout 2.0
    scene city2 with wipeleft
    "Mientras caminamos..."
    "Comienzo a pensar en lo que le voy decir a Yumi."
    "Cielos..."
    "Enserio{w}, ¡¿Qué le voy a decir?!"
    "No le voy decir solo...{w=1.0}{i}'Perdona por salir así de tu casa, adiós'{/i}"
    "Debo dar más explicaciones."
    "..."
    "A parte preguntarle porque me dijo que yo era su novio."
    "Pero{w}...No sé qué debo decirle."
    "Será que...{w}¿Le pregunto a Issei y o Jenni?"
    "Pero..."
    "A quién de ellos le preguntare."
    "Mmm..."
    "Aunque para esto debería tener yo una respuesta."
    "Pero recibir una pequeña ayuda no tiene nada de malo."
    "¿Verdad?"
    menu:
        "Le preguntare a..."
        "Issei.":
            "Mejor le pregunto a Issei."
            pr "¡Issei!"
            pr "Acércate un momento."
            show issei np01 at c11
            play music a7 fadein 2.0
            i "¿Qué pasa bro?"
            pr "No sé qué debo decirle a Yumi para disculparme."
            i np03 "Bueno, yo pienso que deberías decirle que lo sientes y ya."
            i nbp03 "No hay una forma especial de pedir disculpas."
            i np03 "Pero..."
            i nbp02 "Sí el problema es que quieres disculparte por haber salido así de su casa después de su casi 'confesión'."
            i np02 "Entonces dile que no supiste reaccionar ante su 'confesión'."
            show issei np01
            pr "Tiene sentido."
            pr "Pero la duda sigue siendo que si yo no la conozco..."
            pr "¿Por qué me dijo que yo era su novio?"
            i np04 "Bueno..."
            i np03 "Eso no puedo responderlo."
            i nbp03 "Ya que ni tu sabes porque."
            show issei np01
            pr "Tienes razón."
            pr "Gracias Issei."
            i np02 "De nada bro."
            show issei np01
            pause 0.4
            show issei at hidetr
            hide issei
        "Jenni.":
            "Mejor le pregunto a Jenni."
            "Aunque espero que no me diga 'idiota' por no resolver esto yo solo."
            pr "¡Jenni!"
            pr "Ven."
            pr "Acércate un poco."
            play music a7 fadein 2.0
            show jenni np01 at c11
            j "¿Qué ocurre [player!t]?"
            pr "No sé qué debo decirle a Yumi para disculparme."
            j np06 "La verdad no veo porque te mortificas tanto."
            j np12 "Disculparse no debe ser difícil."
            j nbp02 "Sí lo haces de buena manera, tu disculpa será bien recibida."
            show jenni np01
            pr "Tienes razón."
            pr "Pero me sigue entrando la duda de que..."
            j np14 "¿De qué?"
            show jenni np13
            pr "De, ¿Por qué debo disculparme si ella literalmente se burló de mí?"
            j nbp06 "Primero..."
            j "Ella no se burló de ti."
            j "En realidad nadie en la vida le dice a una persona {i}'Tu eres mi novio'{/i}."
            j "Sin siquiera conocerlo."
            j nbp07 "Sigo creyendo que le hiciste algo para que te dijera eso."
            "Lo volvió a decir."
            pr "¡¡Que yo no lo hice nada!!"
            pr "Apenas sabia su nombre."
            j nbp06 "Sí, como sea."
            j nbp02 "Sí quieres disculparte por salir de su casa sin despedirte…"
            j "Entonces solo di que lo sientes y ya."
            j "No es muy complicado."
            show jenni np01
            pr "Okey..."
            pr "Gracias Jenni."
            j np02 "De nada idiota."
            show jenni nbp20 at ztj11
            j "¡JA!"
            show jenni at hidetr
            hide jenni
            pr "¡Oye!"
    pause 2.0
    pr "Bueno..."
    stop music fadeout 2.0
    "Lo único que necesito ahora es dejar el nerviosismo."
    "Pedir una disculpa no es algo súper complicado."
    "El problema es cómo va a reaccionar Yumi."
    "Bueno, tendré que prepararme ante la reacción que tome."
    pause 2.0
    "Unos pasos más y llegamos al edificio."
    scene apartment_exterior with wipeleft_scene
    show issei np01 at c21
    show jenni np01 at c22
    pause 1.0
    pr "Bueno, yo iré a la casa de Yumi."
    show issei np06
    show jenni np13
    pr "Ustedes suban a mi casa y espérenme."
    show jenni np14 at z22
    j "¿Quieres que nos quedemos en tu casa?"
    j ap02 "Pero si también queremos conocer a Yumi."
    j "Además, dijiste que te acompañáramos."
    show jenni ap01
    pr "Pero prefiero ir solo antes de que se burlen de mí."
    j nbp11 "Que mal."
    show issei np01
    j nbp01 "Bueno...."
    j nbp02 "Sabes que en realidad apenas son los alumnos de nuestro salón que conocen la apariencia de Yumi."
    play music a1 fadein 2.0
    j ap03 "Pero no importa si no quieres que no la conozcamos aún."
    show issei np01
    j "De todas formas la conoceremos muy pronto..."
    j ap06 "Cuando formalicen su relación."
    show jenni nbp20 at ztj22
    j "¡JA!"
    pr "¡Oye!"
    show jenni np01
    pr "Nosotros no formalizaremos nada."
    j np12 "Sí como no."
    j np02 "Yo que tu aprovecharía esta oportunidad."
    j "Para que al menos termines la secundaria con al menos una sola relación."
    show jenni np01 at c22
    show issei np02 at z21
    i "Jenni tiene razón."
    i "Deberías tratar de acercártele."
    i np02 "Por lo que me dijiste, debo imaginarme lo bonita que debe ser Yumi."
    i np15 "Así que aprovecha la oportunidad."
    pr "Ustedes dos están bien locos."
    show issei np01
    pr "Mejor me voy antes de que me contagien su locura."
    pr "Adiós."
    show issei np02
    show jenni np02
    ji "Adiós [player!t]."
    stop music fadeout 2.0
    scene apartment_exterior with wipeleft_scene
    "Issei y Jenni, se quedaron unos minutos en la planta baja."
    "Mientras yo subía hasta el apartamento de Yumi."
    "Espero que esta vez no tenga que soportar ese ambiente tan aterrador."
    window hide(Dissolve(.2))
    pause 1.0
    window auto
    "Solo unos pasos más y estoy parado frente a su puerta."
    "Bueno..."
    "Toco el timbre por si acaso."
    pause 0.5
    play audio doorbell
    pause 2.0
    "No hay respuesta."
    "Vuelvo a tocar el timbre."
    play audio doorbell
    pause 2.0
    "Nada de nuevo."
    stop audio fadeout 0.5
    "Voy a tener que entrar otra vez."
    play audio doorcreak3
    scene black with wipeleft_scene
    $ renpy.music.set_volume(0.15, channel="music")
    play music a5 loop fadein 2.0
    scene yumi_livingroom_dark with dissolve
    "La casa sigue estando igual."
    "Esta vez me siento aún más nervioso."
    "Seguro es porque me tengo que disculpar con ella."
    pause 1.0
    scene black with dissolve
    "Iré directamente a su cuarto porque no tengo otra cosa más que hacer aquí."
    pause 1.0
    scene yumi_hall 
    show black zorder 500:
        ease 10 alpha 0.5
    pause 1
    "Me siento extraño otra vez dentro de esta casa."
    "Estar aquí se siente muy extraño."
    "Voy a acercarme sigilosamente a la puerta."
    scene yumi_door 
    show black zorder 500:
        ease 4 alpha 0.5
    with dissolve
    "Esta vez tratare de acercarme más para escuchar que está pasando ahí adentro."
    scene yumi_room_door_1 
    show black zorder 500:
        ease 4 alpha 0.5
    show vignette1 zorder 100
    with dissolve
    "Al acercarme, escucho un llanto."
    play audio yumi_cry
    pause 2.0
    "Me imagino que debe ser Yumi la que está llorando."
    "Voy a abrir la puerta con cuidado."
    play audio doorcreak4
    scene yumi_room_door_2 
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with dissolve
    "¡Cielos!"
    "Casi me da un infarto."
    "Ella está allí sentada."
    "¿Qué estará haciendo?"
    pause 1.4
    y "¿Por qué?"
    pause .30
    y "¿Por qué nadie me quiere?"
    pause .30
    y "¿Será que no soy una buena chica?"
    y "¿Por qué la vida es tan mala conmigo?"
    y "¿Por qué tengo que soportar estar en un mundo en el que nadie me quiere?"
    y "{i}*suspiro*{/i}"
    y "A veces quisiera sentir un poco de felicidad cómo todos."
    y "Me gustaría que estos pensamientos no me atormentaran todos los días."
    pause 1.0
    stop music fadeout 2.0
    "Cielos..."
    "Yumi...."
    $ renpy.music.set_volume(1.0, channel="music")
    play music a9 fadein 2.0
    "¿Yumi tiene depresión?"
    "Me da un poco de tristeza saber eso..."
    "Una chica tan linda…"
    "Y con depresión."
    "No estoy diciendo que ninguna chica linda no pueda desarrollar depresión."
    "Pero me da un poco de lastima…"
    "Cielos…"
    y "Hasta mi imaginación me hace malas jugadas."
    y "Ese chico de ayer, desapareció como apareció."
    y "Súper rápido."
    y "Y pensar que al menos me había imaginado a alguien que me quisiera."
    y "Aunque sea un poco."
    "¿Ella cree que soy un producto de su imaginación?"
    "Eso duele..."
    "Siento como si me clavaran cien cuchillos en mi corazón."
    "Tan sola esta Yumi para creer en ese tipo de cosas."
    "Bueno no es momento de pensar en eso…"
    "Pobre Yumi..."
    "Me imagino como debe de estar sufriendo todos los días."
    "Bueno, en realidad yo no sé cómo funciona la depresión."
    "Lo que me puedo imaginar es que el cerebro de alguien con depresión los hace pensar que no valen nada."
    "No sé si eso es cierto."
    "Aunque existen pastillas para contrarrestar la depresión."
    "Pero aún pienso que es algo que hay que tomar enserio."
    "Aunque me duele pensar el hecho de que Yumi crea que todas las personas a su alrededor no la aprecian."
    "Quizá pueda investigar cómo se trata a una persona con depresión."
    "Si no se me olvida, claro."
    "No estoy diciendo que las personas con depresión hay que tratarlas como si estuviesen locos."
    "Ya estoy repitiendo otra vez todo lo que digo."
    "{i}*suspiro*{/i}"
    "Me voy a armar de valor y ayudar a Yumi a salir de esto."
    "Tratare de cerrar la puerta con cui-{nw}"
    stop music fadeout 0.2
    play audio doorcreak3
    "¡Cielos, hice demasiado ruido!"
    "Ojala no haya escucha-{nw}"
    scene yumi_room_door_3 
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with dissolve
    window hide(Dissolve(.2))
    pause 1.0
    window auto
    pr "Eh...."
    y "Mmmm...."
    y "¿Tú....?"
    pr "H-Hola."
    "Cielos."
    "Me metí en problemas."
    y "Vol...{w=1.0}vol..."
    window hide(Dissolve(.2))
    scene hiroki_surprise:
        zoom 1.30
        xoffset -10
        pause 3.30
        linear 30.000 zoom 1.0 xoffset 0
    with flash
    window auto
    play music a2 fadein 4.0
    y "¡Volviste!"
    y "Pensé que nunca volverías."
    y "Estoy tan feliz."
    y "¡Yeeey!"
    "¿Qué rayos está pasando?"
    "Esto..."
    "Esto se siente..."
    "Un poco bien..."
    "Y a la vez muy incómodo."
    "Sí quiero ayudar a Yumi..."
    "Tendré que seguirle el juego de que soy su novio imaginario."
    "Aunque me incomode."
    scene yumi_door
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100 
    with dissolve
    pause 0.3
    show yumi fsl05 at c11
    y "Pensé que no regresarías, cariño."
    y fsl06 "Yo sabía que mi imaginación no me había defraudado."
    "Eso suena muy triste."
    "Me duele mucho el pensar que ella crea que no existo."
    "Y me hace sentir incómodo a la vez."
    show yumi fsl02 at jr11
    play music a3 fadeout 2.0
    y "¿Y qué quieres hacer hoy?"
    show yumi fsl01
    pr "E-Ehhh...."
    "Cielos, no sé qué responder.."
    "En realidad nunca he tenido una relación en mi vida."
    "¿Cómo debo responder a eso?"
    "..."
    "Veré si esto sirve..."
    pr "Ehh, No lo sé..."
    pr "P-Podemos hacer lo que tú quieras..."
    show yumi fsl04 at c11
    y "Hmm...."
    y fsl02 "¿Te parece tomar un poco de café?"
    show yumi fsl01
    pr "E-Ehh, claro, ¿Por qué no?"
    "Tengo que calmarme un poco."
    "Esto en realidad es muy difícil."
    "Me siento como si estuviera en una escena cliché de algún anime."
    show yumi fsl05 at j11
    y "¡Vamos!"
    show yumi at rhide
    hide yumi
    "Bueno{w=1.5}, qué más da..."
    stop music fadeout 2.0
    "Sigo a Yumi hasta la sala."
    pause 1.0
    scene yumi_livingroom_dark
    show black zorder 500:
        alpha 0.5
    show vignette1 zorder 100
    with wipeleft_scene
    pause 0.20
    show yumi fsl02 at c11
    y "Perdona si mi casa está un poco oscura, iré a abrir las cortinas."
    show yumi fsl01 at lhide
    hide yumi
    pause 0.30
    scene yumi_livingroom with wiperight
    "¡Que!"
    "Vaya diferencia."
    "Es raro como su casa al estar a oscuras se vea tan tenebrosa."
    show yumi fsl05 at l11
    pause 0.20
    y "¿Mejor?"
    show yumi fsl06
    pr "Sí."
    "La casa de Yumi no se ve tan mal como me lo había imaginado."
    show yumi fsl02 at j11
    y "¿Y qué tipo de café te gusta, cariño?"
    show yumi fsl01
    play music a7 fadein 2.0
    pr "¿Eh?"
    pr "Ah."
    pr "A mí me gusta el café con leche."
    show yumi fsl02
    y "¿Te gustaría probar otros?"
    show yumi fsl01
    pr "Nunca es tarde para nuevas experiencias."
    pr "Pero en este caso, nuevos cafés."
    show yumi fsl05 at j11
    y "¡JAJA!"
    y "Eres tan divertido."
    y fsl01 "Bueno, te puedo ofrecer…"
    y fslb02 "Café expreso, café con leche…"
    show yumi fsl06 at j11
    y "El que te gusta."
    y fslb02 "Café helado, capuchino, café normal…"
    show yumi fsl05 at j11
    y "Jeje."
    y fsl02 "Y creo que esos son los únicos que te puedo ofrecer."
    show yumi fsl01
    pr "Mmm...."
    pr "Bueno..."
    "Creo que responder sería lo más adecuado."
    menu:
        pr "Me gustaría un..."
        "Café normal.":
            pr "Me gustaría un café normal."
            pr "Prefiero lo cotidiano."
        "Café expreso.":
            pr "Me gustaría un café expreso."
            pr "Me gusta la espuma que tiene."
        "Café con leche.":
            pr "Me gustaría un café con leche."
            pr "Es bueno para comer con pan."
        "Café helado.":
            pr "Me gustaría un café helado."
            pr "Dicen que es muy bueno para estos días calurosos."
        "Capuchino.": 
            pr "Me gustaría un capuchino."
            pr "Sería la primera vez que lo pruebo."

    y fsl05 "Ahora mismo lo preparo."
    show yumi fsl06 at hidetr
    hide yumi
    pr "Okey, yo espero aquí."
    "Veo disimuladamente alrededor de la sala y veo que está un poco sucia."
    "También puedo alcanzar a ver vasos de fideos instantáneos y alguno que otro papel en el suelo."
    "Bueno no era de esperarse ya que ella tiene su casa descuidada."
    "Ella es muy linda y buena persona."
    "¿Cómo habrá desarrollado su depresión?"
    "O...{w=2.0}¿Será Bipolar?"
    "Bueno, más tarde investigo en internet como las personas pueden llegar a desarrollar depresión o bipolaridad."
    "Aunque no termine sirviendo de nada, porque no soy psicólogo."
    "Y cómo dijo Issei{w=1.0} y bueno{w=2.0} también Jenni..."
    "Voy a tratar de acercarme a ella."
    "Aunque no termine en una relación."
    "Sería bueno terminar siendo su novio real."
    "Ya que esto de fingir ser el novio imaginario no contara, que conste."
    pause 1.0
    show yumi fsl01 at c11
    "Un rato después Yumi regresa con nuestros cafés."
    "Ella se preparó un café con leche." 
    show yumi fsl05 at j11
    y "Toma, cariño."
    show yumi fsl06
    "Tomo la taza de café de su mano."
    pr "G-Gracias."
    "Vamos y nos sentamos en la mesa del comedor."
    "Ella se sienta enfrente de mí."
    scene ycobg
    show yco a1 zorder 1
    show ycodesk1 zorder 10
    show ycolight zorder 100
    with Dissolve(.3)
    pause 0.50
    yc "¿Y....?"
    yc a2 "¿Cuál es tu nombre?"
    yc "Porque te he estado diciendo 'cariño' sin saberlo."
    yc a5 "Jeje."
    yc a6 "Aún no me lo imagino."
    yc "Aunque ya debes tener uno, ¿Verdad?"
    show yco a5 zorder 1 with dissolve
    "Así no funciona la imaginación, Yumi."
    "La verdad no veo porque no te has dado cuenta de que soy una persona de carne y hueso."
    "Aunque es mejor que no te des cuenta ya que si lo haces, lo primero que harás es llamar a la policía..."
    "Y me arrestaran por allanamiento de morada."
    "Y la verdad no quiero que me metan a la cárcel."
    if not player == _("Hiroki"):
        pr "Mi nombre es [player!t]."
    if player == _("Hiroki"):
        pr "Mi nombre es Maki [player!t]."
    yc a6 "Un gusto [player!t]."
    yc "Mi nombre es Akemi Yumi."
    yc a5 "Jeje."
    "Eso ya lo sé."
    yc a1 "Y.....{nw=2}"
    show yco b1 zorder 1
    hide ycodesk1
    show ycodesk2 zorder 2
    with Dissolve(.2)
    "Ella toma un sorbo de su café antes de continuar con su frase."
    hide ycodesk2
    show ycodesk1 zorder 2
    show yco a2 zorder 1
    with Dissolve(.2)
    yc "¿Qué haces normalmente?"
    show yco a1
    pr "¿Cómo así?"
    yc a17 "Que, ¿qué haces en tu día?"
    yc a2 "¿Cómo lo pasas?"
    yc "¿En qué te entretienes?"
    show yco a1
    pr "Ah okey."
    pr "Cuando son días de semana..."
    pr "Voy a la escuela, hablo con mis amigos..."
    pr "Y cuando regreso a mi casa, me pongo a hacer la tarea."
    pr "Sí es que hay."
    if game_reference == "Geometry Dash":
        pr "Y después me pongo a jugar Geometry Dash."
    else:
        pr "Y después me pongo a jugar Friday Night Funkin'."
    yc a3 "¿[game_reference]?"
    yc a18 "¿Qué es eso?"
    show yco a19
    pr "Ah, es mi videojuego favorito."
    pr "Quizá no lo conoces."
    show yco b1 zorder 1
    hide ycodesk1
    show ycodesk2 zorder 2
    with Dissolve(.2)
    "Ella toma otro sorbo de su café."
    hide ycodesk2
    show ycodesk1 zorder 2
    show yco a2 zorder 1
    with Dissolve(.2)
    yc "¿Qué grado cursas?"
    show yco a1
    pr "¿Eh?"
    yc a17 "¿En qué año vas en la escuela?"
    pr "Ahhh..."
    pr "En décimo grado."
    yc a6 "Que curioso, también yo.."
    yc a5 "Jeje."
    yc a6 "Que bien te imagine."
    yc "Eres el novio que cualquier chica quisiera tener."
    "Yumi..."
    "Así no funciona la imaginación."
    "La verdad, me duele mucho cuando ella dice que soy un producto de su imaginación."
    "Y cómo ya dije, esto me hace sentir incómodo."
    "..."
    "Mi café lleva rato desde que Yumi me lo dio."
    "Mejor tomo un poco para no ser descortés."
    pause 1.0
    pr "¿Yumi?"
    yc a2 "¿Qué ocurre, cariño?"
    show yco a1
    pr "¿Te puedo hacer una pregunta?"
    yc a2 "Claro, pregunta."
    show yco a1
    "Hmmm..."
    "Debo pensar que debo preguntarle."
    "Porque si no cuido mis palabras puedo hacerla enojar."
    menu:
        "¿....?"
        "¿Por qué usas un camisón tan transparente?":
            $ persistent.yumiquestions = 0
        "¿Por qué esta tú casa tan sucia?":
            $ persistent.yumiquestions = 1
        "¿Por qué te la pasas encerrada?":
            $ persistent.yumiquestions = 2
        "¿Por qué me dices 'cariño'?":
            $ persistent.yumiquestions = 3
        "¿Por qué estás sola?":
            $ persistent.yumiquestions = 4

    if persistent.yumiquestions == 0:
        "Esta pregunta es un poco rara."
        "Ya que apenas me estoy dando cuenta de que ella está usando un camisón semi-transparente."
        "Debe de ser muy viejo o debe estar muy maltratado."
        "¡Puedo vérselos!"
        "Espero que no comience a circular sangre en el lugar equivocado."
        pr "¿Por qué usas un camisón tan transparente?"
        yc a2 "Bueno, es que no me gusta usar mucho el brasier."
        show yco a1
        pr "Esa no es la pregunta."
        yc a2 "Bueno me gusta andar vestida así."
        yc "Es más fresco."
        yc a21 "¿Me has estado mirando?"
        yc a6 "Uyy, pervertido."
        yc a5 "Jeje."
        pr "Sabes que si recibes a un invitado no puedes andar vestida así."
        yc a2 "Es que no tengo ropa limpia."
        yc "Aparte si uso esta ropa no estoy obligada a usar brasier."
        yc "Ya que me aprieta mucho."
        show yco a1
        "Hay dos grandes razones para eso."
        pr "P-pero..."
        pr "Se te ven los...{nw=0.40}"
        yc a2 "¿Senos?{w=2.0}  ¿Pezones?"
        yc "No tiene nada de malo si tú me miras."
        yc a6 "Eres mi novio después de todo."
        show yco a5
        "No."
        "No lo soy."
        "Aunque en realidad esta oportunidad de ver un par de grandes senos no se va a repetir."
        "¿Qué estoy diciendo?"
        "Sueno como todo un pervertido."
        "Cielos, estar con Yumi me hace pensar cosas que no debería."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 1:
        "Esta pregunta debe ser un poco fácil de responder."
        pr "¿Por qué esta tú casa tan sucia?"
        yc a2 "Es que no me gusta limpiar."
        yc a22 "Me da flojera."
        show yco a23
        pr "Limpiar no tiene que ser aburrido."
        show yco a1
        pr "Puedes poner un poco de la música que te gusta y el ambiente se puede poner mejor."
        pr "Y al final verás que al limpiarla se verá mejor."
        yc a2 "La verdad yo no escucho música."
        yc "Pero voy a pensar en eso."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 2:
        "Esta pregunta es un poco personal."
        "No se cómo se la vaya a tomar."
        pr "¿Por qué te la pasas encerrada?"
        yc a19 "Hmm...."
        yc a24 "Es que no me gusta la gente."
        yc a25 "Me pongo nerviosa cuando hay mucha gente a mí alrededor."
        yc a6 "Creo que soy personifobica."
        yc a5 "Jeje."
        "No creo que así se llame la fobia a otras personas."
        "Bueno, yo tampoco sé cómo se llama."
        "..."
        "Quizás más tarde lo googlee."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 3:

        "Esta pregunta creo que sería más rara para Yumi que para mí."
        pr "¿Por qué me dices 'cariño'?"
        yc a2 "Bueno es que una novia le debe decir cosas bonitas a su novio."
        yc "Una de ellas es decirle: 'cariño', 'mi amor', 'amorcito', 'amor mío', 'mi príncipe'."
        yc a27 "¿Por qué...?"
        yc a26 "¿Te molesta?"
        show yco a27
        pr "E-Ehhhhh..."
        pr "N-No."
        pr "Es solo que me tengo que acostumbrar."
        yc a5 "Okey."
        "La verdad me molesta un poco."
        "Pero a la vez me hace sentir bien."
        "Me puedo acostumbrar a eso."
        show yco a1 with Dissolve(.2)

    if persistent.yumiquestions == 4:

        "Esta pregunta debe de ser muy fuerte."
        pr "¿Por qué estás sola?"
        yc a19 "Hmm..."
        stop music fadeout 2.0
        yc a27 "Bueno...."
        yc a26 "Es que..."
        pr "No tienes que decirme si no-{nw}"
        play music a9 fadein 2.0
        yc a28 "Tuve que alejarme de mi familia desde hace unos tres años."
        yc a29 "No quería seguir siendo una carga para ellos."
        yc a27 "Yo.."
        yc a26 "Ten...."
        yc a30 "Tengo depresión."
        "No pensé que ella lo diría así como así."
        "Ya que muchas personas con depresión no sienten que es bueno decirle a alguien que la tienen."
        yc a26 "Fui diagnosticada a los ocho años de edad."
        yc "En ese entonces nada me motivaba."
        yc a27 "Nada me divertía."
        yc a26 "Ya no me gustaba hacer amigos."
        yc a29 "Mis padres vivían muy tristes a causa mía."
        yc "Ya no podían divertirse."
        yc "Porque tenían que estar pendiente de mí."
        yc a27 "De....{w}"
        extend a26 "De que no cometiera una locura."
        yc a29 "Por eso cuando cumplí los catorce años me vine a vivir aquí."
        yc "Y desde entonces vivo con una de mis tías."
        "Esto es muy triste."
        "Yumi se sentía una carga."
        "Contengo las lágrimas para no verme patético."
        "Ya que soy muy sensible ante estas situaciones."
        yc a27 "No me gusta hacer que la gente sienta lastima por mí."
        yc a26 "Pero un día mi tía me llevo a terapia..."
        yc a31 "Después de varias sesiones..."
        yc "Comencé a mejorar y me regresaron los ánimos de volver a la escuela."
        yc a27 "Pero..."
        yc a32 "Fue horrible."
        yc "Todos mis compañeros de clase me trataron como a una loca."
        yc a33 "Se burlaban, se reían..."
        yc a27 "Y...."
        yc a26 "Nadie me quería."
        yc a28 "Los chicos de mi salón solo me acosaban."
        yc a26 "Un día, uno trato de sobrepasarse conmigo."
        yc "Y desde ese día deje de asistir a esa escuela."
        yc a27 "Hasta que mi tía me volvió a inscribir en otra escuela."
        yc a26 "Está era diferente…"
        yc a31 "Todos me trataban bien."
        yc "Me saludaban."
        yc a27 "Hasta que un día me di cuenta de que nadie quería ser mi amigo."
        yc "Yo era la chica más linda del salón."
        yc "Todas mis compañeras me envidiaban."
        yc a26 "Mis compañeros no se acercaban a mí por temor a ser rechazados."
        yc "Era como si yo estuviera en un podio inalcanzable."
        yc a26 "Y mis esperanzas de ser aceptada se fueron."
        yc a29 "Deje de ir poco a poco a la escuela."
        yc a26 "Yo no quería ser vista como la chica a la que nadie se le puede acercar."
        yc "Y poco a poco deje de ser recordada en la escuela."
        yc a31 "Recibía visitas muy a menudo."
        yc a26 "Pero después comenzaron a hacer menos constantes."
        yc a27 "Hasta que nadie me visitaba."
        yc a34 "Pero…"
        yc a8 "Ahora te tengo a ti."
        yc a35 "Serás el sol que brille sobre mis nubes de lluvia y me permita ver el camino."
        yc a8 "Espero que tú tampoco me dejes o me hagas a un lado."
        "Cielos, Yumi ha sufrido tanto."
        "Me siento un poco mal por ella."
        "¿Cómo alguien puede soportar tanto?"
        "Contengo las lágrimas."
        "Cielos..."
        stop music fadeout 2.0
        yc a6 "Dejemos la tristeza a un lado."
        yc a2 "Mejor toma tu café."
        yc "Que casi no te lo has tomado."
        show yco a1
        pr "Ah verdad, mi café."
        pause 2.0
        
    "Nos quedamos callados por un rato y solo tomamos nuestros cafés."
    window auto
    stop music fadeout 2.0
    pause 3.0
    scene yumi_livingroom with wipeleft_scene
    "Después de tomarme mi café veo la hora y noto que he estado aquí por más de una hora."
    "¡Cielos!"
    "¡Issei y Jenni me van a matar!"
    pr "¿Yumi?"
    show yumi fsl01 at c11
    y "¿Qué ocurre, cariño?"
    pr "Q-Que..."
    pr "Q-Que tengo que irme."
    show yumi fsl07 at tr11
    y "Awww.."
    y fsl08 "¿Tan pronto?"
    show yumi fsl07
    pr "Sí, me tengo que ir."
    pr "Es que se me olvido que tenía que hacer algo en mi casa y no lo hice."
    y fsl08 "Aww..."
    show yumi fsl01 at j11
    y "Bueno, te veré después."
    pr "Gracias por entender."
    pr "Nos vemos después."
    y fsl05 "Adiós cariño."
    scene black with wipeleft_scene
    pause 1.0
    play audio dooropen
    scene apartment_exterior with wiperight_scene
    "Hice esperar demasiado a Issei y Jenni."
    "¡Me van a matar!"
    "Cielos..."
    "..."
    "Aunque..."
    "Hablar con Yumi no fue tan malo."
    "Me hizo..."
    "Sentir bien..."
    "¿Puedo decir que me hizo sentir bien?"
    "..."
    "No lo sé."
    "Bueno..."
    "¿Qué estarán haciendo Issei y Jenni?"
    "S-Seguro deben estar planeando como me van a molestar."
    pause 2.0
    scene apartment_exterior with wipeleft_scene
    "No entiendo como paso el tiempo tan rápido."
    "Bueno, creo que dicen que el tiempo pasa rápido cuando haces algo que disfrutas."
    "Pero...."
    "¿Disfrute estar con Yumi?"
    "..."
    "Creo que sí."
    "Pasar el rato con Yumi si me gustó."
    "Bueno..."
    "Mejor no sigo perdiendo más el tiempo y entro a mi casa."
    play audio dooropen
    scene hiroki_livingroom with wiperight_scene
    pause 0.20
    show issei nbp03 at c11
    i "Bro, ¿Qué te ocurrió que tardaste tanto?"
    show issei np04 at c21
    show jenni ap02 at c22
    j "Si, ¿Por qué te tardaste tanto?"
    show jenni at z22
    j "Te estuvimos esperando por más de una hora."
    show jenni ap01 at c32
    show issei at c31
    show emi n1c17 at c33
    e "¡SI!"
    show emi at z33
    e "¡¿QUE HICISTE?!"
    play music a1 fadein 2.0
    pr "Nada."
    show emi dc03
    pr "No hice nada malo."
    show emi dc04 at ztj33
    e "¡Entonces!, ¡¿Por qué te tardaste tanto?!"
    show emi dc03
    pr "Porque estaba conversando y tomando café con Yumi."
    e nc14 "¿Yumi?"
    e n1c09 "¿Quién es Yumi?"
    show emi nc14 at c33
    show jenni np12 at z32
    show issei np01
    j "Oohhh."
    j "Así que ya formalizaste tu relación con Yumi."
    j "Me imagino que hiciste en esa hora que estuviste en su casa."
    show jenni nbp20 at ztj11
    j "¡JA!"
    pr "¡Oye!"
    show jenni np01
    pr "No hicimos nada malo."
    pr "Solo estuvimos conversando y tomando café."
    pr "Ni que fuera un pervertido que quiere ligar con toda chica que se le coloque al frente."
    show issei np07
    show jenni np18
    show emi n1c18
    al "¡Sí eres un pervertido!"
    show issei np01
    show jenni np01
    show emi nc01
    pr "Bueno, ¡Ya!"
    pr "No soy un depredador sexual."
    pr "Solo estuvimos conversando y tomando café."
    show jenni nbp11 at z32
    j "Que mal."
    j "Perdí la apuesta."
    show jenni nbp01
    e nc18 "Bueno Jenni, te toca pagar."
    show emi nc20
    pr "Esperen…"
    pr "¡¿Apostaron?!"
    show jenni at c32
    show emi nc02 at z33
    e "Sí."
    e "Pero no fue nada malo."
    e n3c02 "Yo aposté que tu no hacías nada sexual con Yumi."
    e "Y Jenni apostó que tu terminarías por llevarla a la cama."
    show emi nc01
    show jenni nbp23 at j32
    pr "¡Jenni!"
    show emi at c33
    show jenni nbp11 at z32
    j "Perdón, perdón."
    j np08 "Es que estábamos tan aburridos que decidimos hacer esta apuesta."
    j nbp24 "La cual perdí."
    show jenni nbp23
    pr "Es que no estoy molesto por la apuesta."
    j np14 "¿No?"
    show jenni np13
    pr "Bueno{w=2.0}, un poco."
    pr "Estoy molesto por que le están enseñando cosas malas a Emi."
    show emi n1c05 at z33
    show jenni at c32
    e "Por favor hermanito."
    e "No soy una niña pequeña."
    show emi nc20
    pr "Sí lo eres."
    pr "Tienes 13 años."
    show emi ac01 at ztj33
    e "¡Que no soy una niña pequeña!"
    show emi at ztj33
    e "¡Ya estoy grande para oír este tipo de cosas!"
    show emi dc01
    pr "No."
    pr "No lo estás."
    e dc06 "Pero quiero escuchar lo que van a hablar."
    show emi dc08
    pr "No."
    pr "Sabes que te he dicho que oír conversaciones ajenas es de mala educación."
    pr "Así que a tu cuarto."
    e dc12 "Pero..."
    show emi dc13
    pr "Sin peros."
    pr "Esas lágrimas falsas no me convencerán."
    pr "A tu cuarto."
    show emi dc01 at ztj33
    e "Hmph..."
    show emi ac01 at ztj33
    e "Te odio."
    pr "Si, yo también."
    pr "Pero a tu cuarto."
    show emi dc01 at ztj33
    e "Hmph..."
    show emi at hidetr
    hide emi
    show issei np01 at c21
    show jenni np01 at c22
    pr "¡Sin berrinches!"
    show issei nbp02 at z21
    i "¿Emi siempre es así?"
    show issei np01
    pr "Si, pero igual la quiero mucho."
    pr "Aunque a veces se comporte como una niña pequeña."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    e "¡QUE NO SOY UNA NIÑA PEQUEÑA!"
    pr "¿Hasta allá me oyó?"
    pr "Que súper oído."
    pr "Jeje."
    show jenni np01
    show issei np01
    pause 2.0
    show jenni nbp02 at z22
    show issei at c21
    j "¿Y...?"
    j ncp02 "¿Cómo te fue con Yumi?"
    show jenni nbp01
    pr "Bien."
    j ap03 "No me digas que solo 'bien'."
    j "Tuviste que hacer algo además de tomar café para durar tanto tiempo allá en su casa."
    show jenni nbp22
    pr "No hice nada malo."
    pr "Solo hablamos y estuvimos tomando café."
    pr "Eso es todo."
    j np14 "Enserio eso fue todo."
    show jenni np13
    pr "Te estoy diciendo que sí."
    show issei np02 at z21
    show jenni at c22
    i "Bro, no creo que solo hayas hecho eso."
    pr "¡No hicimos nada sexual!"
    show issei np04
    show jenni np01
    pr "Sí eso es lo que querían escuchar."
    i np12 "Bueno, si queríamos saber eso."
    i np02 "¿Entonces que hicieron además de tomar café?"
    show issei np01
    pr "Hablar y nada más."
    i np03 "¿Enserio?"
    i nbp03 "Entonces debió ser muy aburrido el estar allá con Yumi."
    show issei np01
    pr "No fue aburrido."
    pr "Me gustó mucho conversar con ella."
    i nbp03 "¿Y te disculpaste?"
    show issei np04
    show jenni np13
    stop music fadeout 2.0
    pr "Ehh..."
    pr "No."
    show issei np01 at c21
    show jenni np14 at z22
    j "Pero si a eso fuiste a la casa de Yumi."
    show jenni np13
    pr "Sí, pero...."
    j nbp07 "¿Pero...?"
    show jenni nbp06
    pr "Es que ella estaba muy contenta por verme que ni siquiera toco ese tema."
    pr "El de que me fui corriendo de su casa ignorándola."
    j np14 "¿Y eso por qué?"
    show jenni np13
    show issei np04
    pr "Es que me entere de algo muy delicado."
    j nbp14 "¿Qué es eso tan delicado?"
    show jenni nbp13
    pr "Bueno...."
    pr "En realidad no debería de contarle esto a nadie."
    pr "..."
    pr "Yumi...."
    j nbp14 "¿Yumi qué..?"
    show jenni nbp13
    pr "Yumi tiene depresión."
    j nbp14 "¿Qué?"
    j np14 "Entonces si es muy delicado."
    j n1p14 "¿Cómo lo supiste?"
    show jenni np13
    pr "Ella misma me lo confeso."
    j np14 "¿Así no más?"
    show jenni np13
    pr "Sí."
    pr "Me sorprendió mucho."
    if persistent.yumiquestions == 4:
        pr "Apenas si pude aguantar las lágrimas con todo lo que me contó de cómo fue su vida hace un par de años."
        pr "La verdad me hizo sentir muy triste."
    else:
        pr "Y me dio mucha tristeza."
    pr "Además vive sola."
    pr "Y lo peor fue que ella dijo...."
    show issei nbp03 at z21
    show jenni at c22
    i "¿Qué te dijo?"
    show issei np04
    pr "Que nadie la quería."
    pr "Que si ella no era una buena chica."
    pr "Y que..."
    show issei nbp03 at z21
    show issei np04
    i "¿Qué?"
    pr "Me dijo que yo era un producto de su imaginación."
    pr "Creado para que ella no se sintiera sola."
    pr "Y que cuando salí corriendo dijo que hasta su imaginación la había abandonado también."
    pr "Pero cuando me vio salto de alegría."
    show issei np03
    i "¿Enserio te dijo que eras un producto de su imaginación?"
    show issei np04
    i "....."
    show jenni np08 at ztj22
    show issei np10 at ztj21
    play music a7 fadein 2.0
    ji "¡JAJAJA!"
    i "¡¿Enserio te dijo que eras un producto{nw}"
    show issei at ztj21
    extend " de su imaginación?!"
    show issei at ztj21
    i "¡JA!"
    pr "¡Vamos Issei!"
    pr "¡Jenni!"
    pr "Eso fue verdad."
    show issei np16
    show jenni np25
    stop music fadeout 2.0
    pr "No estoy mintiendo sobre eso."
    pr "Esto es serio."
    show jenni nbp26 at z22
    show issei at c21
    j "Bueno si, tienes razón."
    j "Nos dio risa fue que dijeras eso."
    j "No nos estábamos riendo de Yumi."
    j "Lo siento."
    pr "Bueno..."
    show issei np04
    j np14 "Entonces.."
    j "Ella debe tener una depresión muy alta."
    j nbp26 "No sé cómo se clasifique a la depresión."
    pause 1.0
    show jenni nbp13
    pr "Continuo..."
    pr "Lo que me dio mucha tristeza fue saber que Yumi cree que está sola."
    pr "O que nadie la quiere."
    pr "Así que me dije..."
    pr "{i}Si quiero ayudar a Yumi tendré que seguirle el juego de que soy su novio imaginario.{/i}"
    pr "Para apoyarla en lo que quiera."
    pr "Y eso haré."
    pr "Aunque me incomode mucho."
    play music a7 fadein 2.0
    show issei np01
    show jenni np01
    pr "Voy a hacer que Yumi vuelva a creer en las personas a su alrededor."
    pr "Que se sienta querida."
    pr "Y sobre todo que ya no crea que está sola."
    show issei np02 at z21 
    show jenni at c22
    i "Eso sería muy bueno de tu parte."
    i "Así se habla bro."
    show issei np01 at c21 
    show jenni nbp02 at z22
    j "Y yo que pensé que eras un pervertido que solo piensa en sí mismo."
    j "Eso está bien. "
    show jenni np01
    pr "Y ustedes me van a ayudar."
    show jenni np10 at ztj22
    j "¡QUE!"
    j "¡¿Quieres que te ayudemos?!"
    j np14 "¿Y qué necesitarías de nosotros?"
    show jenni np13
    pr "Bueno....."
    pr "Me gustaría que me ayudaran sobre cómo tratar a tu pareja."
    pr "Ya que si voy a ayudar a Yumi debo saber eso."
    j np11 "¿Y por qué nos preguntas eso?"
    j "Nosotros no sabríamos como responderte."
    show jenni np13
    pr "Jenni no te hagas la que no sabes."
    pr "Claro que debes de saber."
    pr "Issei y tú son novios desde hace unos años."
    pr "Ya deben de saber ese tipo de cosas."
    pr "O me vas a decir que tu conquistaste a Issei solo con tus {i}'encantos'{/i}"
    show jenni nbp17 at ztj22
    show issei np10 at j21
    j "¡Oye!"
    show jenni nbp06
    show issei at j21
    i "¡JA!"
    i "Tienes razón [player!t]."
    show issei zorder 2 at j21
    i "¡JA!"
    show jenni nbp17 zorder 1 at j11
    with truewhite
    play audio punch
    j "¡Heyy!{nw=0.80}"
    show issei np12 zorder 2 at z21
    i "¡Ouch!"
    show issei np12 zorder 2 at ztj21
    i "¡Perdón! ¡Perdón!"
    i "Jeje."
    show jenni nbp12 zorder 2 at z22
    show issei np01 zorder 1 at c21
    j "Bueno, ¿Qué debemos hacer?"
    show jenni np01
    pr "No sé..."
    pr "¿Cómo le debo hablar a una chica?"
    pr "Porque si voy a fingir que soy el novio de Yumi, debo saber cómo se le habla a una chica."
    j nbp21 "Hmm...."
    play music a4 fadeout 3.0
    j nbp12 "Bueno, par-{nw}"
    show issei np07 at z11
    show jenni np10 at c44
    i "Eso te lo puedo contestar fácilmente, bro."
    show jenni np17
    i ncp07 "Para hablar con una chica debes ser perseverante e inteligente."
    i np07 "¿Por qué?"
    i ncp07 "Porque muchas chicas son como unas víboras."
    i "Solo te quieren por el dinero y por tu cuerpo."
    i "Y siempre te estarán controlando, que si con quien hablas y esas cosas."
    show jenni nbp15 at z11
    show issei np04 at c41
    j "¡Eso no es cierto!"
    j ap02 "Yo no soy así contigo."
    j "Y para que dices estupideces si la que te conquisto fui yo, Issei."
    show jenni ap01
    i np07 "Claro, porque fui el único que acepto salir contigo, además de nadie."
    show issei np08
    show jenni np17 at ztj11
    j "Agh."
    j "Mejor continuo antes de que te de una golpiza."
    show jenni np01
    j nbp02 "Bueno...{nw=2.0}"
    j "Para tratarnos a nosotras las chicas debes de ser amable..."
    j nbp08 "Escuchar, saber cómo responder."
    j nbp09 "Y sobre todo..."
    j nbp08 "Decirnos cosas bonitas."
    j nbp05 "No como otros que nada más te hablan bonito cuando quieren algo y ya."
    show issei np05 at z11
    show jenni np17 at c44
    i "¡Eso no es cierto!"
    show jenni at c22
    show issei np06 at z21
    j "¡Claro que sí!"
    j nbp05 "¡Tu nada más me dices cosas bonitas cuando quieres tener...{nw}"
    show issei np04
    show jenni np13
    pr "¡YA PAREN DE PELEAR!"
    pr "Que no estamos llegando a ningún lado."
    show jenni np26 at z22
    show issei np17 at c21
    ji "Perdón."
    j "Es que nos dejamos llevar por el momento."
    show jenni np01
    show issei np01
    pr "Lo que quiero saber es como debo tratar a Yumi."
    pr "No sé..."
    pr "¿Cómo hablarle?"
    pr "¿Cómo tratarla?"
    pr "Hmm...."
    pr "¿Cómo ayudarla?"
    j np14 "Bueno..."
    j "Lo de cómo hablarle y tratarla si te podemos ayudar."
    j "Pero.{w=2.0}..En lo de cómo ayudarla creo que no."
    j "Bueno, si podemos, pero solo dándote consejos y ya."
    j nbp26 "Ya que esta es una situación tan extraña que lo único que podemos hacer es darte unos consejos y más nada."
    show jenni np13
    pr "Eso es lo único que necesito."
    pr "Y agradeceré mucho que me ayuden."
    pause 1.0
    show jenni np01
    pr "Creo que hemos estado aquí parados por un rato."
    pr "¿Les gustaría quedarse a almorzar?"
    j np02 "Claro."
    j "¿Por qué no?"
    show jenni np01 at c22
    show issei np02 at z21
    i "No hay ningún problema."
    show issei np01
    pr "Iré a buscar a Emi para que me ayude a cocinar."
    i np02 "Vale, nosotros te esperamos."
    show issei np01
    window hide(Dissolve(.2))
    stop music fadeout 2.0
    scene black with wipeleft_scene
    pause 1.0
    "Después de cocinar nos sentamos en la mesa a comer."
    pause 3.0
    window auto
    scene hiroki_livingroom with wipeleft_scene
    show jenni np01 at c31
    show emi nc01 at c32
    show issei np01 at c33
    pause 1.0
    pr "Emi, gracias por la comida."
    pr "Estuvo deliciosa."
    play music a7 fadein 2.0
    show emi nc05 at z32
    e "Gracias hermanito."
    e nc02 "Me esfuerzo mucho en cada comida que hago."
    show issei np02 at z33
    show emi nc01 at c32
    i "Eso se nota mucho."
    i "Prefiero comer tu comida todos los días..."
    i np07 "Que comer la espantosa comida de Jenni."
    pause 1.0
    show issei np12
    i "¿Lo dije o lo pensé?"
    show issei np13
    pr "Lo dijiste."
    show emi nc04 at c31
    show jenni nbp17 at z32
    show issei at c33
    j "Con que mi comida te parece espantosa."
    j "Pero bien que te la tragas."
    show jenni nbp16 at ztj32
    j "¡EH!"
    show issei np12 at tr33
    i "Perdón, perdón."
    i "No quería decir eso."
    i "Lo juro."
    j nbp07 "Más te vale."
    j "Porque si sigues diciendo malos comentarios de mí..."
    j "Ya verás lo que te ocurrirá."
    show jenni nbp16 at ztj32
    j "¡ENTENDISTE!"
    show issei np17
    i "S-Sí."
    i "Perdón, perdón."
    show issei np16
    show emi nc01 at c32
    show jenni nbp02 at z31
    j "Bueno Emi, [player!t]."
    j "Issei y yo nos tenemos que ir."
    j "La comida estuvo muy deliciosa."
    j "Hay cosas que tenemos que hacer."
    show issei np05 at z33
    show jenni np13 at c31
    i "Pero si no tenemos nada que hacer."
    show emi nc04 at c31
    show jenni nbp07 at z32
    show issei np16 at c33
    j "¿Qué dijiste?"
    show issei np17 at tr33
    i "Q-Que si tenemos cosas que hacer."
    "Comprobado."
    "Jenni da mucho miedo."
    show jenni np02
    show issei np16
    j "Aclarado ya el asunto."
    j "Issei y yo pasamos a retirarnos."
    j np08 "Adiós Emi."
    j "Adiós [player!t]."
    show jenni np09
    pr "Adiós Jenni."
    e nc05 "Adiós Jenni."
    show emi nc04
    j nbp07 "Vámonos Issei."
    show jenni nbp06
    i np17 "Adiós [player!t]."
    show issei np16
    pr "Adiós Issei."
    show jenni at rhide
    hide jenni
    show issei at rhide
    hide issei
    window auto
    "Issei y Jenni salen de mi casa."
    "Después de esta rara despedida."
    "..."
    "Se puede escuchar sus discusiones desde aquí."
    j "¡QUIEN TE DIO EL DERECHO DE INSULTAR MI COMIDA!"
    i "¡NO ES MI CULPA QUE COCINES TAN MAL!"
    "Pero después ya no se escucha nada."
    pause 3.0
    show emi nc01 at c11
    "Después de unos minutos termino mi almuerzo."
    "Jenni no se terminó el suyo."
    "Emi termino comiéndose el almuerzo de Issei."
    "Que tampoco se lo comió."
    "Y yo me termine de comer el de Jenni."
    pr "Issei y Jenni son la pareja perfecta."
    pr "¿No crees?"
    show emi nc05 at j11
    e "Si, jeje."
    e "A pesar de que se pelean tanto, se quieren mucho."
    show emi nc01
    pr "Sí es verdad."
    pr "Aunque queda comprobado que hay que tenerle miedo a Jenni."
    e n1c16 "Eso es cierto."
    show emi n1c21
    pause 2.0
    "Nos quedamos callados por un rato."
    "Hasta que Emi decide romper el silencio."
    e nc02 "Hermanito..."
    e "..."
    e "¿Cómo te fue con Yumi?"
    show emi nc01
    pr "¿Cómo sabes que estuve con ella?"
    pr "Además..."
    pr "¿Cómo sabes quién es?"
    e nc05 "Issei y Jenni me lo contaron."
    show emi nc04
    pr "..."
    "Cuando vuelva a ver a Issei y a Jenni, hablare con ellos sobre contar lo que hablamos a Emi."
    "Si no lo olvido."
    show emi nc01
    pr "Hace un rato preguntaste de que quien era Yumi."
    e nc16 "Perdón es que no sabía si estábamos hablando de la misma Yumi."
    show emi nc01
    pr "¿Y qué te contaron?"   
    e nc22 "Que ella te dijo que tú eres su novio."
    show emi dc06 at j11
    e "¡Eso no se vale hermanito!"
    show emi dc04 at j11
    e "¡Yo quiero ser tu esposa!"
    show emi dc01
    pr "Emi ya te lo he dicho millones de veces."
    pr "¡Somos! {w=2.0}¡HERMANOS!"
    e dc04 "Esa Yumi va a tener que competir conmigo por tu amor."
    show emi ac01 at j11
    e "¡Y no me dejare vencer!"
    show emi dc01
    pr "Si, lo que tú digas."
    pr "Me voy a mi habitación a investigar unas cosas."
    e nc05 "Okey hermanito."
    e "No veas películas triple X."
    show emi nc04
    pr "¡¿Qué te pasa?!"
    pr "¡¿Estás loca o qué?!"
    pr "¡Yo no veo películas para adultos!"
    pr "¡Y....."
    pr "¡¿Qué haces viendo mi historial?!"
    show emi nc16 at tr11
    e "E-Ehhhhh..."
    show emi nc05 at j11
    e "{cps=90}Tengo que ir a mi cuarto a hacer algo.{/cps}{nw=0.50}"
    show emi nc04 at j11
    e "Adiós.{nw=0.50}"
    show emi at rhide
    hide emi
    pr "¡Emi!"
    pr "¡Deja de estar revisando mis cosas!"
    pr "Esa niña."
    pause 3.0
    "He estado aquí parado por un rato."
    "Mejor me voy a mi cuarto y aprovecho e investigo sobre que es la depresión y la bipolaridad."
    "Para salir de dudas."
    pause 1.0
    stop music fadeout 2.0
    scene hiroki_room with wipeleft_scene
    pause 1.0
    "Okey..."
    "A lo que vine a mi cuarto."
    "Me acerco al escritorio donde está mi computadora y la enciendo."
    window hide(Dissolve(.2))
    scene pc_off_event_day
    show pcev_light zorder 10
    show snow2 zorder 8
    with dissolve
    pause 1.0
    $ renpy.call_screen("confirm", message= _("La escena de encendido de la computadora puede ser salteada\n¿Deseas saltar la escena?"), yes_action=Jump("pc_on_okey"), no_action=Jump("pc_on"))
    jump pc_on

label pc_on:
    #Escena de encendido de la PC
    pause 1.0
    show pc_on_event_day with (Dissolve(.15))
    pause 1.0
    show pc_scene_1 zorder 2
    pause 3.0
    hide pc_scene_1
    show pc_scene_2 zorder 2
    with Dissolve(.1)
    pause 2.0
    show system_loading zorder 5 with Dissolve(.2)
    pause 5.0
    hide pc_scene_2
    hide system_loading
    show pc_scene_1 zorder 2
    with Dissolve(.3)
    pause 1.0
    show pc_scene_3 zorder 2
    pause 3.0
    jump pc_on_okey

label pc_on_okey:
    hide pc_scene_3
    show pc_scene_4 zorder 2
    pause 1.0
    "Bueno..."
    "Ya encendió{w}, comenzare a investigar."
    pause 1.4
    hide pc_scene_4
    show pc_scene_5 zorder 2
    with Dissolve(.1)
    pause 1.0

label systemevent2:
    if persistent.first_browser == 0:
        $ renpy.call_screen("dialog", message= _("A continuación se te mostraran\nUnas opciones de lo que quieres investigar ya sea sobre:\nDepresión, Bipolaridad o TID."), ok_action=Return())
    elif persistent.first_browser == 1:
        pass
label browser_search:
    pause 1.0
    if persistent.investigationcomp == 3:
        jump ch13
    if persistent.investigationcomp == 0:
        $ investigationtext = _("Investigare primero sobre...")
    if persistent.investigationcomp > 0:
        $ investigationtext = _("Ahora investigare sobre...")
    menu:
        
        "[investigationtext!t]"
        "Depresión":
            $ persistent.browsersearch = 0
            $ renpy.jump("ch12")
        "Bipolaridad":
            $ persistent.browsersearch = 1
            $ renpy.jump("ch12")
        "TID(Transtorno de identidad disociativo)":
            $ persistent.browsersearch = 2
            $ renpy.jump("ch12")
label ch12:
    if persistent.browsersearch == 0:
        if persistent.depressiofinishsearch == 1:
            "Ya investigue mucho sobre la depresión."
            "Debería investigar sobre otra cosa."
            jump browser_search
    if persistent.browsersearch == 1:
        if persistent.bipolaridadfinishsearch == 1:
            "Ya investigue mucho sobre la bipolaridad."
            "Debería investigar sobre otra cosa."
            jump browser_search
    if persistent.browsersearch == 2:
        if persistent.disociativfinishsearch == 1:
            "El trastorno de identidad disociativo no me convence."
            jump browser_search
    scene black with Dissolve(2)
    window auto
    "A ver qué resultados interesantes pueden salir."
    window hide(Dissolve(.2))
    pause 3.0
    scene pc5_on_event_day with Dissolve(1.4)
    if persistent.browsersearch == 0:
        window auto
        "Bueno, aquí encontré uno en Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show depressio at is55
        call shownote(info_depresion, False, "page2") from _call_shownote_1
        show depressio at hidetr
        hide depressio
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "Bueno, esto no me ofrece mucho sobre la depresión."
        "Es solo su concepto."
        "Además, me estoy confundiendo un poco."
        "A ver qué dice más abajo."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_depresion_2, False, "page2") from _call_shownote_2
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "..."
        "Yumi debió a ver desarrollado su depresión por...."
        "Espera..."
        "Sí ella dijo que fue diagnosticada a los ocho años."
        "Entonces no sé porque la habrá desarrollado."
        "Bueno, puede ser que seguro sufría de mucho Bullying en la escuela de pequeña."
        "O no era aceptada por sus compañeros de clase."
        "Eso sería uno de los factores por el cual se desarrolla."
        "Tendré que seguir investigando."
        pause 2.0
        "Tratamiento...."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_depresion_3, False, "page2") from _call_shownote_3
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "De seguro Yumi no toma antidepresivos."
        "..."
        "Es suficiente sobre la depresión."
        pause 1.0
        $ persistent.depressiofinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search
    if persistent.browsersearch ==  1:
        scene pc5_on_event_day
        window auto
        "Bueno, aquí encontré uno en Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show TwoFaces at is55
        call shownote(info_bipolaridad, False, "page2") from _call_shownote_4
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        show TwoFaces at hidetr
        hide TwoFaces
        "¿Será que Yumi es bipolar?"
        "Ya que es un poco raro que ella estaba sentada llorando..."
        "Y se haya levantado de golpe y se haya puesto feliz al verme."
        "Creo que estoy diciendo cosas sin saber."
        pause 1.0
        "Aquí no me dice cómo se desarrolla."
        "A ver..."
        "Clasificación..."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_bipolaridad_2, False, "page2") from _call_shownote_5
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "Bueno, no me voy a quedar a leer toda la clasificación."
        "Es muy larga y me da flojera."
        "....."
        "Periodo depresivo...."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show depressio at is55
        call shownote(info_bipolaridad_3, False, "page2") from _call_shownote_6
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        show depressio at hidetr
        hide depressio
        "Hmm..."
        "Bueno...."
        "La verdad, que como vi a Yumi creo que ella debe ser bipolar."
        "Tratamiento..."
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        call shownote(info_bipolaridad_4, False, "page2") from _call_shownote_7
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        "..."
        "Qué lista de medicamentos más larga."
        "Es suficiente sobre la bipolaridad."
        pause 1.0
        $ persistent.bipolaridadfinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search
    if persistent.browsersearch == 2:
        scene pc5_on_event_day
        window auto
        "Bueno, aquí encontre uno en Wikipedia."
        if not renpy.music.get_playing():
            play music a3 fadein 2.0
        if persistent.blur_on:
            show pc5_on_event_day_blur with Dissolve(.3)
        show TID at is55
        call shownote(info_disociativ, False, "page2") from _call_shownote_8
        if persistent.blur_on:
            scene pc5_on_event_day with Dissolve(.3)
        hide TID at hidetr
        hide TID
        "La verdad no creo que Yumi padezca un trastorno de identidad disociativo."
        "Aquí dice que es causado un 90 por ciento, por un trauma en la infancia."
        "Y la verdad Yumi no se ve que ella haya sufrido uno."
        pause 1.0
        $ persistent.disociativfinishsearch = 1
        $ persistent.first_browser = 1
        $ persistent.investigationcomp += 1
        jump browser_search

label ch13:

    scene pc5_on_event_day
    "Creo que perdí mi tiempo investigando sobre esto."
    "Ya que no soy psicólogo para saber si Yumi tiene o no depresión."
    "Pero es bueno investigar un poco sobre algo que desconocemos."
    "..."
    "Seguiré investigando a ver que otros resultados aparecen."
    window hide(Dissolve(.2))
    stop music fadeout 4.0
    scene black with Dissolve(4.0)
    pause 2.0
    scene pcev_cg_night with Dissolve(1.0)
    window auto
    "...Científicos británicos dicen tener evidencia clara de una relación entre el trastorno bipolar y la inteligencia..."
    "Ya me aburrí."
    pause 1.0
    "Veo mi reloj y noto que estuve investigando como unas 4 horas."
    "Cielos."
    "Dejo salir un gran bostezo..."
    pause 1.5
    "Ya fue suficiente por hoy."
    "Estoy un poco cansado."
    "Cierro mis ojos para descansar un momento."
    scene black with eyeinslow_scene
    "..."
    "..."
    "..."
    window hide(Dissolve(.2))
    pause 3.0
    window auto
    e "Hermanito....."
    pause 1.0
    e "Hermanito....."
    pause 1.0
    scene hiroki_room_night
    show emi nc12 at j11
    e "¡HERMANITO!"
    pr "¡AHHHHHH!"
    pr "¡¿QUE TE PASA?!"
    e n1c16 "Perdón hermanito no quise asustarte."
    e "Es que no te levantabas y me estaba asustando."
    show emi nc21
    play music a1 fadein 2.0
    pr "Casi...{w=1.5}Haces...{w=1.5}Que me dé un infarto."
    e nc16 "Lo siento hermanito la verdad no quería asustarte."
    show emi nc21
    pr "Descuida."
    show emi nc01
    pr "Es que me había quedado dormido."
    pr "¿Y qué haces en mi cuarto?"
    e nc02 "Vine a decirte que la comida esta lista."
    show emi nc01
    pr "..."
    pr "¿Y qué cocinaste?"
    e nc02 "Hice una sopa de ramen de cerdo y soya."
    show emi nc01
    pr "Que bien."
    pr "Vamos a comer entonces."
    show emi nc05 at j11
    e "¡SI!"
    show emi nc04
    stop music fadeout 2.0
    scene black with wipeleft
    pause 3.0
    "Al llegar a la sala..."
    "Nos sentamos en la mesa a comer."
    "A Emi le quedo muy deliciosa la sopa de ramen."
    "Después de comer nos pusimos a ver una película."
    pause 1.0
    play music a7 fadein 2.0
    scene hiroki_livingroom with wipeleft
    show emi nc05 at c11
    e "Estuvo genial, ¿Verdad?"
    show emi nc04
    pr "Si, me encanto."
    pause 1.0
    pr "Bueno..."
    pr "Me iré a acostar."
    pr "Por hoy te dejare dormir tarde."
    pr "Buenas noches Emi."
    show emi at hidetr
    hide emi
    pause 1.0
    show emi nc02 at c11
    e "¿Hermanito?"
    show emi nc01
    pr "¿Qué ocurre Emi?"
    e dc11 "P-Podemos{w}....¿Hablar?"
    show emi dc08
    pr "Eh..."
    pr "Sí."
    pr "¿Qué ocurre?"
    show emi dc11 at tr11
    stop music fadeout 2.0
    e "¿Qué ocurre con Yumi que no me dejaste escuchar?"
    show emi dc08
    pr "Te...{nw}"
    pr "...."
    "Creo que debería decirle que ocurre con Yumi."
    "No quiero que piense que está pasando algo muy malo."
    "O que me metí en un problema con ella."
    "No quiero que me vea como a nuestros padres."
    "Que nos ocultaban todo lo que pasaba."
    pr "Emi."
    show emi dc14 at c11
    e "¿Hmm?"
    pr "Mira..."
    pr "Lo que pasa con Yumi es que..."
    pr "{i}*suspiro*{/i}"
    pr "Mira, Yumi tiene depresión."
    show emi nc23 at tr11
    "Bueno, sigo diciendo que tiene depresión porque no se con exactitud si ella es bipolar."
    pr "Ella se la pasa muy sola y piensa que nadie la quiere."
    pr "Y por eso me comprometí a ayudarla."
    e nc24 "No sabía eso."
    e n1c24 "¿Y cómo pretendes ayudarla?"
    show emi nc23
    pr "Bueno, tengo que seguirle el juego de que soy su novio."
    e nc25 "...."
    e "Yo...."
    pause 1.0
    play music a4 fadein 2.0
    show emi nc12 at j11
    e "¡YO NO ME DEJARE VENCER!"
    e dc04 "Esa Yumi no me vencerá."
    e "Seré tu esposa de una u otra forma."
    e "Ya lo vera."
    show emi dc01
    pr "¡TE...{nw}"
    pr "Sabes que, mejor no te digo nada."
    pr "Voy a parecer disco rayado."
    pr "Siempre diciendo lo mismo."
    pr "Mejor me voy a mi cuarto a dormir."
    pr "Buenas noches."
    e nc05 "Buenas noches hermanito."
    show emi nc04
    pause 1.0
    show emi at lhide
    hide emi
    "Después de esto Emi se va a su cuarto."
    "Esta niña."
    "Siempre con lo mismo."
    "Bueno, eso solo es un capricho infantil."
    "Seguro que cuando crezca ni la palabra me va a querer dirigir."
    "..."
    "Mejor me voy a dormir."
    "Hoy fue un día largo."
    scene hiroki_room_night with wipeleft_scene
    pause 1.0
    "Al llegar a mi cuarto me acuesto en mi cama."
    stop music fadeout 2.0
    scene black with dissolve
    pause 3.0
    "Yumi..."
    "¿Por qué rayos dices que soy tu novio?"
    "Esto es tan extraño."
    "Ella sería mi primera novia."
    "Aunque solo sea de mentira."
    "...."
    "Ojala pueda ayudarla."
    "Ya que no quiero que ella este sola."
    "Nadie merece estar solo."
    "..."
    "{i}*suspiro*{/i}"
    "Mejor me duermo."
    window hide(Dissolve(.2))
    pause 3.0
    scene hiroki_room_night
    play audio stopper
    pause 1.0
    window show(None)
    pr "Un momento..."
    pr "Sí hoy es sábado."
    pr "Y ayer era viernes."
    pr "¡NO HABLE CON HANA!"
    pr "Me distraje al ir a la casa de Yumi."
    e "¡Hermanito! ¡¿Sucede algo?!"
    pr "¡No sucede nada!"
    pr "¡Descuida!"
    e "¡Okey!"
    pause 1.0
    pr "El lunes debería de hablar con Hana."
    pr "{i}*suspiro*{/i}"
    pr "Odio que se me olviden las cosas."
    pr "Mejor me acuesto a dormir."
    pr "Mañana será otro día."
    stop music fadeout 1.0
    window hide(Dissolve(.2))
    scene black with Dissolve(3.0)
    pause 3.0

    return
