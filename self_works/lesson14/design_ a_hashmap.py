class MyHashMap:
    def __init__(self):
        self.map = []

    def __str__(self):
        return f'{self.map}'

    def put(self, key, value):
        if self.map:
            for i in range(len(self.map)):
                if self.map[i][0] == key:
                    self.map[i][1] = value
                    break
            else:
                self.map.append([key, value])
        else:
            self.map.append([key, value])

    def get(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return self.map[i][1]
            else:
                return -1

    def remove(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.get(1)
myHashMap.get(3)
myHashMap.put(2, 1)
myHashMap.get(2)
myHashMap.remove(2)
myHashMap.get(2)
myHashMap.put(5, 6)
myHashMap.put(5, 8)

print(myHashMap.map)
