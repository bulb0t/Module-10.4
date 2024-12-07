from threading import Thread
from time import sleep
from queue import Queue
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    guest.start()
                    print(f"{guest} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)
                print(guest.name, "в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    guest = next(g for g in guests if g.name == table.guest)
                    if not guest.is_alive():
                        print(f"{table.guest} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get().name
                            print(f"{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                            next(g.start() for g in guests if g.name == table.guest)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()