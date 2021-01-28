from time import sleep
import random

# menu_comands, menu и еще одна херня, убрать в одно
# убрать проверку на команду в фильтр
# Закинуть проверку на вводимую команду в функцию
# Проверка на введенное кол-во повторений
# Выход в меню во время занятия



def do_exercise(quantity=15, repeats=3, **kwargs):
    quantity = int(quantity)
    repeats = int(repeats)
    energy_coast = quantity * repeats * kwargs['Энергия']
    if you['Энергия'] < energy_coast:
        print('Чувак, ты спекся... Силёнок не хватает.')
        return None
    for element, coefficient in kwargs.items():
        if element == 'Энергия':
            you[element] -= int(quantity * repeats * coefficient)
        else:
            you[element] += int(quantity * repeats * coefficient)
    getting_stronger()
    return show_stats()


def getting_stronger():
    print('\n*пыхтишь потеешь*')
    print('Оуу маай')
    sleep(2)
    print('Май мусклес ар геттинг стронгер')
    sleep(2)
    print('Вот так вот...')
    sleep(2)
    print('Вот так вот...')
    sleep(2)
    print('Yeah стал сильнее! \n')
    sleep(2)


def show_stats():
    print('_' * 22)
    for x, y in you.items():
        print('|{: <12}|{: >7}|'.format(x, y) + '\n|' + '_' * 12 + '|' + '_' * 7 + '|')
    print('\n#шлеп на enter#')
    input()


def show_menu():
    print('\n--Статистика\n--Продолжить качаца\n--Сохраниться\n--Сбросить результат\n--Помощь\n')


def filter_ex(input_word, dict_part):
    """Возвращает точное значение команды в словаре dict_part в соотсветсвтии с введенной пользователем частью команды input_word.
    В случе нескольких соответствий выводит все варианты соответсвующие запросу и повторяет вызов функции."""
    if not input_word:
        return None
    result = list(filter(lambda x: input_word.lower() in x.lower(), list(dict_part.keys())))
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print('Уточни, что из этого: {},'.format(' или '.join(result)))
        input_word = input()
        return filter_ex(input_word, dict_part)
    else:
        return None


def choose_exercise():
    # Выбор группы мышц
    print('\nЧё качнем?')
    print(' или '.join(list(exercises.keys())) + '\n')
    body_part = input()
    body_part = filter_ex(body_part, exercises)
    while not exercises.get(body_part, None):
        print(abuse[random.randint(0, len(abuse) - 1)] + ' или '.join(list(exercises.keys())))
        body_part = input()
        body_part = filter_ex(body_part, exercises)

    # Выбор упражнения
    print('Тренер: Окей, тут можно: {}\n'.format(', или '.join(list(exercises[body_part].keys()))))
    exercise_word = input()
    exercise_word = filter_ex(exercise_word, exercises[body_part])
    while not exercises[body_part].get(exercise_word, None):
        print('Тренер: {} Еще раз повторяю: {}\n'.format(abuse[random.randint(0, len(abuse) - 1)],
              ', или '.join(list(exercises[body_part].keys()))))
        exercise_word = input()
        exercise_word = filter_ex(exercise_word, exercises[body_part])
    print('Тренер: Сколько повторений и сколько подходов?\n')
    quantity = input()
    repeats = input()
    do_exercise(quantity, repeats, **exercises[body_part][exercise_word])


