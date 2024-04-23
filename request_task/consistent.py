import time
import os

import requests

cpu = os.cpu_count()


def task():
    rec = requests.get('https://www.youtube.com/')
    print(rec.status_code)


def run():
    start_time = time.time()
    for i in range(cpu):
        task()

    end_time = time.time()
    print(f'Finished in {end_time - start_time}')


if __name__ == '__main__':
    run()
