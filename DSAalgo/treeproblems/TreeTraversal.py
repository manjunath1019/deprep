from DSAalgo.treeproblems.TreeNode import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self,node,traversal):
        #ROOT -> LEFT -> RIGHT
        if node is None:
            return -1
        traversal.append(node.value)
        self.preorder(node.left,traversal)
        self.preorder(node.right, traversal)
        return traversal

    def inorder(self, node, traversal):
        #LEFT -> ROOT -> RIGHT
        if node is None:
            return -1

        self.inorder(node.left, traversal)
        traversal.append(node.value)
        self.inorder(node.right, traversal)
        return traversal

    def postorder(self, node, traversal):
        # LEFT -> RIGHT -> ROOT
        if node is None:
            return -1

        self.postorder(node.left, traversal)
        self.postorder(node.right, traversal)
        traversal.append(node.value)

        return traversal

if __name__ == '__main__':
    t = BinaryTree()
    if t.root is None:
        #Level 0
        t.root = TreeNode(1)
    print(t.root.value)


    #Level 1
    t.root.left = TreeNode(2)
    t.root.right = TreeNode(3)

    print("Level 1 : Left: ",t.root.left.value)
    print("Level 1 : right :" ,t.root.right.value)

    #Level 2
    t.root.left.left = TreeNode(4)
    t.root.left.right = TreeNode(5)
    print("level 2 left: ",t.root.left.left.value,t.root.left.right.value)
    #level 2
    t.root.right.left = TreeNode(6)
    t.root.right.right = TreeNode(7)
    print("level 2 right: ", t.root.right.left.value, t.root.right.right.value)


    #DFS
    #Prepordering
    print("Preordering tree")
    a = t.preorder(t.root,[])
    print(a)

    # DFS
    # Inordering
    print("InOrdering tree")
    b = t.inorder(t.root, [])
    print(b)

    # DFS
    # POST pordering
    print(" POST Ordering tree")
    c = t.postorder(t.root, [])
    print(c)