def scene1():
    print('Тренер: Как тебя зовут сопляк?')
    you['Имя'] = input()
    sleep(1)
    print('Тренер: {} респект, что залетел к нам в зал!'.format(you['Имя']))
    sleep(1)
    print('Тренер: Но дрищ ты конечно сказочный, давай зафиксируем твои начальные показатели')
    sleep(1)
    show_stats()
    print('\n#шлеп на enter#')
    input()
    print('Тренер: Пиздец...')
    sleep(1)
    print('Тренер: Ладно, и не таких натягивали. Проведу тебе маленьки ликбез.')
    sleep(1)
    print('Тренер: Если тебе нужно что то сделать, то только через меня, усек? Чтобы я подошел, \
    ты просто, как ебалан посреди зала должен сказать "Меню". Или "Menu". Или "Я еблан, помогите мне.".')
    print('Тренер: Попробуй. \n')
    command = input('{} :'.format(you['Имя'])) 
    command = filter_ex(command, commands)
    while not command:
        print('Тренер: {} Ты должен сказать "Меню". Или "Menu". Или "Я еблан, помогите мне.".\n'
              .format(abuse[random.randint(0, len(abuse) - 1)]))
        command = input('{} :'.format(you['Имя']))
        command = filter_ex(command, commands)
    #current_path = commands[command]  # нужна чтобы отслеживать текущее расположение пользотваеля в структуре меню
    commands[command]()
    print('Тренер: Здесь ты указываешь че те надо. Пока могу тебе только предложить посмотреть статистику или уже начать качаться.')
    command = input('{} :'.format(you['Имя']))  # Выбрать пункт меню
    command = filter_ex(command, menu)
    while not command or command not in 'Статистика Продолжить качаца':
        print('Тренер: {} Либо статистика, либо качаться.".\n'
              .format(abuse[random.randint(0, len(abuse) - 1)]))
        command = input()
        command = filter_ex(command, menu)
    #latest_path, current_path = current_path, menu[command]
    menu[command]()
    #print('\nЧтобы вернуться назад, так и скажи "Назад", ну или "Back", если ты такой уж ахуенный билингв. ')
    #command = input()
    #command = filter_ex(command, commands)
    #while not command:
    #    print('{} Просто скажи: "Назад" или "Back".\n'
    #          .format(abuse[random.randint(0, len(abuse) - 1)]))
    #    command = input()
    #    command = filter_ex(command, menu)
    #commands[command](latest_path)
    #print('Ну вот и вернулись в зад.')
    print('\nЕсли нужна будет помощь кричи как маленькая девочка "Памагите!",\
    а там посмотрим чем я смогу тебе помочь. Дальше сам решай хули тебе тут делать. \n')
    sleep(1)

def scene2():
    print('Ну хеллоу, май диар {}'.format(you['Имя']))
    while you['Энергия'] > 85:
        
        choose_exercise()

def end_of_the_day():
    print('Тренер: Братан, ты спекся...')
    print('Тренер: Капельку в трусы то пустил?')
    print('Тренер: Кайф словил?')
    answer = input()
    if answer == 'Да':
        print('Тренер: Ну красавчик, так и должно быть!')
    elif answer == 'Нет':
        print('Тренер: Ну тогда я тебя в следующий раз так вздрючу сыч дрищавый.')
    else: print('Тренер: Понятно, даже ответить нормально не можешь, значит точно заебался.')
    sleep(1)
    print('Приходи послезавтра, отдохнувший, на протеине и с мощным стояком на железо!')
    print('Возможно я тебя не вспомню, у меня от анаболиков боли коликов.')
    print('*шлеп на enter*')
    you['Дней в зале'] += 1
    input()
    return start_game()


def start_game():
    print('Day {}\n'.format(you['Дней в зале']))
    you['Энергия'] = 100
    #you['Дней в зале'] = 2
    if you['Дней в зале'] == 1:
        scene1()  # Базар с тренером
    if you['Дней в зале'] != 1:
        print('Ну хеллоу, май диар {}'.format(you['Имя']))
    while you['Энергия'] > 85:        
        choose_exercise()
    end_of_the_day()


you = {'Имя': 'Сосяндр', 'Дней в зале': 1, 'Энергия': 100, 'Ручищи': 0,
       'Сисяндры': 0, 'Пузан': 0, 'Спинища': 0, 'Ножки': 0}

menu_commands = ['меню', 'menu', 'Я еблан, помогите мне.']

commands = {'меню': show_menu, 'menu': show_menu, 'Я еблан, помогите мне.': show_menu}

menu = {'Статистика': show_stats, 'Продолжить качаца': choose_exercise, 'Сохраниться': [], 'Сбросить результат': [], 'Помощь': []}

exercises = {
    'Грудь': {
        'унджумания': {'Энергия': 0.15, 'Ручищи': 0.015, 'Сисяндры': 0.04},
        'потягать штангу': {'Энергия': 0.3, 'Ручищи': 0.025, 'Сисяндры': 0.05},
        'пожать гантельки на скамье': {'Энергия': 0.3, 'Ручищи': 0.025, 'Сисяндры': 0.055},
        'попырить на себя в зеркало у кроссовера': {'Энергия': 0.25, 'Сисяндры': 0.07}},
    'Руки': {
        'гантельки на бицушку': {'Энергия': 0.25, 'Ручищи': 0.04},
        'слышал о брахиалисе?': {'Энергия': 0.25, 'Ручищи': 0.03},
        'тупой тренажер на бицепс': {'Энергия': 0.25, 'Ручищи': 0.04}}}

abuse = ['Ты не понял.', 'Посмотри пожалуйста повнимательнее.', 'Чего блять?!', 'Ты тупой?', 'Сука, ты меня уже бесишь...']

start_game()
