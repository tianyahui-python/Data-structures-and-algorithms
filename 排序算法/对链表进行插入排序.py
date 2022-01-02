# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # 添加虚拟头节点
        newHead = ListNode()

        p = head
        # 遍历原始链表
        while p:
            tmp = p.next  # 记录原始链表的下一个节点
            q = newHead  # 每一次遍历都把新的头节点赋值给q
            # 循环遍历的目的 找到当前p节点插入到新的链表中的位置
            while q.next and q.next.val <= p.val:
                q = q.next
            p.next = q.next  # 把新的链表后面的节点追加到当前p节点的后面
            q.next = p  # 再把p赋值给q.next 即q代表的就是，当前的p节点+q.next节点
            p = tmp  # 向后移动一个单位

        return newHead.next
