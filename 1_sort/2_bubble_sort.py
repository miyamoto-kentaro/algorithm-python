# O(n**2)
import random
import time
from typing import List
def time_measurement(sort_func) -> float:

    def wrapper(*args,**kwargs):
        elapsed_time = 0
        for _ in range(1000):
            start_time = time.time()
            sort_func(*args,**kwargs)
            elapsed_time += time.time() - start_time
        return elapsed_time/10
    return wrapper


@time_measurement
def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j],numbers[j + 1] = numbers[j + 1], numbers[j]
    
    return numbers

if __name__=='__main__':
    nums = [random.randint(0, 1000) for _ in range(100)]
    print(bubble_sort(nums))