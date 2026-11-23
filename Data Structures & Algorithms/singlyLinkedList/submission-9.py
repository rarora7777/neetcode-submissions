class Node:
    val: int
    next: Node | None

    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        
        while index and node:
            index -= 1
            node = node.next

        return -1 if not node else node.val

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        node = self.head
        if not node:
            self.insertHead(val)
            return

        while node.next:
            node = node.next
        node.next = Node(val, None)

    def remove(self, index: int) -> bool:
        parent = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            else:
                return False
        
        while 1:
            if parent is None or parent.next is None:
                return False
            elif index == 1:
                parent.next = parent.next.next
                return True
            index -= 1
            parent = parent.next

    def getValues(self) -> List[int]:
        vals = []
        node = self.head

        while node:
            vals.append(node.val)
            node = node.next
        
        return vals
        
