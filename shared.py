import concurrent.futures
import math
import multiprocessing
import random
import time


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
    rand_one = random.randint(8, 12)
    rand_two = random.randint(8, 12)
    placeholder = ["bar" for _ in range((1000000 * (rand_one + rand_two)))]
    del placeholder


def consume_cpu():
    """
    starts cpu consumer in a process pool and then tosses it away
    this ensures cpu is released once the function is completed
    """
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        process = multiprocessing.Process(target=cpu_consumer)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


def cpu_consumer(interval=1, utilization=None):
    """
    Generate a utilization % for a duration of interval seconds
    """
    if utilization is None:
        utilization = random.randint(4, 5)

    start_time = time.time()
    for _ in range(0, int(interval)):
        while time.time() - start_time < utilization / 100.0:
            _ = math.sqrt(64 * 64 * 64 * 64 * 64)
        time.sleep(1 - utilization / 100.0)
        start_time += 1
