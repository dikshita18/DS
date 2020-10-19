
#Program to implement the concept of linear probing
class Hash:
    def __init__(self, keys, lowerrange, higherrange):
        self.value = self.hashfunction(keys, lowerrange, higherrange)

    def get_key_value(self):
        return self.value

    def hashfunction(self,keys,lowerrange, higherrange):
        if lowerrange == 0 and higherrange > 0:
            return keys%(higherrange)

if __name__ == '__main__':
    linear_probing = True
    list_of_keys = [23, 19, 1, 85, 2, 80]
    list_of_list_index = [None, None, None, None, None, None]
    print("Before : " + str(list_of_list_index))
    
    for value in list_of_keys:
        list_index = Hash(value, 0, len(list_of_keys)).get_key_value()
        print("hash value for " + str(value) + " is :" + str(list_index))
        if list_of_list_index[list_index]:
            print("Collission detected!")
        else:
            list_of_list_index[list_index] = value

    print("After: " + str(list_of_list_index))           
