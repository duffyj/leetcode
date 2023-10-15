class Node():
    def __init__(self,k,
            v=None,
            prev=None,
            next=None):
        self.k = k
        self.v = v
        self.prev = prev
        self.next = next



class LRUCache():
    """

    NodeClass:
    * val - value
    * key - key
    * next & prev

    Init
    --- 
    Does NOT crate a node on init
    * capacity. 
    * tail Node
    * map of key to Node


    Get
    ---
    o(c) = 1?
    Look up node in map If node exists (a) move to head of list (handle new) (b) return val
    otherwise return -1

    MoveNodeToHead
    --------------
    if node is tail: Set LRUCache.tail to parent else set child of parent to child of node
    if node not head: set LRUCache.head = node and node.child = oldhead

    Put
    ---
    if k in cache:
        move k to head
        update head with new value
    else:
        add new node at head

   """

    def __init__(self,capacity):
        self.map = {}
        self.capacity = capacity
        self.count = 0
        self.head = None
        self.tail = None

    def show(self):
        print( 'h', (self.head.k,self.head.v)   if self.head.v else '')
        print( 't', (self.tail.k,self.tail.v) if self.tail.v else '')
        n = self.head
        all = []
        while n:
            print(n.k)
            all.append((n.prev.k if n.prev else None,n.k,n.v,n.next.k if n.next else None,))
            n = n.next

        print((all,list(self.map.keys())))



    def moveNodeToHead(self,node):
        if self.head != node:
            parentNode = node.prev
            childNode = node.next
            parentNode.next = childNode      
            if childNode:
                childNode.prev = parentNode
            else:
                self.tail = parentNode
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def get(self,key):
        if node := self.map.get(key):
            self.moveNodeToHead(node)
            return self.head.v
        return -1

    def put(self, key, value):
        if node := self.map.get(key):
             self.moveNodeToHead(node)
             node.v = value
             return
        newNode = Node(key,value,None,self.head)
        if self.head:
            self.head.prev = newNode 
        self.head = newNode
        if not self.tail:
            self.tail = newNode
        self.map[key] = newNode
        if self.count +1 <=  self.capacity:
            self.count+=1
            return 
        print('culling')
        # shrink by one
        tail = self.tail
        prevTail = self.tail.prev
        del self.map[tail.k]
        prevTail.next = None
        tail.prev = None
        self.tail = prevTail



def test1():

    lurc = LRUCache(2)
    lurc.put('A',1)
    lurc.show()     
    lurc.put('B',2)
    lurc.show()     
    lurc.put('C',3)
    lurc.show()    
    lurc.put('B','**')
    lurc.show()       
    lurc.put('D',4)
    lurc.show()     
    lurc.put('A','##')
    lurc.show()         
    lurc.get('D')
    lurc.show()        


test1()

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)