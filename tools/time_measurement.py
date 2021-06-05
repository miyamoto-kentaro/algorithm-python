import time

def time_measurement(sort_func) -> float:

    def wrapper(*args,**kwargs):
        elapsed_time = 0
        for _ in range(1000):
            start_time = time.time()
            sort_func(*args,**kwargs)
            elapsed_time += time.time() - start_time
        return elapsed_time/10
    return wrapper
