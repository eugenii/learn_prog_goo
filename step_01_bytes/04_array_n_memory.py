import array
import sys

# 1. Making an array of 100_000 integers
list_data = list(range(100_000))

# Ответ: по документации самым маленьким типом - 
# int ('b') со знаком,1 байт, int 'B' - без знака,1 байт 

# 2. Making an array of 100_000 integers
array_data = array.array('i', range(100_000))

# 3. Find sizes of objects

list_size = sys.getsizeof(list_data)
array_size = sys.getsizeof(array_data)

# 4. Print sizes and difference
print("размеры: list_size={}, array_size={}, diff={}".format(list_size, array_size, list_size - array_size))

# Размер array_data примерно в 2 раза меньше list_data

# 5. Print length of string from array of bytes
string_from_array = array_data.tobytes()
print("Длина строки, полученная из array_data методом .tobytes(): {}".format(len(string_from_array)))
print("И сама строка (начало и конец: {} ... {}".format(string_from_array[:10], string_from_array[-10:]))

# длина строки ровно 400_000 байт, начало строки заполняется какими-то символами?