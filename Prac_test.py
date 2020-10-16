#prac4
#Performing Queue operations using Circular Array implementation
class ArrayQueue:
    capacity = 6
    
    def __init__ (self):
        self._data = [None] * ArrayQueue.capacity
        self._size = 0
        self._front = 0

    def display(self):
        return self._data

    def __len__(self):        
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):                                                                                                     
        if self.is_empty():
            raise Exception( "Queue is empty" ) 
            return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2  * len(self._data)) # double the array size 
        val = (self._front + self._size) % len(self._data)
        self._data[val] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception( "Queue is empty" )
        fval = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        return fval
                       
    def resize(self, cap): 
        old = self._data
        self._data = [None] * cap 
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old) 
        self._front = 0


c = ArrayQueue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
c.enqueue(5)
c.enqueue(6)
print(c.display())
c.dequeue()
c.dequeue()
c.dequeue()
print(c.display())
c.enqueue(1)
print(c.display())
c.enqueue(2)
print(c.display())
c.enqueue(3)
print(c.display())
