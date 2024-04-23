import time
import os
from multiprocessing import Process

import requests

cpu = os.cpu_count()


def task():
    rec = requests.get('https://www.youtube.com/')
    print(rec.status_code)


def run():
    start_time = time.time()

    processes = [Process(target=task) for _ in range(cpu)]
    for thread in processes:
        thread.start()
    for thread in processes:
        thread.join()

    end_time = time.time()
    print(f'Finished in {end_time - start_time}')


if __name__ == '__main__':
    run()
