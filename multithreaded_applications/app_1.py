import threading
import time
import random


class Worker(threading.Thread):
    def __init__(self, worker_id, semaphore, order_queue):
        super().__init__()
        self.worker_id = worker_id
        self.semaphore = semaphore
        self.order_queue = order_queue

    def run(self):
        while True:
            self.semaphore.acquire()
            if not self.order_queue:
                print('No more orders')
                break
            try:
                order = self.order_queue.pop(0)
                print(f'Worker {self.worker_id} processing order: {order}')
                time.sleep(random.randint(1, 3))
            finally:
                self.semaphore.release()


class Order:
    def __init__(self, order_id, resources_needed):
        self.order_id = order_id
        self.resources_needed = resources_needed

    def __str__(self):
        return f"Order {self.order_id}: {self.resources_needed}"


def main():
    order_queue = [
        Order(1, "resources 1"),
        Order(2, "resources 2"),
        Order(3, "resources 3"),
        Order(4, "resources 4"),
        Order(5, "resources 5"),
    ]

    semaphore = threading.Semaphore(2)
    workers = [Worker(i, semaphore, order_queue) for i in range(1, 4)]

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()


if __name__ == "__main__":
    main()
