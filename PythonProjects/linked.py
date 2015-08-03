class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        counter = 0
        while current!= None:
            current = current.getNext()
            counter += 1
        return counter

    def search(self, item):
        current = self.head
        found = True
        while current != None and not found:
            if current.getData() == item:
                return found
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        temp = None
        found = True
        data = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
                temp = current
               
           
            current = current.getNext()

        return data
                
                
        
                
    
