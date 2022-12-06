#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file_input.txt', 'w', encoding='utf_8') as data:
    data.write('Текст, содержащий "абвгд"\n')
with open('file_input.txt', 'r', encoding='utf_8') as data:
    stroka = data.readline()
    print(stroka.split())
    new_text = ' '.join([word for word in stroka.split() if 'абв' not in word])
with open('file_output.txt', 'w', encoding='utf_8') as data:
    data.write(new_text)