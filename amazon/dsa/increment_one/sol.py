class Node:
    def __init__(self, value = 0, next_node=None):
        self.val = value
        self.next = next_node
        
# Recursion
"""
    Time: O(n), where n is the number of nodes in the linked list
    Space: O(n)
"""
def plusOneNoReverse(head):
    carry = _add_one(head)
    
    if carry:
        new_head = Node(1)
        new_head.next = head
        return new_head
    
    return head

def _add_one(node):
    if node is None:
        return 1
    
    carry = _add_one(node.next)
    total = node.val + carry
    node.val = total % 10
    return total // 10


"""
    Time: O(n), where n is the number of nodes in the linked list
    Space: O(1)
"""
def plusOneNoRverseConstantSpace(head):
    last_not_nine = None
    node = head
    while node:
        if node.val != 9:
            last_not_nine = node
        node = node.next
    
    if last_not_nine is None:
        new_head = Node(1)
        new_head.next = head
        node = head
        while node:
            node.val = 0
            node = node.next
        return new_head
    
    last_not_nine.val += 1
    node = last_not_nine.next
    while node:
        node.val = 0
        node = node.next
    return head
        
        