
class SymbolTable:
    def __init__(self, initial_capacity=23):
        self._capacity = initial_capacity
        self._size = 0
        self._elements = ["!!!0!!!" for i in range(self._capacity)]

    def hash_function(self, element, index):
        return (element % self._capacity + index * (element * element % self._capacity)) % self._capacity

    def add(self, element):
        if element in self._elements:
            return self.get(element)
        for trial in range(self._capacity):
            current_position = self.hash_function(hash(element), trial)
            if self._elements[current_position] == "!!!0!!!":
                self._elements[current_position] = element
                self._size += 1
                return current_position

    def get(self, element):
        for trial in range(self._capacity):
            current_position = self.hash_function(hash(element), trial)
            if self._elements[current_position] == element:
                return current_position
        return -1

    def __str__(self):
        return str(self._elements)
