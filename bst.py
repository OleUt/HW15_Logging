class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root):
        self.root = None

    def print_tree(self, node):             # print all nodes
        if node is None:
            return
        self.print_tree(node.left)
        print(node.data)
        self.print_tree(node.right)

# Test 1. Function 'add_nodes' loads list of nodes and inserts them applying 'insert' and '__find'

    def add_nodes(self, nodes):             # accepts list of new nodes
        for i in nodes:
            self.insert(Node(i))

    def insert(self, obj):                  # add new node
        if self.root is None:
            self.root = obj
            return obj
        s, p, flag_ = self.__find(self.root, None, obj.data)    # find location for new node
        if not flag_ and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def __find(self, node, parent, value):  # finds available location for the new node
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True       # value is already in the tree
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)      # returns available parent
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)     # returns available parent
        return node, parent, False          # returns node, available parent, no this value in the tree

# Test 2. Functions find MIN and MAX in BST

    def find_max(self, node, parent):       # defines MAX
        if node.right:
            # print('right ', node.right)
            return self.find_max(node.right, node)
        print('max ', node, parent)
        return node, parent

    def find_min(self, node, parent):       # defines MIN
        if node.left:
            return self.find_min(node.left, node)
        print('min ', node)
        return node, parent

# Test 3. Function 'del_node' removes the node using '__del_leaf', '__del_one_child', find_min

    def __del_leaf(self, s, p):             # delete a leaf
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):        # delete one child branch
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def del_node(self, key):                                # removes a node
        s, p, flag_ = self.__find(self.root, None, key)     # find the node
        if not flag_:
            return None     # no such a node
        if s.left is None and s.right is None:              # delete a leaf
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:             # delete a node if one child branch
            self.__del_one_child(s, p)
        else:                                               # delete a node if two children branches
            sr, pr = self.find_min(s.right, s)              # search MIN in the right subtree
            s.data = sr.data                                # target node replacement by MIN from the right subtree
            self.__del_one_child(sr, pr)                    # delete MIN from the right subtree


my_tree = Tree(20)
my_nodes = [20, 14, 17, 25, 23, 9, 15, 28]
Tree.add_nodes(my_tree, my_nodes)
print('original tree')
my_tree.print_tree(my_tree.root)
print('reduced tree')
my_tree.del_node(14)
my_tree.print_tree(my_tree.root)
