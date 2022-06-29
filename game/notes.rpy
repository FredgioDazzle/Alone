
init python:
    class note:
        def __init__(self, date1="", date2="", date3= "", date4="", text=""):
            self.date1 = date1
            self.date2 = date2
            self.date3 = date3
            self.date4 = date4
            self.text = text

    note_yumi = note(
    date1 = "Estudiante: Akemi Yumi",
    date2 = "Edad: 17",
    date3 = "Altura: 1,70m",
    date4 = "Peso: ???",
    text = """\
------------------------
Señorita Akemi Yumi, les escribimos esta carta por el motivo de su constante falta de asistencia, 
le pedimos de favor reingresar a la institución a la brevedad para no tomar la decisión de expulsarla
de la escuela.

ATT: La dirección."""
    )

    note_yumi_en = note(
    date1 = "Student: Akemi Yumi",
    date2 = "Age: 17",
    date3 = "Height: 1.70m",
    date4 = "Weight: ???",
    text = """\
------------------------
Miss Akemi Yumi, we are writing you this letter because of her constant lack of attendance,
We ask you to please re-enter the institution as soon as possible so as not to make the decision to expel her.
from school.

ATT: The address."""
     )

    info_depresion = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}La depresión del latín {i}depressio{/i}, que significa 'opresión', 'encogimiento'
o 'abatimiento' es el diagnóstico psiquiátrico y psicológico que describe un
trastorno del estado de ánimo, transitorio o permanente,
caracterizado por sentimientos de abatimiento,
infelicidad y culpabilidad, además de provocar una
incapacidad total o parcial para disfrutar de las cosas y
de los acontecimientos de la vida cotidiana (la
anhedonia). Los trastornos depresivos pueden estar, en
mayor o menor grado, acompañados de ansiedad.


El término médico hace referencia a un síndrome o
conjunto de síntomas que afectan principalmente a la
esfera afectiva: como es la tristeza constante,
decaimiento, irritabilidad, sensación de malestar,
impotencia, frustración a la vida y puede disminuir el
rendimiento en el trabajo o limitar la actividad vital
habitual, independientemente de que su causa sea
conocida o desconocida. Aunque ese es el núcleo
principal de síntomas, la depresión también puede
expresarse a través de afecciones de tipo cognitivo,
volitivo o incluso somático. En la mayor parte de los
casos, el diagnóstico es clínico, aunque debe
diferenciarse de cuadros de expresión parecida, como
los trastornos de ansiedad. La persona aquejada de
depresión puede no vivenciar tristeza, sino pérdida de
interés e incapacidad para disfrutar las actividades
lúdicas habituales, así como una vivencia poco
motivadora y más lenta del transcurso del tiempo.
El origen de la depresión es multifactorial. En su
aparición influyen factores biológicos, genéticos y
psicosociales. La psico-neuro-inmunología plantea un
puente entre los enfoques estrictamente biológicos y
psicológicos.
    """)

    info_depresion_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}Depression from the Latin {i}depressio{/i}, which means 'oppression', 'shrinkage'
or 'dejection' is the psychiatric and psychological diagnosis that describes a
temporary or permanent mood disorder
characterized by feelings of despondency,
unhappiness and guilt, as well as causing a
total or partial inability to enjoy things and
of the events of everyday life
anhedonia). Depressive disorders may be
greater or lesser degree, accompanied by anxiety.


The medical term refers to a syndrome or
set of symptoms that mainly affect the
affective sphere: as is the constant sadness,
listlessness, irritability, feeling unwell,
impotence, frustration to life and can decrease the
work performance or limit vital activity
usual, regardless of whether its cause is
known or unknown. Although that's the core
main symptom, depression can also
expressed through cognitive disorders,
volitional or even somatic. In most of the
cases, the diagnosis is clinical, although it must
differ from pictures of similar expression, such as
anxiety disorders. The person afflicted with
depression may not experience sadness, but loss of
interest and inability to enjoy activities
habitual playful activities, as well as an experience
motivating and slower over time.
The origin of depression is multifactorial. In its
appearance are influenced by biological, genetic and
psychosocial. Psycho-neuro-immunology poses a
bridge between strictly biological approaches and
psychological.
    """)

    info_depression_2 = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}¿Cómo se desarrolla?{/size}
