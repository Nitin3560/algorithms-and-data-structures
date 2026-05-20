def merge_sort(array):
    if len(array) > 1:
        mid=len(array) // 2
        left_half=array[:mid]
        right_half=array[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k]=left_half[i]
                i +=1
            else:
                array[k]=right_half[j]
                j +=1
            k +=1
        while i < len(left_half):
            array[k]=left_half[i]
            i +=1
            k +=1
        while j < len(right_half):
            array[k]=right_half[j]
            j +=1
            k +=1

test_array=[5, 2, 4, 7, 1, 3, 2, 6]
print("Original Array:", test_array)
merge_sort(test_array)
print("Sorted Array:", test_array)
