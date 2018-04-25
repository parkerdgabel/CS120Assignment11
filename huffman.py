def _huffman_walk(tree, func=lambda x: None, huff_seq=[]):
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
    huff_seq = huff_seq

    def _huffman(tree, func=lambda x: None, huff_seq=huff_seq):
        while huff_seq:
            _huffman_walk(tree, func, huff_seq)

    return _huffman


def pre_order(tree, func=lambda val: None):
    if tree is not None:
        func(tree)
        pre_order(tree._left, func)
        pre_order(tree._right, func)


def post_order(tree, func=lambda val: None):
    if tree is not None:
        post_order(tree._left, func)
        post_order(tree._right, func)
        func(tree)


def _construct_tree(pre_order, in_order):
    if not in_order:
        return None
    root = Node(pre_order[0])
    index = in_order.index(pre_order[0])
    root._left = _construct_tree(pre_order[1:index + 1], in_order[:index])
    root._right = _construct_tree(pre_order[index + 1:], in_order[index + 1:])
    return root


class Node:
    def __init__(self, val=None):
        self._value = val
        self._left = None
        self._right = None

    def is_leaf(self):
        return self._left is None and self._right is None


class BTree:
    def __init__(self, pre_order=[], in_order=[]):
        self._root = _construct_tree(pre_order, in_order)

    def collect(self, transversal=lambda: None):
        lst = []
        transversal(self._root, lambda x: lst.append(x._value))
        return lst


def main():
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