\n
{size=-6}Diversos factores ambientales aumentan el riesgo de padecer depresión, tales como el fallecimiento de un ser
querido, la mudanza de país, conflictos familiares, post operatorios, factores de estrés psicosocial,
permeabilidad intestinal aumentada, intolerancias alimentarias, inactividad física, obesidad, tabaquismo, atopia,
enfermedades periodontales, sueño y deficiencia de vitamina D.

Entre los factores psicosociales destacan el estrés y ciertos sentimientos negativos (derivados de una decepción
sentimental, la contemplación o vivencia de un accidente, asesinato o tragedia, el trastorno por malas noticias,
tristeza, contexto social, aspectos de la personalidad, el haber atravesado una experiencia cercana a la muerte)
o una elaboración inadecuada del duelo (por la muerte de un ser querido).
    """)

    info_depression_2_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}How is it developed?{/size}
\n
{size=-6}Various environmental factors increase the risk of depression, such as the death of a loved one
dear, moving to another country, family conflicts, post-operative, psychosocial stress factors,
increased intestinal permeability, food intolerances, physical inactivity, obesity, smoking, atopy,
periodontal diseases, sleep and vitamin D deficiency.

Among the psychosocial factors stress and certain negative feelings stand out (derived from a disappointment
sentimental, the contemplation or experience of an accident, murder or tragedy, bad news disorder,
sadness, social context, personality aspects, having had a near-death experience)
or an inadequate elaboration of the mourning (due to the death of a loved one).
     """)

    info_depresion_3 = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}Tratamiento{/size}
\n
{size=-6}En primer lugar, es fundamental identificar y tratar una posible causa orgánica que simule, cause o potencie el
cuadro depresivo, con lo que se consigue, en una buena parte de los casos, la completa recuperación del
paciente o un considerable alivio de sus síntomas.

Independientemente de que se llegue a un diagnóstico fino del tipo de trastorno depresivo, si la situación
anímica supone una limitación en las actividades habituales del paciente, o una disminución de su capacidad
funcional en cualquiera de sus esferas (social, laboral, etc.) se considera adecuada la instauración de un
tratamiento. El fin del tratamiento es el de mejorar la situación anímica, así como restaurar un adecuado
funcionamiento de las capacidades socio-laborales y mejorar, en general, la calidad de vida del paciente,
disminuyendo la morbilidad y mortalidad, y evitando en lo posible las recaídas.

La selección del tratamiento dependerá del resultado de la evaluación. Existe una gran variedad de
medicamentos antidepresivos y psicoterapias que se pueden utilizar para tratar los trastornos depresivos.
    """)

    info_depression_3_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}Treatment{/size}
\n
{size=-6}In the first place, it is essential to identify and treat a possible organic cause that mimics, causes or potentiates the
depressive picture, with which it is achieved, in a good part of the cases, the complete recovery of the
patient or considerable relief of their symptoms.

Regardless of whether a fine diagnosis of the type of depressive disorder is reached, if the situation
Mood involves a limitation in the patient's usual activities, or a decrease in their ability to
functional in any of its spheres (social, labor, etc.), the establishment of a
treatment. The purpose of the treatment is to improve the emotional situation, as well as to restore an adequate
functioning of socio-occupational capacities and improve, in general, the quality of life of the patient,
reducing morbidity and mortality, and avoiding relapses as much as possible.

The selection of treatment will depend on the result of the evaluation. There is a wide variety of
antidepressant medications and psychotherapies that can be used to treat depressive disorders.
    """)

    info_bipolaridad = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}El trastorno bipolar, también conocido como
trastorno afectivo bipolar (TAB) y antiguamente
como psicosis maníaco-depresiva (PMD), es un
conjunto de trastornos del ánimo que se caracteriza por
fluctuaciones notorias en el humor, el pensamiento, el
comportamiento, la energía y la capacidad de realizar
actividades de la vida diaria.

