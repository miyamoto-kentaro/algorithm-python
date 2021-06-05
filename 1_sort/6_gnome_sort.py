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
def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index += 1
        if numbers[index] > numbers[index - 1]:
            index += 1
        else:
            numbers[index],numbers[index - 1] = numbers[index - 1], numbers[index]
            index -= 1
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100000) for _ in range(100)]
    print(gnome_sort(nums))