'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sorting Performance Analyzer (SPA) in Python
Course: ETCCDS202 - Data Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data Structures (ETCCDS202)

Name of the School:	School of Engineering & Technology 
Program: B.Tech CSE (AI and ML) 
Course Title: Data Structures 
Course Code: ETCCDS202 
Unit Title: Foundations & Algorithmic Analysis 
Student Name: GAURI SHARMA
Roll Number: 2501730108
Section: A 
Semester: 2 
Batch: 2025-26 
Submitted To: Mrs. Neetu Chauhan 
Submission Date: 
'''

import time
import random
import sys

# Increase recursion depth for Quick Sort on sorted datasets
sys.setrecursionlimit(20000)

# --- TASK 1: CORE SORTING ALGORITHMS ---

def insertion_sort(arr):
    """O(n^2) - Stable and In-place"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """O(n log n) - Stable and Out-of-place"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, low, high):
    """O(n log n) Average - Unstable and In-place"""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Using last element as pivot as per assignment recommendation
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- TASK 2: PERFORMANCE MEASUREMENT ---

def measure_time(sort_func, data):
    """Measures execution time on a copy of the data."""
    arr_copy = list(data) # Ensure fair comparison by copying data
    start = time.perf_counter()
    
    if sort_func.__name__ == "quick_sort":
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)
        
    end = time.perf_counter()
    return (end - start) * 1000 # Convert to milliseconds

def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}
    
    for size in sizes:
        datasets[f"Random_{size}"] = [random.randint(1, 100000) for _ in range(size)]
        datasets[f"Sorted_{size}"] = list(range(size))
        datasets[f"Reverse_{size}"] = list(range(size, 0, -1))
        
    return datasets

# --- MAIN RUNNER ---

def main():
    # Correctness Check
    test_list = [5, 2, 9, 1, 5, 6]
    print(f"Correctness Check: {test_list}")
    print(f"Insertion: {insertion_sort(list(test_list))}")
    print(f"Merge:     {merge_sort(list(test_list))}")
    qs_test = list(test_list)
    quick_sort(qs_test, 0, len(qs_test)-1)
    print(f"Quick:     {qs_test}\n")

    datasets = generate_datasets()
    algorithms = [insertion_sort, merge_sort, quick_sort]
    
    print(f"{'Dataset Type':<20} | {'Insertion (ms)':<15} | {'Merge (ms)':<12} | {'Quick (ms)':<12}")
    print("-" * 70)

    for label, data in datasets.items():
        results = []
        for algo in algorithms:
            # Skip Insertion Sort for large sorted/reverse lists if it's too slow
            # or just run it to observe the O(n^2) behavior
            t = measure_time(algo, data)
            results.append(f"{t:.2f}")
        
        print(f"{label:<20} | {results[0]:<15} | {results[1]:<12} | {results[2]:<12}")

if __name__ == "__main__":
    main()