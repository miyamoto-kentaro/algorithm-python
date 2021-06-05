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
def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap/1.3)
        if gap < 1:
            gap = 1
        
        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100000) for _ in range(1000)]
    print(comb_sort(nums))

