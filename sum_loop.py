# calculating empty sum_loop duration 
import time

def large_loop():
    for _ in range(100_000_000):
        do_stuff()

def do_stuff():
    return 1 + 2
start_time = time.time()
large_loop()
end_time = time.time()
print(f"Duration: {end_time - start_time: .2f} seconds")