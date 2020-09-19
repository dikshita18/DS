#Performing Stack operations

class Arraystack:

    def __init__(self):
        self._data = [2, 4, 6, 8, 10]

    def display(self):
        print(self._data)

    def is_empty(self):
        if len(self._data) == 0:
            return 0
        
        else:
            return 1

    def push(self, value):
        self._data.append(value)
        print(self._data,' element added')

    def pop(self):
        if self.is_empty() == 1:
            print('element removed which is ', self._data.pop())
            print(self._data)
            
        else:
            print('The stack is empty')

    def top(self):
        if self.is_empty() == 1:
            print('The topmost element in the stack is: ', self._data[-1])
            
        else:
            print('The stack is empty')        
        
c = Arraystack()
c.push(12)
c.push(14)
c.push(16)
c.display()
c.pop()
c.top()
