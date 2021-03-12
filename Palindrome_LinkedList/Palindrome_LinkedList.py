def Palindrome_Stack(head): #Optimized, using stack
#Iterative process, no need to reverse the list. We push the first half into a stack and then check the second half
    list=[]
    fast = head
    while(fast and fast.next):
        list.append(head.data)
        head=head.next
        fast=fast.next.next
    if fast!=None:
        head=head.next
    while(head):
        if head.data!=list.pop():
            return False
        head = head.next
    return True