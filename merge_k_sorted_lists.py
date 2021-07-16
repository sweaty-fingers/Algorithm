class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return

        val_list = []

        for head_tmp in lists:
            while head_tmp:
                val_list.append(head_tmp.val)
                print(head_tmp.val, end=" ")
                head_tmp = head_tmp.next
            print("")

        val_list.sort(reverse=False)

        head = ListNode()
        tmp = head
        for i in val_list:
            tmp.next = ListNode(i)
            tmp = tmp.next

        return head.next