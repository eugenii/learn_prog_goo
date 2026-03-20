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
        self.table[index].append([key, value])


# для создания теста на bash в дальнейшем...
commands = {
    'put': SimpleMap.put,
}

# data = [1, 11, 21]

table = SimpleMap()

# for elt in data:
#     table.put(elt, elt)

map = SimpleMap()
map.put(1, "первое")
map.put(1, "второе")
print(map.table[1]) # Должно быть только [[1, "второе"]]
