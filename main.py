from BinaryNode import BinaryNode
from nARYNode import NaryNode

root = BinaryNode("Root")

a = BinaryNode(root.add_left("A"))
b = BinaryNode(root.add_right("B"))

c = BinaryNode(a.add_left("C"))
d = BinaryNode(a.add_right("D"))

e = BinaryNode(b.add_right("E"))
f = BinaryNode(e.add_left("F"))

root2 = NaryNode("Root")
root2.add_child("A")
root2.add_child("B")
root2.add_child("C")

a1 = NaryNode("A")
a1.add_child("D")
a1.add_child("E")

b1 = NaryNode("B")
c1 = NaryNode("C")
c1.add_child("F")
d1 = NaryNode("D")
d1.add_child("G")
e1 = NaryNode("E")
f1 = NaryNode("F")
f1.add_child("H")
f1.add_child("I")
g1 = NaryNode("G")
h1 = NaryNode("H")
i1 = NaryNode("I")




if __name__ == '__main__':
    print(root)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(root2)
    print(a1)
    print(b1)
    print(c1)
    print(d1)
    print(e1)
    print(f1)
    print(g1)
    print(h1)
    print(i1)

