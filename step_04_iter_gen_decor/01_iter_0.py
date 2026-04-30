class ReverseIter:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # Начинаем с последнего индекса

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        
        value = self.data[self.index]
        self.index -= 1  # Сдвигаем курсор влево
        return value
    
    def __repr__(self):
        return 'returns reversed list'


data = [1, 2, 3, 4, 5]

revers = ReverseIter(data)
for i in revers:
    print(i)    
print(revers)