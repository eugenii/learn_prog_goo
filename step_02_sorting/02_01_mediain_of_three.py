# 1. Медиана трёх

def median_of_three(a, b, c):  # не использую встроенную сортировку для тренировки. Или стоило?
    if a > b:
        if a > c:
            return max(b, c)
        return a
    elif a > c:
        return a
    return min(b, c)

# тестирование функции "медиана"
# for _ in ((1, 2, 3), (2, 1, 3), (3, 2, 1), (1, 3, 2), (2, 3, 1), (3, 1, 2)):
#     print(_, median_of_three(*_))

def quick_sort_median(arr, start, end):
    if len(arr) <= 1:
        return arr
    pivot = median_of_three(arr[0], arr[len(arr) // 2], arr[-1])
    left, right = start, end
    
    # По всему массиву
    while left <= right:
        # Ищем слева тот, что должен быть(?) справа
        while arr[left] < pivot:
            left += 1
        # Ищем справа тот, что должен быть(?) слева
        while arr[right] > pivot:
            right -= 1
        # Если нашли, меняем местами
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    quick_sort_median(arr, start, right)  # Почему передаётся массив целиком только без некоторых элементов справа?
    quick_sort_median(arr, left, end)  # Аналогично с левой частью?

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    quick_sort_median(arr, 0, len(arr) - 1)
    print(*arr)
        

