class NaryNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, cnode):
        self.children.append(cnode)

    def __str__(self):
        if self.children:
            return f'{self.value}: {" ".join([item for item in self.children])}'
        else:
            return f'{self.value}:'