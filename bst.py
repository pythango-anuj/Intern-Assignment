class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = Node()

    def inorder(self):
        root = self.root
        def printit(root):
            if root is not None:
                printit(root.left)
                print(root.val, end=" ")
                printit(root.right)
        printit(root)

    def insert(self, item):
        if self.root.val == 0:
            self.root.val = item
        else:
            var = Node(item)
            node = self.root
            while node is not None:
                if item > node.val:
                    if node.right is None:
                        node.right = var
                        break
                    node = node.right
                elif item < node.val:
                    if node.left is None:
                        node.left = var
                        break
                    node = node.left
                else:
                    return "Node already exist."

    def delete(self, item):
        root = self.root

        def delete_node(root, item):
            if item > root.val:
                root.right = delete_node(root.right, item)
            elif item < root.val:
                root.left = delete_node(root.left, item)
            else:
                print(root.val)
                if root.right is None:
                    print("check")
                    temp = root.left
                    print(temp.val)
                    root = None
                    return temp
                elif root.left is None:
                    temp = root.right
                    root = None
                    return temp
                current = root.right
                while(current.left is not None):
                    current = current.left

                root.val = current.val
                root.right = delete_node(root.right, current.val)
            return root

        root = delete_node(root, item)

    def search(self, item):
        node = self.root
        flag = False
        while node is not None and flag == False:
            if item == node.val:
                flag = True
            else:
                if item > node.val:
                    node = node.right
                else:
                    node = node.left
        return flag

    def size(self):
        node = self.root

        def count(node):
            if node is None:
                return 0
            else:
                return 1 + count(node.left) + count(node.right)
        return count(node)


if __name__ == '__main__':
    t = BST()
    t.insert(10)
    t.insert(7)
    t.insert(8)
    t.insert(6)
    t.insert(9)
    t.insert(13)
    t.insert(12)
    t.insert(11)
    t.insert(14)
    t.insert(15)
    t.inorder()
    print()
    print(t.size())
    print(t.search(12))
    t.delete(12)
    print(t.search(12))
    t.inorder()
    print()
    print(t.search(7))
    t.delete(7)
    print(t.search(7))
    t.inorder()
    print()
    print(t.size())


