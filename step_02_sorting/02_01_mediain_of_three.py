# 1. Медиана трёх

def median_of_three(a, b, c): 
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
    if start >= end:
        return arr
    pivot = arr[median_of_three(start, (start + end) // 2, end)]  # pivot - значение
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
    if start < right:
        quick_sort_median(arr, start, right)  # Здесь разобрался
        quick_sort_median(arr, left, end)  # тоже самое

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    quick_sort_median(arr, 0, len(arr) - 1)
    print(*arr)

    assert median_of_three(1, 7, 4) == 4

        

