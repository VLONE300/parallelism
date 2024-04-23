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
    for i in range(cpu):
        task()

    end_time = time.time()
    print(f'Finished in {end_time - start_time}')


if __name__ == '__main__':
    run()
