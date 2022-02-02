class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left_value = None
        self.right_value = None

    def add_left(self, value_left):
        self.left_value = value_left
        return self.left_value

    def add_right(self, value_right):
        self.right_value = value_right
        return self.right_value

    def __str__(self):
        return f'{self.value}: {self.left_value} {self.right_value}'




