import random

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

# Example Usage
if __name__ == "__main__":
    example_array = [3, 2, 1, 5, 4, 6]
    i = 3  
    array_copy = example_array.copy()
    result = quickselect(array_copy, 0, len(array_copy) - 1, i)
    print(f"The {i+1}-th smallest element in the array is: {result}")
