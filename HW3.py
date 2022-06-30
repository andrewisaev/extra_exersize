questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
right_answers = 0
score = 0

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
is_ready = input()
if is_ready == 'ready':
    for i in range(len(questions)):
        for attempt in range(2, -1, -1):
            print(questions[i])
            user_answer = input()
            if user_answer == answers[i]:
                print('Ответ верный!')
                right_answers += 1
                score += attempt + 1
                break
            else:
                if attempt == 0:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}')
                else:
                    print(f'Осталось попыток: {attempt}, попробуйте еще раз!')

    print(f'Вот и все! Вы ответили на {right_answers} вопросов из {len(questions)} верно, вы набрали {score} баллов.')
else:
    print('Кажется, вы не хотите играть. Очень жаль.')
