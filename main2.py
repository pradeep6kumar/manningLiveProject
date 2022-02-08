from BinaryNode2 import BinaryNode
from NaryNode2 import NaryNode
#from nARYNode2 import NaryNode

root = BinaryNode('Root')
a = BinaryNode('A')
root.add_left(a)
b = BinaryNode('B')
root.add_right(b)
c = BinaryNode('C')
a.add_left(c)
d = BinaryNode('D')
a.add_right(d)
e = BinaryNode('E')
b.add_right(e)
f = BinaryNode('F')
e.add_left(f)


root2 = NaryNode('Root')
a2= root2.add_child('a')
b2 = root2.add_child('b')
c2 = root2.add_child('c')
d2 = a2.add_child('d')
e2 = a2.add_child('e')
g2 = d2.add_child('g')
f2 = c2.add_child('f')
h2 = f2.add_child('h')
i2 = f2.add_child('i')

if __name__ == '__main__':
    print(root)
    print("======Printing Nary Node=====")
    print('')
    print(root2)

