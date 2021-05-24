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
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers -1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end -1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        start += 1

    return numbers

if __name__=='__main__':
    nums = [random.randint(0, 1000) for _ in range(100)]
    print(cocktail_sort(nums))