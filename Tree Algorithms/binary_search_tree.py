'''Binary Search Tree (BST) Operations:
a. Insertion:
Insertion operation adds a new node with the given value into the BST while maintaining the BST property 
(left child is smaller, right child is larger).
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

'''
Time Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
Space Complexity: O(h) - where h is the height of the tree (recursive stack space).
'''

'''
b. Deletion:
Deletion operation removes a node with the given value from the BST while maintaining the BST property.
'''


def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete(root, data):
    if root is None:
        return root
    
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    
    return root

'''
Time Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
Space Complexity: O(h) - where h is the height of the tree (recursive stack space).
'''

'''
c. Search:
Search operation finds a node with the given value in the BST.
'''


def search(root, data):
    if root is None or root.data == data:
        return root
    
    if data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)
    
'''
Time Complexity: O(h) - where h is the height of the tree, and in the worst case, it can be O(n) for a skewed tree.
Space Complexity: O(h) - where h is the height of the tree (recursive stack space).
'''

def pre_order_traversal(node):
    if node is None:
        return
    
    print(node.data, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

# Create an empty tree
root = None

# Insert nodes into the tree
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Print the initial tree
print("Initial tree:")
pre_order_traversal(root)

# Delete a node from the tree
root = delete(root, 20)

# Print the updated tree
print("\nTree after deletion:")
pre_order_traversal(root)

'''
Initial tree:
50 30 20 40 70 60 80 
Tree after deletion:
50 30 40 70 60 80 %    
'''
