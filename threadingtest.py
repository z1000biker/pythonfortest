import numpy as np
import timeit
import threading
from numba import jit

# Simple Python for loop
def simple_sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# JIT-compiled function to calculate the sum of squares using Numba
@jit(nopython=True)
def numba_sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# Function to calculate the sum of squares in a thread
def thread_sum_of_squares(start, end, result, index):
    total = 0
    for i in range(start, end):
        total += i * i
    result[index] = total

def multi_threaded_sum_of_squares(n, num_threads):
    threads = []
    results = [0] * num_threads
    chunk_size = n // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=thread_sum_of_squares, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

# Parameters
n = 10_000_000
num_threads = 4

# Measure simple for loop execution time
simple_time = timeit.timeit(lambda: simple_sum_of_squares(n), number=10)

# Measure Numba execution time
numba_time = timeit.timeit(lambda: numba_sum_of_squares(n), number=10)

# Measure multithreaded execution time
multi_threaded_time = timeit.timeit(lambda: multi_threaded_sum_of_squares(n, num_threads), number=10)

# Print results
print(f"Simple for loop time (average over 10 runs): {simple_time:.4f} seconds")
print(f"Numba sum of squares time (average over 10 runs): {numba_time:.4f} seconds")
print(f"Multithreaded sum of squares time (average over 10 runs): {multi_threaded_time:.4f} seconds")
