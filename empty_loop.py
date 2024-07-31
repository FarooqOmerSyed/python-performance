# calculating empty loop duration 
import time

def large_loop():
    for _ in range(100_000_000):
        pass

start_time = time.time()
large_loop()
end_time = time.time()
print(f"Duration: {end_time - start_time}")