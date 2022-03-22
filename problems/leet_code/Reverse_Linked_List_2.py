class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # m-1 의 head
        # m의 head
        # n+1의 head
        # reverse

        head_fix = head_left = prev = head_left_prev = head

        repeat_n = right - left + 1

        if left != 1:
            for _ in range(1, left - 1):
                head_left_prev = head_left_prev.next
            head_left = head_left_prev.next

        for _ in range(right):
            prev = prev.next

        for _ in range(repeat_n):
            next, head_left.next = head_left.next, prev
            head_left, prev = next, head_left

        if left == 1:
            return prev
        if left != 1:
            head_left_prev.next = prev
            return head