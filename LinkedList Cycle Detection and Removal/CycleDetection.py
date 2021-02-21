class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None
def DetectCycle(node): #Hashing Method
    HashTable = dict()
    prev = node
    while(True):
        if HashTable.get(node)==None:
            HashTable.update({node: node.data})
            prev = node
            node=node.next
        else:
            prev.next = None
            return
def FloydCycleDetection(node): #Floyd's cycle finding method
    slow = node
    fast = node.next
    while(True):
        if slow.next == fast.next:
            fast = fast.next
            print(f"Cycle Found at {fast.data}")
            break
        slow = slow.next
        fast = fast.next
        fast = fast.next
    slow = node
    while(True):
        if slow.next == fast.next:
            fast.next = None
            return
        slow = slow.next
        fast = fast.next





