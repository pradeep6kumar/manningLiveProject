class BinaryNode:
    gaps = '  '
    count = 0

    def __init__(self, value):
        self.value = value
        self.left_value = None
        self.right_value = None

    def values(self):
        return self.value

    def add_left(self, value_left):
        BinaryNode.count += 1
        self.left_value = value_left
        self.right_value = BinaryNode('None' + str(BinaryNode.count))
        # self.add_right("None" + str(BinaryNode2.count))

    def traverse_preorder(self):
        v = []
        self._traverse_preorder(v)
        return [item for item in v if item.find('None')]

    def traverse_inorder(self, v=None):
        v = []
        self._traverse_inorder(v)
        return [item for item in v if item.find('None')]

    def traverse_postorder(self, v=None):
        v = []
        self._traverse_postorder(v)
        return [item for item in v if item.find('None')]

    def _traverse_preorder(self, v=None):

        if self is None:
            return None

        v.append(self.values())

        if self.left_value:
            self.left_value._traverse_preorder(v)

        if self.right_value:
            self.right_value._traverse_preorder(v)

    def _traverse_inorder(self, v=None):
        if self is None:
            return self

        if self.left_value:
            self.left_value._traverse_inorder(v)
        v.append(self.values())
        if self.right_value:
            self.right_value._traverse_inorder(v)

    def _traverse_postorder(self, v=None):
        if self is None:
            return self

        if self.left_value:
            self.left_value._traverse_postorder(v)

        if self.right_value:
            self.right_value._traverse_postorder(v)
        v.append(self.values())

    def traverse_breadth_first(self):
        v = []
        self._level_order(v)
        return v

    def add_right(self, value_right):
        BinaryNode.count += 1
        self.right_value = value_right
        if self.left_value is None:
            self.left_value = BinaryNode('None' + str(BinaryNode.count))

    def find_node(self, value_to_find):
        v = []
        self._traverse_preorder(v)
        return f'Found {value_to_find}' if value_to_find in v else f'Value {value_to_find} not found'

    def _level_order(self, v=None):
        temp = []
        level_value = 0
        v[self.values()] = (level_value, 'c')
        temp_object = self

        while True:
            # print('while loop starts')
            if temp_object.left_value is not None:
                temp.append((temp_object.left_value, level_value + 1))
                v[temp_object.left_value.values()] = (temp[-1][1], 'l')

            if temp_object.right_value is not None:
                temp.append((temp_object.right_value, level_value + 1))
                v[temp_object.right_value.values()] = (temp[-1][1], 'r')

            level_value += 1
            if temp is not None and temp != []:
                j_temp = temp.pop(0)
                temp_object = j_temp[0]
                level_value = j_temp[1]
            else:
                break
            if temp_object is None:
                break

    def __str__(self):
        nodes = []
        nodes_with_levels = {}
        self._traverse_preorder(nodes)
        self._level_order(nodes_with_levels)
        stroutput = ''
        for item in nodes:
            if item.find('None'):
                stroutput += BinaryNode.gaps * nodes_with_levels[item][0] + item + ':\n'
            else:
                stroutput += BinaryNode.gaps * nodes_with_levels[item][0] + 'None' + '\n'

        return stroutput

