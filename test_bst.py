import pytest
from bst import Node, Tree

my_tree = Tree(20)
my_nodes = [20, 14, 17, 25, 23, 9, 15, 32, 28]
my_tree.add_nodes(my_nodes)

# Tree.print_tree(my_tree, my_tree.root)
# print(my_tree.root, my_tree.root.left, my_tree.root.left.left,
#       my_tree.root.left.right, my_tree.root.left.right.left,
#       my_tree.root.right, my_tree.root.right.left,
#       my_tree.root.right.right, my_tree.root.right.right.left)

@pytest.mark.parametrize('a, b', [(my_tree.root, 20),
                                  (my_tree.root.left, 14),
                                  (my_tree.root.left.left, 9),
                                  (my_tree.root.left.right, 17),
                                  (my_tree.root.left.right.left, 15),
                                  (my_tree.root.right, 25),
                                  (my_tree.root.right.left, 23),
                                  (my_tree.root.right.right, 32),
                                  (my_tree.root.right.right.left, 28)])
def test_add_nodes(a, b):
    assert str(a) == str(b)


def test_del_leaf():
    Tree.del_node(my_tree, 9)
    assert my_tree.root.left.left is None

def test_one_child():
    Tree.del_node(my_tree, 17)
    assert str(my_tree.root.left.right) == str(15)
    assert my_tree.root.left.right.left is None

def test_del_node_if_branch():
    Tree.del_node(my_tree, 25)
    assert str(my_tree.root.right) == str(28)
    assert my_tree.root.right.right.left is None
