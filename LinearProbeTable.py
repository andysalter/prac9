from Exceptions import DictFullError

class Dictionary:
    def __init__(self, size=7919, prime=31415, items=None):
        # complexity: O(n)
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
        # complexity: O(k) where k is length of key
        value = 0
        a = self.base
        b = 27183
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.tablesize
            a = a * b % (self.tablesize - 1)
        return value

    def __setitem__(self, key, data):
        # complexity: best = O(1), worst = O(n)
        position = self.hash(key)

        for _ in range(self.tablesize):
            if self.array[position] is None:
                # found empty slot
                self.array[position] = (key, data)
                self.count += 1
                return
            elif self.array[position][0] == key:
                # found key
                self.array[position] = (key, data)
                return
            else:
                # not found, try n+1
                position = (position + 1) % self.tablesize

        raise (DictFullError, 'The dictionary is full and key is non-existent')

    def __getitem__(self, key):
        # complexity: best = O(1), worst = O(n)
        position = self.hash(key)

        for i in range(self.tablesize):
            if self.array[position] is None:
                # found empty slot
                return None
            elif self.array[position][0] == key:
                # found key
                return self.array[position][1]
            else:
                # not found, try n+1
                position = (position + 1) % self.tablesize

        raise KeyError(key)

    def is_full(self):
        return len(self) == self.tablesize

