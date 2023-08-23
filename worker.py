"""
starts a worker process
"""
import time

from shared import consume_memory


def main():
    """
    starts a no-op worker that consumes resources
    """
    while True:
        print("consuming resources")
        consume_memory()
        print("sleeping for 60 seconds")
        time.sleep(60)


if __name__ == "__main__":
    main()