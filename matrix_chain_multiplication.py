import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less) + equal + quicksort(greater)

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort_random(less) + equal + quicksort_random(greater)

if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", test_array)

    sorted_array = quicksort(test_array)
    print("Sorted array (non-random pivot):", sorted_array)

    sorted_array_random = quicksort_random(test_array)
    print("Sorted array (random pivot):", sorted_array_random)
