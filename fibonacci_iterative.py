def remove_duplicates(array):
    if not array:
        return array 
    i = 0
    for j in range(1, len(array)):
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]
    return array[:i+1]

# Examples
array1 = [2, 2, 2, 2, 2]
print(remove_duplicates(array1))  

array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(array2))  

