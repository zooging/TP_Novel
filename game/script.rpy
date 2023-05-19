init python:
    # создаем переменные для ответов
    q1_answer = 0
    q2_answer = 0
    q3_answer = 0
    q4_answer = 0
    myname = ""
    onn = ImageDissolve("gui/eyes.png", 2.0, 20, reverse=False)
    off = ImageDissolve("gui/eyes.png", 2.0, 20, reverse=True)




#Персонажи
image younger = "gui/pchel.png"
image actor = "gui/pchel2.png"
image singer = "gui/pchel3.png"
image whoho = "gui/pchel4.png"


define actorc = Character("Якоб Хенц",color ="#4ca6ff")
define young = Character ("Ян",color ="#aaaa")
define sing = Character ("Андреа Каррерас", color = "#4ca6ff")
define my = Character("[myname]")
define someone = Character ("Кто-то",color = "#aaaa")
define who = Character ("Незнакомец", color= "#aaaa")





#Фоны
image test_background = "gui/test_background.png"
image background_first_scene = "gui/background_first_scene.png"
image background_ship = "gui/background_ship.jpg"
image background_kauta = "gui/background_kauta.jpg"
image bg_black = "gui/bg_black.jpg"
image bg_kafe = "gui/bg_kafe.jpg"
image art = "gui/art.jpg"
image embankment = "gui/embankment.jpg"
image grand_house = "gui/grand_house.jpg"

