class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Preorder Traversal
# Root -> Left -> Right
def preorder_recursive(node):
    if node:
        print(node.val)
        preorder_recursive(node.left)
        preorder_recursive(node.right)


def preorder_iterative(root):
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# 2. Inorder Traversal
# Left -> Root -> Right
def inorder_recursive(node):
    if node:
        inorder_recursive(node.left)
        print(node.val)
        inorder_recursive(node.right)


def inorder_iterative(root):
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        print(cur.val)
        cur = cur.right


# 3. Postorder Traversal
# Left -> Right -> Root
def postorder_recursive(node):
    if node:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.val)


def postorder_iterative(root):
    if not root:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.val)


def create_test_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def test_traversals():
    root = create_test_tree()

    print("Preorder (Recursive):", end=" ")
    preorder_recursive(root)
    print()

    print("Preorder (Iterative):", end=" ")
    preorder_iterative(root)
    print()

    print("Inorder (Recursive):", end=" ")
    inorder_recursive(root)
    print()

    print("Inorder (Iterative):", end=" ")
    inorder_iterative(root)
    print()

    print("Postorder (Recursive):", end=" ")
    postorder_recursive(root)
    print()

    print("Postorder (Iterative):", end=" ")
    postorder_iterative(root)
    print()


if __name__ == "__main__":
    test_traversals()
