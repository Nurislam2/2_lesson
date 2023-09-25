sentence = input("Введите предложение: ")
word = input("Введите слово: ")
list= sentence.split(" ")
if word in list:
    print("Слово найдено")
else:
    print("такого слова нет")



# # Получаем строку от пользователя
# input_string = input("Введите строку: ")
#
# # Получаем "полуслово" от пользователя
# search_prefix = input("Введите начало слова для поиска: ")
#
# # Разбиваем строку на слова
# words = input_string.split()
#
# # Создаем список для хранения слов, начинающихся с "полуслова"
# matching_words = []
#
# # Проверяем каждое слово в строке
# for word in words:
#     # Если слово начинается с "полуслова", добавляем его в список
#     if word.startswith(search_prefix):
#         matching_words.append(word)
#
# # Выводим результат
# if matching_words:
#     print(f"Слова, начинающиеся с '{search_prefix}':")
#     for word in matching_words:
#         print(word)
# else:
#     print(f"Слова, начинающиеся с '{search_prefix}', не найдены в строке.")
