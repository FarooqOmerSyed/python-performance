
import time

@profile
def large_loop():
    print('Do something before...')
    print('Do something before...')
    print('Do something before...')

    for _ in range(100_000_000):
        pass

    print("DO something after ...")
    print("DO something after ...")

start_time = time.time()
large_loop()
end_time = time.time()
print(f"Duration: {end_time - start_time}")