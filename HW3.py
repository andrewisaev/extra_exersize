questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
right_answers = 0

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
is_ready = input()
if is_ready == 'ready':
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input()
        if user_answer == answers[i]:
            print('Ответ верный!')
            right_answers += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')
    right_answers_percent = right_answers / len(questions) * 100
    print(f'Вот и все! Вы ответили на {right_answers} вопросов из {len(questions)} верно, это {round(right_answers_percent)} процентов.')
else:
    print('Кажется, вы не хотите играть. Очень жаль.')
