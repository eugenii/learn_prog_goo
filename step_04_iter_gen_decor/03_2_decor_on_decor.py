def repeater(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Тут должен быть цикл for на n итераций
            for _ in range(n):
                result = func(*args, **kwargs)
            # Внутри цикла вызывай func(*args, **kwargs)
            # В конце верни результат ПОСЛЕДНЕГО вызова
            return result
        return wrapper
    return decorator

@repeater(3)
def greet(name):
    print(f"Привет, {name}!")

greet("Мир")
# Ожидаемый вывод:
# Привет, Мир!
# Привет, Мир!
# Привет, Мир!
