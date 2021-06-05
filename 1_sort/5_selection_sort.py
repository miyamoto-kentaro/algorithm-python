# O(n**2)
import random
import time
from typing import List

def time_measurement(sort_func) -> float:

    def wrapper(*args,**kwargs):
        elapsed_time = 0
        for _ in range(10):
            start_time = time.time()
            sort_func(*args,**kwargs)
            elapsed_time += time.time() - start_time
        return elapsed_time/10
    return wrapper

@time_measurement
def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        
        numbers[i],numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100000) for _ in range(1000)]
    print(selection_sort(nums))