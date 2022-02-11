class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child):
        child_value = NaryNode(child)
        self.children[child] = child_value
        return child_value

    def values(self):
        return self.value

    def _traverse_preorder(self, v=None):

        if self is None:
            return self

        v.append(self.value)
        if self.value is not None:
            for node, value in self.children.items():
                self = value
                self._traverse_preorder(v)

    def _traverse_postorder(self, v=None):

        if not self.children:
            v.append(self.values())
            return None

        for items in self.children.keys():
            self.children[items]._traverse_postorder(v)

        v.append(self.values())

    def traverse_postorder(self):
        v = []
        self._traverse_postorder(v)
        return v

    def traverse_preorder(self):
        v = []
        self._traverse_preorder(v)
        return v

    def traverse_breadth_first(self):
        v = []
        lev = []
        self._traverse_breadth_first(v, lev)
        return v

    def find_node(self, value_to_find):
        v = []
        self._traverse_preorder(v)
        return f'Found {value_to_find}' if value_to_find in v else f'Value {value_to_find} not found'

    def _traverse_breadth_first(self, v=None, lev=None):

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
                lev.append(level)
                v.append(q.value)

                for key, val in q.children.items():
                    queue.append((val, level + 1))

                if queue is None or queue == []:
                    break

    def __str__(self):
        values, levels = [], []
        self._traverse_breadth_first(values, levels)
        d = dict(zip(values, levels))

        preorder = []
        self._traverse_preorder(preorder)

        s = ''
        for item in preorder:
            s += ' ' * d[item] + str(item) + ':\n'

        return s
