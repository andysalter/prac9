from Node import Node


class List:
    def __init__(self, py_list=[]):
        self.head = None
        self.count = 0
        if len(py_list) != 0:
            for item in py_list:
                self.append(item)

    def __len__(self):
        return self.count


    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if index > len(self) + 1:
            raise IndexError("Index out of range")

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __setitem__(self, index, value):
        if index < 0:
            index += len(self)
        if index > len(self) + 1:
            raise IndexError("Index is out of range")

        node = self[index]
        node.item = value

    def __str__(self):
        string = ''
        if self.count == 0:
            string = '0|\n'
        else:
            node = self.head
            for index in range(self.count):
                string += str(index) + '\t|\t' + str(node.item) + '\n'
                node = node.next
        return string


    def __repr__(self):
        return repr(self.to_list())


    def __iter__(self):
        for x in self.to_list():
            yield x


    def to_list(self):
        the_list = []
        node = self.head
        for _ in range(self.count):
            the_list.append(node.item)
            node = node.next
        return the_list


    def format_item(self, index):
        string = ""
        if index < 0:
            index += len(self)
        if index >= len(self):
            index = len(self) - 1
        if index < 0:
            index = 0

        if self.count == 0:
            string = "0|\n"
        else:
            string += str(index) + "\t|\t" + str(self[index]) + "\n"
        return string


    def is_empty(self):
        return self.count == 0


    def reset(self):
        self.__init__()


    def insert(self, index, item):
        if index < 0:
            index += len(self)
        if index >= len(self):
            index = len(self)
        if index < 0:
            index = 0

        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self[index - 1]
            node.next = Node(item, node.next)
        self.count += 1


    def insert_block(self, index, linked_list):
        assert isinstance(self, List), "argument linked_list is not an instance of List"
        if index < 0:
            index += len(self) + 1
        if index >= len(self):
            index = len(self)
        if index < 0:
            index = 0

        if index == 0:
            linked_list[linked_list.count - 1].next = self.head
            self.head = linked_list.head
        else:
            node = self[index - 1]
            linked_list[linked_list.count - 1].next = node.next
            node.next = linked_list.head
        self.count += len(linked_list)


    def append(self, item):
        if self.count == 0:
            self.head = Node(item, self.head)
        else:
            node = self[self.count - 1]
            node.next = Node(item, node.next)
        self.count += 1


    def delete(self, index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0:
            index += len(self)
        if index >= len(self):
            index = len(self) - 1
        if index < 0:
            index = 0

        if index == 0:
            self.head = self.head.next
        else:
            node = self[index - 1]
            node.next = node.next.next

        self.count -= 1

    def replace(self, index, linked_list):
        self.delete(index)
        self.insert_block(index, linked_list)