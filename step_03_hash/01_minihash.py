# mini-hash

class SimpleMap:
    def __init__(self, size=10):
        """Массив корзин. Размер по умолчанию 10."""
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        """Хеш-функция. Возвращает индекс корзины."""
        return abs(hash(key)) % self.size
    
    def put(self, key, value):
        """Добавляет пару (ключ, значение) в таблицу."""
        index = self._get_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])  # Изменил кортеж на список

    def get(self, key):
        index = self._get_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
            return None
        
    def delete(self, key):
        index = self._get_hash(key)
        for i,  item in enumerate(self.table[index]):  # перебираю пары (ключ, значение)
            if item[0] == key:
                x = item[1]
                self.table[index].pop(i)  # удалил эту ПАРУ!
                return x
        return None


# для создания теста на bash в дальнейшем...
commands = {
    'put': SimpleMap.put,
}

# data = [1, 11, 21]

# table = SimpleMap()

# take 1
# for elt in data:
#     table.put(elt, elt)

# take 2
# map = SimpleMap()
# map.put(1, "первое")
# map.put(1, "второе")
# print(map.table[1]) # Должно быть только [[1, "второе"]]

# take 3
# my_map = SimpleMap()
# my_map.put(10, "apple")
# print(my_map.get(10))  # Должно вывести: apple
# print(my_map.get(999)) # Должно вывести: None

# take 4
map = SimpleMap()
map.put(5, "пять")
print(map.delete(5)) # Должно вывести: пять
print(map.get(5))    # Должно вывести: None

