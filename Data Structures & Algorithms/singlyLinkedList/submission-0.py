class ListNode: 
    def __init__(self, val, next_node=None): 
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1) 
        self.tail = self.head 
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr: 
            if i == index: 
                return curr.val 
            i += 1 
            curr = curr.next
        return -1 
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val) 
        newNode.next = self.head.next 
        self.head.next = newNode 
        if not newNode.next: #if the list was empty pre-insertion 
            self.tail = newNode 

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val) 
        self.tail.next = newNode
        self.tail = self.tail.next 
        
    def remove(self, index: int) -> bool:
        prev = self.head 
        curr = self.head.next
        i = 0
        while curr: 
            if i == index: #index found
                if curr == self.tail: 
                    self.tail = prev 
                prev.next = curr.next
                return True 
            prev = curr
            curr = curr.next 
            i += 1 
        return False 
        

    def getValues(self) -> List[int]:
        newList = []
        curr = self.head.next
        while curr:
            newList.append(curr.val) 
            curr = curr.next 
        return newList




        
