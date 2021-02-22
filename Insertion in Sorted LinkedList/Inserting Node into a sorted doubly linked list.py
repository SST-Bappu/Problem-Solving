class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
def sortedinsert(node,data):
    curNode = node

    prev = None
    while(True):
        if curNode.data == None:
            curNode.data = data
            return node
        elif curNode.data>=data:
            NewNode = ListNode(data)
            prev.next = NewNode
            NewNode.prev = prev
            NewNode.next = curNode
            curNode.prev = NewNode
            return node
        else:
            prev = curNode
            curNode = curNode.next


if __name__=="__main__":
    node = ListNode()
    t = int(input("t = "))
    while(t):
        n = int(input("n = "))
        print("Node Data Values = ")
        curNode = node
        prev = None
        while(n):
            curNode.data=int(input())
            curNode.next=ListNode()
            curNode.prev = prev
            prev = curNode
            curNode = curNode.next
            n-=1
        data = int(input("Data = "))
        curNode = sortedinsert(node,data)
        while(curNode.next != None):
            print(curNode.data,end="->")
            curNode = curNode.next
        t-=1
