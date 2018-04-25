def _huffman_walk(tree, func=lambda x: None, huff_seq=[]):
    """Walks a huffman tree based on the sequence.
    Parameters: tree is a node
                func is the function to apply.
                huff_seq is the huffman sequence
    Returns: None
    Pre-conditions: None
    Post-conditions: None
    """
    if tree is not None:
        if tree.is_leaf():
            func(tree)
        else:
            if huff_seq:
                if huff_seq[0] == 0:
                    huff_seq.pop(0)
                    _huffman_walk(tree._left, func, huff_seq)
                elif huff_seq[0] == 1:
                    huff_seq.pop(0)
                    _huffman_walk(tree._right, func, huff_seq)


def huffman(huff_seq=[]):
    """Closure to walk a huffman sequence.
    Parameters: huff_seq is the huffman sequence.
    Returns: a function to traverse the sequence.
    Pre-conditions: None
    Post-conditions: A function is returned."""
    huff_seq = huff_seq

    def _huffman(tree, func=lambda x: None, huff_seq=huff_seq):
        if huff_seq:
            _huffman_walk(tree, func, huff_seq)
            _huffman(tree, func, huff_seq)

    return _huffman



def post_order(tree, func=lambda val: None):
    """Post order transversal for a tree.
    Parameters: tree is a node
                func is the function to apply
    Returns: None
    Pre-conditions: tree is a node
    Post-conditions: None"""
    if tree is not None:
        post_order(tree._left, func)
        post_order(tree._right, func)
        func(tree)


def _construct_tree(pre_order, in_order):
    """Constructs a binary tree from a preorder and postorder.
    Parameters: preorder is the preorder transversal
                inorder is the inorder transversal
    Returns: A node
    Pre-conditions: Preorde and inorder are lists.
    Post-conditions: a node is returned."""
    if not in_order:
        return None
    root = Node(pre_order[0])
    index = in_order.index(pre_order[0])
    root._left = _construct_tree(pre_order[1:index + 1], in_order[:index])
    root._right = _construct_tree(pre_order[index + 1:], in_order[index + 1:])
    return root


class Node:
    """Node abstraction for the Binary Tree.
    Attributes: _value is the value of the node
                _left is the left child.
                _right is the right child
    Methods:    __init__ is the constructor.
                is_leaf checks if the node is a leaf."""
    def __init__(self, val=None):
        """Constructor for Node.
        Parameters: val is the value to store in the Node
        Returns: a node
        Pre-construct: None
        Post-conditions: a node is born"""
        self._value = val
        self._left = None
        self._right = None

    def is_leaf(self):
        """Checks if the node is a leaf.
        Parameters: None
        Returns: True if the node is a leaf.
        Pre-conditions: None
        Post-conditions: a boolean is returned."""
        return self._left is None and self._right is None


class BTree:
    """Binary Tree abstraction.
    Attributes: _root is the root of the tree
    Methods: __init__ constructor for the tree
             collect returns a list of the nodes based on a designated transversal."""
    def __init__(self, pre_order=[], in_order=[]):
        self._root = _construct_tree(pre_order, in_order)

    def collect(self, transversal=lambda: None):
        lst = []
        transversal(self._root, lambda x: lst.append(x._value))
        return lst


def main():
    """Builds and decodes a huffman tree and sequence.
    Parameters: None
    Returns: An A++ on this assignment.
    Pre-conditions: None
    Post-conditions: All specs are met.
    """
    infile = input("Input file: ")
    try:
        infile = open(infile)
    except:
        print("ERROR: Could not open file " + infile)
        exit()
    infile = infile.readlines()
    infile = [x.strip() for x in infile]
    pre = infile[0].split()
    ino = infile[1].split()
    huff = [int(x) for x in infile[2]]
    ht = BTree(pre, ino)
    post = ht.collect(post_order)
    print(" ".join(post))
    huff_decode = ht.collect(huffman(huff))
    huff_decode = [str(x) for x in huff_decode]
    print("".join(huff_decode))


main()