label start:
    $ myname = renpy.input("Как зовут вашего героя?", allow="ячсмитьбюфывапролджэйцукенгшщзхъ-ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЪ").strip()
    scene test_background
    with fade
    # выводим первый вопрос
    menu:
        "Вам часто приходят в голову негативные мысли о будущем или о неизвестности?"
        "Часто":
            $ q1_answer = 4
        "Периодически":
            $ q1_answer = 3
        "Редко":
            $ q1_answer = 2
        "Очень редко":
            $ q1_answer = 1

    # выводим второй вопрос
    menu:
        "Вы легко волнуетесь или беспокоитесь о различных аспектах своей жизни, таких как работа, здоровье, отношения или финансы?"
        "Да, почти каждый день":
            $ q2_answer = 4
        "Да, переодически":
            $ q2_answer = 3
        "Редко задумываюсь, когда все хорошо":
            $ q2_answer = 2
        "Только когда есть проблемы":
            $ q2_answer = 1

    # выводим третий вопрос
    menu:
        "Вам сложно контролировать свои беспокойные мысли, и они мешают вам сосредоточиться на текущих делах?"
        "Да":
            $ q3_answer = 4
        "Скорее да":
            $ q3_answer = 3
        "Скорее нет":
            $ q3_answer = 2
        "Нет":
            $ q3_answer = 1

    # выводим четвертый вопрос
    menu:
        "Вам трудно расслабиться или успокоиться, даже когда нет явных причин для беспокойства?"
        "Да":
            $ q4_answer = 4
        "Скорее да":
            $ q4_answer = 3
        "Скорее нет":
            $ q4_answer = 2
        "Нет":
            $ q4_answer = 1

    # выводим результаты теста
    label show_results:
        # суммируем ответы
        $ total_score = q1_answer + q2_answer + q3_answer + q4_answer
        scene background_first_scene
        with fade

        my "Вот и начинается мое маленькое путешествие. Давно я не видел свою бабулю. До сих пор не понимаю, как она решилась на старости лет переехать на отдельный остров, да еще и через залив."
        my "Вот у кого энергии не занимать. Мы обменивались письмами долгое время, но я всегда хотел ее навестить. Надеюсь, она приготовит свои фирменные пирожки. Сегодня такой солнечный день, посадка на корабль уже началась…. Надеюсь, меня не укачает”"

        show younger
        young "Позвольте вам помочь с багажом, мистер"

        my"Спасибо"

        scene background_ship
        with fade

        my "Еще раз спасибо, вы работник корабля?"

        show younger
        young "Да, знаю, что выгляжу юно, меня зовут Ян, о,нет,сэр, мне не нужны ваши деньги, я просто делаю свою работу, можете показать ваш билет мне?"

        my "Да конечно, вот, держите."

        show younger
        young "Спасибо, ваша каюта будет слева, вон желтый указатель, следуйте ему и придете в свою комнату, я пока помогу еще кому-то, увидимся во время плавания, можете обращаться ко мне по любому вопросу"

        my "Спасибо вам,Ян, до встречи"

        "Ян убегает..."

        my "Весьма приятный юноша, на вид лет 15, но он ведет себя так взросло.. Чтож, пойду в свою каюту."

        scene background_kauta
        with fade


        my "Ох, плыть всего неделю, но я уже устал… Неужели вся энергия в нашей семье передается только женщинам? Что мама, что бабушка,авантюристки. До отплытия еще пол часа, посплю пока"

        scene black with off
        pause 1.0
        scene background_kauta with onn

        my "Мы что? Уже плывем? Cколько же я спал..? Ну что ж…пойду на палубу, полюбуюсь видом"

        scene background_ship
        with fade
        my "*Красиво конечно, море,закат, легкий бриз, такие моменты хочется запечатлеть в памяти..*"

        someone "Да что это такое? Ненавижу все это. Этот корабль, это море, мой голос. Как вы можете так спокойно смотреть на это солнце? Глаза ж болят, а впрочем вы все равно ничего не понимаете, что с вами разговаривать, пойду лучше к себе"

        show actor
        actorc "Крикливый, да?"

        my "Да, есть немного, а кто это был?"

        show actor
        actorc "Андреа Каррерас, он довольно популярный оперный певец, на суши много листовок с ним"

        my "А, его называют восходящей звездой, но последний концерт отменили"

        show actor
        actorc "Ага, были слухи, что он на нервной почве потерял на время голос. Якоб Хенц кстати"

        my "Gриятно познакомиться, меня зовут [myname]. А вы видимо художник?"

        show actor
        actorc "Dы весьма наблюдательны, но нет, я писатель, а бумагу ношу с собой для удачного случая, вдруг надо будет что-то записать"

        my "О чем пишите?"

        show actor
        actorc "Как не странно о себе, не подумайте, я не нарцисс, просто хочу оставить что-то после себя, поэтому поехал в путешествие"

        my "О, это интересно, не расскажете подробнее?"

        show actor
        actorc "Вечером в кафе будет какое-то представление, могу рассказать там поподробнее"

        my "Хорошо, до встречи"

        "Несколько часов спустя..."

        scene bg_kafe
        with fade

        my "Якоба еще нет, займу пока столик. Приятное местечко, как и все на этом корабле сделано со вкусом"

        "Неожиданно, какой-то мимо проходящий мужчина роняет свои таблетки, вы решаете ему помочь"

        show singer
        sing "*хриплым голосом*:”Спасибо.."

        my "На здоровье, от кашля?"

        show singer
        sing "Нет, снотворное, от кашля сироп"

        my "Вот как..."

        show singer
        sing "Ага, снотворное одно время помогало от навязчивых мыслей. Даже был от них зависим. Но оказалось, что проблема не в малой дозе снотворного, а в большом комке мыслей в голове, так что сейчас разбираюсь в себе."

        my "..."

        show singer
        sing "Вы молчаливы, с вами легко болтать. Я могу одолжить ваши уши в полдень 4-того дня, до моей консультации с врачом?"

        my "Да, конечно"

        show singer
        sing "Спасибо еще раз, а то на этом корабле даже не с кем поговорить. До свидания"

        my "Не за что, мне тоже с вами будет интересно провести с вами беседу, увидимся позже"

        "Как только Андреа ушёл, вы зачаете, что к вам подходит Якоб.."

        hide singer

        show actor
        actorc "Болтали с певцом?"

        my "Перекинулись парой слов. Так вы отправились в путешествии для написания книги? Куда направляетесь?"

        show actor
        actorc "На остров сенджу, говорят, там прекрасные цветы, хочу их описать в своей автобиографии"

        my "Ого, до него далеко, придется добираться с пересадками. Как вы начали писать?"

        show actor
        actorc "Это долгая и грустная история, но жалости я не ищу. Дело в том, что 24 года назад я потерял свое сердце. Я познакомился с ней, когда мне было 23, как бы банально это не звучало, но да,любовь с первого взгляда, увидел ее на городском празднике и не смог оторвать взгляд."

        actorc "Переборол себя, познакомился, она была не против, все произошло быстро. Через четыре месяца я сделал предложение, но она отказалась. Сказала, что сначала надо создать свое уютное место. Купить жилплощадь, наполнить ее мебелью и совместными воспоминанием, а потом уже под венец"

        actorc "Очаровательно, правда?Я согласился, мы приступили к задуманному. Было много, не хочу рассказывать, а то вам будет неинтересно читать книгу. Но через полтора года все оборвалось. Она заболела, я поддерживал, и она победила, но болезнь оставила свой след на ее здоровье."

        actorc "Я предлагал сходить в дом малютки, но она не хотела. Ей нужно было время. Время побыть одной. Принять обстоятельства, изменения в своем организме, обдумать все. Я отпустил. А напоследок она попросила написать меня автобиографию, представляетe?"

        actorc "Если ее выпустят, то это будет сигналом для нее, она отправит письмо в редакцию. Писать книгу долго и этого времени хватит. И вот я пишу книгу иже 5тый год. На моем пути было много неудач. Сначала я не мог начать, просто не верилось, что она ушла. Потом мое творение то сжигала обозленная служанка, то на него проливали воду, то рвали на части. "

        actorc "Я методично переписывал текст из раза в раз, а стоит помнить, что редакция не будет печать абы что. Книга должна получиться хорошая. Так до сих пор ее и не закончил, но я уже близко. Наконец придумал конец, осталось связать его с основной историей, возможно, вы ее скоро увидите на прилавках”"

        my "Ого, и вы верите, что она ждет?"

        show actor
        actorc "Я просто хочу с ней пообщаться,даже если она уже замужем"

        my "Как вам удается быть таким оптимистичным?"

        show actor
        actorc "Я уже не молод, нет смысла тратить силы на негатив. Да, сначала я злился и нервничал, да и до сих пор испытываю мышечное напряжение и невроз при стрессовых ситуациях, но  в этой жизни все контролировать не получится. Вообще приучил себя пользоваться одной методике."

        actorc "Если чувствуешь, что тревожность накрывает, возьми карандаш и листочек,нарисуй человечка и где скапливается его стресс, какую форму он принимает, рисуй стресс, как хочешь, а потом очерти человечка от стресса, оторви, скомкай листочек с стрессом и выкини его"

        actorc "Можно в принципе человечка не рисовать, но стресс обязательно. Неплохо помогает."

        my "Спасибо за совет, никогда раньше не слышал про такую технику"

        show actor
        actorc "да, сам сначала не верил, а теперь карандаш с бумагой всегда под рукой, я даже рисовать немного начал"

        menu:
            "Якоб протягивает вам листок бумаги с каким-то рисунком"
            "Посмотреть, что за рисунок":
                jump look

            "Вежливо отказаться и не смотреть, что нарисовано на бумаге":
                jump dont_look

