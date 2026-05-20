import time
import random
import matplotlib.pyplot as plot # type: ignore

def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j]<array[min]:
                min=j
        array[i],array[min]= array[min],array[i]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n - i - 1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

def display_benchmark_results(sizes, insertion_times, selection_times, bubble_times):
    print("Benchmark Results (Time in seconds):")
    print(f"{'Size':<10}{'Insertion Sort':<20}{'Selection Sort':<20}{'Bubble Sort':<20}")
    print("-" * 70)

    for i in range(len(sizes)):
        print(f"{sizes[i]:<10}{insertion_times[i]:<20.6f}{selection_times[i]:<20.6f}{bubble_times[i]:<20.6f}")
    print("\n")

def benchmark_sorting_algorithms():
    sizes = [5,10,20,50,100,500,1000,2000,5000,10000]
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in sizes:
        array = [random.randint(0,10000) for _ in range(size)]

        array_copy = array.copy()
        start_time = time.time()
        insertion_sort(array_copy)
        insertion_time = time.time() - start_time
        insertion_times.append(insertion_time)

        array_copy = array.copy()
        start_time = time.time()
        selection_sort(array_copy)
        selection_time = time.time() - start_time
        selection_times.append(selection_time)

        array_copy = array.copy()
        start_time = time.time()
        bubble_sort(array_copy)
        bubble_time = time.time() - start_time
        bubble_times.append(bubble_time)

    plot.figure(figsize=(10,6))
    plot.plot(sizes,insertion_times,label='Insertion Sort',marker='o')
    plot.plot(sizes,selection_times,label='Selection Sort',marker='o')
    plot.plot(sizes,bubble_times,label='Bubble Sort',marker='o')
    plot.xlabel('Input Size (n)')
    plot.ylabel('Time (seconds)')
    plot.title('Benchmarking Sorting Algorithms')
    plot.legend()
    plot.grid()
    plot.show()


