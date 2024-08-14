# Palindrome Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create List and Use Two pointers approach
# T: O(n)
# S: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]):
        if not head or not head.next:
            return True

        lArr = []
        cur = head
        while cur:
            lArr.append(cur.val)
            cur = cur.next

        length = len(lArr)

        for i in range(length // 2):
            if lArr[i] != lArr[length - 1 - i]:
                return False

        return True


# Create List and Use Two pointers approach
# T: O(n)
# S: O(n)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]):
        if not head or not head.next:
            return True

        lArr = []
        cur = head
        while cur:
            lArr.append(cur.val)
            cur = cur.next
        return lArr == lArr[::-1]


# Recursion
# T: O(n)
# S: O(n)
"""
Each time a function is called within a function, the computer needs
to keep track of where it is up to (and the values of any local variables)
in the current function before it goes into the called function. It does
this by putting an entry called the runtime stack (call stack) on stack frame.
Once it has created a tack frame for the current function, it can then go into 
the called function. Then once it is finished with the called function, it pops
the top stack frame to resume the function it had been in before the function call
was made.
So, the space usage is on the runtime stack because we are creating n stack frames.

It is worse than the first approach because in many languages, stack frames are large,
and there's a maximum runtime stack depth of 1000. With every node creating a stack frame,
this will greatly limit the maximum linked list size the algorithm can handle.
"""


class Solution3:
    def isPalindrome(self, head: Optional[ListNode]):
        self.front_pointer = head
        """
        인스턴스 변수. Solution 클래스의 인스턴스마다 고유하게 존재하며,클래스의 다른 메소드들에서도
        접근할 수 있다. front_pointer 변수는 Solution 클래스의 인스턴스 전체에서 유지된다. 
        즉, recursively_check 함수가 호출될 때마다 이 변수는 계속 업데이트된다.
        하지만 여기서는 isPalindrome과 그 하위 메소드에서만 필요로 하기 때문에 메소드 내에서 정의되었다.
        만약 다른 메소들에서도 사용된다면 생성자(__init__)안에서 정의된다.
        
        front_pinter = head로 사용한다면 이 변수는 로컬 변수로 간주된다. 이 경우
        front_pointer는 isPalindrome 메소드 안에서만 유효하며, recursively_check 함수에서
        그 값을 참조할 수 없다.
        """

        def recursively_check(cur=head):
            if cur:
                if not recursively_check(cur.next):
                    return False
                if self.front_pointer.val != cur.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


# Reverse Second Half In-place
# T: O(n)
# S: O(1)
"""
The strategy we can use is to reverse the second half of the LL in-place,
and then comparing it with the first half. Afterwards, we should re-reverse
the second half and put the list back together.
"""


class Solution3:
    def isPalindrome(self, head: Optional[ListNode]):
        if not head or not head.next:
            return True

        # Find the end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_half_start:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head: ListNode):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode):
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