El trastorno bipolar no es un estado de ánimo pasajero o
un estado donde pueda pasarse de una emoción a otra
en un corto lapso de tiempo (Ej. reír mientras se está
llorando). Este trastorno afecta al individuo durante
meses o años por etapas, donde la calma y el
comportamiento normal se intercala entre los episodios
maníacos y la depresión.

La persona afectada por este trastorno alterna su estado
de ánimo entre la manía o hipomanía —fase de alegría,
exaltación, euforia y grandiosidad— y la depresión, con
tristeza, inhibición e ideas de muerte.

Se han definido cuatro tipos de trastorno bipolar de
acuerdo con la severidad y alternancia de estados de
ánimo en el tiempo: trastorno bipolar tipo I, trastorno
bipolar tipo II, ciclotimia y trastorno bipolar
inespecífico.
    """)

    info_bipolarity_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}Bipolar disorder, also known as
bipolar affective disorder (TAB) and formerly
as manic-depressive psychosis (PMD), is a
group of mood disorders characterized by
noticeable fluctuations in mood, thinking,
behavior, energy, and ability to perform
daily life activities.

Bipolar disorder is not a passing mood or
a state where you can switch from one emotion to another
in a short period of time (e.g. laughing while being
crying). This disorder affects the individual during
months or years in stages, where calm and
normal behavior is interspersed between episodes
manics and depression.

The person affected by this disorder alternates his state
of mood between mania or hypomania - phase of happiness,
elation, euphoria, and grandiosity—and depression, with
sadness, inhibition and ideas of death.

Four types of bipolar disorder have been defined
according to the severity and alternation of states of
mood over time: bipolar I disorder
bipolar type II, cyclothymia and bipolar disorder
nonspecific
    """)

    info_bipolaridad_2 = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}Clasificación{/size}
\n
{size=+3}Trastorno bipolar tipo I{/size}
\n
{size=+3}Trastorno bipolar tipo II{/size}
\n
{size=+3}Trastorno bipolar tipo III{/size}
\n
{size=+3}Ciclotimia{/size}
\n
{size=+3}Trastorno bipolar no especificado{/size}
\n
    """)

    info_bipolarity_2_en = note(
         date1 = "{size=+6}Wikipedia{/size}",
         text = """\
{size=+6}Classification{/size}
\n
{size=+3}Bipolar disorder type I{/size}
\n
{size=+3}Bipolar disorder type II{/size}
\n
{size=+3}Bipolar disorder type III{/size}
\n
{size=+3}Cyclothymia{/size}
\n
{size=+3}Bipolar Disorder Not Otherwise Specified{/size}
\n
     """)

    info_bipolaridad_3 = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}Periodo depresivo{/size}
\n
{size=-6}Las señales y los síntomas del período depresivo en el trastorno bipolar
incluyen (pero en ningún sentido se limitan solo a ellos): sentimientos
constantes de tristeza, ansiedad, culpa, ira y soledad y/o desesperanza,
desórdenes de sueño, apetito, fatiga, pérdida de interés por actividades de
las que la persona antes disfrutaba, problemas de concentración, odio
hacia uno mismo, apatía o indiferencia, despersonalización, perdida de
interés en la actividad sexual, timidez o ansiedad social, irritabilidad,
dolor crónico (con o sin causa conocida), falta de motivación, e incluso
ideas suicidas.

{size=+3}Durante la fase depresiva el paciente puede presentar:{/size}
\n
   {b}1.{/b}Pérdida de la autoestima.
   {b}2.{/b}Desánimos continuos.
   {b}3.{/b}Ensimismamiento.
   {b}4.{/b}Sentimientos de desesperanza o minusvalía.
   {b}5.{/b}Sentimientos de culpabilidad excesivos o inapropiados.
   {b}6.{/b}Fatiga (cansancio o aburrimiento) que dura semanas o
    meses.
   {b}7.{/b}Lentitud exagerada (inercia).
   {b}8.{/b}Somnolencia diurna persistente.
   {b}9.{/b}Insomnio.
   {b}10.{/b}Problemas de concentración, fácil distracción por sucesos sin trascendencia.
   {b}11.{/b}Dificultad para tomar decisiones y confusión general enfermiza, ejemplos: deciden un cambio
   repentino de empleo, una mudanza, o abandonar a las personas que más aman como puede
   {size=+6}Cuadro clínico{/size}
   {size=+3}Período depresivo
   {b}1.{/b}Las personas que se encuentran en un episodio maníaco pueden estar eufóricas, irritables y/o
    suspicaces, con un incremento en sus actividades y cualidades tanto físicas como mentales.
   {b}2.{/b}Ser una pareja o un familiar (cuando el paciente es tratado a tiempo deja de lado las situaciones "alocadas" y regresa a la vida real, para recuperar sus afectos y su vida).
   {b}3.{/b}Pérdida del apetito.
   {b}4.{/b}Pérdida involuntaria de peso.
   {b}5.{/b}Pensamientos anormales sobre la muerte.
   {b}6.{/b}Pensamientos sobre el suicidio, planificación de suicidio o intentos de suicidio.
   {b}7.{/b}Ver los logros personales como parte del azar y con una prognosis negativa del futuro (logré eso por suerte, pero si sigo seguro fallaré).

    """)

    info_bipolarity_3_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=+6}Depressive period{/size}
\n
{size=-6}Signs and symptoms of the depressive period in bipolar disorder
include (but are by no means limited to): feelings
constants of sadness, anxiety, guilt, anger and loneliness and/or hopelessness,
sleep disorders, appetite, fatigue, loss of interest in activities of
that the person previously enjoyed, problems concentrating, hate
towards oneself, apathy or indifference, depersonalization, loss of
interest in sexual activity, shyness or social anxiety, irritability,
chronic pain (with or without a known cause), lack of motivation, and even
suicidal thoughts.

{size=+3}During the depressive phase the patient may present:{/size}
\n
   {b}1.{/b}Loss of self-esteem.
   {b}2.{/b}Continuous discouragement.
   {b}3.{/b}Absorption.
   {b}4.{/b}Feelings of hopelessness or worthlessness.
   {b}5.{/b}Excessive or inappropriate feelings of guilt.
   {b}6.{/b}Fatigue (tiredness or boredom) that lasts for weeks or
    months.
   {b}7.{/b}Exaggerated slowness (inertia).
   {b}8.{/b}Persistent daytime sleepiness.
   {b}9.{/b}Insomnia.
   {b}10.{/b}Concentration problems, easily distracted by inconsequential events.
   {b}11.{/b}Difficulty making decisions and general unhealthy confusion, examples: they decide to change
   sudden loss of employment, a move, or leaving the people you love most as you can
   {size=+6}Clinical chart{/size}
   {size=+3}Depressive period
   {b}1.{/b}People in a manic episode may be elated, irritable, and/or
    suspicious, with an increase in their activities and both physical and mental qualities.
   {b} 2. {/ b} Being a partner or family member (when the patient is treated in time, he puts aside the "crazy" situations and returns to real life, to recover his affections and her life).
   {b}3.{/b}Loss of appetite.
   {b}4.{/b}Involuntary weight loss.
   {b}5.{/b}Abnormal thoughts about death.
   {b}6.{/b}Thoughts about suicide, suicide planning, or suicide attempts.
   {b}7.{/b}See personal achievements as part of chance and with a negative prognosis of the future (luckily I managed that, but if I continue to be sure I will fail).

    """)

    info_bipolarity_4_en = note(
        date1 = "{size=+6}Wikipedia{/size}" ,
        text = """\
{size=+6}Treatment{/size}
\n
{size=-6}Currently there are different treatments for bipolar disorder and in many cases it produces
recovery.68 The goal of treatment is effective control of the long-term course of the disease.
term, which may involve treating emerging symptoms. To achieve this, techniques
pharmacological and psychological. Pharmacological treatment is based on the use of stabilizers of the state of
encouragement and various psychological techniques, among which psychoeducation or interpersonal therapy and
of the social rhythm.

