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
        
   
#Using No Alternate Buffer (ex.:prev in the above node)

def DeleteDups_NoAlternateBuffer(head):
    HashTable=dict({head.data:head.data})
    while(head.next):
        if HashTable.get(head.next.data):
            head.next = head.next.next
        else:
            HashTable.update({head.next.data:head.next.data})
            head=head.next
