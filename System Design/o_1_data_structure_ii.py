import random

class MyStructure:
    def __init__(self):
        self.arr = []
        self.map = {}
        self.size=0

    def insert(self, x):
        if x not in self.map:
            index = self.size
            self.arr.append(x)
            self.size+=1
            self.map[x] = index

    def remove(self, x):
        if x in self.map:
            index = self.map[x]
            del self.map[x]
            if index != self.size - 1:
                last = self.size - 1
                self.arr[index], self.arr[last] = self.arr[last], self.arr[index]
                if last != index:
                    self.map[self.arr[index]] = index
            self.arr.pop()
            self.size-=1

    def search(self, x):
        return self.map.get(x, -1)

    def getRandom(self):
        random_index = random.randint(0, self.size - 1)
        return self.arr[random_index]

ds = MyStructure()
ds.insert(10)
ds.insert(20)
ds.insert(30)
ds.insert(40)
print(ds.search(30))
ds.remove(40)
ds.insert(50)
print(ds.search(50))
print(ds.getRandom())

# This code is modified by Susobhan Akhuli