label look:
    my "Ого, покажете?"
    show actor
    actorc "А то!"
    show art
    my "выглядит просто потрясающе! У вас хорошие навыки"
    show actor
    actorc "Хах, спасибо, что ж мы с вами заболтались, представление подошло к концу, если захотите автопортрет, заходите ко мне, нарисую вас на фоне моря, будет на  память"
    my "Обязательно!"
    jump continue_story

label dont_look:
    show actor
    actorc "Чтож, если захотите автопортрет, заходите ко мне, нарисую вас на фоне моря, будет на память"
    my "Спасибо вам большое, зайду как-нибудь, до свидания"
    jump continue_story

label continue_story:
            "Вы возвращаетесь к себе в каюту..."
            scene background_kauta
            with fade

            my "Не спиться, все не могу забыть историю якоба. На корабле много интересных людей, хорошо, что бабушка позвала меня в гости. Так поздно, за окном шумит море. Все, пора спать.."
            scene black with off
            pause 1.0
            scene background_kauta with onn
            scene background_kauta
            with fade

            my "И снова прекрасное морское утро, да уж, если б не Якоб и Ян, я б уже наверное всю “войну и мир” прочел бы. Пора на завтрак, возьму еду и пойду на нос корабля, поем, любуясь утренним морем"

            scene background_ship
            with fade

            show younger

            my "О, привет, ян, снова тут"

            young "Здравствуйте, мистер, конечно, это ж моя любимая часть дня"

            "Вы вместе смотрите на море"

            my "Даа, понимаю"

            my "Слушай, а почему ты сидишь поодаль? Около перил видно лучше, а еще можно рассмотреть плескающуюся рыбу"

            young "Если честно, я боюсь высоты….и громких звуков…Странно, знаю, я ведь юнга, но это не то, с чем можно справиться быстро"

            my "Это личный вопрос, не отвечай, если не хочешь, но как ты оказался на корабле?"

            young "Сам пришел, меня и приняли. До этого в приюте жил, о нас особо не заботились."
            young "Я и сбежал, думал смогу притвориться кем-то другим, над кем не издевались старшие мальчишки, на кого не кричали воспитательницы, кого не лишали еды за малейшие провинности и кто не стоял с табуреткой на вытянутых руках. Вы пробовали?"

            my "Что?"

            young "Стоять с табуреткой на вытянутых руках?"

            menu:
                "Пробовали ли вы стоять с табуреткой на вытянутых руках?"
                "Да":
                    young "Тогда вы понимаете, как руки ноют спустя минут 5"
                "Нет":
                    young "Нет? Тогда попробуйте. Сначала с подушкой, руки через минут 5 просто ноют"

            show younger
            young "Хах. Не вышло у меня притворяться таким. Хорошо, рядом моряки были. Все по-разному ко мне относились, но злости от них я ни разу не видел. Сначала просто общался, потом начал потихоньку открываться"
            young "Тяжело было начать снова кому-то доверять, с кем-то смеяться. Но у меня получилось"
            young "Я как-то общался с одним старым морским волком, он дал мне совет, который стал моим девизом:”Надейся на все, не ожидай ничего”. Верь в лучшее если перевести, я и стараюсь верить, в чем смысл фокусироваться на плохом?"
            young "Ты так только тратишь себя и свою энергию. А так… Начинаешь что-то делать. Я готовить например начал. Сначала кирпичи горелые были, теперь хлеб в яйцах получается. Хах. Мое любимое блюдо"

            "Ян подходит к перилам"

            my "Тебе же страшно смотреть вниз, зачем подошел?"

            young "Подождите немного, мне нужно время. Вдоооооох, выыыыыдох, вдоооооох,выыыыыдох. Фух. Потому что я научился жить с своими страхами. И теперь хочу их преодолеть"

            my "Что ты делал? С дыханием?"

            young "А, это была дыхательная техника. Я ей пользуюсь уже не первый год, помогает успокоиться и привести мысли в порядок"

            "Вы слышите звук звонка: <Дзынь,Дзынь>"

            young "О, завтрак окончен, я нужен на кухне, все, побежал, до свидания,мистер"

            my "Пока, ян, увидимся"

            hide younger

            "Вы слышите звуки страшного грохота"

            someone "Да чтоб вас всех! О, это ж вы"

            "Вы оборачиваетесь на голос"

            my "Здравствуйте, Андреа, как ваши дела"

            show singer
            sing "Лучше,чем в первый день. Консультации помогают. Отказался от снотворного. Удивительно, стоило обменяться письмами с директором театра, и оказалось, что они не ищут мне замену."
            sing "Я то думал, меня на преждевременную пенсию отправили. А нет, ждут"

            menu:
                "Что бы вы спросили у Андреа?"
                "Спросить про голос":
                    my "И голос улучшился"
                    sing "Да, выступать пока не стоит, но может под конец путешествия я вам спою… Как думаете, я бы смог стать кем-то кроме певца?"
                    sing "Учился с 5 лет музыке, она моя страсть, разве может быть что-то еще? Мне посоветовали найти хобби. Ума не приложу, чем вообще я еще могу заняться"

                "Cпросить почему ему должны были найти замену":
                    my "Отчего ж вам замену искать?"
                    sing "Это слишком личный вопрос, я пока не готов на него ответить"

            menu:
                "О чем спросите дальше?"
                "Как насчет рисования?":
                    sing "Не знаю, никогда этим не занимался, буду рисовать цветных змей. Хах изогнутые линии. Ярко. Повешу в комнате"
                    my "Это будут прекрасные змеи"

                "Как на счет завести домашнее животное?":
                    sing "Я часто в разъездах, не хочу, чтобы домашний питомец тосковал, может позже. Знаете, я осознал, что когда-нибудь выйду на настоящую пенсию…"
                    sing "Наверное, стану учить детей, если смогу усмирить свою раздражительность."

            sing "АРГХ, эта палуба! я споткнулся! кто вообще поставил здесь эту коробку, *пинает* ее надо ставить в угол!"

            "В коробке что-то трещит"

            sing "Вот блин, да что ж это такое!"

            hide singer

            "К вам подбегает незнакомец, и срываясь на крик, спрашивает:"

            show whoho
            who "”Что вы сделали с моей коробкой???!”"
            hide whoho

            show singer
            sing "Это моя вина,  не надо было ее трогать.."
            hide singer

            show whoho
            who "”Вот именно!!!! Ах, я вас узнал, вы же тот оперный певец, помните хотя бы как извиняться надо в отличие от оперы?”"
            hide whoho


            show singer
            sing "Вы были на том выступлении?"

            hide singer

            show whoho
            who "ДА! И лучше б не ходил, вы просто портите мне настроение. сколько заплатил за билет. И за что? Посмотреть на твое смазливое личико? Ни голоса, не памяти, еще и коробка!"
            hide whoho

            show singer
            sing "Извините за коробку, но то выступление… Мы вернули деньги и добавили бесплатный ужин"
            hide singer

            show whoho
            who "Да и что? сдался мне ваш ужин. Зачем ты вообще вышел на сцену? Пел б в хоре,не позорился"
            hide whoho

            "Андреа злится и хрипит"

            show singer
            sing "Слушай, ты, поставил свое барахло на центр, не удивительно, что его пнули, сам иди в хор пой, я прослежу, чтобы ты больше не на одно мое выступление не попал”"
            hide singer

            show whoho
            who "Ой, да я больше и не хочу, звездная болезнь тебя все таки настигла, думаешь, тебе все можно, раз пару раз постоял перед камерами?"

            my "затевается драка, что же делать?"

            menu:
                "Увести Андреа":
                    "Вы решаете открыть коробку и посмотреть, что же там было"

                    my "ого, красивые бокалы"

                    who "Неужели целы? В любом случае, не трогайте мои вещи"

                    my "Целы, берите, мы пойдем"

                    "Вы и Андреа уходите"

                "Поговорить с незнакомцем":
                    my "Подождите, а что было в коробке?"

                    who "Редкие бокалы"

                    my "Упакованные?"

                    who "Конечно! Кто я по-вашему такой?!"

                    my "Давайте откроем коробку"

                    "Вы открываете коробку"

                    my "Все бокалы целы, мистер, уберите их в каюту лучше,а мы пойдем, раз все в порядке"

                    who "Хмф, и вправду целы, ну идите, идите, аккуратнее только, ничего не пинайте"

            hide whoho

            show singer

            sing "Вот злодей! Мое горло, не надо было кричать, теперь горло болит.. и коробку пинать не надо было, все злюсь по пустякам” *тяжелая одышка*"

            my "Андреа, давайте подышим морским воздухом. Вдооооох,выыыыдох, вдооооох, выыыыдох"

            "Андреа проводит серию дыхательный упражнений"

            sing "Мне стало лучше"

            my "Меня этому научил ян, он юнга тут, хороший паренек"

            sing "да, и вправду, узнаю его, поблагодарю, буду теперь тоже так дышать. Я так устал от этих нервов, мне очень хочется спать."
            sing "Я с вами попрощаюсь на этом, спасибо вам, а то я б еще и в драку ввязался, так и вижу заголовки"

            my "Рад был помочь, спокойного вам сна, я еще посижу"

            "Вечер, море, палуба..."

            my "Насыщенный день получился. Чем дольше плыву, тем больше нового узнаю...."
            my "Приятный ветерок…И море….Что же будет дальше…. Вдоооох, выыыыдох, вдооооох, выыыдох…. Пора и мне спать, пойду я.."

            "Вы возвращаетесь к себе в каюту..."
            scene background_kauta
            with fade

            my "Чтож, надеюсь я хорошо высплюсь.."
            scene black with off
            pause 1.0
            scene background_kauta with onn
            scene background_kauta
            with fade

            my "Последний день путешествия. Пора собирать вещи."

            scene background_ship
            with fade

            show younger
            young "Позвольте ваш багаж,сэр"

            my "Конечно, Ян, спасибо тебе за все"

            young "Да не за что, хорошего вам путешествия на суше"

            my "И тебе, но только в море"

            scene embankment
            with fade

            show actor
            actorc "Здравствуйте. Кажется, здесь наши пути расходятся, через 30 минут у меня следующий корабль"

            my "Да, последний раз. Здравствуйте, приятного вам продолжения пути."
            my "С удовольствием прочту вашу книгу"

            actorc "Не последний, а крайний.Земля круглая, еще увидимся."
            actorc "Хахаха.До свидания."

            my "До встречи"
            hide actor

            show singer
            sing "О, а вот и вы. Пора прощаться. Дайте ж вам обнять"

            my "Здравствуйте, как ваш сон?"

            sing "Лучше с каждым днем."
            sing "Скажу честно, тревоги не отпускают меня. Все так же волнуюсь, что потеряю голос, или что не смогу запомнить текст, или что меня уволят из театра."
            sing "Но благодаря дыхательной технике и консультациям сейчас легче. Я осознал причины стресса, теперь мне предстоит долгий путь, но я верю, что однажды смогу жить счастливо."
            sing "Мир не сошелся на пении..."
            sing "Все думал про ваш совет на счет хобби. Я попробую. Спасибо вам за все"

            my "На здоровье, Андреа. Я искренне рад за вас"

            sing "Дайте мне ваш адрес, я отправлю вам приглашение на мое выступление. Это будет триумфальное возвращение"

            menu:
                "Дать адрес":
                    "Вы решаете написать свой адрес на бумаге для Андреа"

                    my "С удовольствием"

                "Не давать адрес":
                    "Вы решаете не давать Андреа свой адрес"

                    my "Андреа, вы так известны, я хочу сам купить билет и поспособствовать вашей популярности"

                    sing "Хах, спасибо, я потрачу эти деньги на хобби"

            sing "Ну вот и все. До свидания, мне пора на поезд."
            my "До свидания"
            hide singer

            my "Ну вот и все, мне тоже пора, как там моя бабуля, соскучилась наверное"

            scene grand_house
            with fade

            my "А вот и ее дом"
