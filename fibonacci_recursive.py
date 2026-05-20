def merge_and_sort(k_arrays):
    merged_array = []
    for array in k_arrays:
        merged_array.extend(array)
    for i in range(1, len(merged_array)):
        key = merged_array[i]
        j=i-1
        while j>=0 and key < merged_array[j]:
            merged_array[j+1] = merged_array[j]
            j-=1
        merged_array[j+1] = key

    return merged_array

# Example usage
k = 3
n = 4
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
k_arrays = [array1, array2, array3]

result = merge_and_sort(k_arrays)
print(result)
