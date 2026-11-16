import time
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys

# Increase recursion depth for Quick Sort on nearly sorted arrays
sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

ALGORITHMS = {
    1: ("Bubble Sort", bubble_sort),
    4: ("Merge Sort", merge_sort),
    5: ("Quick Sort", quick_sort)
}

def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def generate_nearly_sorted_array(size, noise_level):
    arr = sorted(generate_random_array(size))
    num_swaps = int(size * noise_level)
    for _ in range(num_swaps):
        idx1 = random.randint(0, size - 1)
        idx2 = random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def measure_time(algo_func, arr, repetitions):
    times = []
    for _ in range(repetitions):
        arr_copy = arr.copy()
        start_time = time.time()
        algo_func(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times), np.std(times)

def run_experiment(algo_ids, sizes, experiment_type, repetitions):
    # Part B results (Random)
    results_b = {algo_id: {"means": [], "stds": []} for algo_id in algo_ids}
    # Part C results (Nearly Sorted)
    results_c = {algo_id: {"means": [], "stds": []} for algo_id in algo_ids}
    
    noise_level = 0.05 if experiment_type == 1 else 0.20

    for size in sizes:
        print(f"Testing size: {size}")
        
        # Part B: Random Array
        arr_random = generate_random_array(size)
        # Part C: Nearly Sorted Array
        arr_nearly = generate_nearly_sorted_array(size, noise_level)
            
        for algo_id in algo_ids:
            if algo_id not in ALGORITHMS:
                continue
            name, func = ALGORITHMS[algo_id]
            
            # Skip Bubble Sort for very large arrays to avoid freezing
            if name == "Bubble Sort" and size > 10000:
                print(f"  Skipping {name} for size {size} (too slow)")
                results_b[algo_id]["means"].append(None)
                results_b[algo_id]["stds"].append(None)
                results_c[algo_id]["means"].append(None)
                results_c[algo_id]["stds"].append(None)
                continue

            # Measure Part B
            mean_b, std_b = measure_time(func, arr_random, repetitions)
            results_b[algo_id]["means"].append(mean_b)
            results_b[algo_id]["stds"].append(std_b)
            
            # Measure Part C
            mean_c, std_c = measure_time(func, arr_nearly, repetitions)
            results_c[algo_id]["means"].append(mean_c)
            results_c[algo_id]["stds"].append(std_c)
            
            print(f"  {name} - Random: {mean_b:.6f}s, Nearly: {mean_c:.6f}s")
            
    return results_b, results_c

def plot_results(results, sizes, title, filename):
    plt.figure(figsize=(10, 6))
    for algo_id, data in results.items():
        if algo_id not in ALGORITHMS:
            continue
        name = ALGORITHMS[algo_id][0]
        # Filter out None values for large arrays
        valid_sizes = [s for s, m in zip(sizes, data["means"]) if m is not None]
        valid_means = [m for m in data["means"] if m is not None]
        valid_stds = [s for s in data["stds"] if s is not None]
        
        if valid_means:
            plt.errorbar(valid_sizes, valid_means, yerr=valid_stds, label=name, marker='o', capsize=5)
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sorting Algorithm Experiments')
    parser.add_argument('-a', '--algorithms', nargs='+', type=int, default=[1, 4, 5], help='Algorithm IDs (1-Bubble, 4-Merge, 5-Quick)')
    parser.add_argument('-s', '--sizes', nargs='+', type=int, default=[100, 500, 1000, 2000, 5000], help='Array sizes')
    parser.add_argument('-e', '--experiment', type=int, default=1, help='Part C Noise level: 1-5%, 2-20%')
    parser.add_argument('-r', '--repetitions', type=int, default=5, help='Number of repetitions')

    args = parser.parse_args()
    
    valid_algos = [aid for aid in args.algorithms if aid in ALGORITHMS]
    
    results_b, results_c = run_experiment(valid_algos, args.sizes, args.experiment, args.repetitions)
    
    # Generate result1.png (Part B - Random)
    plot_results(results_b, args.sizes, "Part B: Sorting Random Arrays", "result1.png")
    
    # Generate result2.png (Part C - Nearly Sorted)
    noise_str = "5%" if args.experiment == 1 else "20%"
    plot_results(results_c, args.sizes, f"Part C: Sorting Nearly Sorted Arrays ({noise_str} Noise)", "result2.png")
    
    print("Experiments completed. Plots saved as result1.png and result2.png")
