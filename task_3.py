# Получаем предложение от пользователя
sentence = input("Введите предложение: ")

# Получаем знак от пользователя
character = input("Введите знак для выделения слов: ")

# Разбиваем предложение на слова
words = sentence.split()

# Инициализируем переменную для хранения самого короткого слова
shortest_word = None

# Ищем самое короткое слово, начинающееся с заданного знака
for word in words:
    # Проверяем, начинается ли слово с заданного знака
    if word.startswith(character):
        # Если shortest_word пусто или текущее слово короче, сохраняем его
        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word

# Выводим результат
if shortest_word:
    print(f"Самое короткое слово, начинающееся с '{character}', это '{shortest_word}'")
else:
    print(f"Нет слов, начинающихся с '{character}' в данном предложении.")
