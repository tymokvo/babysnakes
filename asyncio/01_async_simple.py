"""
Demonstrating asyncio behavior versus typical synchronous behavior.

Inspired by: https://realpython.com/async-io-python/
"""
import asyncio
import time

def the_function(val):
    return val * 2

async def long_computation_running(val, duration):
    """A placeholder for something that takes a long time."""
    await asyncio.sleep(duration)
    return the_function(val)

async def print_then_sleep(name: str, num_prints: int, duration: float):
    """Await some expensive compute operation over some locally-generated range of values."""
    for i in range(num_prints):
        res = await long_computation_running(i, duration)
        print(name, res)

async def make_coroutines():
    """Scale it up."""
    def f(name):
        return print_then_sleep(name, 3, 1.0)

    await asyncio.gather(f("a"), f("b"), f("c"))

def do_async():
    print("Doing asyncio stuff.")
    t_0 = time.perf_counter()

    asyncio.run(make_coroutines())

    print(f"Async executed in {time.perf_counter() - t_0:.3f} seconds.")

# Synchronous land!
def long_computation_running_sync(val, duration):
    time.sleep(duration)
    return the_function(val)

def print_then_sleep_sync(name: str, num_prints: int, duration: float):
    for i in range(num_prints):
        res = long_computation_running_sync(i, duration)
        print(name, res)

def do_sync():
    print("Doing synchronous stuff.")
    t_0 = time.perf_counter()

    def f(name):
        print_then_sleep_sync(name, 3, 1.0)
    
    f("a")
    f("b")
    f("c")

    print(f"Synchronous executed in {time.perf_counter() - t_0:.3f} seconds.")

if __name__ == "__main__":
    do_async()
    do_sync()

    

