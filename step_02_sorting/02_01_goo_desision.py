def get_median_index(arr, start, mid, end):
    # Логика поиска индекса среднего из трех
    a, b, c = arr[start], arr[mid], arr[end]
    if (b <= a <= c) or (c <= a <= b): return start
    if (a <= b <= c) or (c <= b <= a): return mid
    return end

def quick_sort(arr, start, end):
    if start >= end:
        return

    # 1. Выбираем пивот через медиану трех
    mid_idx = (start + end) // 2
    pivot_idx = get_median_index(arr, start, mid_idx, end)
    pivot = arr[pivot_idx]

    left, right = start, end

    # 2. Partition (схема Хоара)
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # 3. Рекурсивные вызовы
    # Важно: используем полученные границы right и left
    if start < right:
        quick_sort(arr, start, right)
    if left < end:
        quick_sort(arr, left, end)

arr = [int(i) for i in input().split()]
quick_sort(arr, 0, len(arr) - 1)
print(*arr)