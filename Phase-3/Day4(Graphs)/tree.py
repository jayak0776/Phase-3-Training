class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def addNode(self, root, value):
        newNode = Node(value)
        if root is None:
            return newNode
        else:
            if value < root.data:
                if root.left is None:
                    root.left = newNode
                else:
                    root.left = self.addNode(root.left, value)
            else:
                if root.right is None:
                    root.right = newNode
                else:
                    root.right = self.addNode(root.right, value)
        return root

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)                

    def levelOrder(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while len(q) != 0:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    def digional(self,root):
        pass
val = [16, 9, 4, 10, 8, 23, 83]
tree = BST()
root = None
for v in val:
    root = tree.addNode(root, v)

tree.inOrder(root)
print()
tree.levelOrder(root)
