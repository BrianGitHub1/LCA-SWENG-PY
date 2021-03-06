
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLcaInt(root, n1, n2, v):

    if root is None:
        return None

    if root.key == n1 :
        v[0] = True
        return root

    if root.key == n2:
        v[1] = True
        return root

    left_lca = findLcaInt(root.left, n1, n2, v)
    right_lca = findLcaInt(root.right, n1, n2, v)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


def find(root, k):

    if root is None:
        return False

    if (root.key == k or find(root.left, k) or
            find(root.right, k)):
        return True

    return False

def findLCA(root, n1, n2):

    v = [False, False]

    lca = findLcaInt(root, n1, n2, v)

    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
            find(lca, n1)):
        return lca

    return None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)


print(lca.key)

def build():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root
#yup