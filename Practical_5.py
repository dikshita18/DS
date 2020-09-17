#Program to search an element in the list using Linear and Binary search

list_values = [2, 4, 6, 8, 10]

def binary_search(list_values, search, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if list_values[mid] == search:
        return mid

    elif search < list_values[mid]:
        return binary_search(list_values, search, start, mid - 1)

    else:
        return binary_search(list_values, search, mid - 1, end)

    
def linear_search(list_values, search):
    index_counter = 0
    list_size = len(list_values)

    while index_counter < list_size:
        temp_value = list_values[index_counter]

        if temp_value == search:
            return index_counter
        index_counter += 1
    return -1


#Taking input from the user
ip = int(input("Enter 1 for binary search OR \nEnter 2 for linear search on list:"))

if ip == 1:
    print(binary_search(list_values, 6, 0, len(list_values)))

else:
    print(linear_search(list_values, 6))

    


