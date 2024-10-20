from threading import Thread
from time import sleep

class Knight(Thread):

    warriors = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        count_days = 0
        print(f'{self.name}, на нас напали!\n')
        while self.warriors > 0:
            self.warriors -= self.power
            count_days += 1
            if self.warriors < 0:
                print(f"{self.name} сражается {count_days} день(дня).., осталось 0 воинов.\n")
            else:
                print(f"{self.name} сражается {count_days} день(дня).., осталось {self.warriors} воинов.\n")
            sleep(1)
        print(f'{self.name} одержал победу спустя {count_days} дней(дня)!\n')



first_knight = Knight('Sir Lancelot', 13)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
