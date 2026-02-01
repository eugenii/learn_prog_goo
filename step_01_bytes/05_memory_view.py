import timeit

# Твои данные
data = bytearray(10_000_000)
view = memoryview(data)

# 1. Определяем функции для теста
def test_slice():
    # Обычный срез создает копию данных в памяти
    return data[1000:6000]

def test_view():
    # Срез через memoryview — это просто "ссылка" на часть данных
    return view[1000:6000]


# 2. Замеряем время (выполним каждую функцию 1 000 000 раз)
time_slice = timeit.timeit(test_slice, number=1000000)
time_view = timeit.timeit(test_view, number=1000000)

print(f"Обычный срез: {time_slice:.4f} сек")
print(f"Memoryview срез: {time_view:.4f} сек")

for n in range(1, 6):
    time_slice = timeit.timeit(test_slice, number=n * 1000000)
    time_view = timeit.timeit(test_view, number=n * 1000000)
    print(f"Разница во времени для {n} млн вызовов: {time_slice - time_view:.4f} сек")

# Зависимость увеличения разности очень похожа на линейную
# (примерно по 0.14 секунды на каждый млн вызовов)

# Если memoryview быстрее, то он может быть полезен для больших данных.
# Если к тому же он позволяет изменять данные в "этом окне" , то вообще незаменим
# а он позволяет?
