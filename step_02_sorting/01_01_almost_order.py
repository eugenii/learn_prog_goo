# Почти порядок

data = list(map(int, input().split()))

last_element = data[-1]
j = len(data) - 2
while j >= 0 and data[j] > last_element:
    data[j + 1] = data[j]
    j -= 1
data[j + 1] = last_element

print(*data)