class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 홀수 노드, 짝수 노드에 대한 head 생성,
        # 홀수 노드 연결 리스트, 짝수 노드 연결 리스트 만들기,
        # 홀수 노드 연결 리스트 tail에 짝수노드 head 붙이기.
        # 빈 리스트가 들어왔을 때 바로 종료하기

        if not head:
            return head

        head_odd = head
        head_even = head.next

        head_odd_temp = head_odd
        head_even_temp = head_even

        while head_even_temp and head_even_temp.next:

            head_odd_temp.next = head_even_temp.next
            head_odd_temp = head_odd_temp.next
            head_even_temp.next = head_odd_temp.next
            head_even_temp = head_even_temp.next

        head_odd_temp.next = head_even

        return head_odd
