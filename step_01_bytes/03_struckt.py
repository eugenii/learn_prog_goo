import struct


ID = 42
rating = 95.5

# 1. Упаковываем ('i' - 4 байта, 'f' - 4 байта)
header = struct.pack('if', ID, rating)
print(len(header))

# 2. Распаковываем
# unpack всегда возвращает кортеж (tuple), даже если там одно число
unpacked_data = struct.unpack('if', header)
new_ID, new_rating = unpacked_data
print("Распаковали: new_ID = {}, new_rating = {}".format(new_ID, new_rating))

# 3. Изменение bytearray
mutable_header = bytearray(header)
mutable_header[3] = 255  
new_unpacked_header = struct.unpack('if', mutable_header)
new_ID_2, new_rating_2 = new_unpacked_header
print("Распаковали_2: new_ID = {}, new_rating = {}".format(new_ID_2, new_rating_2))

# если указать mutable_header[1..3] - для id получается ерунда, но ведь id занимает 4 байта?
# рейтинг меняется при изменении байтов 4..7