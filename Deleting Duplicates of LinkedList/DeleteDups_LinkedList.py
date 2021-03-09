def DeleteDups(head):
    HashTable=dict()
    prev=None
    while(head):
        if HashTable.get(head.data):
            prev.next = head.next
        else:
            HashTable.update({head.data:head.data})
            prev = head
        head=head.next