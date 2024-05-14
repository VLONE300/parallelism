import threading


class Cinema:
    def __init__(self):
        self.movies = {}
        self.lock = threading.Lock()
        self.semaphore = threading.Semaphore(2)
        self.condition = threading.Condition(self.lock)

    def add_movie(self, movie_name, sessions, seats):
        with self.lock:
            self.movies[movie_name] = {'sessions': sessions, 'seats': seats}

    def book_seat(self, movie_name, session, seat_number):
        with self.condition:
            while self.movies[movie_name]['seats'][seat_number - 1] == 0:
                print(f"Seat {seat_number} for {movie_name} - {session} is already booked. Waiting...")
                self.condition.wait()
            self.movies[movie_name]['seats'][seat_number - 1] = 0
            print(f"Seat {seat_number} booked for {movie_name} - {session}")


def book_seats(cinema, movie_name, session, seat_number):
    with cinema.semaphore:
        cinema.book_seat(movie_name, session, seat_number)
        with cinema.condition:
            cinema.condition.notify()


cinema = Cinema()

cinema.add_movie("Movie 1", ["Session 1", "Session 2"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
cinema.add_movie("Movie 2", ["Session 1", "Session 2"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

threads = []
for i in range(10):
    thread = threading.Thread(target=book_seats, args=(cinema, "Movie 1", "Session 1", i + 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All bookings completed.")
