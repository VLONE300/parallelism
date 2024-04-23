import threading
import time
import os

cpu = os.cpu_count()


def task():
    result = 0
    for i in range(1000000):
        result += abs(round(i ** 2 / 122) + i * 3.14)
    print(result)



def run():
    start_time = time.time()

    threads = [threading.Thread(target=task) for _ in range(cpu)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f'Finished in {end_time - start_time}')


if __name__ == '__main__':
    run()
