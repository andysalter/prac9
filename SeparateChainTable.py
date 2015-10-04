from linked_list import List

class Dictionary:
    def __init__(self, size=7919, prime=31415, items=None):
        self.count = 0
        self.array = [None] * size
        self.tablesize = size
        self.base = prime
        if items is not None:
            for key, data in items:
                self[key] = data



    def __len__(self):
        return self.count


    def hash(self, key):
        value = 0
        a = self.base
        b = 27183
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.tablesize
            a = a * b % (self.tablesize - 1)
        return value


    def __setitem__(self, key, data):
        position = self.hash(key)

        if self.array[position] is None:
            # found empty slot
            self.array[position] = List([(key, data)])
            self.count += 1
            return
        else:
            # if not empty, search list
            for index in range(len(self.array[position])):
                if self.array[position][index].item[0] == key:
                    self.array[position][index].item = (key, data)
                    self.count += 1
                    return
            # if key not in list, append it to the list
            self.array[position].append((key, data))
            self.count += 1
            return


    def __getitem__(self, key):
        position = self.hash(key)

        if self.array[position] is None:
            # found empty slot
            return None
        else:
            # if not empty search list
            for index in range(len(self.array[position])):
                if self.array[position][index].item[0] == key:
                    return self.array[position][index].item[1]

        raise KeyError(key)
