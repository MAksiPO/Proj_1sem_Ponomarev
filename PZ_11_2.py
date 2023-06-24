# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

file1 = open('text18-20.txt', 'r', encoding="UTF-8")
text = file1.read()
file1.close()

text = text.split('\n')
max_length = 0
for x, y in enumerate(text):
    if max_length < len(y):
        max_length = len(y)
        max_length_text = y

file2 = open('text_max_length.txt', 'w', encoding="UTF-8")
file2.write(max_length_text)
file2.close()