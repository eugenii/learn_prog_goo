def logger(func):
    def wrapper(*args, **kwargs):  # *args и **kwargs нужны, чтобы прокинуть любые аргументы
        # 1. Напиши тут print
        print('Выполняю функцию {}.'.format(func.__name__))
        # 2. Вызови func и сохрани результат
        result = func(*args, **kwargs)
        # 3. Напиши тут print
        print("Функция завершена.")
        # 4. Верни результат
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 7))
