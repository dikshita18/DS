#practical 1a
list1 = [5, 4, 3, 2, 1]
print("List 1: ",list1)

#sorting the list1
list1.sort()
print("sorted list 1",list1)

def search_list1():
    i = int(input("Enter element to search in the list:"))
    if i in list1:
        print("The element is in the list")
        print("Position of the element is", list1.index(i))
    else:
        print("The element is not in the list")
        
search_list1()

def reverse_list1():
    print("Reversing the list1: ", list1[::-1])
    
reverse_list1()

list2 = ["E", "D", "C", "B", "A"]
print("List 2: ",list2)

#sorting the list2
list2.sort()
print("sorted list 2", list2)

def merge_list():
    list3 = list1 + list2
    print("Merging two lists: ", list3)

merge_list()


    

    
