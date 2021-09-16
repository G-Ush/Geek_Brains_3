import random
'''1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.'''
'''2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы —
результат тоже должен быть с заглавной.'''
dict_of_num = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(user_num):
    if user_num.istitle():
        correct_key = user_num.lower()
        return dict_of_num.get(correct_key).capitalize()
    else:
        return dict_of_num.get(user_num)


# result = num_translate(input('Type the number in English: '))
# print(result)

'''3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, 
содержащие имена, начинающиеся с соответствующей буквы.'''

empty_dict = {}


def thesaurus(*name_list):
    for i in range(len(name_list)):
        empty_dict.setdefault(name_list[i][0], [el for el in name_list if el[0] == name_list[i][0]])
    return empty_dict


dict_name = thesaurus('Вася', 'Надя', 'Света', 'Коля', 'Кристина', 'Вадим', 'Неля', 'Сергей')
# print(dict_name)

'''5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого)'''

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
joke_list = []


def get_joke(n):
    for i in range(n):
        random_string = f'{nouns[random.randrange(len(nouns))]} {adverbs[random.randrange(len(adverbs))]}' \
                        f' {adjectives[random.randrange(len(adjectives))]}'
        joke_list.append(random_string)
    return joke_list


list_of_joke = get_joke(2)
# print(list_of_joke)
'''НЕ УСПЕЛ :(Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?'''