class FrogJump:

    def __init__(self, data, step=1):
        self.data = data
        self.step = step
        self.pos = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos >= len(self.data):
            raise StopIteration
        
        elt = self.data[self.pos]
        self.pos += self.step
        return elt
    

frog = FrogJump([10, 20, 30, 40, 50, 60], step=2)
for val in frog:
    print(val)
# Должно вывести:
# 10
# 30
# 50