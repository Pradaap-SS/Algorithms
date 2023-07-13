'''Tree Traversal Algorithms:


a. Pre-order Traversal:
Pre-order traversal visits the nodes in the following order: root, left subtree, right subtree.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is None:
        return
    
    print(node.data, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


# Create the nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Call the pre_order_traversal function
print("Pre-order traversal:")
pre_order_traversal(root)

'''
Time Complexity: O(n) - where n is the number of nodes in the tree.
Space Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
'''


'''
b. In-order Traversal:
In-order traversal visits the nodes in the following order: left subtree, root, right subtree.
'''

def in_order_traversal(node):
    if node is None:
        return
    
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)

'''
Time Complexity: O(n) - where n is the number of nodes in the tree.
Space Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
'''

'''
c. Post-order Traversal:
Post-order traversal visits the nodes in the following order: left subtree, right subtree, root.
'''

def post_order_traversal(node):
    if node is None:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=" ")

'''
Time Complexity: O(n) - where n is the number of nodes in the tree.
Space Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
'''