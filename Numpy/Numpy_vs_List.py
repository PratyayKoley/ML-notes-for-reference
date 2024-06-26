from time import process_time
import numpy as np

# For a list calculate the time taken for an operation

process_list = [i for i in range(100000000)]

start_time = process_time()

process_list = [i+5 for i in process_list]

end_time = process_time()

print(f"Total time for list = {end_time - start_time:.10f}")

# For a numpy array calculate the time taken for an operation

numpy_array = np.array([i for i in range(100000000)])

start_time = process_time()

numpy_array += 5

end_time = process_time()

print(f"Total time for numpy array = {end_time - start_time:.10f}")