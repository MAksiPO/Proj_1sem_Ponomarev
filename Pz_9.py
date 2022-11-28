##Используя словарь посчитать количество уникальных слов в заданном
##предложении «Изучаем язык Питон». Вывести на экран каждую пару
##«ключ:значение».
favorite_languiges = {
    'Макс': 'python',
    'Киря': 'c',
    'Коля': 'ruby',
    'Жека': 'c#',
    'Олежа': 'ruby',
    'Лева': ['delphi', 'python']
}

langs = []
for lang in favorite_languiges.values():
    if type(lang) == list:
        langs += lang
    else:
        langs.append(lang)

print(set(langs))  # {'c#', 'python', 'c', 'ruby', 'delphi'}