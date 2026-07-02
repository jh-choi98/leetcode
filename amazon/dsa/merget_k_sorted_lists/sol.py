from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(nlogn), n is the nubmer of total nodes
# Space: O(n)      
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        heap = []
        tie = 0
        
        for llist in lists:
            node = llist
            while node:
                heapq.heappush(heap, (node.val, tie, node))
                tie += 1
                node = node.next

        cur = dummy_head
        while heap:
            _, _, new_node = heapq.heappop(heap)
            cur.next = new_node
            cur = new_node
        
        return dummy_head.next

# Time: O(nlogk), k is the number of lists
# Space: O(k)
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        tie = 0
        
        # push only the head of each list -> heap size k
        for llist in lists:
            if llist:
                heapq.heappush(heap, (llist.val, tie, llist))
                tie += 1
                
        dummy_head = ListNode(-1)
        cur = dummy_head
        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            
            # push the next node from the SAME list
            if node.next:
                heapq.heappush(heap, (node.next.val, tie, node.next))
                tie += 1
        
        return dummy_head.next
        