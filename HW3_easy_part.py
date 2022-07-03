from sklonenya import end_of_words

# объявляем переменные
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
right_answers = 0

# Вывод приветствия и условий для начала игры
print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
is_ready = input()

# Проверка условия на запуск игры
if is_ready == 'ready':
    # Создадим цикл, который будет перебирать индексы вопросов и ответов
    for i in range(len(questions)):
        # задаем вопрос и получаем ответ
        print(questions[i])
        user_answer = input()

        # проверяем корректный ли ответ
        if user_answer == answers[i]:
            print('Ответ верный!')

            # увеличиваем количество правильных ответов на 1
            right_answers += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')

    # считаем проценты правильных ответов
    right_answers_percent = right_answers / len(questions) * 100

    # выводим общий результат
    print_first_part = f'Вы ответили на {right_answers} вопрос{end_of_words(right_answers)} из {len(questions)} верно'
    print_second_part = f'это {round(right_answers_percent)} процент{end_of_words(round(right_answers_percent))}.'

    print(f'Вот и все! {print_first_part}, {print_second_part}')
else:
    # Если пользователь ввел не ready
    print('Кажется, вы не хотите играть. Очень жаль.')
