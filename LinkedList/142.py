# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Hash Set
# T: O(n)
# S: O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]):
        nodes_seen = set()
        cur = head
        while cur:
            if cur in nodes_seen:
                return cur
            nodes_seen.add(cur)
            cur = cur.next
        return


# Floyd's Tortoise and Hare Algorithm
# T: O(n)
# S: O(1)
"""
It is used to detect cycles in sequences or linked lists.

Let's define a as the length of the path from the start of the list 
to the entrance of the cycle.
    
Let's define b as the length of the path from the cycle's entrance 
to the meeting point of the hare and the tortoise inside the cycle.
    
Let's define c as the total length of the cycle.

Then a + b + k * c = 2(a + b), since the hare is twice as fast as the tortoise.
We obtain k * c = a + b.


After finding a meeting point inside the cycle, you'll leave the tortoise there 
and move the hare back to the starting point of the park (or the head of the linked list).
Then, have both the hare and the tortoise move at the same pace (one step at a time). 
When they meet again, that meeting point is the entrance to the cycle.
    
If we move the hare back to the start of the straight path and make it move at the same speed 
as the tortoise, here's what happens:
- The hare has a distance to travel to reach the entrance of the cycle. 
  We can rearrange the above equation to say that the hare will reach the entrance of the cycle 
  in a = k⋅c−b steps.
- Currently, the tortoise is b away from the entrance of the cycle. 
  In k⋅c−b steps, where will the tortoise be? Relative to the entrance of the cycle, 
  the tortoise will be at (k⋅c−b)+b = k⋅c. Because k is an integer, c is defined as the length of the cycle, 
  and this distance is relative to the entrance of the cycle, the tortoise will be at the entrance!

Therefore, to find the entrance of the cycle, we don't actually need the values of a,b,c,k. 
We can just return the node at which they meet again.

Algorithm

1. Initialize the tortoise and hare pointers to the head of the linked list.

2. Move the tortoise one step and the hare two steps at a time until they meet 
   or either hare or hare.next becomes null.
   
3. If the hare or hare.next pointer is null, it means the hare came to the dead end 
   and we return null as there is no cycle.
   
4. Reset the hare pointer to the head of the linked list.

5. Move both pointers one step at a time until they meet again. 
   The meeting point is the node where the cycle begins.
   
6. Return the meeting point node.
"""


class Solution2:
    def detectCycle(self, head: Optional[ListNode]):
        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break
        if not hare or not hare.next:
            return

        hare = head

        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise
