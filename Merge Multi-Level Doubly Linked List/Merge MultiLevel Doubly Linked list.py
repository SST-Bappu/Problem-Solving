class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None
def MergeList(node):
    prev = None
    while(node.next!=None):
        if node.child is not None:
            next = node.next
            node.next = node.child
            child = node.child
            child.prev = node
            flat = MergeList(child)
            flat.next = next
            next.prev = flat
            node = next
            prev = flat
        else:
            prev = node
            node = node.next
    return prev

def FlattenDoublyList(node):
    while(node.next!=None):
        if node.child is not None:
            next = node.next
            node.next = node.child
            child = node.child
            child.prev = node
            flat = MergeList(child)
            flat.next = next
            next.prev = flat
            node = next
        else:
            node = node.next
