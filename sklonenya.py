def end_of_words(x: int):
    """ Добавляет нужное окончание в зависимости от переменной"""
    if 5 <= x <= 20:
        ending = 'ов'
    elif x % 10 == 1:
        ending = ''
    elif 2 <= x % 100 <= 4:
        ending = 'а'
    else:
        ending = 'ов'
    return ending

"sdg".isdigit()