#doubly_linked_list
class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        self.previous = None
        
    def display(self):
        print(self.element)

class DlinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
               
    def _len_(self):
        return self.size
        
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        while first:            
            print(first.element)
            first = first.next
                
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e) 
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
            
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        new_value.previous = self.get_tail()
        self.get_tail().next = new_value
        self.size += 1
                   
    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1

    def find_second_last_element(self):               
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first        
        else:
            print("Size not sufficient")            
        return None
    
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
  
    def get_prev_node_at(self,position):
        if position == 0:
            print('No previous element')
            return None
        return self.get_node_at(position).previous
    
    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            next_node.previous = prev_node
            self.size -= 1
            
    def add_between_list(self,position,element):
        element_node = Node(element)
        if position > self.size:
            print("Index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position-1)
            current_node = self.get_node_at(position)
            prev_node.next = element_node
            element_node.previous = prev_node
            element_node.next = current_node
            current_node.previous = element_node 
            self.size += 1
        
    def search(self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False
    
    def merge(self, linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            linkedlist_value.head.previous = last_node
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size
            
    
#List 1
print('List 1')
list1 = DlinkedList()
list1.add_head(2)
list1.add_head(1)
list1.add_tail(3)
list1.add_tail(4)
list1.add_tail(5)
list1.add_tail(7)
list1.display()
list1.remove_head()
list1.remove_tail()
print('Head and Tail elements removed')
list1.display()

print('Added element between the list')
list1.add_between_list(2,6)
list1.display()

print('Removed element from between the list')
list1.remove_between_list(2)
list1.display()

#List 2
list2 = DlinkedList()
list2.add_head(7)
list2.add_head(6)
list2.add_tail(8)
list2.add_tail(9)
print('List 2')
list2.display()

#merging lists
list1.merge(list2)
print('List after merging')
list1.display()
