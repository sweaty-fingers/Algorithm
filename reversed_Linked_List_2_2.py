class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # m-1 의 head
        # m의 head
        # n+1의 head
        # reverse

        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next