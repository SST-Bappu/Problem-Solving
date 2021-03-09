def DeleteMiddle(head):
    prev = None
    slow = head
    fast = head.next
    while(fast and fast.next!=None):
        prev = slow
        slow = slow.next
        fast=fast.next.next
    if prev!=None and slow.next!=None:
        prev.next = slow.next