{size=+3}Mood Stabilizers{/size}
\n
{size=+3}Anticonvulsants{/size}
\n
{size=+3}Antipsychotics{/size}
\n
{size=+3}Antidepressants{/size}
\n
{size=+3}Tricyclic antidepressants{/size}
\n
{size=+3}Benzodiazepines{/size}
\n
{size=+3}Lithium salts{/size}
\n
{size=+3}Atypical antipsychotics{/size}
\n
{size=+3}Atypical antipsychotics{/size}
\n
    """)
    info_disociativ = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}El trastorno de identidad disociativo (TID) , antes
conocido como desorden de personalidad múltiple
(DPM), es un trastorno disociativo que se caracteriza
por la existencia de dos o más identidades en una
persona, cada una con su propio patrón de percibir y
actuar con el ambiente. Estadísticamente, la mayoría de
las personas afectadas son mujeres, aunque
lamentablemente no existen muchos estudios al respecto
(más que las estadísticas arrojadas en algunos países,
como Turquía). Al menos dos de estas personalidades
toman el control del comportamiento del individuo de
forma rutinaria, y están asociadas también con un grado
de pérdida de memoria más allá de la falta de memoria
normal. A esta pérdida de memoria se le conoce con
frecuencia como «tiempo perdido» o «tiempo
amnésico». Se le asocia con el trastorno límite de la
personalidad, el trastorno por estrés postraumático, la
depresión, el trastorno por abuso de sustancias,
autolesiones o ansiedad.

La causa se debe a un trauma infantil. En aproximadamente el '90%' de los casos hay un historial de abuso en
la infancia, mientras que otros casos están relacionados con experiencias de guerra o problemas de salud
durante la infancia. Los factores genéticos también se cree que juegan un papel. Estudios entre profesionales
de la salud demuestran un amplio escepticismo contra la idea de que este diagnóstico representa en sí un
desorden mental en vez de un delirio con base cultural o iatrogénica.
    """)
    
    info_dissociativ_en = note(
        date1 = "{size=+6}Wikipedia{/size}",
        text = """\
{size=-6}Dissociative identity disorder (DID), formerly
known as multiple personality disorder
(PMD) is a dissociative disorder characterized
by the existence of two or more identities in one
person, each with their own pattern of perceiving and
act with the environment. Statistically, most of
affected people are women, although
Unfortunately, there are not many studies on this.
(more than the statistics released in some countries,
like Turkey). At least two of these personalities
take control of an individual's behavior
routinely, and are also associated with a degree
of memory loss beyond forgetfulness
normal. This memory loss is known as
frequently as "lost time" or "time
amnesic". It is associated with borderline personality disorder.
personality, post-traumatic stress disorder,
depression, substance use disorder,
self-harm or anxiety.

The cause is due to childhood trauma. In approximately '90%' of cases there is a history of abuse in
childhood, while other cases are related to war experiences or health problems
during childhood. Genetic factors are also believed to play a role. Studies between professionals
health professionals show widespread skepticism against the idea that this diagnosis in itself represents a
mental disorder rather than a culturally based or iatrogenic delusion.
    """)
image page1 = "gui/page1.png"
image page2 = "gui/page2.png"

init -501 screen note(currentnote, page="page1"):

    style_prefix "note"
    vbox:
        add page
    viewport:
        xalign 0.5 xysize (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentnote.date1 == "{size=+6}Wikipedia{/size}":
                text "[currentnote.date1]\n\n[currentnote.text]" style "wikipedia_text"
        else:
            text "[currentnote.date1]\n\n[currentnote.date2]\n\n[currentnote.date3]\n\n[currentnote.date4]\n\n[currentnote.text]" style "note_text"
        null height 100


style note_vbox:
    xalign 0.5

style wikipedia_text:
    font "gui/font/CENSCBK.TTF"
    size 26
    color "#000"
    outlines []

style note_text:
    size 26
    color "#000"
    font "gui/font/CENTURY.TTF"
    outlines []

init -501 style note_viewport:
    xalign 0.5
    ysize 710

style note_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    ysize 700

label shownote(note=None, play_pageflip=True, set_page="page1"):

    if note == None:
        return
    if play_pageflip:
        play audio pageflip
    window hide
    show screen note(note, set_page)
    if not persistent.firstnote:
        $ persistent.firstnote = True
        show expression "gui/note_dismiss.png" as note_dismiss:
            xpos 1060 ypos 590
    with Dissolve(1)
    $ pause()
    hide screen note
    hide note_dismiss
    with Dissolve(1)
    window auto

    return