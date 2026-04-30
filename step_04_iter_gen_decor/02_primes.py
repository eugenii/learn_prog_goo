def primes(n):
    for num in range(2, n + 1):
        # ... тут проверка: если num простое ...
        div = int(num ** 0.5) + 1
        for i in range(2, div):
            if num % i == 0 and num != 2:
                break
        else:
            yield num
        

for p in primes(10):
    print(p) # Должно вывести 2, 3, 5, 7
