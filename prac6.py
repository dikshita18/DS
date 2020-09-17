
list_students_rolls = [ 19, 27, 62, 24, 21, 2, 51]

#Selection sort
def select_sort(list_students_rolls):
    for i in range(len(list_students_rolls)):
        min_val_index = i
        for j in range(i + 1, len(list_students_rolls)):
            if list_students_rolls[min_val_index] > list_students_rolls[j]:
                min_val_index = j
        list_students_rolls[i], list_students_rolls[min_val_index] = list_students_rolls[min_val_index],  list_students_rolls[i]
    print("Selection Sort: ", list_students_rolls)
        
#Insertion sort
def insert_sort(list_students_rolls):
    for i in range(len(list_students_rolls)):
        value = list_students_rolls[i]
        j = i - 1

        while j >= 0 and value < list_students_rolls[j]:
            list_students_rolls[j + 1] = list_students_rolls[j]
            j -= 1

        list_students_rolls[j + 1] = value
    print("Insertion Sort: ", list_students_rolls)
    
#Bubble sort
def bubble_sort(list_students_rolls):

    for i in range(len(list_students_rolls)):
        
        for j in range(len(list_students_rolls) - 1):
            if list_students_rolls[j] > list_students_rolls[j+1]:
                list_students_rolls[j], list_students_rolls[j+1] = list_students_rolls[j+1], list_students_rolls[j]
    print("Bubble Sort: ", list_students_rolls)


#Taking input from the user
ip = int(input("Enter 1 to perform selection sort,\nEnter 2 to perform Insertion sort, \nEnter 3 to perform Bubble sort: "))
if ip == 1:
    select_sort(list_students_rolls)
elif ip == 2:
    insert_sort(list_students_rolls)
else:
    bubble_sort(list_students_rolls)
    
    

           

