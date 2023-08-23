import concurrent.futures
import random


def consume_memory():
    """
    starts memory consumer in a process pool and then tosses it away
    this ensures memory is released once the function is completed
    """
    futures = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        futures.append(executor.submit(memory_consumer))
        concurrent.futures.wait(futures)


def memory_consumer():
    """
    allocates a variable with a random size
    """
    rand_one = random.randint(16, 32)
    rand_two = random.randint(16, 32)
    placeholder = ['bar' for _ in range((1000000 * (rand_one + rand_two)))]
    del placeholder
