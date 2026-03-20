# Вторая тренировочная задача. Манипуляции с байтовым ммассивом.

phrase = "Learning bytes is fun!"

# 1. Создаём байтовый массив
b_phrase = bytearray(phrase, "utf-8")

# 2. Заменяем первый символ

b_phrase[0] = 87

# 3. Срез из последних трёх символов

sclice_b_phrase = b_phrase[-3:]

# 4. Добавляем в конец байт "!"

b_phrase.extend(b'!')


print(b_phrase.decode("utf-8"))

# Что бы посмотреть разницу:
print(b_phrase)
print(sclice_b_phrase.decode("utf-8"))
print(sclice_b_phrase)

# Используем число 87, а не букву - так как внутри b_phrase лежат байтовыне представления, а не символы?