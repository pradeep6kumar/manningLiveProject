class NaryNode:

    gaps = ' '

    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child):
        child_value = NaryNode(child)
        self.children[child] = child_value
        return child_value

    def pre_order(self, v=None):

        if self is None:
            return self
        v.append(self.value)
        if self.value is not None:
            for node, value in self.children.items():
                self = value
                self.pre_order(v)

    def find_node(self, value_to_find):
        v = []
        self.pre_order(v)
        return f'Found {value_to_find}' if value_to_find in v else f'Value {value_to_find} not found'

    def level_order(self, v=None, l=None):

        if self is None:
            return None

        queue = []
        level = 0
        # levels = []
        root = self.value
        queue.append((self, level))

        if self.children is None:
            return root
        else:
            while True:
                q, level = queue.pop(0)
                l.append(level)
                v.append(q.value)
                # levels.append(level)

                for key, val in q.children.items():
                    queue.append((val, level + 1))

                if queue is None or queue == []:
                    break

    def __str__(self):
        values, levels = [], []
        self.level_order(values, levels)
        d = dict(zip(values, levels))

        preorder = []
        self.pre_order(preorder)

        s = ''
        for item in preorder:
            s += NaryNode.gaps * d[item] + str(item) + ':\n'

        return s


